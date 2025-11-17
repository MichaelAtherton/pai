# Pixi - Concepts

**Pages:** 17

---

## pixi workspace export conda-environment#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/export/conda-environment/

**Contents:**
- pixi workspace export conda-environment#
- About#
- Usage#
- Arguments#
- Options#
- Global Options#

Export workspace environment to a conda environment.yaml file

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace export conda-environment [OPTIONS] [OUTPUT_PATH]
```

---

## pixi run#

**URL:** https://pixi.sh/latest/reference/cli/pixi/run/

**Contents:**
- pixi run#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Update Options#
- Global Options#
- Description#
- Examples#

Runs task in the pixi environment

Runs task in the pixi environment.

This command is used to run tasks in the pixi environment. It will activate the environment and run the task in the environment. It is using the deno_task_shell to run the task.

pixi run will also update the lockfile and install the environment if it is required.

In pixi the deno_task_shell is the underlying runner of the run command. Checkout their documentation for the syntax and available commands. This is done so that the run commands can be run across all platforms.

Cross environment tasks

If you're using the depends-on feature of the tasks, the tasks will be run in the order you specified them. The depends-on can be used cross environment, e.g. you have this pixi.toml:

Then you're able to run the build from the build environment and start from the default environment. By only calling: pixi run start

**Examples:**

Example 1 (unknown):
```unknown
pixi run [OPTIONS] [TASK]...
```

Example 2 (unknown):
```unknown
pixi run python
pixi run cowpy "Hey pixi user"
pixi run --manifest-path ~/myworkspace/pixi.toml python
pixi run --frozen python
pixi run --locked python
# If you have specified a custom task in the pixi.toml you can run it with run as well
pixi run build
# Extra arguments will be passed to the tasks command.
pixi run task argument1 argument2
# Skip dependencies of the task
pixi run --skip-deps task
# Run in dry-run mode to see the commands that would be run
pixi run --dry-run task

# If you have multiple environments you can select the right one with the --environment flag.
pixi run --environment cuda python

# THIS DOESN'T WORK ON WINDOWS
# If you want to run a command in a clean environment you can use the --clean-env flag.
# The PATH should only contain the pixi environment here.
pixi run --clean-env "echo \$PATH"
```

Example 3 (unknown):
```unknown
[tasks]
start = { cmd = "python start.py", depends-on = ["build"] }

[feature.build.tasks]
build = "cargo build"
[feature.build.dependencies]
rust = ">=1.74"

