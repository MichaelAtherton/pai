# Pixi - Integration

**Pages:** 5

---

## VSCode

**URL:** https://pixi.sh/latest/integration/editor/vscode/

**Contents:**
- VSCode
- Python Extension#
- Direnv Extension#
- Devcontainer Extension#
- Secrets#

Visual Studio Code is a popular editor that can be extended to support most programming languages by installing the suitable extension.

First, install the Python extension from the marketplace. Typically, the extension will detect and select the Pixi default environment automatically as soon as you open a Python file. In case it doesn't or you want to select a different environment, you can open the environment selector to select the environment of your choice.

Direnv provides a language agnostic way of running VSCode in a Pixi environment. First, install the Direnv extension from the marketplace. Then follow the instructions in our Direnv doc page.

VSCode Devcontainers are a popular tool to develop on a workspace with a consistent environment. They are also used in GitHub Codespaces which makes it a great way to develop on a workspace without having to install anything on your local machine.

To use pixi inside of a devcontainer, follow these steps:

Create a new directory .devcontainer in the root of your workspace. Then, create the following two files in the .devcontainer directory:

In the above example, we mount the .pixi directory into a volume. This is needed since the .pixi directory shouldn't be on a case insensitive filesystem (default on macOS, Windows) but instead in its own volume. There are some conda packages (for example ncurses-feedstock#73) that contain files that only differ in case which leads to errors on case insensitive filesystems.

If you want to authenticate to a private conda channel, you can add secrets to your devcontainer.

These secrets need to be present either as an environment variable when starting the devcontainer locally or in your GitHub Codespaces settings under Secrets.

**Examples:**

Example 1 (unknown):
```unknown
FROM mcr.microsoft.com/devcontainers/base:jammy

ARG PIXI_VERSION=v0.59.0

RUN curl -L -o /usr/local/bin/pixi -fsSL --compressed "https://github.com/prefix-dev/pixi/releases/download/${PIXI_VERSION}/pixi-$(uname -m)-unknown-linux-musl" \
    && chmod +x /usr/local/bin/pixi \
    && pixi info

# set some user and workdir settings to work nicely with vscode
USER vscode
WORKDIR /home/vscode

RUN echo 'eval "$(pixi completion -s bash)"' >> /home/vscode/.bashrc
```

Example 2 (unknown):
```unknown
{
    "name": "my-workspace",
    "build": {
      "dockerfile": "Dockerfile",
      "context": "..",
    },
    "customizations": {
      "vscode": {
        "settings": {},
        "extensions": ["ms-python.python", "charliermarsh.ruff", "GitHub.copilot"]
      }
    },
    "features": {
      "ghcr.io/devcontainers/environments/docker-in-docker:2": {}
    },
    "mounts": ["source=${localWorkspaceFolderBasename}-pixi,target=${containerWorkspaceFolder}/.pixi,type=volume"],
    "postCreateCommand": "sudo chown vscode .pixi && pixi install"
}
```

Example 3 (unknown):
```unknown
{
    "build": "Dockerfile",
    "context": "..",
    "options": [
        "--secret",
        "id=prefix_dev_token,env=PREFIX_DEV_TOKEN",
    ],
    // ...
}
```

Example 4 (unknown):
```unknown
# ...
RUN --mount=type=secret,id=prefix_dev_token,uid=1000 \
    test -s /run/secrets/prefix_dev_token \
    && pixi auth login --token "$(cat /run/secrets/prefix_dev_token)" https://repo.prefix.dev
```

---

## pixi workspace export conda-explicit-spec#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/export/conda-explicit-spec/

**Contents:**
- pixi workspace export conda-explicit-spec#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Update Options#
- Global Options#

