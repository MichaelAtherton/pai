# Pixi - Other

**Pages:** 29

---

## Starship

**URL:** https://pixi.sh/latest/integration/third_party/starship/

**Contents:**
- Starship

Starship is a cross-platform and cross-shell prompt for developers, similar to oh-my-zsh, but with a focus on performance and simplicity. It also has full Pixi support. You can install it using the following command:

For information about how to configure and set up starship, see the official documentation.

In order for starship to always find the right python executable, you can adjust its configuration file.

By default, starship uses 🧚🏻 as pixi's symbol. You can adjust it as follows if you want a different symbol

As starship already displays a custom message when a pixi environment is active, you can disable pixi's custom PS1:

**Examples:**

Example 1 (unknown):
```unknown
pixi global install starship
```

Example 2 (unknown):
```unknown
[python]
# customize python binary path for pixi
python_binary = [
  # this is the python from PATH if in a pixi shell
  # (assuming you don't have python on your global PATH)
  "python",
  # fall back to pixi's python if it's available
  ".pixi/envs/default/bin/python",
]
```

Example 3 (unknown):
```unknown
[pixi]
symbol = "📦 "
```

Example 4 (unknown):
```unknown
pixi config set shell.change-ps1 "false"
```

---

## FAQ

**URL:** https://pixi.sh/latest/misc/FAQ/

**Contents:**
- FAQ
- What is the difference with conda, mamba, poetry, pip#
- Why the name pixi#
- Where is pixi build#

Starting with the name prefix we iterated until we had a name that was easy to pronounce, spell and remember. There also wasn't a CLI tool yet using that name. Unlike px, pex, pax, etc. When in code mode we spell it like this pixi, otherwise we always start with an uppercase letter: Pixi. We think the name sparks curiosity and fun, if you don't agree, I'm sorry, but you can always alias it to whatever you like.

PowerShell: New-Alias -Name not_pixi -Value pixi

TL;DR: It's coming we promise!

pixi build is going to be the subcommand that can generate a conda package out of a Pixi workspace. This requires a solid build tool which we're creating with rattler-build which will be used as a library in pixi.

**Examples:**

Example 1 (unknown):
```unknown
alias not_pixi="pixi"
```

Example 2 (unknown):
```unknown
New-Alias -Name not_pixi -Value pixi
```

---

## Dependency Overrides

**URL:** https://pixi.sh/latest/advanced/override/

**Contents:**
- Dependency Overrides
- Overview#
- Example#
  - Override a dependency version#
  - Override a dependency version in a specific feature#
  - Interact with other overrides#

Sometimes our direct dependency declares outdated intermediate dependency or is too tight to solve with other direct dependencies. In this case, we can override the intermediate dependency in our pyproject.tomlor pixi.toml file.

[!Note] This option is not recommended unless you know what you are doing, as uv will ignore all the version constraints of the dependency and use the version you specified.

# pyproject.toml [tool.pixi.pypi-options.dependency-overrides] numpy = ">=2.0.0" or in pixi.toml:

# pixi.toml [pypi-options.dependency-overrides] numpy = ">=2.0.0" This will override the version of numpy used by all dependencies to be at least 2.0.0, regardless of what the dependencies specify. This is useful if you need a specific version of a library that is not compatible with the versions specified by your dependencies.

it can also be specified in feature level, [features.dev.pypi-options.dependency-overrides] numpy = ">=2.0.0" This will override the version of numpy used by all dependencies in the dev feature to be at least 2.0.0, regardless of what the dependencies specify when the dev feature is enabled.

For a specific environment, all the dependency-overrides defined in different features will be combined in the order they were when defining the environment.

If the same dependency is overridden multiple times, we'll use the override from the prior feature in that environment.

Also, the default feature will always come, and come last in the list of all overrides.

# pixi.toml [pypi-options] dependency-overrides = { numpy = ">=2.1.0" } [pypi-dependencies] numpy = ">=1.25.0" [feature.dev.pypi-options.dependency-overrides] numpy = "==2.0.0" [feature.outdated.pypi-options.dependency-overrides] numpy = "==1.21.0" [environments] dev = ["dev"] outdated = ["outdated"] conflict_a=["outdated", "dev"] conflict_b=["dev","outdated"] the following constrains are merged out: default: numpy >= 2.1.0 dev: numpy == 2.0.0 outdated: numpy == 1.21.0 conflict_a: numpy == 1.21.0 (from outdated) conflict_b: numpy == 2.0.0 (from dev)

This may contrast with the intuition that all overrides are applied and combined to a result, but it is done this way to avoid conflicts and confusion. Since users are granted fully control over the overrides, it is up to ourselves to choose the right overrides for the environment.

**Examples:**

Example 1 (unknown):
```unknown
# pyproject.toml
[tool.pixi.pypi-options.dependency-overrides]
numpy = ">=2.0.0"
```

Example 2 (unknown):
```unknown
# pixi.toml
[pypi-options.dependency-overrides]
numpy = ">=2.0.0"
```

Example 3 (unknown):
```unknown
[features.dev.pypi-options.dependency-overrides]
numpy = ">=2.0.0"
```

Example 4 (unknown):
```unknown
# pixi.toml
[pypi-options]
dependency-overrides = { numpy = ">=2.1.0" }

[pypi-dependencies]
numpy = ">=1.25.0"

[feature.dev.pypi-options.dependency-overrides]
numpy = "==2.0.0"

[feature.outdated.pypi-options.dependency-overrides]
numpy = "==1.21.0"

[environments]
dev = ["dev"]
outdated = ["outdated"]
conflict_a=["outdated", "dev"]
conflict_b=["dev","outdated"]
```

---

## Making a Pixi workspace#

**URL:** https://pixi.sh/latest/first_workspace/

**Contents:**
- Making a Pixi workspace#
- Creating a Pixi workspace#
- Managing dependencies#
  - PyPI dependencies#
- Lock file#
- Managing tasks#
- Environments#

Pixi's biggest strength is its ability to create reproducible, powerful, and flexible workspaces. A workspace lives in a directory on your system, and is a collection of Pixi environments that can be used to develop one or many projects in that directory. Let's go over the common steps to create a simple Pixi workspace.

To create a new Pixi workspace, you can use the pixi init command:

This command creates a new directory called my_workspace with the following structure:

The pixi.toml file is the manifest of your Pixi workspace. It contains all the information about your workspace, such as its channels, platforms, dependencies, tasks, and more.

The file created by pixi init is a minimal manifest that looks like this:

As pixi.toml has a JSON schema, it is possible to use IDE’s like VSCode to edit the field with autocompletion. Install the Even Better TOML VSCode extension to get the best experience. Or use the integrated schema support in PyCharm.

After creating the workspace, you can start adding dependencies. Pixi uses the pixi add command to add dependencies to a workspace. This command will, by default, add the conda dependency to the pixi.toml, solve the dependencies, write the lock file, and install the package in the environment. For example, let's add numpy and pytest to the workspace.

pixi add numpy pytest This results in these lines being added:

You can also specify the version of the dependency you want to add.

Pixi normally uses conda packages for dependencies, but you can also add dependencies from PyPI. Pixi will make sure it doesn't try to install the same package from both sources, and avoid conflicts between them.

If you want to add them to your workspace you can do that with the --pypi flag:

pixi add --pypi httpx This will add the httpx package from PyPI to the workspace:

To learn more about the differences between conda and PyPI, see our Conda & PyPI concept documentation.

Pixi will always create a lock file when the dependencies are solved. This file will contain all the exact versions of the workspace's dependencies (and their dependencies). This results in a reproducible environment, which you can share with others, and use for testing and deployment.

The lockfile is called pixi.lock and it is created in the root of the workspace. To learn more about lock files, see our detailed lock file documentation.

Pixi has a built-in cross-platform task runner which allows you to define tasks in the manifest. Think of tasks as commands (or chains of commands) which you may want to repeat many times over the course of developing a project (for example, running the tests).

This is a great way to share tasks with others and to ensure that the same tasks are run in the same environment on different machines. The tasks are defined in the pixi.toml file under the [tasks] section.

You can add one to your workspace by running the pixi task add command.

pixi task add hello "echo Hello, World!" This will add the following lines to the pixi.toml file:

pixi.toml[tasks] hello = "echo Hello, World!" You can then run the task using the pixi run command:

pixi run hello This will execute the command echo Hello, World! in the workspace's default environment.

Tasks can be much more powerful, for example:

[tasks.name-of-powerful-task] cmd = "echo This task can do much more! Like have {{ arguments }} and {{ "minijinja" | capitalize }} templates." # List of tasks that must be run before this one. depends-on = ["other-task"] # Working directory relative to the root of the workspace cwd = "current/working/directory" # List of arguments for the task args = [{ arg = "arguments", default = "default arguments" }] # Run the command if the input files have changed input = ["src"] # Run the command if the output files are missing output = ["output.txt"] # Set environment variables for the task env = { MY_ENV_VAR = "value" } More information about tasks can be found in the Tasks section of the documentation.

Pixi always creates an environment for your workspace (the "default" environment), which contains your dependencies and in which your tasks are run. You can also include multiple environments in one workspace. These environments are located in the .pixi/envs directory in the root of your workspace.

Using these environments is as simple as running the pixi run or pixi shell command. pixi run will execute the remaining input as a command (or a task if the input matches the name of a defined task) in the environment, while pixi shell will spawn a new shell session in the environment. Both commands "activate" the environment — learn more at our environment activation documentation.

**Examples:**

Example 1 (unknown):
```unknown
pixi init my_workspace
```

Example 2 (unknown):
```unknown
my_workspace
├── .gitattributes
├── .gitignore
└── pixi.toml
```

Example 3 (unknown):
```unknown
[workspace]
authors = ["Jane Doe <jane.doe@example.com>"]
channels = ["conda-forge"]
name = "my_workspace"
platforms = ["osx-arm64"]
version = "0.1.0"

[tasks]

[dependencies]
```

Example 4 (unknown):
```unknown
pixi add numpy pytest
```

---

## Lock File

**URL:** https://pixi.sh/latest/workspace/lockfile/

**Contents:**
- Lock File
- What is a lock file?#
- Why a lock file#
- When is a lock file generated?#
- How to use a lock file#
- Lock file satisfiability#
- The version of the lock file#
- Your lock file is big#
- You don't need a lock file because...#
- Removing the lock file#

A lock file is the protector of the environments, and Pixi is the key to unlock it.

A lock file locks the environment in a specific state. Within Pixi a lock file is a description of the packages in an environment. The lock file contains two definitions:

The environments that are used in the workspace with their complete set of packages. e.g.:

The definition of the packages themselves. e.g.:

Pixi uses the lock file for the following reasons:

This gives you (and your collaborators) a way to really reproduce the environment they are working in. Using tools such as docker suddenly becomes much less necessary.

A lock file is generated when you install a package. More specifically, a lock file is generated from the solve step of the installation process. The solve will return a list of packages that are to be installed, and the lock file will be generated from this list. This diagram tries to explain the process:

Do not edit the lock file

A lock file is a machine only file, and should not be edited by hand.

That said, the pixi.lock is human-readable, so it's easy to track the changes in the environment. We recommend you track the lock file in git or other version control systems. This will ensure that the environment is always reproducible and that you can always revert back to a working state, in case something goes wrong. The pixi.lock and the manifest file pixi.toml/pyproject.toml should always be in sync.

Running the following commands will check and automatically update the lock file if you changed any dependencies:

All the commands that support the interaction with the lock file also include some lock file usage options:

Syncing the lock file with the manifest file

The lock file is always matched with the whole configuration in the manifest file. This means that if you change the manifest file, the lock file will be updated. flowchart TD C[manifest] --> A[lock file] --> B[environment]

The lock file is a description of the environment, and it should always be satisfiable. Satisfiable means that the given manifest file and the created environment are in sync with the lock file. If the lock file is not satisfiable, Pixi will generate a new lock file automatically.

Steps to check if the lock file is satisfiable:

If you want to get more details checkout the actual code as this is a simplification of the actual code.

The lock file has a version number, this is to ensure that the lock file is compatible with the local version of pixi.

Pixi is backward compatible with the lock file, but not forward compatible. This means that you can use an older lock file with a newer version of pixi, but not the other way around.