[environments]
build = ["build"]
```

Example 4 (unknown):
```unknown
pixi run start
```

---

## Pixi Manifest

**URL:** https://pixi.sh/latest/reference/pixi_manifest/

**Contents:**
- Pixi Manifest
- Manifest discovery#
- The workspace table#
  - channels#
  - platforms#
  - name (optional)#
  - version (optional)#
  - authors (optional)#
  - description (optional)#
  - license (optional)#

The pixi.toml is the workspace manifest, also known as the Pixi workspace configuration file. It specifies environments for a workspace, and the package dependency requirements for those environments. It can also specify tasks which can run in those environments, as well as many other configuration options.

A toml file is structured in different tables. This document will explain the usage of the different tables.

We also support the pyproject.toml file. It has the same structure as the pixi.toml file. except that you need to prepend the tables with tool.pixi instead of just the table name. For example, the [workspace] table becomes [tool.pixi.workspace]. There are also some small extras that are available in the pyproject.toml file, checkout the pyproject.toml documentation for more information.

The manifest can be found at the following locations.

If multiple locations exist, the manifest with the highest priority will be used.

The minimally required information in the workspace table is:

This is a list that defines the channels used to fetch the packages from. If you want to use channels hosted on anaconda.org you only need to use the name of the channel directly.

Channels situated on the file system are also supported with absolute file paths:

To access private or public channels on prefix.dev or Quetz use the url including the hostname:

Defines the list of platforms that the workspace supports. Pixi solves the dependencies for all these platforms and puts them in the lock file (pixi.lock).

The available platforms are listed here: link

Special macOS behavior

macOS has two platforms: osx-64 for Intel Macs and osx-arm64 for Apple Silicon Macs. To support both, include both in your platforms list. Fallback: If osx-arm64 can't resolve, use osx-64. Running osx-64 on Apple Silicon uses Rosetta for Intel binaries.

The name of the workspace. If the name is not specified, the name of the directory that contains the workspace is used.

The version of the workspace. This should be a valid version based on the conda Version Spec. See the version documentation, for an explanation of what is allowed in a Version Spec.

This is a list of authors of the workspace.

This should contain a short description of the workspace.

The license as a valid SPDX string (e.g. MIT AND Apache-2.0)

Relative path to the license file.

Relative path to the README file.

URL of the workspace homepage.

URL of the workspace source repository.

URL of the workspace documentation.

Mapping of channel name or URL to location of mapping that can be URL/Path. Mapping should be structured in json format where conda_name: pypi_package_name. Example:

If conda-forge is not present in conda-pypi-map pixi will use prefix.dev mapping for it.

This is the setting for the priority of the channels in the solver step.

We strongly recommend not to switch the default.

disabled: There is no priority, all package variants from all channels will be set per package name and solved as one. Care should be taken when using this option. Since package variants can come from any channel when you use this mode, packages might not be compatible. This can cause hard to debug ABI incompatibilities.

We strongly discourage using this option.

channel-priority = "disabled" is a security risk

Disabling channel priority may lead to unpredictable dependency resolutions. This is a possible security risk as it may lead to packages being installed from unexpected channels. It's advisable to maintain the default strict setting and order channels thoughtfully. If necessary, specify a channel directly for a dependency. [workspace] # Putting conda-forge first solves most issues channels = ["conda-forge", "channel-name"] [dependencies] package = {version = "*", channel = "channel-name"}

This is the setting for the strategy used in the solver step.

When multiple features used in an environment set a specific solve strategy, the one from the left-most feature declared in the environment is used. [feature.one] solve-strategy = "lowest" [feature.two] solve-strategy = "lowest-direct" [environments] combined = ["two", "one"] # <- The solve strategy from feature `two` is used

The required version spec for pixi itself to resolve and build the workspace. If unset (Default), any version is ok. If set, it must be a string to a valid conda version spec, and the version of a running pixi must match the required spec before resolving or building the workspace, or exit with an error when not match.

For example, with the following manifest, pixi shell will fail on pixi 0.39.0, but success after upgrading to pixi 0.40.0:

The upper bound can also be limit like this:

This option should be used to improve the reproducibility of building the workspace. A complicated requirement spec may be an obstacle to setup the building environment.

When specified this will exclude any package from consideration that is newer than the specified date. This is useful to reproduce installations regardless of new package releases.

The date may be specified in the following formats:

Both PyPi and conda packages are considered.

!! note Note that for Pypi package indexes the package index must support the upload-time field as specified in PEP 700. If the field is not present for a given distribution, the distribution will be treated as unavailable. PyPI provides upload-time for all packages.

Build variants require the pixi-build preview feature to be enabled: [workspace] preview = ["pixi-build"]

Build variants allow you to specify different dependency versions for building packages in your workspace, creating a "build matrix" that targets multiple configurations. This is particularly useful for testing packages against different compiler versions, Python versions, or other critical dependencies.

Build variants are defined as key-value pairs where each key represents a dependency name and the value is a list of version specifications to build against.

When build variants are specified, Pixi will:

Build variants can also be specified per-platform:

For detailed examples and tutorials, see the build variants documentation.

Build variant files require the pixi-build preview feature to be enabled: [workspace] preview = ["pixi-build"]

Use build-variants-files to reference external variant definitions from YAML files. Paths are resolved relative to the workspace root and processed in the listed order—entries from earlier files take precedence over values loaded from later ones.

Each entry must point to either a conda_build_config.yaml or another .yaml file that defines build variants. If the file is called conda_build_config.yaml, it will attempt to parse it with a subset of conda-build's variant syntax. Otherwise, it will use rattler-build's syntax as outlined in the rattler-build documentation.

Tasks are a way to automate certain custom commands in your workspace. For example, a lint or format step. Tasks in a Pixi workspace are essentially cross-platform shell commands, with a unified syntax across platforms. For more in-depth information, check the Advanced tasks documentation. Pixi's tasks are run in a Pixi environment using pixi run and are executed using the deno_task_shell.

You can modify this table using pixi task.

Specify different tasks for different platforms using the target table

If you want to hide a task from showing up with pixi task list or pixi info, you can prefix the name with _. For example, if you want to hide depending, you can rename it to _depending.

The system requirements are used to define minimal system specifications used during dependency resolution.

For example, we can define a unix system with a specific minimal libc version. [system-requirements] libc = "2.28" or make the workspace depend on a specific version of cuda: [system-requirements] cuda = "12"

More information in the system requirements documentation.

The pypi-options table is used to define options that are specific to PyPI registries. These options can be specified either at the root level, which will add it to the default options feature, or on feature level, which will create a union of these options when the features are included in the environment.

The options that can be defined are:

These options are explained in the sections below. Most of these options are taken directly or with slight modifications from the uv settings. If any are missing that you need feel free to create an issue requesting them.

Strict Index Priority

Unlike pip, because we make use of uv, we have a strict index priority. This means that the first index is used where a package can be found. The order is determined by the order in the toml file. Where the extra-index-urls are preferred over the index-url. Read more about this on the uv docs

Often you might want to use an alternative or extra index for your workspace. This can be done by adding the pypi-options table to your pixi.toml file, the following options are available:

There are some examples in the Pixi repository, that make use of this feature.

Authentication Methods

To read about existing authentication methods for private registries, please check the PyPI Authentication section.

Even though build isolation is a good default. One can choose to not isolate the build for a certain package name, this allows the build to access the pixi environment. This is convenient if you want to use torch or something similar for your build-process.

Setting no-build-isolation also affects the order in which PyPI packages are installed. Packages are installed in that order: - conda packages in one go - packages with build isolation in one go - packages without build isolation installed in the order they are added to no-build-isolation

It is also possible to remove all packages from build isolation by setting the no-build-isolation to true.

Conda dependencies define the build environment

To use no-build-isolation effectively, use conda dependencies to define the build environment. These are installed before the PyPI dependencies are resolved, this way these dependencies are available during the build process. In the example above adding torch as a PyPI dependency would be ineffective, as it would not yet be installed during the PyPI resolution phase.

When enabled, resolving will not run arbitrary Python code. The cached wheels of already-built source distributions will be reused, but operations that require building distributions will exit with an error.

Can be either set per package or globally. [pypi-options] # No sdists allowed no-build = true # default is false or: [pypi-options] no-build = ["package1", "package2"]

When features are merged, the following priority is adhered: no-build = true > no-build = ["package1", "package2"] > no-build = false So, to expand: if no-build = true is set for any feature in the environment, this will be used as the setting for the environment.

Don't install pre-built wheels.

The given packages will be built and installed from source. The resolver will still use pre-built wheels to extract package metadata, if available.

Can be either set per package or globally.

[pypi-options] # Never use pre-build wheels no-binary = true # default is false or: [pypi-options] no-binary = ["package1", "package2"]

When features are merged, the following priority is adhered: no-binary = true > no-binary = ["package1", "package2"] > no-binary = false So, to expand: if no-binary = true is set for any feature in the environment, this will be used as the setting for the environment.

The strategy to use when resolving against multiple index URLs. Description modified from the uv documentation:

By default, uv and thus pixi, will stop at the first index on which a given package is available, and limit resolutions to those present on that first index (first-match). This prevents dependency confusion attacks, whereby an attack can upload a malicious package under the same name to a secondary index.

One index strategy per environment

Only one index-strategy can be defined per environment or solve-group, otherwise, an error will be shown.

The index-strategy only changes PyPI package resolution and not conda package resolution.

For more detail regarding the dependency types, make sure to check the Run, Host, Build dependency documentation.

This section defines what dependencies you would like to use for your workspace.

There are multiple dependencies tables. The default is [dependencies], which are dependencies that are shared across platforms.

Dependencies are defined using a VersionSpec. A VersionSpec combines a Version with an optional operator.

Dependencies can also be defined as a mapping where it is using a matchspec:

The dependencies can be easily added using the pixi add command line. Running add for an existing dependency will replace it with the newest it can use.

To specify different dependencies for different platforms use the target table

Add any conda package dependency that you want to install into the environment. Don't forget to add the channel to the workspace table should you use anything different than conda-forge. Even if the dependency defines a channel that channel should be added to the workspace.channels list.

We use uv, which is a new fast pip replacement written in Rust.

We integrate uv as a library, so we use the uv resolver, to which we pass the conda packages as 'locked'. This disallows uv from installing these dependencies itself, and ensures it uses the exact version of these packages in the resolution. This is unique amongst conda based package managers, which usually just call pip from a subprocess.

The uv resolution is included in the lock file directly.

Pixi directly supports depending on PyPI packages, the PyPA calls a distributed package a 'distribution'. There are Source and Binary distributions both of which are supported by pixi. These distributions are installed into the environment after the conda environment has been resolved and installed. PyPI packages are not indexed on prefix.dev but can be viewed on pypi.org.

Important considerations

These dependencies don't follow the conda matchspec specification. The version is a string specification of the version according to PEP404/PyPA. Additionally, a list of extra's can be included, which are essentially optional dependencies. Note that this version is distinct from the conda MatchSpec type. See the example below to see how this is used in practice:

When using SSH URLs in git dependencies, make sure to have your SSH key added to your SSH agent. You can do this by running ssh-add which will prompt you for your SSH key passphrase. Make sure that the ssh-add agent or service is running and you have a generated public/private SSH key. For more details on how to do this, check the Github SSH documentation.

The full specification of a PyPI dependencies that Pixi supports can be split into the following fields:

A list of extras to install with the package. e.g. ["dataframe", "sql"] The extras field works with all other version specifiers as it is an addition to the version specifier.

The version of the package to install. e.g. ">=1.0.0" or * which stands for any version, this is Pixi specific. Version is our default field so using no inline table ({}) will default to this field.

The index parameter allows you to specify the URL of a custom package index for the installation of a specific package. This feature is useful when you want to ensure that a package is retrieved from a particular source, rather than from the default index.

For example, to use some other than the official Python Package Index (PyPI) at https://pypi.org/simple, you can use the index parameter:

This is useful for PyTorch specifically, as the registries are pinned to different CUDA versions. Learn more about installing PyTorch here.

A git repository to install from. This support both https:// and ssh:// urls.

Use git in combination with rev or subdirectory:

A local path to install from. e.g. path = "./path/to/package" We would advise to keep your path projects in the workspace, and to use a relative path.

Set editable to true to install in editable mode, this is highly recommended as it is hard to reinstall if you're not using editable mode. e.g. editable = true

A URL to install a wheel or sdist directly from an url.

Use the --pypi flag with the add command to quickly add PyPI packages from the CLI. E.g pixi add --pypi flask

This does not support all the features of the pypi-dependencies table yet.

The Source Distribution Format is a source based format (sdist for short), that a package can include alongside the binary wheel format. Because these distributions need to be built, the need a python executable to do this. This is why python needs to be present in a conda environment. Sdists usually depend on system packages to be built, especially when compiling C/C++ based python bindings. Think for example of Python SDL2 bindings depending on the C library: SDL2. To help built these dependencies we activate the conda environment that includes these pypi dependencies before resolving. This way when a source distribution depends on gcc for example, it's used from the conda environment instead of the system.

The activation table is used for specialized activation operations that need to be run when the environment is activated.

There are two types of activation operations a user can modify in the manifest:

These activation operations will be run before the pixi run and pixi shell commands.

The script specified in the scripts section are not directly sourced in the pixi shell, but rather they are called, and the environment variables they set are then set in the pixi shell, so any defined function or other non-environment variable modification to the environment will be ignored.

The activation operations are run by the system shell interpreter as they run before an environment is available. This means that it runs as cmd.exe on windows and bash on linux and osx (Unix). Only .sh, .bash and .bat files are supported.

And the environment variables are set in the shell that is running the activation script, thus take note when using e.g. $ or %.

If you have scripts or env variable per platform use the target table.

The target table is a table that allows for platform specific configuration. Allowing you to make different sets of tasks or dependencies per platform.

The target table is currently implemented for the following sub-tables:

The target table is defined using [target.PLATFORM.SUB-TABLE]. E.g [target.linux-64.dependencies]

The platform can be any of:

The sub-table can be any of the specified above.

To make it a bit more clear, let's look at an example below. Currently, Pixi combines the top level tables like dependencies with the target-specific ones into a single set. Which, in the case of dependencies, can both add or overwrite dependencies. In the example below, we have cmake being used for all targets but on osx-64 or osx-arm64 a different version of python will be selected.

Here are some more examples:

The feature table allows you to define features that can be used to create different [environments]. The [environments] table allows you to define different environments. The design is explained in the this design document.

This will create an environment called test that has pytest installed.

The feature table allows you to define the following fields per feature.

These tables are all also available without the feature prefix. When those are used we call them the default feature. This is a protected name you can not use for your own feature.

The [environments] table allows you to define environments that are created using the features defined in the [feature] tables.

The environments table is defined using the following fields:

Full environments table specification[environments] test = {features = ["test"], solve-group = "test"} prod = {features = ["prod"], solve-group = "test"} lint = {features = ["lint"], no-default-feature = true} As shown in the example above, in the simplest of cases, it is possible to define an environment only by listing its features:

When an environment comprises several features (including the default feature):

The global configuration options are documented in the global configuration section.

Pixi sometimes introduces new features that are not yet stable, but that we would like for users to test out. These features are called preview features. Preview features are disabled by default and can be enabled by setting the preview field in the workspace manifest. The preview field is an array of strings that specify the preview features to enable, or the boolean value true to enable all preview features.

An example of a preview feature in the manifest:

Preview features in the documentation will be marked as such on the relevant pages.

pixi-build is a preview feature, and will change until it is stabilized. Please keep that in mind when you use it for your workspaces. [workspace] preview = ["pixi-build"]

The package section can be added to a workspace manifest to define the package that is built by Pixi.

A package section needs to be inside a workspace, either in the same manifest file as the [workspace] table or in a sub folder pixi.toml/pyproject.toml file.

These packages will be built into a conda package that can be installed into a conda environment. The package section is defined using the following fields:

And to extend the basics, it can also contain the following fields:

Workspace inheritance

Most extra fields can be inherited from the workspace manifest. This means that you can define the description, authors, license in the workspace manifest, and they will be inherited by the package manifest. [workspace] name = "my-workspace" [package] name = { workspace = true } # Inherit the name from the workspace

The build system specifies how the package can be built. The build system is a table that can contain the following fields:

More documentation on the backends can be found in the build backend documentation.

The dependencies of a package are split into three tables. Each of these tables has a different purpose and is used to define the dependencies of the package.

Build dependencies are required in the build environment and contain all tools that are not needed on the host of the package.

Following packages are examples of typical build dependencies:

When using SSH URLs in git dependencies, make sure to have your SSH key added to your SSH agent. You can do this by running ssh-add which will prompt you for your SSH key passphrase. Make sure that the ssh-add agent or service is running and you have a generated public/private SSH key. For more details on how to do this, check the Github SSH documentation.

Host dependencies are required during build phase, but in contrast to build packages they have to be present on the host.

Following packages are typical examples for host dependencies:

The run-dependencies are the packages that will be installed in the environment when the package is run.

**Examples:**

Example 1 (unknown):
```unknown
[workspace]
channels = ["conda-forge"]
name = "project-name"
platforms = ["linux-64"]
```

Example 2 (unknown):
```unknown
channels = ["conda-forge", "robostack", "bioconda", "nvidia", "pytorch"]
```

Example 3 (unknown):
```unknown
channels = ["conda-forge", "file:///home/user/staged-recipes/build_artifacts"]
```

Example 4 (unknown):
```unknown
channels = ["conda-forge", "https://repo.prefix.dev/channel-name"]
```

---

## pixi workspace environment list#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/environment/list/

**Contents:**
- pixi workspace environment list#
- About#
- Usage#

List the environments in the manifest file

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace environment list
```