Export workspace environment to a conda explicit specification file

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace export conda-explicit-spec [OPTIONS] <OUTPUT_DIR>
```

---

## JupyterLab

**URL:** https://pixi.sh/latest/integration/editor/jupyterlab/

**Contents:**
- JupyterLab
- Basic usage#
  - What kernels are available?#
- Advanced usage#
  - Configuring JupyterLab#

Using JupyterLab with Pixi is very simple. You can just create a new Pixi workspace and add the jupyterlab package to it. The full example is provided under the following Github link.

This will create a new Pixi workspace and add the jupyterlab package to it. You can then start JupyterLab using the following command:

If you want to add more "kernels" to JupyterLab, you can simply add them to your current workspace – as well as any dependencies from the scientific stack you might need.

You can easily install more "kernels" for JupyterLab. The conda-forge repository has a number of interesting additional kernels - not just Python!

If you want to have only one instance of JupyterLab running but still want per-directory Pixi environments, you can use one of the kernels provided by the pixi-kernel package.

To get started, create a Pixi workspace, add jupyterlab and pixi-kernel and then start JupyterLab:

This will start JupyterLab and open it in your browser.

pixi-kernel searches for a manifest file, either pixi.toml or pyproject.toml, in the same directory of your notebook or in any parent directory. When it finds one, it will use the environment specified in the manifest file to start the kernel and run your notebooks.

**Examples:**

Example 1 (unknown):
```unknown
pixi init
pixi add jupyterlab
```

Example 2 (unknown):
```unknown
pixi run jupyter lab
```

Example 3 (unknown):
```unknown
pixi add bash_kernel ipywidgets matplotlib numpy pandas  # ...
```

Example 4 (unknown):
```unknown
pixi init
pixi add jupyterlab pixi-kernel
pixi run jupyter lab
```

---

## GitHub Actions

**URL:** https://pixi.sh/latest/integration/ci/github_actions/

**Contents:**
- GitHub Actions
- Usage#
- Features#
  - Caching#
  - Multiple environments#
    - Multiple environments using a matrix#
    - Install multiple environments in one job#
  - Global Environments#
  - Authentication#
    - Token#

We created prefix-dev/setup-pixi to facilitate using pixi in CI.

Pin your action versions

Since pixi is not yet stable, the API of this action may change between minor versions. Please pin the versions of this action to a specific version (i.e., prefix-dev/setup-pixi@v0.9.2) to avoid breaking changes. You can automatically update the version of this action by using Dependabot.

Put the following in your .github/dependabot.yml file to enable Dependabot for your GitHub Actions:

To see all available input arguments, see the action.yml file in setup-pixi. The most important features are described below.

The action supports caching of the project and global pixi environments. By default, project environment caching is enabled if a pixi.lock file is present. It will then use the pixi.lock file to generate a hash of the environment and cache it. If the cache is hit, the action will skip the installation and use the cached environment. You can specify the behavior by setting the cache input argument.

Global environment caching is disabled by default and can be enabled by setting the global-cache input to true. As there is no lockfile for global environments, the cache will expire at the end of every month to ensure it does not go stale.

Customize your cache key

If you need to customize your cache-key, you can use the cache-key and global-cache-key input arguments. These will be the prefixes of the cache keys. The full cache keys will be <cache-key><conda-arch>-<hash> and <global-cache-key><conda-arch>-<YYYY-MM>-<hash> respectively.

Only save caches on main

In order to not exceed the 10 GB cache size limit as fast, you might want to restrict when the cache is saved. This can be done by setting the cache-write argument.

With pixi, you can create multiple environments for different requirements. You can also specify which environment(s) you want to install by setting the environments input argument. This will install all environments that are specified and cache them.

The following example will install the py311 and py312 environments in different jobs.

The following example will install both the py311 and the py312 environment on the runner.

separated by spaces, equivalent to

Caching behavior if you don't specify environments

If you don't specify any environment, the default environment will be installed and cached, even if you use other environments.

You can specify pixi global install commands by setting the global-environments input argument. This will create one environment per line, and install them. This is useful in particular to install executables that are needed for pixi install to work properly. For instance, the keyring, or gcloud executables. The following example shows how to install both in separate global environments. By default, global environments are not cached. You can enable caching by setting the global-cache input to true.

There are currently five ways to authenticate with pixi:

For more information, see Authentication.

Handle secrets with care

Please only store sensitive information using GitHub secrets. Do not store them in your repository. When your sensitive information is stored in a GitHub secret, you can access it using the ${{ secrets.SECRET_NAME }} syntax. These secrets will always be masked in the logs.

Specify the token using the auth-token input argument. This form of authentication (bearer token in the request headers) is mainly used at prefix.dev.

Specify the username and password using the auth-username and auth-password input arguments. This form of authentication (HTTP Basic Auth) is used in some enterprise environments with artifactory for example.

Specify the conda-token using the conda-token input argument. This form of authentication (token is encoded in URL: https://my-quetz-instance.com/t/<token>/get/custom-channel) is used at anaconda.org or with quetz instances.

Specify the S3 key pair using the auth-access-key-id and auth-secret-access-key input arguments. You can also specify the session token using the auth-session-token input argument.

See the S3 section for more information about S3 authentication.

You can specify whether to use keyring to look up credentials for PyPI.

setup-pixi allows you to run command inside of the pixi environment by specifying a custom shell wrapper with shell: pixi run bash -e {0}. This can be useful if you want to run commands inside of the pixi environment, but don't want to use the pixi run command for each command.

You can even run Python scripts like this:

If you want to use PowerShell, you need to specify -Command as well.

How does it work under the hood?

Under the hood, the shell: xyz {0} option is implemented by creating a temporary script file and calling xyz with that script file as an argument. This file does not have the executable bit set, so you cannot use shell: pixi run {0} directly but instead have to use shell: pixi run bash {0}. There are some custom shells provided by GitHub that have slightly different behavior, see jobs.<job_id>.steps[*].shell in the documentation. See the official documentation and ADR 0277 for more information about how the shell: input works in GitHub Actions.

With pixi exec, you can also run a one-off command inside a temporary pixi environment.

See here for more information about pixi exec.

Instead of using a custom shell wrapper, you can also make all pixi-installed binaries available to subsequent steps by "activating" the installed environment in the currently running job. To this end, setup-pixi adds all environment variables set when executing pixi run to $GITHUB_ENV and, similarly, adds all path modifications to $GITHUB_PATH. As a result, all installed binaries can be accessed without having to call pixi run.

If you are installing multiple environments, you will need to specify the name of the environment that you want to be activated.

Activating an environment may be more useful than using a custom shell wrapper as it allows non-shell based steps to access binaries on the path. However, be aware that this option augments the environment of your job.

You can specify whether setup-pixi should run pixi install --frozen or pixi install --locked depending on the frozen or the locked input argument. See the official documentation for more information about the --frozen and --locked flags.

If you don't specify anything, the default behavior is to run pixi install --locked if a pixi.lock file is present and pixi install otherwise.

There are two types of debug logging that you can enable.

The first one is the debug logging of the action itself. This can be enabled by for the action by re-running the action in debug mode:

Debug logging documentation

For more information about debug logging in GitHub Actions, see the official documentation.

The second type is the debug logging of the pixi executable. This can be specified by setting the log-level input.

If nothing is specified, log-level will default to default or vv depending on if debug logging is enabled for the action.

On self-hosted runners, it may happen that some files are persisted between jobs. This can lead to problems or secrets getting leaked between job runs. To avoid this, you can use the post-cleanup input to specify the post cleanup behavior of the action (i.e., what happens after all your commands have been executed).

If you set post-cleanup to true, the action will delete the following files:

If nothing is specified, post-cleanup will default to true.

On self-hosted runners, you also might want to alter the default pixi install location to a temporary location. You can use pixi-bin-path: ${{ runner.temp }}/bin/pixi to do this.

You can also use a preinstalled local version of pixi on the runner by not setting any of the pixi-version, pixi-url or pixi-bin-path inputs. This action will then try to find a local version of pixi in the runner's PATH.

setup-pixi will automatically pick up the pyproject.toml if it contains a [tool.pixi.workspace] section and no pixi.toml. This can be overwritten by setting the manifest-path input argument.

If you only want to install pixi and not install the current workspace, you can use the run-install option.

You can also download pixi from a custom URL by setting the pixi-url input argument. Optionally, you can combine this with the pixi-url-headers input argument to supply additional headers for the download request, such as a bearer token.

The pixi-url input argument can also be a Handlebars template string. It will be rendered with the following variables:

By default, pixi-url is equivalent to the following template:

Alternatively to setting the inputs in the with section, you can also set each of them using environment variables. The corresponding environment variable names are derived from the input names by converting them to uppercase, replacing hyphens with underscores, and prefixing them with SETUP_PIXI_.

For example, the pixi-bin-path input can be set using the SETUP_PIXI_PIXI_BIN_PATH environment variable.

This is particularly useful if executing the action on a self-hosted runner.

Inputs always take precedence over environment variables.

If you want to see more examples, you can take a look at the GitHub Workflows of the setup-pixi repository.

**Examples:**

Example 1 (unknown):
```unknown
- uses: prefix-dev/setup-pixi@v0.9.2
  with:
    pixi-version: v0.59.0
    cache: true
    auth-host: prefix.dev
    auth-token: ${{ secrets.PREFIX_DEV_TOKEN }}