The lock file can grow quite large, especially if you have a lot of packages installed. This is because the lock file contains all the information about the packages.

If you can not think of a case where you would benefit from a fast reproducible environment, then you don't need a lock file.

But take note of the following:

If you want to remove the lock file, you can simply delete it.

This will remove the lock file, and the next time you run a command that requires the lock file, it will be generated again.

This does remove the locked state of the environment, and the environment will be updated to the latest version of the packages.

**Examples:**

Example 1 (unknown):
```unknown
environments:
    default:
        channels:
          - url: https://conda.anaconda.org/conda-forge/
        packages:
            linux-64:
            ...
            - conda: https://conda.anaconda.org/conda-forge/linux-64/python-3.12.2-hab00c5b_0_cpython.conda
            ...
            osx-64:
            ...
            - conda: https://conda.anaconda.org/conda-forge/osx-64/python-3.12.2-h9f0c242_0_cpython.conda
            ...
```

Example 2 (unknown):
```unknown
- kind: conda
  name: python
  version: 3.12.2
  build: h9f0c242_0_cpython
  subdir: osx-64
  url: https://conda.anaconda.org/conda-forge/osx-64/python-3.12.2-h9f0c242_0_cpython.conda
  sha256: 7647ac06c3798a182a4bcb1ff58864f1ef81eb3acea6971295304c23e43252fb
  md5: 0179b8007ba008cf5bec11f3b3853902
  depends:
    - bzip2 >=1.0.8,<2.0a0
    - libexpat >=2.5.0,<3.0a0
    - libffi >=3.4,<4.0a0
    - libsqlite >=3.45.1,<4.0a0
    - libzlib >=1.2.13,<1.3.0a0
    - ncurses >=6.4,<7.0a0
    - openssl >=3.2.1,<4.0a0
    - readline >=8.2,<9.0a0
    - tk >=8.6.13,<8.7.0a0
    - tzdata
    - xz >=5.2.6,<6.0a0
  constrains:
    - python_abi 3.12.* *_cp312
  license: Python-2.0
  size: 14596811
  timestamp: 1708118065292
```

Example 3 (unknown):
```unknown
graph TD
    A[Install] --> B[Solve]
    B --> C[Generate and write lock file]
    C --> D[Install Packages]
```

Example 4 (unknown):
```unknown
flowchart TD
    C[manifest] --> A[lock file] --> B[environment]
```

---

## Info Command

**URL:** https://pixi.sh/latest/advanced/explain_info_command/

**Contents:**
- Info Command
- Global info#
  - Platform#
  - Virtual packages#
  - Cache dir#
  - Auth storage#
  - Cache size#
- Workspace info#
  - Manifest file#
  - Last updated#

pixi info prints out useful information to debug a situation or to get an overview of your machine/workspace. This information can also be retrieved in json format using the --json flag, which can be useful for programmatically reading it.

The first part of the info output is information that is always available and tells you what Pixi can read on your machine.

This defines the platform you're currently on according to pixi. If this is incorrect, please file an issue on the Pixi repo.

The virtual packages that Pixi can find on your machine.

In the Conda ecosystem, you can depend on virtual packages. These packages aren't real dependencies that are going to be installed, but rather are being used in the solve step to find if a package can be installed on the machine. A simple example: When a package depends on Cuda drivers being present on the host machine it can do that by depending on the __cuda virtual package. In that case, if Pixi cannot find the __cuda virtual package on your machine the installation will fail.

The directory where Pixi stores its cache. Checkout the cache documentation for more information.

Check the authentication documentation

[requires --extended]

The size of the previously mentioned "Cache dir" in Mebibytes.

Everything below Workspace is info about the workspace you're currently in. This info is only available if your path has a manifest file.

The path to the manifest file that describes the workspace.

The last time the lock file was updated, either manually or by Pixi itself.

The environment info defined per environment. If you don't have any environments defined, this will only show the default environment.

This lists which features are enabled in the environment. For the default this is only default

The list of channels used in this environment.

The amount of dependencies defined that are defined for this environment (not the amount of installed dependencies).

The list of dependencies defined for this environment.

The platforms the workspace has defined.

**Examples:**

Example 1 (unknown):
```unknown
➜ pixi info
      Pixi version: 0.13.0
          Platform: linux-64
  Virtual packages: __unix=0=0
                  : __linux=6.5.12=0
                  : __glibc=2.36=0
                  : __cuda=12.3=0
                  : __archspec=1=x86_64
         Cache dir: /home/user/.cache/rattler/cache
      Auth storage: /home/user/.rattler/credentials.json

Workspace
------------
           Version: 0.13.0
     Manifest file: /home/user/development/pixi/pixi.toml
      Last updated: 25-01-2024 10:29:08

Environments
------------
default
          Features: default
          Channels: conda-forge
  Dependency count: 10
      Dependencies: pre-commit, rust, openssl, pkg-config, git, mkdocs, mkdocs-material, pillow, cairosvg, compilers
  Target platforms: linux-64, osx-arm64, win-64, osx-64
             Tasks: docs, test-all, test, build, lint, install, build-docs
```

---

## 

**URL:** https://pixi.sh/latest/

**Contents:**
- Why Pixi?#
- Quick Demo#
- What is the difference with Pixi?#
- Available Software#
- Installation#
- Getting Started#
- What Developers Say#
- Useful Links#

Pixi is a fast, modern, and reproducible package management tool for developers of all backgrounds.

Isolated, easily recreated environments with lockfiles built-in

Manage complex pipelines effortlessly.

Works on Linux, macOS, Windows, and more.

Compose multiple environments in one manifest.

Support for pyproject.toml and PyPI through uv.

Install global tools, safely isolated. Replacing apt, homebrew, winget

Project setup is a breeze with Pixi.

Install your favorite tools with a single command.

Pixi defaults to the biggest Conda package repository, conda-forge, which contains over 30,000 packages.

And browse the thousands more on prefix.dev, or host your own channels

To install pixi, run:

Now restart your terminal or shell!

The installation needs to become effective by restarting your terminal or sourcing your shell.

You can check the installation sh script: download and the ps1: download. The scripts are open source and available on GitHub.

See all installation options →

More details on how to use Pixi with Python can be found in the Python tutorial.

This is more of an example to show off how easy it is to use Pixi with Rust. Not a recommended way to build Rust projects. More details on how to use Pixi with Rust can be found in the Rust tutorial.

Add dependencies: pixi add ros-humble-desktop

Depending on your internet connection, this will take a while to install, as it will download the entire ROS2 desktop package.

Start Rviz pixi run rviz2

More details on how to use Pixi with ROS2 can be found in the ROS2 tutorial.

"Pixi is my tool of choice for Python environment management. It has significantly reduced boilerplate by offering seamless support for both PyPI and conda-forge indexes - a critical requirement in my workflow."

"I can’t stress enough how much I love using Pixi global as a package manager for my daily CLI tools. With the global manifest, even sharing my setup across machines is trivial!"

"We are changing how we manage ROS dependencies on Windows. We will be using Pixi to install and manage dependencies from conda. I'm pretty excited about how much easier it will be for users going forward."

**Examples:**

Example 1 (unknown):
```unknown
pixi init hello-world
cd hello-world
pixi add python
pixi run python -c 'print("Hello World!")'
```

Example 2 (unknown):
```unknown
pixi global install gh nvim ipython btop ripgrep
```

Example 3 (unknown):
```unknown
curl -fsSL https://pixi.sh/install.sh | sh
```

Example 4 (unknown):
```unknown
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

---

## Pixi Install-to-prefix

**URL:** https://pixi.sh/latest/integration/extensions/pixi_install_to_prefix/

**Contents:**
- Pixi Install-to-prefix

Pixi installs your environments to .pixi/envs/<env-name> by default. If you want to install your environment to an arbitrary location on your system, you can use pixi-install-to-prefix.

You can install pixi-install-to-prefix with:

Instead of installing pixi-install-to-prefix globally, you can also use pixi exec to run pixi-install-to-prefix in a temporary environment:

**Examples:**

Example 1 (unknown):
```unknown
pixi global install pixi-install-to-prefix
```

Example 2 (unknown):
```unknown
pixi exec pixi-install-to-prefix ./my-environment
```

Example 3 (unknown):
```unknown
Usage: pixi-install-to-prefix [OPTIONS] <PREFIX>

Arguments:
  <PREFIX>  The path to the prefix where you want to install the environment

Options:
  -l, --lockfile <LOCKFILE>        The path to the pixi lockfile [default: pixi.lock]
  -e, --environment <ENVIRONMENT>  The name of the pixi environment to install [default: default]
  -p, --platform <PLATFORM>        The platform you want to install for [default: <your-system-platform>]
  -c, --config <CONFIG>            The path to the pixi config file. By default, no config file is used
  -s, --shell <SHELL>              The shell(s) to generate activation scripts for. Default: see README
      --no-activation-scripts      Disable the generation of activation scripts
  -v, --verbose...                 Increase logging verbosity
  -q, --quiet...                   Decrease logging verbosity
  -h, --help                       Print help