---

## Multi Environment

**URL:** https://pixi.sh/latest/workspace/multi_environment/

**Contents:**
- Multi Environment
  - Motivating Example#
- Design Considerations#
  - Feature & Environment Set Definitions#
  - lock file Structure#
  - User Interface Environment Activation#
  - Ambiguous Environment Selection#
- Initial write-up#
- Real world example use cases#

There are multiple scenarios where multiple environments are useful.

This prepares pixi for use in large workspaces with multiple use-cases, multiple developers and different CI needs.

There are a few things we wanted to keep in mind in the design:

Introduce environment sets into the pixi.toml this describes environments based on features. Introduce features into the pixi.toml that can describe parts of environments. As an environment goes beyond just dependencies the feature fields can be described by including the following fields:

The environment definition should contain the following fields:

Within the pixi.lock file, a package may now include an additional environments field, specifying the environment to which it belongs. To avoid duplication the packages environments field may contain multiple environments so the lock file is of minimal size.

Users can manually activate the desired environment via command line or configuration. This approach guarantees a conflict-free environment by allowing only one feature set to be active at a time. For the user the cli would look like this:

It's possible to define tasks in multiple environments, in this case the user should be prompted to select the environment.

Here is a simple example of a task only manifest:

pixi.toml[workspace] name = "test_ambiguous_env" channels = [] platforms = ["linux-64", "win-64", "osx-64", "osx-arm64"] [tasks] default = "echo Default" ambi = "echo Ambi::Default" [feature.test.tasks] test = "echo Test" ambi = "echo Ambi::Test" [feature.dev.tasks] dev = "echo Dev" ambi = "echo Ambi::Dev" [environments] default = ["test", "dev"] test = ["test"] dev = ["dev"] Trying to run the ambi task will prompt the user to select the environment. As it is available in all environments.