- run: pixi run test
```

Example 2 (unknown):
```unknown
version: 2
updates:
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: monthly # (1)!
    groups:
      dependencies:
        patterns:
          - "*"
```

Example 3 (unknown):
```unknown
- uses: prefix-dev/setup-pixi@v0.9.2
  with:
    cache: true
    cache-write: ${{ github.event_name == 'push' && github.ref_name == 'main' }}
```

Example 4 (unknown):
```unknown
[workspace]
name = "my-package"
channels = ["conda-forge"]
platforms = ["linux-64"]

[dependencies]
python = ">=3.11"
pip = "*"
polars = ">=0.14.24,<0.21"

[feature.py311.dependencies]
python = "3.11.*"
[feature.py312.dependencies]
python = "3.12.*"

[environments]
py311 = ["py311"]
py312 = ["py312"]
```

---

## Pixi Diff-to-markdown

**URL:** https://pixi.sh/latest/integration/ci/updates_github_actions/

**Contents:**
- Pixi Diff-to-markdown
- How to use#
- Triggering CI in automated PRs#
- Customizing the summary#
- Using reusable workflows#

You can leverage GitHub Actions in combination with pavelzw/pixi-diff-to-markdown to automatically update your lockfiles similar to dependabot or renovate in other ecosystems.

Dependabot/Renovate support for pixi

You can track native Dependabot support for pixi in dependabot/dependabot-core #2227.

To get started, create a new GitHub Actions workflow file in your repository.

In order for this workflow to work, you need to set "Allow GitHub Actions to create and approve pull requests" to true in your repository settings (in "Actions" -> "General").

If you don't have any pypi-dependencies, you can use pixi update --json --no-install to speed up diff generation.

In order to prevent accidental recursive GitHub Workflow runs, GitHub decided to not trigger any workflows on automated PRs when using the default GITHUB_TOKEN. There are a couple of ways how to work around this limitation. You can find excellent documentation for this in peter-evans/create-pull-request, see here.

You can customize the summary by either using command-line-arguments of pixi-diff-to-markdown or by specifying the configuration in pixi.toml under [tool.pixi-diff-to-markdown]. See the pixi-diff-to-markdown documentation or run pixi-diff-to-markdown --help for more information.

If you want to use the same workflow in multiple repositories in your GitHub organization, you can create a reusable workflow. You can find more information in the GitHub documentation.

**Examples:**

Example 1 (unknown):
```unknown
name: Update lockfiles

permissions: # (1)!
  contents: write
  pull-requests: write

on:
  workflow_dispatch:
  schedule:
    - cron: 0 5 1 * * # (2)!

jobs:
  pixi-update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up pixi
        uses: prefix-dev/setup-pixi@v0.8.3
        with:
          run-install: false
      - name: Update lockfiles
        run: |
          set -o pipefail
          pixi update --json | pixi exec pixi diff-to-markdown >> diff.md
      - name: Create pull request
        uses: peter-evans/create-pull-request@v7
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: Update pixi lockfile
          title: Update pixi lockfile
          body-path: diff.md
          branch: update-pixi
          base: main
          labels: pixi
          delete-branch: true
          add-paths: pixi.lock
```

---