```

---

## Changelog#

**URL:** https://pixi.sh/latest/CHANGELOG/

**Contents:**
- Changelog#
  - [0.59.0] - 2025-10-29#
    - ✨ Highlights#
    - Added#
    - Changed#
    - Documentation#
    - Fixed#
    - New Contributors#
  - [0.58.0] - 2025-10-22#
    - ✨ Highlights#

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog, and this project adheres to Semantic Versioning.

This release introduces the ability to set the strategy used in the solve. You can learn more about this feature in the documentation.

However, the main reason we are making this release is because one of our dependencies astral-tokio-tar below 0.5.6 has a high severity security issue titled TARmageddon. Updating that dependency fixes that.

This release adds important bugfixes and changes in the discovery logic. Pixi Build already had the ability to directly depend on recipe.yaml files backed by pixi-build-rattler-build without the need to specify a separate package manifest. So the following code just works:

This still works, but we stopped hardcoding the channel for the backends. Now, it will first try to find a workspace manifest and extract its channels. If that doesn't work, it will fallback to the default channels in your Pixi config.

There's a new way to include variants in to a pixi workspace! Use build-variants-files to reference external variant definitions from YAML files.

Read more about this feature in the docs.

We deprecated the following syntax in the pixi manifest and give explicit warning when it's used: - [project]: should be replaced by [workspace]. - [build-dependencies] and [host-dependencies]: should be replaced by [dependencies].

If you're working on pixi-build backend note that we deprecated build-api v0.

And we also fixed a lot of things!

Install a .conda package directly using pixi global install: pixi global install --path /path/to/package-name.conda

This cycle, the Pixi team focused on squashing bugs. We especially focused on problems that were annoying and open for some time, but never quite important to fix right now.

The environment variable overwriting logic is changed. If you think you haven't read this for the first time, then you are right! We already attempted to fix the order and other weird aspects of our environment variable handling in the past, but had to revert it, since it broke too many things. This time we touched significantly less logic so we hope that the impact will be minimal.

Previously, the variables in your own environment would overwrite the variables set in the Pixi manifest. This is now reversed, meaning that the variables set in the Pixi manifest will overwrite the variables in your own environment. Also task environment variables will now be considered even if that environment variable was already defined outside of Pixi. More info can be found in the documentation.

Small improvements and bug fixes.

You can now use pixi global tree to visualize the dependency tree of a global environment.

And you can install subsets of packages now works, for both conda and pypi packages: # Define which packages you want to install and which you want to skip. pixi install --only packageA --only packageB --skip packageC # Using this modified environment without updating it again can be done with: pixi run --as-is my_command pixi shell --as-is

Only for users using preview = ["pixi-build"]: In #4410 we've made package.name optional. e.g. [package] name = "my-package" # This is now optional version = "0.1.0" # This is now optional Soon, the backends will be able to automatically get those values from pyproject.toml, Cargo.toml, package.xml etc. However, this results in the lockfiles not being --locked anymore. Running pixi lock or pixi update should fix this!

We've removed --no-lockfile-update and replaced it with --no-install --frozen. On pixi run/shell you can use --as-is to run the command without installing the dependencies or touching the lockfile.

You can now use pixi global to install source dependencies. pixi global install --path path/to/my-package my-package At the moment, you still have to specify the package name, which we will improve on later!

In v0.51.0 we changed the environment variable overwriting logic. This has be reverted in this release, as there are some issues with it.

Pixi now supports --skip on install which means you can skip the installation of a package. Which can be useful for things like layering Docker images.

Pixi build got a lot of improvements, including the ability to use build backends from source. Starting with this release you can get build backends from conda-forge. We will release stable versions of the build backends on conda-forge, and we maintain a rolling distribution on the pixi-build-backends channel. The documentation has been updated to reflect this change.

The environment variable overwriting logic is changed. Previously, the variables in your own environment would overwrite the variables set in the Pixi manifest. This is now reversed, meaning that the variables set in the Pixi manifest will overwrite the variables in your own environment. More info can be found in the documentation.

Use pixi import to import environment.yml files into your Pixi manifest.

This release contains loads of bug fixes and refactors, primarily to make pixi build more stable and feature rich in the near future.

This release enables pixi to pick up extensions that are installed as pixi-. This is similar to cargo, git and other tools. This means that you can now install extensions like this:

It also allows you to use pixi exec more easily: pixi exec --with numpy python -c "import numpy; print(numpy.__version__)" # Previous command is equivalent to: pixi exec --spec numpy --spec python python -c "import numpy; print(numpy.__version__)"

This is a minor release with a couple of bugfixes. A new feature is the support for mojoproject.toml files which is used to develop on projects written in the Mojo programming language. This enables users to migrate from the deprecated Magic package manager to Pixi.

This is a minor release with a couple of bugs fixed. Additionally, pixi self-update accepts now the flags --force and --no-release-note.

Support for recursive source run dependencies when using pixi build. This means, you can now add source dependencies in the run-dependencies section of your Pixi package:

arg names in tasks can no longer contain dashes (-). This restriction is due to the integration of Minijinja for rendering tasks, where dashes could be misinterpreted as a subtraction operator.

This release comes with another set of features for the tasks! - The command of a task is now able to use minijinja for rendering the command. [tasks] # The arg `text`, converted to uppercase, will be printed. task1 = { cmd = "echo {{ text | upper }}", args = ["text"] } # If arg `text` contains 'hoi', it will be converted to lowercase. The result will be printed. task2 = { cmd = "echo {{ text | lower if 'hoi' in text }}", args = [ { arg = "text", default = "" }, ] } # With `a` and `b` being strings, they will be appended and then printed. task3 = { cmd = "echo {{ a + b }}", args = ["a", { arg = "b", default = "!" }] } # `names` will be split by whitespace and then every name will be printed separately task4 = { cmd = "{% for name in names | split %} echo {{ name }};{% endfor %}", args = [ "names", ] } - Shortened composition of tasks with depends-on key. [tasks] test-all = [{ task = "test", args = ["all"] }] # Equivalent to: test-all = { depends-on = [{task = "test", args = ["all"] }]} - The depends-on key can now include the environment that the task should run in. [tasks] # Using the shortened composition of tasks test-all = [ { task = "test", environment = "py311" }, { task = "test", environment = "py312" }, ]

This release brings in numerous improvements and bug fixes and one big feature: argument variables tasks! If you do add args, you will have more convenient way of specifying arguments, which works with pipes and even allows you to set defaults.

Let's say you define this manifest:

Both of the invocations now work, since type is optional:

If you don't specify args for your tasks everything which you append to the CLI will also be appended to the task.

Therefore, running pixi run install --debug --path /path/to/manifest will lead to cargo install --debug --path /path/to/manifest being run inside the environment. This was already the behavior before this release, so existing tasks should continue to work.

Learn more in our documentation: https://pixi.sh/v0.45.0/workspace/advanced_tasks/#using-task-arguments

This release introduces an improved way of dealing with Virtual Packages. For example, previously pixi would not allow this configuration on a non-CUDA machine: [system-requirements] cuda = "12" [dependencies] python = "*" Now this setup also works on non-CUDA machines, because it only stops if the packages themselves actually depend on CUDA. This is a first step to make the use of system-requirements/virtual-packages more flexible.

This release add support for S3 backends. You can configure a custom S3 backend in your pixi.toml file. This allows you to use a custom S3 bucket as a channel for your project.

This release introduces the ability to add environment variables to the init --import command. We also upgraded the uv crate to v0.5.29.

This release introduces lazily creating solve environments for the pypi-dependencies resulting in a significant speedup for environments that only depend on wheels. If you want to force the use of wheels you can now also set no-build in the pypi-options table. To test this you can now just use pixi lock to create a lockfile without installing an environment.

This release will greatly improve the git dependency experience for PyPI packages.

We've reverted the breaking change of the depends_on field from 0.40.0, replacing it with a warning.

This release also brings a performance boost to our Windows and Linux-musl builds by using faster allocators. On the (holoviews) project, we measured a significant speedup: # Linux musl Summary pixi-0.40.1 list --no-install ran 12.65 ± 0.46 times faster than pixi-0.40.0 list --no-install # Windows pixi-0.40.1 list --no-install ran 1.66 ± 0.07 times faster than pixi-0.40.0 list --no-install 1.67 ± 0.09 times faster than pixi-0.39.5 list --no-install 2.10 ± 0.09 times faster than pixi-0.39.4 list --no-install

Manifest file parsing has been significantly improved. Errors will now be clearer and more helpful, for example: × Expected one of 'first-index', 'unsafe-first-match', 'unsafe-best-match' ╭─[pixi.toml:2:27] 1 │ 2 │ index-strategy = "UnsafeFirstMatch" · ──────────────── 3 │ ╰──── help: Did you mean 'unsafe-first-match'?

The depends_on field has been renamed to depends-on for better consistency. Using the old format without a dash (depends_on) will now result in an error. The new errors should help you find the location: Error: × field 'depends_on' is deprecated, 'depends-on' has replaced it ╭─[pixi.toml:22:51] 21 │ install = "cargo install --path . --locked" 22 │ install-as = { cmd = "python scripts/install.py", depends_on = [ · ─────┬──── · ╰── replace this with 'depends-on' 23 │ "build-release", ╰────

By updating resolvo to the latest version we now significantly lower the RAM usage during the solve process. 🚀 As this improvement removes a huge set of data from the solve step it also speeds it up even more, especially for hard to solve environments.

Some numbers from the resolvo PR, based on the resolve test dataset: - Average Solve Time: 'pixi v0.39.5' was 1.68 times faster than 'pixi v0.39.4' - Median Solve Time: 'pixi v0.39.5' was 1.33 times faster than 'pixi v0.39.4' - 25th Percentile: 'pixi v0.39.5' was 1.22 times faster than 'pixi v0.39.4' - 75th Percentile: 'pixi v0.39.5' was 2.28 times faster than 'pixi v0.39.4'

Last release got an additional speedup for macOS specifically! 🚀

This release includes a little Christmas present, the environment installation got a huge speedup! 🚀

Patch release to fix the binary generation in CI.

We've merged in the main pixi build feature branch. This is a big change but shouldn't have affected any of the current functionality. If you notice any issues, please let us know.

It can be turned on by preview = "pixi-build" in your pixi.toml file. It's under heavy development so expect breaking changes in that feature for now.

We now allow the use of prefix.dev channels with sharded repodata:

Running pixi search rubin-env using hyperfine on the default versus our channels gives these results:

pixi global now exposed binaries are not scripts anymore but actual executables. Resulting in significant speedup and better compatibility with other tools.

This is the first release with the new pixi global implementation. It's a full reimplementation of pixi global where it now uses a manifest file just like pixi projects. This way you can declare your environments and save them to a VCS.

It also brings features like, adding dependencies to a global environment, and exposing multiple binaries from the same environment that are not part of the main installed packages.

Test it out with: # Normal feature pixi global install ipython # New features pixi global install \ --environment science \ # Defined the environment name --expose scipython=ipython \ # Expose binaries under custom names ipython scipy # Define multiple dependencies for one environment

This should result in a manifest in $HOME/.pixi/manifests/pixi-global.toml: version = 1 [envs.ipython] channels = ["conda-forge"] dependencies = { ipython = "*" } exposed = { ipython = "ipython", ipython3 = "ipython3" } [envs.science] channels = ["conda-forge"] dependencies = { ipython = "*", scipy = "*" } exposed = { scipython = "ipython" }

Checkout the updated documentation on this new feature: - Main documentation on this tag: https://pixi.sh/v0.33.0/ - Global CLI documentation: https://pixi.sh/v0.33.0/reference/cli/#global - The implementation documentation: https://pixi.sh/v0.33.0/features/global_tools/ - The initial design proposal: https://pixi.sh/v0.33.0/design_proposals/pixi_global_manifest/

The biggest fix in this PR is the move to the latest rattler as it came with some major bug fixes for macOS and Rust 1.81 compatibility.

Thanks to our maintainer @baszamstra! He sped up the resolver for all cases we could think of in #2162 Check the result of times it takes to solve the environments in our test set:

I want to thank @synapticarbors and @abkfenris for starting the work on pixi project export. Pixi now supports the export of a conda environment.yml file and a conda explicit specification file. This is a great addition to the project and will help users to share their projects with other non pixi users.

This release contains a lot of refactoring and improvements to the codebase, in preparation for future features and improvements. Including with that we've fixed a ton of bugs. To make sure we're not breaking anything we've added a lot of tests and CI checks. But let us know if you find any issues!

As a reminder, you can update pixi using pixi self-update and move to a specific version, including backwards, with pixi self-update --version 0.27.0.

This fixes the issue where pixi would generate broken environments/lockfiles when a mapping for a brand-new version of a package is missing.

[!TIP] These new features are part of the ongoing effort to make pixi more flexible, powerful, and comfortable for the python users. They are still in progress so expect more improvements on these features soon, so please report any issues you encounter and follow our next releases!

A quick bug-fix release for pixi list.

[!WARNING] This versions build failed, use v0.15.1

Now, solve-groups can be used in [environments] to ensure dependency alignment across different environments without simultaneous installation. This feature is particularly beneficial for managing identical dependencies in test and production environments. Example configuration:

[environments] test = { features = ["prod", "test"], solve-groups = ["group1"] } prod = { features = ["prod"], solve-groups = ["group1"] } This setup simplifies managing dependencies that must be consistent across test and production.

This release is pretty crazy in amount of features! The major ones are: - We added support for multiple environments. :tada: Checkout the documentation - We added support for sdist installation, which greatly improves the amount of packages that can be installed from PyPI. :rocket:

Renaming of PIXI_PACKAGE_* variables: PIXI_PACKAGE_ROOT -> PIXI_PROJECT_ROOT PIXI_PACKAGE_NAME -> PIXI_PROJECT_NAME PIXI_PACKAGE_MANIFEST -> PIXI_PROJECT_MANIFEST PIXI_PACKAGE_VERSION -> PIXI_PROJECT_VERSION PIXI_PACKAGE_PLATFORMS -> PIXI_ENVIRONMENT_PLATFORMS Check documentation here: https://pixi.sh/environment/

The .pixi/env/ folder has been moved to accommodate multiple environments. If you only have one environment it is now named .pixi/envs/default.

Full Changelog: https://github.com/prefix-dev/pixi/compare/v0.11.0...v0.12.0

Full Changelog: https://github.com/prefix-dev/pixi/compare/v0.10.0...v0.11.0

Full Changelog: https://github.com/prefix-dev/pixi/compare/v0.9.1...v0.10.0

Full Changelog: https://github.com/prefix-dev/pixi/compare/v0.9.0...v0.9.1

Full Changelog: https://github.com/prefix-dev/pixi/compare/v0.8.0...v0.9.0

[!NOTE] [pypi-dependencies] support is still incomplete, missing functionality is listed here: https://github.com/orgs/prefix-dev/projects/6. Our intent is not to have 100% feature parity with pip, our goal is that you only need pixi for both conda and pypi packages alike.

Full Changelog: https://github.com/prefix-dev/pixi/compare/v0.7.0...v0.8.0

Full Changelog: https://github.com/prefix-dev/pixi/compare/v0.6.0...v0.7.0

This release fixes some bugs and adds the --cwd option to the tasks.

Full Changelog: https://github.com/prefix-dev/pixi/compare/v0.5.0...v0.6.0

We rebuilt pixi shell, fixing the fact that your rc file would overrule the environment activation.

Full Changelog: https://github.com/prefix-dev/pixi/compare/v0.4.0...v0.5.0

This release adds the start of a new cli command pixi project which will allow users to interact with the project configuration from the command line.

Full Changelog: https://github.com/prefix-dev/pixi/compare/v0.3.0...v0.4.0

This releases fixes a lot of issues encountered by the community as well as some awesome community contributions like the addition of pixi global list and pixi global remove.

As this is our first Semantic Versioning release, we'll change from the prototype to the developing phase, as semver describes. A 0.x release could be anything from a new major feature to a breaking change where the 0.0.x releases will be bugfixes or small improvements.

Improving the reliability is important to us, so we added an integration testing framework, we can now test as close as possible to the CLI level using cargo.

Fixing Windows installer build in CI. (#145)

A new command, auth which can be used to authenticate the host of the package channels. A new command, shell which can be used to start a shell in the pixi environment of a project. A refactor of the install command which is changed to global install and the install command now installs a pixi project if you run it in the directory. Platform specific dependencies using [target.linux-64.dependencies] instead of [dependencies] in the pixi.toml

Lots and lots of fixes and improvements to make it easier for this user, where bumping to the new version of rattler helped a lot.

**Examples:**

Example 1 (unknown):
```unknown
[dependencies]
package = { path = "/path/to/recipe.yaml" }
```

Example 2 (unknown):
```unknown
[workspace]
build-variants-files = [
    "./pinning/conda_build_config.yaml",
    "./variants/overrides.yaml",
]
```

Example 3 (unknown):
```unknown
pixi global install --path /path/to/package-name.conda
```

Example 4 (unknown):
```unknown
# Define which packages you want to install and which you want to skip.
pixi install --only packageA --only packageB --skip packageC