As you can see it runs the task defined in the feature.task but it is run in the default environment. This happens because the ambi task is defined in the test feature, and it is overwritten in the default environment. So the tasks.default is now non-reachable from any environment.

Some other results running in this example: ➜ pixi run --environment test ambi ✨ Pixi task (ambi in test): echo Ambi::Test Ambi::Test ➜ pixi run --environment dev ambi ✨ Pixi task (ambi in dev): echo Ambi::Dev Ambi::Dev # dev is run in the default environment ➜ pixi run dev ✨ Pixi task (dev in default): echo Dev Dev # dev is run in the dev environment ➜ pixi run -e dev dev ✨ Pixi task (dev in dev): echo Dev Dev

Initial write-up of the proposal: GitHub Gist by 0xbe7a

In polarify they want to test multiple versions combined with multiple versions of polars. This is currently done by using a matrix in GitHub actions. This can be replaced by using multiple environments.

This is an example of a workspace that has a test feature and prod environment. The prod environment is a production environment that contains the run dependencies. The test feature is a set of dependencies and tasks that we want to put on top of the previously solved prod environment. This is a common use case where we want to test the production environment with additional dependencies.

pixi.toml[workspace] name = "my-app" # ... channels = ["conda-forge"] platforms = ["osx-arm64", "linux-64"] [tasks] postinstall-e = "pip install --no-build-isolation --no-deps --disable-pip-version-check -e ." postinstall = "pip install --no-build-isolation --no-deps --disable-pip-version-check ." dev = "uvicorn my_app.app:main --reload" serve = "uvicorn my_app.app:main" [dependencies] python = ">=3.12" pip = "*" pydantic = ">=2" fastapi = ">=0.105.0" sqlalchemy = ">=2,<3" uvicorn = "*" aiofiles = "*" [feature.test.dependencies] pytest = "*" pytest-md = "*" pytest-asyncio = "*" [feature.test.tasks] test = "pytest --md=report.md" [environments] # both default and prod will have exactly the same dependency versions when they share a dependency default = {features = ["test"], solve-group = "prod-group"} prod = {features = [], solve-group = "prod-group"} In ci you would run the following commands: pixi run postinstall-e && pixi run test Locally you would run the following command: pixi run postinstall-e && pixi run dev

Then in a Dockerfile you would run the following command: DockerfileFROM ghcr.io/prefix-dev/pixi:latest # this doesn't exist yet WORKDIR /app COPY . . RUN pixi run --environment prod postinstall EXPOSE 8080 CMD ["/usr/local/bin/pixi", "run", "--environment", "prod", "serve"]

This is an example for an ML workspace that should be executable on a machine that supports cuda and mlx. It should also be executable on machines that don't support cuda or mlx, we use the cpu feature for this.

**Examples:**

Example 1 (unknown):
```unknown
[dependencies] # short for [feature.default.dependencies]
python = "*"
numpy = "==2.3"

[pypi-dependencies] # short for [feature.default.pypi-dependencies]
pandas = "*"

[system-requirements] # short for [feature.default.system-requirements]
libc = "2.33"

[activation] # short for [feature.default.activation]
scripts = ["activate.sh"]
```

Example 2 (unknown):
```unknown
[feature.py39.dependencies]
python = "~=3.9.0"
[feature.py310.dependencies]
python = "~=3.10.0"
[feature.test.dependencies]
pytest = "*"
```

Example 3 (unknown):
```unknown
[feature.cuda]
dependencies = {cuda = "x.y.z", cudnn = "12.0"}
pypi-dependencies = {torch = "1.9.0"}
platforms = ["linux-64", "osx-arm64"]
activation = {scripts = ["cuda_activation.sh"]}
system-requirements = {cuda = "12"}
# Channels concatenate using a priority instead of overwrite, so the default channels are still used.
# Using the priority the concatenation is controlled, default is 0, the default channels are used last.
# Highest priority comes first.
channels = ["nvidia", {channel = "pytorch", priority = -1}] # Results in:  ["nvidia", "conda-forge", "pytorch"] when the default is `conda-forge`
tasks = { warmup = "python warmup.py" }
target.osx-arm64 = {dependencies = {mlx = "x.y.z"}}
```