# Using this modified environment without updating it again can be done with:
pixi run --as-is my_command
pixi shell --as-is
```

---

## Direnv

**URL:** https://pixi.sh/latest/integration/third_party/direnv/

**Contents:**
- Direnv

direnv is a tool which automatically activates an environment as soon as you enter a directory with a .envrc file that you accepted at some point. This tutorial will demonstrate how to use direnv with Pixi`.

First install direnv by running the following command:

Then create a .envrc file in your Pixi workspace root with the following content:

While direnv comes with hooks for the common shells, these hooks into the shell should not be relied on when using and IDE.

Here you can see how to set up direnv for your favorite editor:

**Examples:**

Example 1 (unknown):
```unknown
pixi global install direnv
```

Example 2 (unknown):
```unknown
watch_file pixi.lock # (1)!
eval "$(pixi shell-hook)" # (2)!
```

Example 3 (unknown):
```unknown
$ cd my-project
direnv: error /my-project/.envrc is blocked. Run `direnv allow` to approve its content
$ direnv allow
direnv: loading /my-project/.envrc
✔ Project in /my-project is ready to use!
direnv: export +CONDA_DEFAULT_ENV +CONDA_PREFIX +PIXI_ENVIRONMENT_NAME +PIXI_ENVIRONMENT_PLATFORMS +PIXI_PROJECT_MANIFEST +PIXI_PROJECT_NAME +PIXI_PROJECT_ROOT +PIXI_PROJECT_VERSION +PIXI_PROMPT ~PATH
$ which python
/my-project/.pixi/envs/default/bin/python
$ cd ..
direnv: unloading
$ which python
python not found
```

---

## Shell

**URL:** https://pixi.sh/latest/advanced/pixi_shell/

**Contents:**
- Shell
- Issues With Pixi Shell#
- Traditional conda activate-like activation#

The pixi shell command is similar to conda activate but works a little different under the hood. Instead of requiring a change to your ~/.bashrc or other files, it will launch a fresh shell. That also means that, instead of conda deactivate, it's enough to just exit the current shell, e.g. by pressing Ctrl+D.

On Unix systems the shell command works by creating a "fake" PTY session that will start the shell, and then send a string like source /tmp/activation-env-12345.sh to the stdin in order to activate the environment. If you would peek under the hood of the the shell command, then you would see that this is the first thing executed in the new shell session.

The temporary script that we generate ends with echo "PIXI_ENV_ACTIVATED" which is used to detect if the environment was activated successfully. If we do not receive this string after three seconds, we will issue a warning to the user.

As explained, pixi shell only works well if we execute the activation script after launching shell. Certain commands that are run in the ~/.bashrc might swallow the activation command, and the environment won't be activated.

For example, if your ~/.bashrc contains code like the following, pixi shell has little chance to succeed:

In order to fix this, we would advise you to follow the steps below to use pixi shell-hook instead.

If you prefer to use the traditional conda activate-like activation, you can use the pixi shell-hook command.

For example, with bash and zsh you can use the following command:

With the --manifest-path option you can also specify which environment to activate. If you want to add a bash function to your ~/.bashrc that will activate the environment, you can use the following command:

After adding this function to your ~/.bashrc/~/.zshrc, you can activate the environment by running:

With fish, you can also evaluate the output of pixi shell-hook:

Or, if you want to add a function to your ~/.config/fish/config.fish:

function pixi_activate # default to current directory if no path is given set -l manifest_path $argv[1] test -z "$manifest_path"; and set manifest_path "." pixi shell-hook --manifest-path "$manifest_path" | source end After adding this function to your ~/.config/fish/config.fish, you can activate the environment by running:

See our direnv page on how to leverage pixi shell-hook to integrate with direnv.

**Examples:**

Example 1 (unknown):
```unknown
# on WSL - the `wsl.exe` somehow takes over `stdin` and prevents `pixi shell` from succeeding
wsl.exe -d wsl-vpnkit --cd /app service wsl-vpnkit start

# on macOS or Linux, some users start fish or nushell from their `bashrc`
# If you wish to start an alternative shell from bash, it's better to do so
# from `~/.bash_profile` or `~/.profile`
if [[ $- = *i* ]]; then
  exec ~/.pixi/bin/fish
fi
```

Example 2 (unknown):
```unknown
$ which python
python not found
$ eval "$(pixi shell-hook)"
$ (default) which python
/path/to/project/.pixi/envs/default/bin/python
```

Example 3 (unknown):
```unknown
eval "$(pixi shell-hook)"
```

Example 4 (unknown):
```unknown
function pixi_activate() {
    # default to current directory if no path is given
    local manifest_path="${1:-.}"
    eval "$(pixi shell-hook --manifest-path $manifest_path)"
}
```

---

## Lock File

**URL:** https://pixi.sh/latest/workspace/lockfile

**Contents:**
- Lock File
- What is a lock file?#
- Why a lock file#
- When is a lock file generated?#
- How to use a lock file#
- Lock file satisfiability#
- The version of the lock file#
- Your lock file is big#
- You don't need a lock file because...#
- Removing the lock file#

A lock file is the protector of the environments, and Pixi is the key to unlock it.

A lock file locks the environment in a specific state. Within Pixi a lock file is a description of the packages in an environment. The lock file contains two definitions:

The environments that are used in the workspace with their complete set of packages. e.g.:

The definition of the packages themselves. e.g.:

Pixi uses the lock file for the following reasons:

This gives you (and your collaborators) a way to really reproduce the environment they are working in. Using tools such as docker suddenly becomes much less necessary.

A lock file is generated when you install a package. More specifically, a lock file is generated from the solve step of the installation process. The solve will return a list of packages that are to be installed, and the lock file will be generated from this list. This diagram tries to explain the process:

Do not edit the lock file

A lock file is a machine only file, and should not be edited by hand.

That said, the pixi.lock is human-readable, so it's easy to track the changes in the environment. We recommend you track the lock file in git or other version control systems. This will ensure that the environment is always reproducible and that you can always revert back to a working state, in case something goes wrong. The pixi.lock and the manifest file pixi.toml/pyproject.toml should always be in sync.

Running the following commands will check and automatically update the lock file if you changed any dependencies:

All the commands that support the interaction with the lock file also include some lock file usage options:

Syncing the lock file with the manifest file

The lock file is always matched with the whole configuration in the manifest file. This means that if you change the manifest file, the lock file will be updated. flowchart TD C[manifest] --> A[lock file] --> B[environment]

The lock file is a description of the environment, and it should always be satisfiable. Satisfiable means that the given manifest file and the created environment are in sync with the lock file. If the lock file is not satisfiable, Pixi will generate a new lock file automatically.

Steps to check if the lock file is satisfiable:

If you want to get more details checkout the actual code as this is a simplification of the actual code.

The lock file has a version number, this is to ensure that the lock file is compatible with the local version of pixi.

Pixi is backward compatible with the lock file, but not forward compatible. This means that you can use an older lock file with a newer version of pixi, but not the other way around.

The lock file can grow quite large, especially if you have a lot of packages installed. This is because the lock file contains all the information about the packages.

If you can not think of a case where you would benefit from a fast reproducible environment, then you don't need a lock file.

But take note of the following:

If you want to remove the lock file, you can simply delete it.

This will remove the lock file, and the next time you run a command that requires the lock file, it will be generated again.

This does remove the locked state of the environment, and the environment will be updated to the latest version of the packages.

**Examples:**

Example 1 (unknown):
```unknown
environments:
    default:
        channels:
          - url: https://conda.anaconda.org/conda-forge/
        packages:
            linux-64:
            ...
            - conda: https://conda.anaconda.org/conda-forge/linux-64/python-3.12.2-hab00c5b_0_cpython.conda
            ...
            osx-64:
            ...
            - conda: https://conda.anaconda.org/conda-forge/osx-64/python-3.12.2-h9f0c242_0_cpython.conda
            ...
```

Example 2 (unknown):
```unknown
- kind: conda
  name: python
  version: 3.12.2
  build: h9f0c242_0_cpython
  subdir: osx-64
  url: https://conda.anaconda.org/conda-forge/osx-64/python-3.12.2-h9f0c242_0_cpython.conda
  sha256: 7647ac06c3798a182a4bcb1ff58864f1ef81eb3acea6971295304c23e43252fb
  md5: 0179b8007ba008cf5bec11f3b3853902
  depends:
    - bzip2 >=1.0.8,<2.0a0
    - libexpat >=2.5.0,<3.0a0
    - libffi >=3.4,<4.0a0
    - libsqlite >=3.45.1,<4.0a0
    - libzlib >=1.2.13,<1.3.0a0
    - ncurses >=6.4,<7.0a0
    - openssl >=3.2.1,<4.0a0
    - readline >=8.2,<9.0a0
    - tk >=8.6.13,<8.7.0a0
    - tzdata
    - xz >=5.2.6,<6.0a0
  constrains:
    - python_abi 3.12.* *_cp312
  license: Python-2.0
  size: 14596811
  timestamp: 1708118065292
```

Example 3 (unknown):
```unknown
graph TD
    A[Install] --> B[Solve]
    B --> C[Generate and write lock file]
    C --> D[Install Packages]
```

Example 4 (unknown):
```unknown
flowchart TD
    C[manifest] --> A[lock file] --> B[environment]
```

---

## Community

**URL:** https://pixi.sh/latest/misc/Community/

**Contents:**
- Community
- Built using Pixi#

When you want to show your users and contributors that they can use Pixi in your repo, you can use the following badge:

To further customize the look and feel of your badge, you can add &style=<custom-style> at the end of the URL. See the documentation on shields.io for more info.

**Examples:**

Example 1 (unknown):
```unknown
[![Pixi Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json)](https://pixi.sh)
```

---

## Conda & PyPI

**URL:** https://pixi.sh/latest/concepts/conda_pypi/

**Contents:**
- Conda & PyPI
- Tool Comparison#
- uv by Astral#
- Solvers#

Pixi is built on top of both the conda and PyPI ecosystems.

Conda is a cross-platform, cross-language package ecosystem that allows users to install packages and manage environments. It is widely used in the data science and machine learning community, but it is also used in other fields. Its power comes from the fact that it always installs binary packages, meaning that it doesn’t need to compile anything. This makes the ecosystem very fast and easy to use.

PyPI is the Python Package Index, which is the main package index for Python packages. It is a much larger ecosystem than conda, especially because the barrier to entry for uploading packages is lower. This means that there are a lot of packages available, but it also means that the quality of the packages is not always as high as in the conda ecosystem.

Pixi can install packages from both ecosystems, but it uses a conda-first approach.

The simplified process is as follows:

Here is a non-exhaustive comparison of the features of conda and PyPI ecosystems.

Pixi uses the uv library to handle PyPI packages. Pixi doesn't install uv (the tool) itself: because both tools are built in Rust, it is used as a library.

We're extremely grateful to the Astral team for their work on uv, which is a great library that allows us to handle PyPI packages in a much better way than before.

Initially, next to pixi we were building a library called rip which had the same goals as uv, but we decided to switch to uv because it quickly became a more mature library, and it has a lot of features that we need.

Because Pixi supports both ecosystems, it currently needs two different solvers to handle the dependencies.

The holy grail of Pixi is to have a single solver that can handle both ecosystems. Because resolvo is written to support both ecosystems, it is possible to use it for PyPI packages as well, but this is not yet implemented.

Because PyPI packages need a base environment to install into, we need to use the conda-first approach, which means that we first solve the conda dependencies, then the PyPI dependencies.

Pixi first runs the conda (rattler) solver, which will resolve the conda dependencies. Then it maps the conda packages to PyPI packages, using parselmouth. Then it runs the PyPI (uv) solver, which will resolve the remaining PyPI dependencies.

The consequence is that Pixi will install the conda package (and not the PyPI package) if both are available and specified as dependencies.

Here is an example of how this works in practice: pixi.toml[dependencies] python = ">=3.8" numpy = ">=1.21.0" [pypi-dependencies] numpy = ">=1.21.0"

Which results in the following output: ➜ pixi list -x Package Version Build Size Kind Source numpy 2.3.0 py313h41a2e72_0 6.2 MiB conda https://conda.anaconda.org/conda-forge/ python 3.13.5 hf3f3da0_102_cp313 12.3 MiB conda https://conda.anaconda.org/conda-forge/

In this example, Pixi will first resolve the conda dependencies and install the numpy and python conda packages. Then it will map the numpy conda package to the numpy PyPI package and resolve any PyPI dependencies. Since there are no remaining PyPI dependencies (as numpy was already installed as a conda package), no PyPI packages will be installed.

Another example is when you have a PyPI package dependency that is not specified as a conda package dependency: pixi.toml[dependencies] python = ">=3.8" [pypi-dependencies] numpy = ">=1.21.0" Which results in the following output: > pixi list --explicit Package Version Build Size Kind Source numpy 2.3.1 43.8 MiB pypi numpy-2.3.1-cp313-cp313-macosx_11_0_arm64.whl python 3.13.5 hf3f3da0_102_cp313 12.3 MiB conda https://conda.anaconda.org/conda-forge/ In this example, Pixi will first resolve the conda dependencies and install the python conda package. Then, since numpy is not specified as a conda dependency, Pixi will resolve the PyPI dependencies and install the numpy PyPI package.

To override or change the mapping of conda packages to PyPI packages, you can use the conda-pypi-map field in the pixi.toml file.

**Examples:**

Example 1 (unknown):
```unknown
[dependencies]
python = ">=3.8"
numpy = ">=1.21.0"

[pypi-dependencies]
numpy = ">=1.21.0"
```

Example 2 (unknown):
```unknown
➜ pixi list -x
Package  Version  Build               Size      Kind   Source
numpy    2.3.0    py313h41a2e72_0     6.2 MiB   conda  https://conda.anaconda.org/conda-forge/
python   3.13.5   hf3f3da0_102_cp313  12.3 MiB  conda  https://conda.anaconda.org/conda-forge/
```

Example 3 (unknown):
```unknown
[dependencies]
python = ">=3.8"

[pypi-dependencies]
numpy = ">=1.21.0"
```

Example 4 (unknown):
```unknown
> pixi list --explicit
Package  Version  Build               Size      Kind   Source
numpy    2.3.1                        43.8 MiB  pypi   numpy-2.3.1-cp313-cp313-macosx_11_0_arm64.whl
python   3.13.5   hf3f3da0_102_cp313  12.3 MiB  conda  https://conda.anaconda.org/conda-forge/
```

---

## Basic usage of Pixi#

**URL:** https://pixi.sh/latest/getting_started/

**Contents:**
- Basic usage of Pixi#
- Managing workspaces#
- Managing global installations#
- Running one-off commands#
- Multiple environments#
- Tasks#
- Multi platform support#
- Utilities#
- Going further#

Pixi can do alot of things, but it is designed to be simple to use. Let's go through the basic usage of Pixi.

Pixi can manage global installations of tools and environments. It installs the environments in a central location, so you can use them from anywhere.

More information: Global Tools

Pixi can run one-off commands in a specific environment.

Pixi workspaces allow you to manage multiple environments. An environment is build out of one or multiple features.

More information: Multiple environments

Pixi can run cross-platform tasks using it's built-in task runner. This can be a predefined task or any normal executable.

Tasks can have other tasks as dependencies. Here is an example of a more complex task usecase pixi.toml[tasks] build = "make build" # using the toml table view [tasks.test] cmd = "pytest" depends-on = ["build"] More information: Tasks

Pixi supports multiple platforms out of the box. You can specify which platforms your workspace supports and Pixi will ensure that the dependencies are compatible with those platforms.

More information: Multi platform support

Pixi comes with a set of utilities to help you debug or manage your setup.

There is still much more that Pixi has to offer. Check out the topics on the sidebar on the left to learn more.

And don't forget to join our Discord to join our community of Pixi enthusiasts!

**Examples:**

Example 1 (unknown):
```unknown
> pixi exec python -VV
Python 3.13.5 | packaged by conda-forge | (main, Jun 16 2025, 08:24:05) [Clang 18.1.8 ]
> pixi exec --spec "python=3.12" python -VV
Python 3.12.11 | packaged by conda-forge | (main, Jun  4 2025, 14:38:53) [Clang 18.1.8 ]
```

Example 2 (unknown):
```unknown
[tasks]
build = "make build"
# using the toml table view
[tasks.test]
cmd = "pytest"
depends-on = ["build"]
```

---

## Trampolines

**URL:** https://pixi.sh/latest/global_tools/trampolines/

**Contents:**
- Trampolines
- Trampolines#

To increase efficiency, pixi uses trampolines—small, specialized binary files that manage configuration and environment setup before executing the main binary. The trampoline approach allows for skipping the execution of activation scripts that have a significant performance impact.

When you execute a globally installed executable, a trampoline performs the following sequence of steps:

The trampoline will take care that the PATH contains the newest changes on your local PATH while avoiding caching temporary PATH changes during installation. If you want to control the base PATH pixi considers, you can set export PIXI_BASE_PATH=$PATH in your shell startup script.

---

## Zed

**URL:** https://pixi.sh/latest/integration/editor/zed/

**Contents:**
- Zed
- Python#
- Direnv#

Zed is a code editor that provides support for many languages out of the box. By installing extensions more languages can be supported.

Zed supports Pixi and Python out of the box. If Zed hasn't done so already, select a suitable Pixi environment in the environment selector and you are good to go!

Zed supports Direnv out of the box. Set up Direnv with Pixi as described in our Direnv page and Zed will activate the environment automatically.

---

## Jetbrains

**URL:** https://pixi.sh/latest/integration/editor/jetbrains/

**Contents:**
- Jetbrains
- Pycharm#
  - Multiple environments#
  - Multiple Pixi workspaces#
  - Debugging#
  - Install as an optional dependency#
  - Alternate approach using environments.txt#
- Direnv#

Native Pixi support on YouTrack

There is a tracking issue for native Pixi support in PyCharm, PY-79041. Feel free to upvote it if it is relevant to you. For CLion, you can track CPP-42761.

You can use PyCharm with Pixi environments by using the conda shim provided by the pixi-pycharm package. An alternate approach that does not use the shim is also described below.

To get started, add pixi-pycharm to your Pixi workspace.

This will ensure that the conda shim is installed in your workspace's environment.

Having pixi-pycharm installed, you can now configure PyCharm to use your Pixi environments. Go to the Add Python Interpreter dialog (bottom right corner of the PyCharm window) and select Conda Environment. Set Conda Executable to the full path of the conda file (on Windows: conda.bat) which is located in .pixi/envs/default/libexec. You can get the path using the following command:

This is an executable that tricks PyCharm into thinking it's the proper conda executable. Under the hood it redirects all calls to the corresponding pixi equivalent.

Use the conda shim from this Pixi workspace

Please make sure that this is the conda shim from this Pixi workspace and not another one. If you use multiple Pixi workspaces, you might have to adjust the path accordingly as PyCharm remembers the path to the conda executable.

Having selected the environment, PyCharm will now use the Python interpreter from your Pixi environment.

PyCharm should now be able to show you the installed packages as well.

You can now run your programs and tests as usual.

Mark .pixi as excluded

In order for PyCharm to not get confused about the .pixi directory, please mark it as excluded.

Also, when using a remote interpreter, you should exclude the .pixi directory on the remote machine. Instead, you should run pixi install on the remote machine and select the conda shim from there.

If your workspace uses multiple environments to tests different Python versions or dependencies, you can add multiple environments to PyCharm by specifying Use existing environment in the Add Python Interpreter dialog.

You can then specify the corresponding environment in the bottom right corner of the PyCharm window.

When using multiple Pixi workspaces, remember to select the correct Conda Executable for each workspace as mentioned above. It also might come up that you have multiple environments with the same name.

It is recommended to rename the environments to something unique.

Logs are written to ~/.cache/pixi-pycharm.log. You can use them to debug problems. Please attach the logs when filing a bug report.

In some cases, you might only want to install pixi-pycharm on your local dev-machines but not in production. To achieve this, we can use multiple environments.

Now you as a user can run pixi shell, which will start the default environment. In production, you then just run pixi run -e prod COMMAND, and the minimal prod environment is installed.

There is another approach for configuring PyCharm that avoids the need for the pixi-pycharm shim. It requires that you have conda installed locally (PyCharm will detect it automatically if installed in a standard location).

To configure an interpreter for a new workspace:

Edit conda's environment list located at ~/.conda/environments.txt. Simply append the full file paths of any pixi environments you wish to include, e.g.:

In PyCharm, when adding the interpreter for your workspace, scroll down to the bottom of the Python Interpreter dropdown menu and choose Show All ... to bring up the Python Interpreters dialog.

Select the + button to add a new local existing conda interpreter using the standard conda location and choose the desired prefix from the list. (If you edited the environment file while PyCharm was running, you may need to reload the environments.)

This will add the environment but will automatically give it a name matching the last component of the directory path, which will often just be default for pixi environments. This is particularly problematic if you work on many workspaces. You can change PyCharm's name for the environment by clicking on the pencil icon or using the right-click dropdown menu.

Once you have added and renamed the environments, select the desired interpreter to use in PyCharm from the list.

If your workspace uses more than one environment, you can switch between them by selecting interpreter name in the status bar at the bottom of the PyCharm window and selecting the interpreter for the desired interpreter from the list. Note that this will trigger PyCharm reindexing and might not be very fast.

As with the pixi-pycharm shim, you should avoid using the PyCharm UI to attempt to add or remove packages from your environments and you should make sure to exclude the .pixi directory from PyCharm indexing.

In order to use Direnv with Jetbrains products you first have to install the Direnv plugin. Then follow the instructions in our Direnv doc page. Now your Jetbrains IDE will be run within the selected Pixi environment.

**Examples:**

Example 1 (unknown):
```unknown
pixi add pixi-pycharm
```

Example 2 (unknown):
```unknown
pixi run 'echo $CONDA_PREFIX/libexec/conda'
```

Example 3 (unknown):
```unknown
pixi run 'echo $CONDA_PREFIX\\libexec\\conda.bat'
```