Example 4 (unknown):
```unknown
[feature.test.tasks]
test = "pytest"

[environments]
test = ["test"]

# `pixi run test` == `pixi run --environment test test`
```

---

## pixi task add#

**URL:** https://pixi.sh/latest/reference/cli/pixi/task/add/

**Contents:**
- pixi task add#
- About#
- Usage#
- Arguments#
- Options#
- Examples#

Add a command to the workspace

This adds the following to the manifest file:

Which you can then run with the run command:

**Examples:**

Example 1 (unknown):
```unknown
pixi task add [OPTIONS] <NAME> <COMMAND>...
```

Example 2 (unknown):
```unknown
pixi task add cow cowpy "Hello User"
pixi task add tls ls --cwd tests
pixi task add test cargo t --depends-on build
pixi task add build-osx "METAL=1 cargo build" --platform osx-64
pixi task add train python train.py --feature cuda
pixi task add publish-pypi "hatch publish --yes --repo main" --feature build --env HATCH_CONFIG=config/hatch.toml --description "Publish the package to pypi"
```

Example 3 (unknown):
```unknown
[tasks]
cow = "cowpy \"Hello User\""
tls = { cmd = "ls", cwd = "tests" }
test = { cmd = "cargo t", depends-on = ["build"] }

[target.osx-64.tasks]
build-osx = "METAL=1 cargo build"

[feature.cuda.tasks]
train = "python train.py"

[feature.build.tasks]
publish-pypi = { cmd = "hatch publish --yes --repo main", env = { HATCH_CONFIG = "config/hatch.toml" }, description = "Publish the package to pypi" }
```

Example 4 (unknown):
```unknown
pixi run cow
# Extra arguments will be passed to the tasks command.
pixi run test --test test1
```

---

## Environments

**URL:** https://pixi.sh/latest/workspace/environment/

**Contents:**
- Environments
- Activation#
- Traditional conda activate-like activation#
- Structure#
  - Environment Installation Metadata#
  - Cleaning up#
- Solving environments#
- Caching packages#

Pixi is a tool to manage environments. This document explains what an environment looks like and how to use it.

An environment is nothing more than a set of files that are installed into a certain location, that somewhat mimics a global system install. You need to activate the environment to use it. In the most simple sense that mean adding the bin directory of the environment to the PATH variable. But there is more to it in a conda environment, as it also sets some environment variables.

To do the activation we have multiple options:

Where the run command is special as it runs its own cross-platform shell and has the ability to run tasks. More information about tasks can be found in the tasks documentation.

Using the pixi shell-hook in Pixi you would get the following output:

It sets the PATH and some more environment variables. But more importantly it also runs activation scripts that are presented by the installed packages. An example of this would be the libglib_activate.sh script. Thus, just adding the bin directory to the PATH is not enough.

Shell used for activation: - On Windows, Pixi executes activation under cmd.exe. - On Linux and macOS, Pixi executes activation under bash.

This affects both [activation.env] and activation.scripts: they are applied by the platform's shell during activation, before any task runs.

You can modify the activation with the activation table in the manifest, you can add more activation scripts or inject environment variables into the activation scripts. [activation.env] # Python users often set: PYTHONIOENCODING = "utf-8" PYTHONNOUSERSITE = "1" # R users often set: PIXI_R_LIBS = "$CONDA_PREFIX/lib/R/library" R_LIBS = "$PIXI_R_LIBS" R_LIBS_USER = "$PIXI_R_LIBS" [target.unix.activation] # Use sh scripts on unix scripts = [ # Common in the ROS workspaces "install/setup.sh", # Want to add some personal scripts to the activation: "activation.sh", ] # Use batch scripts on windows [target.win.activation] scripts = ["install/setup.bat"] Find the reference for the activation table here.

If you prefer to use the traditional conda activate-like activation, you can use the pixi shell-hook command.

For example, with bash and zsh you can use the following command:

With the --manifest-path option you can also specify which environment to activate. If you want to add a bash function to your ~/.bashrc that will activate the environment, you can use the following command:

After adding this function to your ~/.bashrc/~/.zshrc, you can activate the environment by running:

With fish, you can also evaluate the output of pixi shell-hook:

Or, if you want to add a function to your ~/.config/fish/config.fish:

function pixi_activate # default to current directory if no path is given set -l manifest_path $argv[1] test -z "$manifest_path"; and set manifest_path "." pixi shell-hook --manifest-path "$manifest_path" | source end After adding this function to your ~/.config/fish/config.fish, you can activate the environment by running:

See our direnv page on how to leverage pixi shell-hook to integrate with direnv.

A Pixi environment is located in the .pixi/envs directory of the workspace by default. This keeps your machine and your workspace clean and isolated from each other, and makes it easy to clean up after a workspace is done. While this structure is generally recommended, environments can also be stored outside of workspace directories by enabling detached environments.

If you look at the .pixi/envs directory, you will see a directory for each environment, the default being the one that is normally used, if you specify a custom environment the name you specified will be used.

These directories are conda environments, and you can use them as such, but you cannot manually edit them, this should always go through the pixi.toml. Pixi will always make sure the environment is in sync with the pixi.lock file. If this is not the case then all the commands that use the environment will automatically update the environment, e.g. pixi run, pixi shell.

On environment installation, Pixi will write a small file to the environment that contains some metadata about installation. This file is called pixi and is located in the conda-meta folder of the environment. This file contains the following information:

The environment_lock_file_hash is used to check if the environment is in sync with the pixi.lock file. If the hash of the pixi.lock file is different from the hash in the pixi file, Pixi will update the environment.

This is used to speedup activation, in order to trigger a full revalidation and installation use pixi install or pixi reinstall. A broken environment would typically not be found with a hash comparison, but a revalidation would reinstall the environment. By default, all lock file modifying commands will always use the revalidation and on pixi install it always revalidates.

If you want to clean up the environments, you can simply delete the .pixi/envs directory, and Pixi will recreate the environments when needed.

When you run a command that uses the environment, Pixi will check if the environment is in sync with the pixi.lock file. If it is not, Pixi will solve the environment and update it. This means that Pixi will retrieve the best set of packages for the dependency requirements that you specified in the pixi.toml and will put the output of the solve step into the pixi.lock file. Solving is a mathematical problem and can take some time, but we take pride in the way we solve environments, and we are confident that we can solve your environment in a reasonable time. If you want to learn more about the solving process, you can read these:

Pixi solves both the conda and PyPI dependencies, where the PyPI dependencies use the conda packages as a base, so you can be sure that the packages are compatible with each other. These solvers are split between the rattler and uv library, these control the heavy lifting of the solving process, which is executed by our custom SAT solver: resolvo. resolvo is able to solve multiple ecosystem like conda and PyPI. It implements the lazy solving process for PyPI packages, which means that it only downloads the metadata of the packages that are needed to solve the environment. It also supports the conda way of solving, which means that it downloads the metadata of all the packages at once and then solves in one go.

For the [pypi-dependencies], uv implements sdist building to retrieve the metadata of the packages, and wheel building to install the packages. For this building step, pixi requires to first install python in the (conda)[dependencies] section of the pixi.toml file. This will always be slower than the pure conda solves. So for the best Pixi experience you should stay within the [dependencies] section of the pixi.toml file.

Pixi caches all previously downloaded packages in a cache folder. This cache folder is shared between all Pixi workspaces and globally installed tools.

Normally the location would be the following platform-specific default cache folder:

This location is configurable by setting the PIXI_CACHE_DIR or RATTLER_CACHE_DIR environment variable.

When you want to clean the cache, you can simply delete the cache directory, and Pixi will re-create the cache when needed.

The cache contains multiple folders concerning different caches from within pixi.

**Examples:**

Example 1 (unknown):
```unknown
export PATH="/home/user/development/pixi/.pixi/envs/default/bin:/home/user/.local/bin:/home/user/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/home/user/.pixi/bin"
export CONDA_PREFIX="/home/user/development/pixi/.pixi/envs/default"
export PIXI_PROJECT_NAME="pixi"
export PIXI_PROJECT_ROOT="/home/user/development/pixi"
export PIXI_PROJECT_VERSION="0.12.0"
export PIXI_PROJECT_MANIFEST="/home/user/development/pixi/pixi.toml"
export CONDA_DEFAULT_ENV="pixi"
export PIXI_ENVIRONMENT_PLATFORMS="osx-64,linux-64,win-64,osx-arm64"
export PIXI_ENVIRONMENT_NAME="default"
export PIXI_PROMPT="(pixi) "
. "/home/user/development/pixi/.pixi/envs/default/etc/conda/activate.d/activate-binutils_linux-64.sh"
. "/home/user/development/pixi/.pixi/envs/default/etc/conda/activate.d/activate-gcc_linux-64.sh"
. "/home/user/development/pixi/.pixi/envs/default/etc/conda/activate.d/activate-gfortran_linux-64.sh"
. "/home/user/development/pixi/.pixi/envs/default/etc/conda/activate.d/activate-gxx_linux-64.sh"
. "/home/user/development/pixi/.pixi/envs/default/etc/conda/activate.d/libglib_activate.sh"
. "/home/user/development/pixi/.pixi/envs/default/etc/conda/activate.d/rust.sh"
```

Example 2 (unknown):
```unknown
[activation.env]
# Python users often set:
PYTHONIOENCODING = "utf-8"
PYTHONNOUSERSITE = "1"
# R users often set:
PIXI_R_LIBS = "$CONDA_PREFIX/lib/R/library"
R_LIBS = "$PIXI_R_LIBS"
R_LIBS_USER = "$PIXI_R_LIBS"


[target.unix.activation]
# Use sh scripts on unix
scripts = [
  # Common in the ROS workspaces
  "install/setup.sh",
  # Want to add some personal scripts to the activation:
  "activation.sh",
]

# Use batch scripts on windows
[target.win.activation]
scripts = ["install/setup.bat"]
```

Example 3 (unknown):
```unknown
$ which python
python not found
$ eval "$(pixi shell-hook)"
$ (default) which python
/path/to/project/.pixi/envs/default/bin/python
```

Example 4 (unknown):
```unknown
eval "$(pixi shell-hook)"
```

---

## Environment Variables

**URL:** https://pixi.sh/latest/reference/environment_variables/

**Contents:**
- Environment Variables
- Configurable Environment Variables#
- Environment Variables Set By Pixi#
- Environment Variable Priority#
      - Example 1: task.env > activation.env#
      - Example 2: activation.env > activation.scripts#
      - Example 3: activation.scripts > activation scripts of dependencies#
      - Example 4: activation scripts of dependencies > outside environment variable#
      - Example 5: Complex Example - All priorities combined#

Pixi can also be configured via environment variables.

The following environment variables are set by Pixi, when using the pixi run, pixi shell, or pixi shell-hook command:

Even though the variables are environment variables these cannot be overridden. E.g. you can not change the root of the project by setting PIXI_PROJECT_ROOT in the environment.

The following priority rule applies for environment variables: task.env > activation.env > activation.scripts > activation scripts of dependencies > outside environment variables. Variables defined at a higher priority will override those defined at a lower priority.

In older versions of Pixi, this priority was not well-defined, and there are a number of known deviations from the current priority which exist in some older versions. Please see the warning in the advanced tasks documentation for further details and migration guidance.

In pixi.toml, we defined an environment variable HELLO_WORLD in both tasks.hello and activation.env.

When we run echo $HELLO_WORLD, it will output: Hello world!

In pixi.toml, we defined the same environment variable DEBUG_MODE in both activation.env and in the activation script file setup.sh. When we run echo Debug mode: $DEBUG_MODE, it will output: Debug mode: enabled

In pixi.toml, we have our local activation script and a dependency my-package that also sets environment variables through its activation scripts. When we run echo Library path: $LIB_PATH, it will output: Library path: /my/lib

pixi.toml[activation] scripts = ["local_setup.sh"] [dependencies] my-package = "*" # This package has its own activation scripts that set LIB_PATH="/dep/lib" local_setup.shexport LIB_PATH="/my/lib"

If we have a dependency that sets PYTHON_PATH and the same variable is already set in the outside environment. When we run echo Python path: $PYTHON_PATH, it will output: Python path: /pixi/python # Outside environment export PYTHON_PATH="/system/python" pixi.toml[dependencies] python-utils = "*" # This package sets PYTHON_PATH="/pixi/python" in its activation scripts