Example 4 (unknown):
```unknown
[workspace]
name = "multi-env"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["numpy"]

[tool.pixi.workspace]
channels = ["conda-forge"]
platforms = ["linux-64"]

[tool.pixi.feature.lint.dependencies]
ruff =  "*"

[tool.pixi.feature.dev.dependencies]
pixi-pycharm = "*"

[tool.pixi.environments]
# The production environment is the default feature set.
# Adding a solve group to make sure the same versions are used in the `default` and `prod` environments.
prod = { solve-group = "main" }

# Setup the default environment to include the dev features.
# By using `default` instead of `dev` you'll not have to specify the `--environment` flag when running `pixi run`.
default = { features = ["dev"], solve-group = "main" }

# The lint environment doesn't need the default feature set but only the `lint` feature
# and thus can also be excluded from the solve group.
lint = { features = ["lint"], no-default-feature = true }
```

---

## S3

**URL:** https://pixi.sh/latest/deployment/s3/

**Contents:**
- S3
- Using AWS configuration#
- Using Pixi's Configuration#
- Public S3 Buckets#
- S3-Compatible Storage#
  - MinIO#
  - Cloudflare R2#
  - Wasabi#
  - Backblaze B2#
  - Google Cloud Storage#

If you want to use S3 object storage to fetch your packages, you can use the s3:// protocol as a channel.

In the bucket, your objects need to adhere to the standard conda repository structure:

Pixi supports two ways to configure access to your S3 bucket:

These two options are mutually exclusive! Specifying s3-options (see below) will deactivate the AWS credentials fetching. You can either use the AWS credentials from the conventional locations (by not specifying s3-options) or from pixi's authentication storage (by specifying s3-options).

You can specify AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in your environment variables for Pixi to use them.

You can also specify AWS_CONFIG_FILE and AWS_PROFILE to use a custom AWS configuration file and profile.

You can specify the workspace.s3-options in your pixi.toml file. This might be useful when you want to use a custom S3-compatible host and not AWS's configuration.

You need to configure this per bucket you use, i.e. use [workspace.s3-options.<bucket-name>].

You can also specify the s3-options in your Pixi configuration.

Public buckets that don't need authentication can be used by just specifying the endpoint as a regular https URL. For example, on AWS, you might have a bucket that is publicly accessible via https://my-public-bucket.s3.eu-central-1.amazonaws.com.

Note that for this, you need to configure your S3 bucket in such a way that it allows public access. On AWS, you need the GetObject and ListBucket permissions for this. Here is an example policy for AWS S3:

Cloudflare R2 also supports public buckets through a Cloudflare-managed r2.dev subdomain or a custom domain under your control, see here.

Many other cloud providers offer S3-compatible storage APIs. You can use them with Pixi by specifying the s3-options in your manifest file.

Note Pixi also supports gcs:// URLs.

You can upload to S3 using rattler-build upload s3. For more information, see rattler-build's documentation.

Every time you upload new packages to your package repository, the repodata.json file needs to be updated. This is done automatically for conda package servers like anaconda.org or prefix.dev. For S3 buckets, on the other hand, we need to do this manually since an S3 bucket is only a storage system and not a package server.

To re-index an S3 bucket, you can use the rattler-index package which is available on conda-forge.

**Examples:**

Example 1 (unknown):
```unknown
[workspace]
# ...
channels = ["s3://my-bucket/custom-channel"]
```

Example 2 (unknown):
```unknown
my-bucket/
    custom-channel/
        noarch/
            repodata.json
            ...
        linux-64/
            repodata.json
            ...
```

Example 3 (unknown):
```unknown
[profile conda]
sso_account_id = 123456789012
sso_role_name = PowerUserAccess
sso_start_url = https://my-company.awsapps.com/start
sso_region = eu-central-1
region = eu-central-1
output = json
```

Example 4 (unknown):
```unknown
$ export AWS_CONFIG_FILE=/path/to/aws.config
$ export AWS_PROFILE=conda
$ aws sso login
Attempting to automatically open the SSO authorization page in your default browser.
If the browser does not open or you wish to use a different device to authorize this request, open the following URL:

https://my-company.awsapps.com/start/#/device

Then enter the code:

DTBC-WFXC
Successfully logged into Start URL: https://my-company.awsapps.com/start
$ pixi search -c s3://my-s3-bucket/channel my-private-package
# ...
```

---

## Channel Logic

**URL:** https://pixi.sh/latest/advanced/channel_logic/

**Contents:**
- Channel Logic
- Channel Specific Dependencies#
- Channel Priority#
- Use Case: pytorch and nvidia with conda-forge#
- Force a Specific Channel Priority#

All logic regarding the decision which dependencies can be installed from which channel is done by the instruction we give the solver.

The actual code regarding this is in the rattler_solve crate. This might however be hard to read. Therefore, this document will continue with simplified flow charts.

When a user defines a channel per dependency, the solver needs to know the other channels are unusable for this dependency. [workspace] channels = ["conda-forge", "my-channel"] [dependencies] packgex = { version = "*", channel = "my-channel" } In the packagex example, the solver will understand that the package is only available in my-channel and will not look for it in conda-forge.

The flowchart of the logic that excludes all other channels:

Channel priority is dictated by the order in the workspace.channels array, where the first channel is the highest priority. For instance: [workspace] channels = ["conda-forge", "my-channel", "your-channel"] If the package is found in conda-forge the solver will not look for it in my-channel and your-channel, because it tells the solver they are excluded. If the package is not found in conda-forge the solver will look for it in my-channel and if it is found there it will tell the solver to exclude your-channel for this package. This diagram explains the logic: flowchart TD A[Start] --> B[Given a Dependency] B --> C{Loop Over Channels} C --> D{Package in This Channel?} D -->|No| C D -->|Yes| E{"This the first channel for this package?"} E -->|Yes| F[Include Package in Candidates] E -->|No| G[Exclude Package from Candidates] F --> H{Any Other Channels?} G --> H H -->|Yes| C H -->|No| I{Any Other Dependencies?} I -->|No| J[End] I -->|Yes| B

This method ensures the solver only adds a package to the candidates if it's found in the highest priority channel available. If you have 10 channels and the package is found in the 5th channel it will exclude the next 5 channels from the candidates if they also contain the package.

A common use case is to use pytorch with nvidia drivers, while also needing the conda-forge channel for the main dependencies. [workspace] channels = ["nvidia/label/cuda-11.8.0", "nvidia", "conda-forge", "pytorch"] platforms = ["linux-64"] [dependencies] cuda = {version = "*", channel="nvidia/label/cuda-11.8.0"} pytorch = {version = "2.0.1.*", channel="pytorch"} torchvision = {version = "0.15.2.*", channel="pytorch"} pytorch-cuda = {version = "11.8.*", channel="pytorch"} python = "3.10.*" What this will do is get as much as possible from the nvidia/label/cuda-11.8.0 channel, which is actually only the cuda package.

Then it will get all packages from the nvidia channel, which is a little more and some packages overlap the nvidia and conda-forge channel. Like the cuda-cudart package, which will now only be retrieved from the nvidia channel because of the priority logic.

Then it will get the packages from the conda-forge channel, which is the main channel for the dependencies.

But the user only wants the pytorch packages from the pytorch channel, which is why pytorch is added last and the dependencies are added as channel specific dependencies.

We don't define the pytorch channel before conda-forge because we want to get as much as possible from the conda-forge as the pytorch channel is not always shipping the best versions of all packages.

For example, it also ships the ffmpeg package, but only an old version which doesn't work with the newer pytorch versions. Thus breaking the installation if we would skip the conda-forge channel for ffmpeg with the priority logic.

If you want to force a specific priority for a channel, you can use the priority (int) key in the channel definition. The higher the number, the higher the priority. Non specified priorities are set to 0 but the index in the array still counts as a priority, where the first in the list has the highest priority.

This priority definition is mostly important for multiple environments with different channel priorities, as by default feature channels are prepended to the workspace channels.

[workspace] name = "test_channel_priority" platforms = ["linux-64", "osx-64", "win-64", "osx-arm64"] channels = ["conda-forge"] [feature.a] channels = ["nvidia"] [feature.b] channels = [ "pytorch", {channel = "nvidia", priority = 1}] [feature.c] channels = [ "pytorch", {channel = "nvidia", priority = -1}] [environments] a = ["a"] b = ["b"] c = ["c"] This example creates 4 environments, a, b, c, and the default environment. Which will have the following channel order:

Using pixi info you can check the priority of the channels in the environment. pixi info Environments ------------ Environment: default Features: default Channels: conda-forge Dependency count: 0 Target platforms: linux-64 Environment: a Features: a, default Channels: nvidia, conda-forge Dependency count: 0 Target platforms: linux-64 Environment: b Features: b, default Channels: nvidia, pytorch, conda-forge Dependency count: 0 Target platforms: linux-64 Environment: c Features: c, default Channels: pytorch, conda-forge, nvidia Dependency count: 0 Target platforms: linux-64

**Examples:**

Example 1 (unknown):
```unknown
[workspace]
channels = ["conda-forge", "my-channel"]

[dependencies]
packgex = { version = "*", channel = "my-channel" }
```

Example 2 (unknown):
```unknown
flowchart TD
    A[Start] --> B[Given a Dependency]
    B --> C{Channel Specific Dependency?}
    C -->|Yes| D[Exclude All Other Channels for This Package]
    C -->|No| E{Any Other Dependencies?}
    E -->|Yes| B
    E -->|No| F[End]
    D --> E
```

Example 3 (unknown):
```unknown
[workspace]
channels = ["conda-forge", "my-channel", "your-channel"]
```

Example 4 (unknown):
```unknown
flowchart TD
    A[Start] --> B[Given a Dependency]
    B --> C{Loop Over Channels}
    C --> D{Package in This Channel?}
    D -->|No| C
    D -->|Yes| E{"This the first channel
     for this package?"}
    E -->|Yes| F[Include Package in Candidates]
    E -->|No| G[Exclude Package from Candidates]
    F --> H{Any Other Channels?}
    G --> H
    H -->|Yes| C
    H -->|No| I{Any Other Dependencies?}
    I -->|No| J[End]
    I -->|Yes| B
```

---

## Authentication

**URL:** https://pixi.sh/latest/deployment/authentication/

**Contents:**
- Authentication
- Examples#
- Where does Pixi store the authentication information?#
- Fallback storage#
- Override the authentication storage#
- PyPI authentication#
  - Keyring authentication#
    - Installing keyring#
    - Configuring your workspace to use keyring#
    - Installing your environment#

You can authenticate Pixi with a server like prefix.dev, a private quetz instance or anaconda.org. Different servers use different authentication methods. In this documentation page, we detail how you can authenticate against the different servers and where the authentication information is stored.

The different options are "token", "conda-token" and "username + password".

The token variant implements a standard "Bearer Token" authentication as is used on the prefix.dev platform. A Bearer Token is sent with every request as an additional header of the form Authentication: Bearer <TOKEN>.

The conda-token option is used on anaconda.org and can be used with a quetz server. With this option, the token is sent as part of the URL following this scheme: conda.anaconda.org/t/<TOKEN>/conda-forge/linux-64/....

The last option, username & password, are used for "Basic HTTP Authentication". This is the equivalent of adding http://user:password@myserver.com/.... This authentication method can be configured quite easily with a reverse NGinx or Apache server and is thus commonly used in self-hosted systems.

Login to anaconda.org:

Login to a basic HTTP secured server:

Login to an S3 bucket:

S3 authentication is also supported through AWS's typical AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables, see the S3 section for more details.

The storage location for the authentication information is system-dependent. By default, Pixi tries to use the keychain to store this sensitive information securely on your machine.

On Windows, the credentials are stored in the "credentials manager". Searching for rattler (the underlying library Pixi uses) you should find any credentials stored by Pixi (or other rattler-based programs).

On macOS, the passwords are stored in the keychain. To access the password, you can use the Keychain Access program that comes pre-installed on macOS. Searching for rattler (the underlying library Pixi uses) you should find any credentials stored by Pixi (or other rattler-based programs).

On Linux, one can use GNOME Keyring (or just Keyring) to access credentials that are securely stored by libsecret. Searching for rattler should list all the credentials stored by Pixi and other rattler-based programs.

If you run on a server with none of the aforementioned keychains available, then Pixi falls back to store the credentials in an insecure JSON file. This JSON file is located at ~/.rattler/credentials.json and contains the credentials.