In pixi.toml, we define the same variable APP_CONFIG across multiple levels: pixi.toml[tasks.start] cmd = "echo Config: $APP_CONFIG" env = { APP_CONFIG = "task-specific" } [activation.env] APP_CONFIG = "activation-env" [activation] scripts = ["app_setup.sh"] [dependencies] config-loader = "*" # Sets APP_CONFIG="dependency-config" app_setup.shexport APP_CONFIG="activation-script" # Outside environment export APP_CONFIG="system-config"

Since task.env has the highest priority, when we run pixi run start it will output:

**Examples:**

Example 1 (unknown):
```unknown
Hello world!
```

Example 2 (unknown):
```unknown
[tasks.hello]
cmd = "echo $HELLO_WORLD"
env = { HELLO_WORLD = "Hello world!" }
[activation.env]
HELLO_WORLD = "Activate!"
```

Example 3 (unknown):
```unknown
Debug mode: enabled
```

Example 4 (unknown):
```unknown
[activation.env]
DEBUG_MODE = "enabled"

[activation]
scripts = ["setup.sh"]
```

---

## RStudio

**URL:** https://pixi.sh/latest/integration/editor/r_studio/

**Contents:**
- RStudio
- Installing R packages#
- Using R packages in RStudio#
- Full example#

You can use pixi to manage your R dependencies. The conda-forge channel contains a wide range of R packages that can be installed using pixi.

R packages are usually prefixed with r- in the conda-forge channel. To install an R package, you can use the following command:

To use the R packages installed by pixi in RStudio, you need to run rstudio from an activated environment. This can be achieved by running RStudio from pixi shell or from a task in the pixi.toml file.

The full example can be found here: RStudio example. Here is an example of a pixi.toml file that sets up an RStudio task:

Once RStudio has loaded, you can execute the following R code that uses the ggplot2 package:

This example assumes that you have installed RStudio system-wide. We are working on updating RStudio as well as the R interpreter builds on Windows for maximum compatibility with pixi.

**Examples:**

Example 1 (unknown):
```unknown
pixi add r-<package-name>
# for example
pixi add r-ggplot2
```

Example 2 (unknown):
```unknown
[workspace]
name = "r"
channels = ["conda-forge"]
platforms = ["linux-64", "osx-64", "osx-arm64"]

[target.linux.tasks]
rstudio = "rstudio"

[target.osx.tasks]
rstudio = "open -a rstudio"
# or alternatively with the full path:
# rstudio = "/Applications/RStudio.app/Contents/MacOS/RStudio"

[dependencies]
r = ">=4.3,<5"
r-ggplot2 = ">=3.5.0,<3.6"
```

Example 3 (unknown):
```unknown
# Load the ggplot2 package
library(ggplot2)

# Load the built-in 'mtcars' dataset
data <- mtcars

# Create a scatterplot of 'mpg' vs 'wt'
ggplot(data, aes(x = wt, y = mpg)) +
  geom_point() +
  labs(x = "Weight (1000 lbs)", y = "Miles per Gallon") +
  ggtitle("Fuel Efficiency vs. Weight")
```

---

## pixi workspace environment add#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/environment/add/

**Contents:**
- pixi workspace environment add#
- About#
- Usage#
- Arguments#
- Options#

Adds an environment to the manifest file

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace environment add [OPTIONS] <NAME>
```

---

## Tasks

**URL:** https://pixi.sh/latest/workspace/advanced_tasks/

**Contents:**
- Tasks
- Depends on#
  - Shorthand Syntax#
  - Environment specification for task dependencies#
- Working directory#
- Task Arguments#
  - Why Use Task Arguments?#
  - Defining Task Arguments#
  - Using Task Arguments#
  - Passing Arguments to Dependent Tasks#

When building a package, you often have to do more than just run the code. Steps like formatting, linting, compiling, testing, benchmarking, etc. are often part of a workspace. With Pixi tasks, this should become much easier to do.

Here are some quick examples

Just like packages can depend on other packages, our tasks can depend on other tasks. This allows for complete pipelines to be run with a single command.

An obvious example is compiling before running an application.

Checkout our cpp_sdl example for a running example. In that package we have some tasks that depend on each other, so we can assure that when you run pixi run start everything is set up as expected.

Results in the following lines added to the pixi.toml

The tasks will be executed after each other:

If one of the commands fails (exit with non-zero code.) it will stop and the next one will not be started.

With this logic, you can also create aliases as you don't have to specify any command in a task.

Tasks can be hidden from user facing commands by naming them with an _ prefix.

Pixi supports a shorthand syntax for defining tasks that only depend on other tasks. Instead of using the more verbose depends-on field, you can define a task directly as an array of dependencies.

results in the following pixi.toml:

Now you can run both tools with one command.

You can specify the environment to use for a dependent task:

This allows you to run tasks in different environments as part of a single pipeline. When you run the main task, Pixi ensures each dependent task uses its specified environment:

The environment specified for a task dependency takes precedence over the environment specified via the CLI --environment flag. This means even if you run pixi run test-all --environment py312, the first dependency will still run in the py311 environment as specified in the TOML file.

In the example above, the test-all task runs the test task in both Python 3.11 and 3.12 environments, allowing you to verify compatibility across different Python versions with a single command.

Pixi tasks support the definition of a working directory.

cwd stands for Current Working Directory. The directory is relative to the Pixi workspace root, where the pixi.toml file is located.

By default, tasks are executed from the Pixi workspace root. To change this, use the --cwd flag. For example, consider a Pixi workspace structured as follows:

To add a task that runs the bar.py file from the scripts directory, use:

This will add the following line to manifest file:

Tasks can accept arguments that can be referenced in the command. This provides more flexibility and reusability for your tasks.

Task arguments make your tasks more versatile and maintainable:

For example, instead of creating separate build tasks for development and production modes, you can create a single parameterized task that handles both cases.

Define arguments in your task using the args field:

Argument naming restrictions

Argument names cannot contain dashes (-) due to them being seen as a minus sign in MiniJinja. Use underscores (_) or camelCase instead.

When running a task, provide arguments in the order they are defined:

You can pass arguments to tasks that are dependencies of other tasks:

When executing a dependent task, the arguments are passed to the dependency:

When a dependent task doesn't specify all arguments, the default values are used for the missing ones:

For a dependent task to accept arguments to pass to the dependency, you can use the same syntax as passing arguments to the command:

Task commands support MiniJinja templating syntax for accessing and formatting argument values. This provides powerful flexibility when constructing commands.

Basic syntax for using an argument in your command:

You can also use filters to transform argument values:

For more information about available filters and template syntax, see the MiniJinja documentation.

A task name follows these rules:

Hiding tasks can be useful if your workspace defines many tasks but your users only need to use a subset of them.

When you specify inputs and/or outputs to a task, Pixi will reuse the result of the task.

For the cache, Pixi checks that the following are true:

If all of these conditions are met, Pixi will not run the task again and instead use the existing result.

Inputs and outputs can be specified as globs, which will be expanded to all matching files. You can also use MiniJinja templates in your inputs and outputs fields to parameterize the paths, making tasks more reusable:

When using template variables in inputs/outputs, Pixi expands the templates using the provided arguments or environment variables, and uses the resolved paths for caching decisions. This allows you to create generic tasks that can handle different files without duplicating task configurations:

Note: if you want to debug the globs you can use the --verbose flag to see which files are selected.

You can set environment variables directly for a task, as well as by other means. See the environment variable priority documentation for full details of ways to set environment variables, and how those ways interact with each other.

Notes on environment variables in tasks: - Values set via tasks.<name>.env are interpreted by deno_task_shell when the task runs. Shell-style expansions like env = { VAR = "$FOO" } therefore work the same on all operating systems.

In older versions of Pixi, this priority was not well-defined, and there are a number of known deviations from the current priority which exist in some older versions:

If you previously relied on a certain priority which no longer applies, you may need to change your task definitions.

For the specific case of overriding task.env with outside environment variables, this behaviour can now be recreated using task arguments. For example, if you were previously using a setup like:

you can now recreate this behaviour like:

You can make sure the environment of a task is "Pixi only". Here Pixi will only include the minimal required environment variables for your platform to run the command in. The environment will contain all variables set by the conda environment like "CONDA_PREFIX". It will however include some default values from the shell, like: "DISPLAY", "LC_ALL", "LC_TIME", "LC_NUMERIC", "LC_MEASUREMENT", "SHELL", "USER", "USERNAME", "LOGNAME", "HOME", "HOSTNAME","TMPDIR", "XPC_SERVICE_NAME", "XPC_FLAGS"

[tasks] clean_command = { cmd = "python run_in_isolated_env.py", clean-env = true} This setting can also be set from the command line with pixi run --clean-env TASK_NAME.

clean-env not supported on Windows

On Windows it's hard to create a "clean environment" as conda-forge doesn't ship Windows compilers and Windows needs a lot of base variables. Making this feature not worthy of implementing as the amount of edge cases will make it unusable.

To support the different OS's (Windows, OSX and Linux), Pixi integrates a shell that can run on all of them. This is deno_task_shell. The task shell is a limited implementation of a bourne-shell interface. Task command lines and the values of tasks.<name>.env are parsed and expanded by this shell.

Next to running actual executable like ./myprogram, cmake or python the shell has some built-in commands.

More info in deno_task_shell documentation.

**Examples:**

Example 1 (unknown):
```unknown
[tasks]
# Commands as lists so you can also add documentation in between.
configure = { cmd = [
    "cmake",
    # Use the cross-platform Ninja generator
    "-G",
    "Ninja",
    # The source is in the root directory
    "-S",
    ".",
    # We wanna build in the .build directory
    "-B",
    ".build",
] }