You can use the RATTLER_AUTH_FILE environment variable to override the default location of the credentials file. When this environment variable is set, it provides the only source of authentication data that is used by pixi.

RATTLER_AUTH_FILE has higher precedence than the CLI argument.

The JSON should follow the following format:

Note: if you use a wildcard in the host, any subdomain will match (e.g. *.prefix.dev also matches repo.prefix.dev).

Lastly you can set the authentication override file in the global configuration file.

Currently, we support the following methods for authenticating against PyPI:

We want to add more methods in the future, so if you have a specific method you would like to see, please let us know.

Currently, Pixi supports the uv method of authentication through the python keyring library.

To install keyring you can use pixi global install:

For other registries, you will need to adapt these instructions to add the right keyring backend.

Use keyring to store your credentials e.g:

Add the following configuration to your Pixi manifest, making sure to include your_username@ in the URL of the registry:

After making sure you are logged in, for instance by running gcloud auth login, add the following configuration to your Pixi manifest:

To find this URL more easily, you can use the gcloud command:

After following the keyrings.artifacts instructions and making sure that keyring works correctly, add the following configuration to your Pixi manifest:

Ensure you are logged in e.g via aws sso login and add the following configuration to your Pixi manifest:

Either configure your Global Config, or use the flag --pypi-keyring-provider which can either be set to subprocess (activated) or disabled:

pixi allows you to access private registries securely by authenticating with credentials stored in a .netrc file.

In the .netrc file, you store authentication details like this:

For more details, you can access the .netrc docs.

**Examples:**

Example 1 (unknown):
```unknown
Usage: pixi auth login [OPTIONS] <HOST>

Arguments:
  <HOST>  The host to authenticate with (e.g. repo.prefix.dev)

Options:
      --token <TOKEN>                                The token to use (for authentication with prefix.dev)
      --username <USERNAME>                          The username to use (for basic HTTP authentication)
      --password <PASSWORD>                          The password to use (for basic HTTP authentication)
      --conda-token <CONDA_TOKEN>                    The token to use on anaconda.org / quetz authentication
      --s3-access-key-id <S3_ACCESS_KEY_ID>          The S3 access key ID
      --s3-secret-access-key <S3_SECRET_ACCESS_KEY>  The S3 secret access key
      --s3-session-token <S3_SESSION_TOKEN>          The S3 session token
  -v, --verbose...                                   Increase logging verbosity
  -q, --quiet...                                     Decrease logging verbosity
      --color <COLOR>                                Whether the log needs to be colored [env: PIXI_COLOR=] [default: auto] [possible values: always, never, auto]
      --no-progress                                  Hide all progress bars, always turned on if stderr is not a terminal [env: PIXI_NO_PROGRESS=]
  -h, --help                                         Print help
```

Example 2 (unknown):
```unknown
pixi auth login prefix.dev --token pfx_jj8WDzvnuTHEGdAhwRZMC1Ag8gSto8
```

Example 3 (unknown):
```unknown
pixi auth login anaconda.org --conda-token xy-72b914cc-c105-4ec7-a969-ab21d23480ed
```

Example 4 (unknown):
```unknown
pixi auth login myserver.com --username user --password password
```

---

## Conda Deny

**URL:** https://pixi.sh/latest/integration/third_party/conda_deny/

**Contents:**
- Conda Deny
  - 💿 Installation#
  - 🎯 Usage#
  - 🔒 Authorized access to allowlist#
  - Output Formats#

conda-deny in one command:

In your favorite pixi workspace, run: pixi exec conda-deny check --osi

This will check your workspace for license compliance against the list of OSI approved licenses.

conda-deny is a CLI tool for checking software environment dependencies for license compliance. Compliance is checked with regard to an allowlist of licenses provided by the user.

You can install conda-deny using pixi:

Or by downloading our pre-built binaries from the releases page.

conda-deny can be configured in your pixi.toml or pyproject.toml (pixi.toml is preferred). The tool expects a configuration in the following format:

After the installation, you can run conda-deny check in your workspace. This checks the dependencies defined by your pixi.lock against your allowlist.

If a Bearer Token is needed to access your allowlist, you can provide it using CONDA_DENY_BEARER_TOKEN. An example use case would be a private repository containing your allowlist.

conda-deny supports different output formats via the --output (or -o) flag. Output formatting works for both, the list and the check command.

By running conda-deny bundle, conda-deny will create a directory containing all your dependencies' original license files.

This can come in handy when creating SBOMs or sharing compliance information with other people.

**Examples:**

Example 1 (unknown):
```unknown
pixi exec conda-deny check --osi
```

Example 2 (unknown):
```unknown
pixi global install conda-deny
```

Example 3 (unknown):
```unknown
[tool.conda-deny]
#--------------------------------------------------------
# General setup options:
#--------------------------------------------------------
license-allowlist = "https://raw.githubusercontent.com/quantco/conda-deny/main/tests/test_remote_base_configs/conda-deny-license_allowlist.toml" # or ["license_allowlist.toml", "other_license_allowlist.toml"]
platform = "linux-64" # or ["linux-64", "osx-arm64"]
environment = "default" # or ["default", "py39", "py310", "prod"]
lockfile = "environment/pixi.lock" # or ["environment1/pixi.lock", "environment2/pixi.lock"]
# lockfile also supports glob patterns:
# lockfile = "environments/**/*.lock"

#--------------------------------------------------------
# License allowlist directly in configuration file:
#--------------------------------------------------------
safe-licenses = ["MIT", "BSD-3-Clause"]
ignore-packages = [
    { package = "make", version = "0.1.0" },
]
```

Example 4 (unknown):
```unknown
$ conda-deny list --output csv
package_name,version,license,platform,build,safe
_openmp_mutex,4.5,BSD-3-Clause,linux-aarch64,2_gnu,false
_openmp_mutex,4.5,BSD-3-Clause,linux-64,2_gnu,false
...
```

---

## Pixi Diff

**URL:** https://pixi.sh/latest/integration/extensions/pixi_diff/

**Contents:**
- Pixi Diff

It can happen that you want to know what changed in your lockfile after repeatedly adding and removing dependencies within a pull request. For this, you can use pavelzw/pixi-diff to calculate the differences between two lockfiles. This can be leveraged in combination with pavelzw/pixi-diff-to-markdown to generate a markdown file that shows the diff in a human-readable format. With charmbracelet/glow, you can even render the markdown file in the terminal.

Install the tools globally

All of the above-mentioned tools are available on conda-forge and can be installed using pixi global install.

pixi diff --before pixi.lock.old --after pixi.lock.new will output a JSON object that contains the differences between the two lockfiles similar to pixi update --json.

Named pipes can be handy for comparing lockfiles from different states in your git history:

Or specify either the "before" or "after" lockfile via stdin:

This can be integrated with pixi-diff-to-markdown to generate a markdown file that shows the diff in a human-readable format:

pixi-diff-to-markdown in GitHub Actions updates

For other usages of pixi-diff-to-markdown, see also our page about updating lockfiles using GitHub Actions.

You can view this generated markdown file in your terminal using glow.

You can also view the markdown file directly from stdin using glow.

**Examples:**

Example 1 (unknown):
```unknown
pixi global install pixi-diff pixi-diff-to-markdown glow-md
```

Example 2 (unknown):
```unknown
$ pixi diff --before pixi.lock.old --after pixi.lock.new
{
  "version": 1,
  "environment": {
    "default": {
      "osx-arm64": [
        {
          "name": "libmpdec",
          "before": null,
          "after": {
            "conda": "https://conda.anaconda.org/conda-forge/osx-arm64/libmpdec-4.0.0-h99b78c6_0.conda",
            "sha256": "f7917de9117d3a5fe12a39e185c7ce424f8d5010a6f97b4333e8a1dcb2889d16",
            "md5": "7476305c35dd9acef48da8f754eedb40",
            "depends": [
              "__osx >=11.0"
            ],
            "license": "BSD-2-Clause",
            "license_family": "BSD",
            "size": 69263,
            "timestamp": 1723817629767
          },
          "type": "conda"
        },
// ...
```

Example 3 (unknown):
```unknown
# bash / zsh
pixi diff --before <(git show HEAD~20:pixi.lock) --after pixi.lock

# fish
pixi diff --before (git show HEAD~20:pixi.lock | psub) --after pixi.lock
```

Example 4 (unknown):
```unknown
git show HEAD~20:pixi.lock | pixi diff --before - --after pixi.lock
```

---

## Pixi Pack

**URL:** https://pixi.sh/latest/deployment/pixi_pack/

**Contents:**
- Pixi Pack
  - pixi-unpack: Unpacking an environment#
  - Cross-platform Packs#
  - Self-Extracting Binaries#
    - Custom pixi-unpack executable path#
      - Example Usage#
  - Inject Additional Packages#
  - PyPi support#
  - Mirror and S3 middleware#
  - Setting maximum number of parallel downloads#

pixi-pack is a simple tool that takes a Pixi environment and packs it into a compressed archive that can be shipped to the target machine. The corresponding pixi-unpack tool can be used to unpack the archive and install the environment.

Both tools can be installed via

Or by downloading our pre-built binaries from the releases page.

Instead of installing pixi-pack and pixi-unpack globally, you can also use pixi exec to run pixi-pack in a temporary environment:

You can also write pixi pack (and pixi unpack) if you have pixi, and pixi-pack and pixi-unpack installed globally.

You can pack an environment with

This will create an environment.tar file that contains all conda packages required to create the environment.

With pixi-unpack environment.tar, you can unpack the environment on your target system. This will create a new conda environment in ./env that contains all packages specified in your pixi.toml. It also creates an activate.sh (or activate.bat on Windows) file that lets you activate the environment without needing to have conda or micromamba installed.

Since pixi-pack just downloads the .conda and .tar.bz2 files from the conda repositories, you can trivially create packs for different platforms.

You can only unpack a pack on a system that has the same platform as the pack was created for.

You can create a self-extracting binary that contains the packed environment and a script that unpacks the environment. This can be useful if you want to distribute the environment to users that don't have pixi-unpack installed.

When creating a self-extracting binary, you can specify a custom path or URL to a pixi-unpack executable to avoid downloading it from the default location.

You can provide one of the following as the --pixi-unpack-source:

The produced executable is a simple shell script that contains both the pixi-unpack binary as well as the packed environment.

You can inject additional packages into the environment that are not specified in pixi.lock by using the --inject flag:

This can be particularly useful if you build the package itself and want to include the built package in the environment but still want to use pixi.lock from the workspace.

You can also pack PyPi wheel packages into your environment. pixi-pack only supports wheel packages and not source distributions. If you happen to use source distributions, you can ignore them by using the --ignore-pypi-non-wheel flag. This will skip the bundling of PyPi packages that are source distributions.

The --inject option also supports wheels.

In contrast to injecting from conda packages, we cannot verify that injected wheels are compatible with the target environment. Please make sure the packages are compatible.

You can use mirror middleware by creating a configuration file as described in the pixi documentation and referencing it using --config.

If you are using S3 in pixi, you can also add the appropriate S3 config in your config file and reference it.

Use pixi-pack --config config.toml to use the custom configuration file. See pixi docs for more information.

You can cache downloaded packages to speed up subsequent pack operations by using the --use-cache flag:

This will store all downloaded packages in the specified directory and reuse them in future pack operations. The cache follows the same structure as conda channels, organizing packages by platform subdirectories (e.g., linux-64, win-64, etc.).

Using a cache is particularly useful when:

If you don't have pixi-pack available on your target system, and do not want to use self-extracting binaries (see above), you can still install the environment if you have conda or micromamba available. Just unarchive the environment.tar, then you have a local channel on your system where all necessary packages are available. Next to this local channel, you will find an environment.yml file that contains the environment specification. You can then install the environment using conda or micromamba:

The environment.yml and repodata.json files are only for this use case, pixi-unpack does not use them.

Both conda and mamba are always installing pip as a side effect when they install python, see conda's documentation. This is different from how pixi works and can lead to solver errors when using pixi-pack's compatibility mode since pixi doesn't include pip by default. You can fix this issue in two ways:

**Examples:**

Example 1 (unknown):
```unknown
pixi global install pixi-pack pixi-unpack
```

Example 2 (unknown):
```unknown
pixi exec pixi-pack
pixi exec pixi-unpack environment.tar
```

Example 3 (unknown):
```unknown
pixi-pack --environment prod --platform linux-64 pixi.toml
```

Example 4 (unknown):
```unknown
# environment.tar
| pixi-pack.json
| environment.yml
| channel
|    ├── noarch
|    |    ├── tzdata-2024a-h0c530f3_0.conda
|    |    ├── ...
|    |    └── repodata.json
|    └── linux-64
|         ├── ca-certificates-2024.2.2-hbcca054_0.conda
|         ├── ...
|         └── repodata.json
```

---

## Pixi Extensions#

**URL:** https://pixi.sh/latest/integration/extensions/introduction/

**Contents:**
- Pixi Extensions#
- How Extensions Work#
- Extension Discovery#
  - 1. PATH Environment Variable#
  - 2. pixi global Directories#
- Installing Extensions#
  - Using pixi global (Recommended)#
  - Manual Installation#
- Contributing Extensions#
  - Creating an Extension#

Pixi allows you to extend its functionality with various extensions. When executing e.g. pixi diff, Pixi will search for the executable pixi-diff in your PATH and in your pixi global directories. Then it will execute it by passing any additional arguments to it.

Pixi extensions are standalone executables that follow a simple naming convention: they must be named pixi-{command} where {command} is the name of the subcommand you want to add. When you run pixi {command}, Pixi will automatically discover and execute the corresponding pixi-{command} executable.

Pixi discovers extensions by searching for pixi-* executables in the following locations, in order:

Pixi searches all directories in your PATH environment variable for executables with the pixi- prefix.

Pixi also searches in directories managed by pixi global, which allows for organized extension management without cluttering your system PATH.

When you run pixi --list, all discovered extensions are automatically listed alongside all built-in commands, making the commands easily discoverable.

The easiest way to install Pixi extensions is using pixi global install:

This approach has several advantages: - Isolated environments: Each extension gets its own environment, preventing dependency conflicts - Automatic discovery: Extensions are automatically found by Pixi without modifying PATH - Easy management: Use pixi global list and pixi global remove to manage extensions - Consistent experience: Extensions appear in pixi --list with all the built-in commands, just like how Cargo handles it

You can also install extensions manually by placing the executable in any directory in your PATH:

Choose a descriptive name: Your extension should be named pixi-{command} where {command} clearly describes its functionality.

Create the executable: Extensions can be written in any language (Rust, Python, shell scripts, etc.) as long as they produce an executable binary.

Handle arguments: Extensions receive all arguments passed after the command name.

Save this as pixi-hello, make it executable (chmod +x pixi-hello), and place it in your PATH.

Usage: pixi hello Alice outputs Hello, Alice!

Pixi includes intelligent command suggestions powered by string similarity. If you mistype a command name, Pixi will suggest the closest match from both built-in commands and available extensions:

This works for both built-in commands and any extensions you have installed, making extension discovery seamless.

**Examples:**

Example 1 (unknown):
```unknown
# Install a single extension
pixi global install pixi-pack

# Install multiple extensions at once
pixi global install pixi-pack pixi-diff
```

Example 2 (unknown):
```unknown
# Download or build the extension
curl -L https://github.com/user/pixi-myext/releases/download/v1.0.0/pixi-myext -o pixi-myext
chmod +x pixi-myext
mv pixi-myext ~/.local/bin/
```

Example 3 (python):
```python
#!/usr/bin/env python3
import sys

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
```

Example 4 (unknown):
```unknown
$ pixi pck
error: unrecognized subcommand 'pck`
tip: a similar subcommand exists: 'pack'
```

---

## Shebang

**URL:** https://pixi.sh/latest/advanced/shebang/

**Contents:**
- Shebang

Only on Unix-like systems

The following approach only works on Unix-like systems (i.e. Linux and macOS) since Windows does not support shebang lines.

For simple scripts, you can use pixi exec to run them directly without needing to take care of installing dependencies or setting up an environment. This can be done by adding a shebang line at the top of the script, which tells the system how to execute the script. Usually, a shebang line starts with #!/usr/bin/env followed by the name of the interpreter to use.

Instead of adding an interpreter, you can also just add pixi exec at the beginning of the script. The only requirement for your script is that you must have pixi installed on your system.

Making the script executable

You might need to make the script executable by running chmod +x my-script.sh.

Explanation what's happening

The #! are magic characters that tell your system how to execute the script (take everything after the #! and append the file name).

The /usr/bin/env is used to find pixi in the system's PATH. The -S option tells /usr/bin/env to use the first argument as the interpreter and the rest as arguments to the interpreter. pixi exec --spec bat creates a temporary environment containing only bat. bash -e (separated with --) is the command that is executed in this environment. So in total, pixi exec --spec bat -- bash -e use-bat.sh is being executed when you run ./use-bat.sh.

You can also write self-contained python files that ship with their dependencies. This example shows a very simple CLI that installs a Pixi environment to an arbitrary prefix using py-rattler and typer.

**Examples:**

Example 1 (unknown):
```unknown
#!/usr/bin/env -S pixi exec --spec bat -- bash -e

bat my-file.json
```

Example 2 (python):
```python
#!/usr/bin/env -S pixi exec --spec py-rattler>=0.10.0,<0.11 --spec typer>=0.15.0,<0.16 -- python

import asyncio
from pathlib import Path
from typing import get_args

from rattler import install as rattler_install
from rattler import LockFile, Platform
from rattler.platform.platform import PlatformLiteral
from rattler.networking import Client, MirrorMiddleware, AuthenticationMiddleware
import typer


app = typer.Typer()


async def _install(
    lock_file_path: Path,
    environment_name: str,
    platform: Platform,
    target_prefix: Path,
) -> None:
    lock_file = LockFile.from_path(lock_file_path)
    environment = lock_file.environment(environment_name)
    if environment is None:
        raise ValueError(f"Environment {environment_name} not found in lock file {lock_file_path}")
    records = environment.conda_repodata_records_for_platform(platform)
    if not records:
        raise ValueError(f"No records found for platform {platform} in lock file {lock_file_path}")
    await rattler_install(
        records=records,
        target_prefix=target_prefix,
        client=Client(
            middlewares=[
                MirrorMiddleware({"https://conda.anaconda.org/conda-forge": ["https://repo.prefix.dev/conda-forge"]}),
                AuthenticationMiddleware(),
            ]
        ),
    )


@app.command()
def install(
    lock_file_path: Path = Path("pixi.lock").absolute(),
    environment_name: str = "default",
    platform: str = str(Platform.current()),
    target_prefix: Path = Path("env").absolute(),
) -> None:
    """
    Installs a pixi.lock file to a custom prefix.
    """
    if platform not in get_args(PlatformLiteral):
        raise ValueError(f"Invalid platform {platform}. Must be one of {get_args(PlatformLiteral)}")
    asyncio.run(
        _install(
            lock_file_path=lock_file_path,
            environment_name=environment_name,
            platform=Platform(platform),
            target_prefix=target_prefix,
        )
    )


if __name__ == "__main__":
    app()
```

---

## Poetry

**URL:** https://pixi.sh/latest/switching_from/poetry/

**Contents:**
- Poetry
- Why Pixi?#
- Quick look at the differences#
- Support both poetry and pixi in my workspace#

Welcome to the guide designed to ease your transition from poetry to pixi. This document compares key commands and concepts between these tools, highlighting pixi's unique approach to managing environments and packages. With pixi, you'll experience a workspace-based workflow similar to poetry while including the conda ecosystem and allowing for easy sharing of your work.

Poetry is most-likely the closest tool to Pixi in terms of workspace management, in the python ecosystem. On top of the PyPI ecosystem, pixi adds the power of the conda ecosystem, allowing for a more flexible and powerful environment management.

You can allow users to use poetry and pixi in the same workspace, they will not touch each other's parts of the configuration or system. It's best to duplicate the dependencies, basically making an exact copy of the tool.poetry.dependencies into tool.pixi.pypi-dependencies. Make sure that python is only defined in the tool.pixi.dependencies and not in the tool.pixi.pypi-dependencies.

Mixing pixi and poetry

It's possible to use poetry in pixi environments but this is advised against. Pixi supports PyPI dependencies in a different way than poetry does, and mixing them can lead to unexpected behavior. As you can only use one package manager at a time, it's best to stick to one.

If using poetry on top of a Pixi workspace, you'll always need to install the poetry environment after the pixi environment. And let pixi handle the python and poetry installation.

---

## System Requirements

**URL:** https://pixi.sh/latest/workspace/system_requirements/

**Contents:**
- System Requirements
- Maximum or Minimum System Requirements#
- Default System Requirements#
- Customizing System Requirements#
  - Adjusting for Older Systems#
  - Using CUDA in pixi#
  - Setting System Requirements environment specific#
  - Available Override Options#
- Additional Resources#

System requirements tell Pixi the system specifications needed to install and run your workspace’s environment. They ensure that the dependencies match the operating system and hardware of your machine.

Think of it like this:

You’re defining what “kind of machines” your workspace can run on. [system-requirements] linux = "4.18" libc = { family = "glibc", version = "2.28" } cuda = "12" macos = "13.0" This results in a workspace that can run on:

When resolving dependencies, Pixi combines:

This way, Pixi guarantees your environment is consistent and compatible with your machine.

System specifications are closely related to virtual packages, allowing for flexible and accurate dependency management.

Need to support multiple types of systems that don't share the same specifications?

You can define system-requirements for different features in your workspace. For example, if you have a feature that requires CUDA and another that does not, you can specify the system requirements for each feature separately. Check the example below for more details.

The system requirements don't specify a maximum or minimum version. They specify the version that can be expected on the host system. It's up to the dependency resolver to determine if the system meets the requirements based on the versions available. e.g.:

Most of the time, packages will specify the minimum version (>=) it requires. So we often say that the system-requirements define the minimum version of the system specifications.

For example cuda-version-12.9-h4f385c5_3.conda contains the following package constraints:

The following configurations outline the default system requirements for different operating systems:

Windows currently has no minimal system requirements defined. If your workspace requires specific Windows configurations, you should define them accordingly.

You only need to define system requirements if your workspace necessitates a different set from the defaults. This is common when installing environments on older or newer versions of operating systems.

If you're encountering an error like:

This indicates that the workspace's system requirements are higher than your current system's specifications. To resolve this, you can lower the system requirements in your workspace's configuration:

This adjustment informs the dependency resolver to accommodate the older system version.

To utilize CUDA in your workspace, you must specify the desired CUDA version in the system-requirements table. This ensures that CUDA is recognized and appropriately locked into the lock file if necessary.

Example Configuration

This can be set per feature in the the manifest file.

In certain scenarios, you might need to override the system requirements detected on your machine. This can be particularly useful when working on systems that do not meet the workspace's default requirements.

You can override virtual packages by setting the following environment variables:

For more detailed information on managing virtual packages and overriding system requirements, refer to the Conda Documentation.

**Examples:**

Example 1 (unknown):
```unknown
[system-requirements]
linux  = "4.18"
libc   = { family = "glibc", version = "2.28" }
cuda   = "12"
macos  = "13.0"
```

Example 2 (unknown):
```unknown
cudatoolkit 12.9|12.9.*
__cuda >=12
```

Example 3 (unknown):
```unknown
# Default system requirements for Linux
[system-requirements]
linux = "4.18"
libc = { family = "glibc", version = "2.28" }
```

Example 4 (unknown):
```unknown
# Default system requirements for macOS
[system-requirements]
macos = "13.0"
```

---

## Pixi Inject

**URL:** https://pixi.sh/latest/integration/extensions/pixi_inject/

**Contents:**
- Pixi Inject

pixi-inject is a simple executable that injects a conda package into an existing pixi environment.

You can also specify a custom conda prefix to inject the package into.

**Examples:**

Example 1 (unknown):
```unknown
pixi inject --environment default --package my-package-0.1.0-py313h8aa417a_0.conda
```

Example 2 (unknown):
```unknown
pixi inject --prefix /path/to/conda/env --package my-package-0.1.0-py313h8aa417a_0.conda
```

---