# Depend on other tasks
build = { cmd = ["ninja", "-C", ".build"], depends-on = ["configure"] }

# Using environment variables
run = "python main.py $PIXI_PROJECT_ROOT"
set = "export VAR=hello && echo $VAR"

# Cross platform file operations
copy = "cp pixi.toml pixi_backup.toml"
clean = "rm pixi_backup.toml"
move = "mv pixi.toml backup.toml"
```

Example 2 (unknown):
```unknown
pixi task add configure "cmake -G Ninja -S . -B .build"
pixi task add build "ninja -C .build" --depends-on configure
pixi task add start ".build/bin/sdl_example" --depends-on build
```

Example 3 (unknown):
```unknown
[tasks]
# Configures CMake
configure = "cmake -G Ninja -S . -B .build"
# Build the executable but make sure CMake is configured first.
build = { cmd = "ninja -C .build", depends-on = ["configure"] }
# Start the built executable
start = { cmd = ".build/bin/sdl_example", depends-on = ["build"] }
```

Example 4 (unknown):
```unknown
pixi task add fmt ruff
pixi task add lint pylint
```

---

## pixi task alias#

**URL:** https://pixi.sh/latest/reference/cli/pixi/task/alias/

**Contents:**
- pixi task alias#
- About#
- Usage#
- Arguments#
- Options#
- Examples#

Alias another specific command

**Examples:**

Example 1 (unknown):
```unknown
pixi task alias [OPTIONS] <ALIAS> <DEPENDS_ON>...
```

Example 2 (unknown):
```unknown
pixi task alias test-all test-py test-cpp test-rust
pixi task alias --platform linux-64 test test-linux
pixi task alias moo cow
```

---

## pixi workspace environment remove#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/environment/remove/

**Contents:**
- pixi workspace environment remove#
- About#
- Usage#
- Arguments#

Remove an environment from the manifest file

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace environment remove <NAME>
```

---

## pixi task remove#

**URL:** https://pixi.sh/latest/reference/cli/pixi/task/remove/

**Contents:**
- pixi task remove#
- About#
- Usage#
- Arguments#
- Options#
- Examples#

Remove a command from the workspace

**Examples:**

Example 1 (unknown):
```unknown
pixi task remove [OPTIONS] [TASK_NAME]...
```

Example 2 (unknown):
```unknown
pixi task remove cow
pixi task remove --platform linux-64 test
pixi task remove --feature cuda task
```

---

## pixi workspace environment#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/environment/

**Contents:**
- pixi workspace environment#
- About#
- Usage#
- Subcommands#
- Global Options#

Commands to manage workspace environments

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace environment [OPTIONS] <COMMAND>
```

---

## pixi task#

**URL:** https://pixi.sh/latest/reference/cli/pixi/task/

**Contents:**
- pixi task#
- About#
- Usage#
- Subcommands#
- Global Options#

Interact with tasks in the workspace

**Examples:**

Example 1 (unknown):
```unknown
pixi task [OPTIONS] <COMMAND>
```

---

## pixi task list#

**URL:** https://pixi.sh/latest/reference/cli/pixi/task/list/

**Contents:**
- pixi task list#
- About#
- Usage#
- Options#
- Examples#

List all tasks in the workspace

**Examples:**

Example 1 (unknown):
```unknown
pixi task list [OPTIONS]
```

Example 2 (unknown):
```unknown
pixi task list
pixi task list --environment cuda
pixi task list --summary
```

---
