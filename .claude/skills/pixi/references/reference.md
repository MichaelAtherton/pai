# Pixi - Reference

**Pages:** 60

---

## pixi shell#

**URL:** https://pixi.sh/latest/reference/cli/pixi/shell/

**Contents:**
- pixi shell#
- About#
- Usage#
- Options#
- Config Options#
- Update Options#
- Global Options#
- Examples#

Start a shell in a pixi environment, run exit to leave the shell

**Examples:**

Example 1 (unknown):
```unknown
pixi shell [OPTIONS]
```

Example 2 (unknown):
```unknown
pixi shell
pixi shell --manifest-path ~/myworkspace/pixi.toml
pixi shell --frozen
pixi shell --locked
pixi shell --environment cuda
exit
```

---

## pixi clean cache#

**URL:** https://pixi.sh/latest/reference/cli/pixi/clean/cache/

**Contents:**
- pixi clean cache#
- About#
- Usage#
- Options#
- Description#
- Examples#

Clean the cache of your system which are touched by pixi

Clean the cache of your system which are touched by pixi.

Specify the cache type to clean with the flags.

**Examples:**

Example 1 (unknown):
```unknown
pixi clean cache [OPTIONS]
```

Example 2 (unknown):
```unknown
pixi clean cache # clean all pixi caches
pixi clean cache --pypi # clean only the pypi cache
pixi clean cache --conda # clean only the conda cache
pixi clean cache --mapping # clean only the mapping cache
pixi clean cache --exec # clean only the `exec` cache
pixi clean cache --repodata # clean only the `repodata` cache
pixi clean cache --yes # skip the confirmation prompt
```

---

## pixi list#

**URL:** https://pixi.sh/latest/reference/cli/pixi/list/

**Contents:**
- pixi list#
- About#
- Usage#
- Arguments#
- Options#
- Update Options#
- Global Options#
- Description#
- Examples#

List workspace's packages

List workspace's packages.

Highlighted packages are explicit dependencies.

Output will look like this, where python will be green as it is the package that was explicitly added to the manifest file:

**Examples:**

Example 1 (unknown):
```unknown
pixi list [OPTIONS] [REGEX]
```

Example 2 (unknown):
```unknown
pixi list
pixi list py
pixi list --json-pretty
pixi list --explicit
pixi list --sort-by size
pixi list --platform win-64
pixi list --environment cuda
pixi list --frozen
pixi list --locked
pixi list --no-install
```

Example 3 (unknown):
```unknown
➜ pixi list
 Package           Version     Build               Size       Kind   Source
 _libgcc_mutex     0.1         conda_forge         2.5 KiB    conda  _libgcc_mutex-0.1-conda_forge.tar.bz2
 _openmp_mutex     4.5         2_gnu               23.1 KiB   conda  _openmp_mutex-4.5-2_gnu.tar.bz2
 bzip2             1.0.8       hd590300_5          248.3 KiB  conda  bzip2-1.0.8-hd590300_5.conda
 ca-certificates   2023.11.17  hbcca054_0          150.5 KiB  conda  ca-certificates-2023.11.17-hbcca054_0.conda
 ld_impl_linux-64  2.40        h41732ed_0          688.2 KiB  conda  ld_impl_linux-64-2.40-h41732ed_0.conda
 libexpat          2.5.0       hcb278e6_1          76.2 KiB   conda  libexpat-2.5.0-hcb278e6_1.conda
 libffi            3.4.2       h7f98852_5          56.9 KiB   conda  libffi-3.4.2-h7f98852_5.tar.bz2
 libgcc-ng         13.2.0      h807b86a_4          755.7 KiB  conda  libgcc-ng-13.2.0-h807b86a_4.conda
 libgomp           13.2.0      h807b86a_4          412.2 KiB  conda  libgomp-13.2.0-h807b86a_4.conda
 libnsl            2.0.1       hd590300_0          32.6 KiB   conda  libnsl-2.0.1-hd590300_0.conda
 libsqlite         3.44.2      h2797004_0          826 KiB    conda  libsqlite-3.44.2-h2797004_0.conda
 libuuid           2.38.1      h0b41bf4_0          32.8 KiB   conda  libuuid-2.38.1-h0b41bf4_0.conda
 libxcrypt         4.4.36      hd590300_1          98 KiB     conda  libxcrypt-4.4.36-hd590300_1.conda
 libzlib           1.2.13      hd590300_5          60.1 KiB   conda  libzlib-1.2.13-hd590300_5.conda
 ncurses           6.4         h59595ed_2          863.7 KiB  conda  ncurses-6.4-h59595ed_2.conda
 openssl           3.2.0       hd590300_1          2.7 MiB    conda  openssl-3.2.0-hd590300_1.conda
 python            3.12.1      hab00c5b_1_cpython  30.8 MiB   conda  python-3.12.1-hab00c5b_1_cpython.conda
 readline          8.2         h8228510_1          274.9 KiB  conda  readline-8.2-h8228510_1.conda
 tk                8.6.13      noxft_h4845f30_101  3.2 MiB    conda  tk-8.6.13-noxft_h4845f30_101.conda
 tzdata            2023d       h0c530f3_0          116.8 KiB  conda  tzdata-2023d-h0c530f3_0.conda
 xz                5.2.6       h166bdaf_0          408.6 KiB  conda  xz-5.2.6-h166bdaf_0.tar.bz2
```

---

## Multi Platform

**URL:** https://pixi.sh/latest/workspace/multi_platform_configuration/

**Contents:**
- Multi Platform
- Platform definition#
- Target specifier#
  - Dependencies#
  - Activation#

Pixi's vision includes being supported on all major platforms. Sometimes that needs some extra configuration to work well. On this page, you will learn what you can configure to align better with the platform you are making your application for.

Here is an example manifest file that highlights some of the features:

The workspace.platforms defines which platforms your workspace supports. When multiple platforms are defined, Pixi determines which dependencies to install for each platform individually. All of this is stored in a lock file.

Running pixi install on a platform that is not configured will warn the user that it is not setup for that platform:

With the target specifier, you can overwrite the original configuration specifically for a single platform. If you are targeting a specific platform in your target specifier that was not specified in your workspace.platforms then Pixi will throw an error.

It might happen that you want to install a certain dependency only on a specific platform, or you might want to use a different version on different platforms.

In the above example, we specify that we depend on msmpi only on Windows. We also specifically want python on 3.8 when installing on Windows. This will overwrite the dependencies from the generic set of dependencies. This will not touch any of the other platforms.

You can use pixi's cli to add these dependencies to the manifest file.

This also works for the host and build dependencies.

Which results in this.

Pixi's vision is to enable completely cross-platform workspaces, but you often need to run tools that are not built by your projects. Generated activation scripts are often in this category, default scripts in unix are bash and for windows they are bat

To deal with this, you can define your activation scripts using the target definition.

pixi.toml[activation] scripts = ["setup.sh", "local_setup.bash"] [target.win-64.activation] scripts = ["setup.bat", "local_setup.bat"] When this workspace is used on win-64 it will only execute the target scripts not the scripts specified in the default activation.scripts

**Examples:**

Example 1 (unknown):
```unknown
[workspace]
# Default workspace info....
# A list of platforms you are supporting with your package.
platforms = ["win-64", "linux-64", "osx-64", "osx-arm64"]

[dependencies]
python = ">=3.8"

[target.win-64.dependencies]
# Overwrite the needed python version only on win-64
python = "3.7"


[activation]
scripts = ["setup.sh"]

[target.win-64.activation]
# Overwrite activation scripts only for windows
scripts = ["setup.bat"]
```

Example 2 (unknown):
```unknown
[tool.pixi.workspace]
# Default workspace info....
# A list of platforms you are supporting with your package.
platforms = ["win-64", "linux-64", "osx-64", "osx-arm64"]

[tool.pixi.dependencies]
python = ">=3.8"

[tool.pixi.target.win-64.dependencies]
# Overwrite the needed python version only on win-64
python = "~=3.7.0"


[tool.pixi.activation]
scripts = ["setup.sh"]

[tool.pixi.target.win-64.activation]
# Overwrite activation scripts only for windows
scripts = ["setup.bat"]
```

Example 3 (unknown):
```unknown
❯ pixi install
 WARN Not installing dependency for (default) on current platform: (osx-arm64) as it is not part of this project's supported platforms.
```

Example 4 (unknown):
```unknown
[dependencies]
python = ">=3.8"

[target.win-64.dependencies]
msmpi = "*"
python = "3.8"
```

---

## pixi lock#

**URL:** https://pixi.sh/latest/reference/cli/pixi/lock/

**Contents:**
- pixi lock#
- About#
- Usage#
- Options#
- Update Options#
- Global Options#
- Examples#

Solve environment and update the lock file without installing the environments

**Examples:**

Example 1 (unknown):
```unknown
pixi lock [OPTIONS]
```

Example 2 (unknown):
```unknown
pixi lock
pixi lock --manifest-path ~/myworkspace/pixi.toml
pixi lock --json
pixi lock --check
```

---

## pixi upgrade#

**URL:** https://pixi.sh/latest/reference/cli/pixi/upgrade/

**Contents:**
- pixi upgrade#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Update Options#
- Global Options#
- Description#
- Examples#

Checks if there are newer versions of the dependencies and upgrades them in the lockfile and manifest file

The pixi upgrade command will update only versions, except when you specify the exact package name (pixi upgrade numpy).

Then it will remove all fields, apart from:

In v0.55.0 and earlier releases, by default only the default feature was upgraded. Pass --feature=default if you want to emulate this behaviour on newer releases.

Checks if there are newer versions of the dependencies and upgrades them in the lockfile and manifest file.

pixi upgrade loosens the requirements for the given packages, updates the lock file and the adapts the manifest accordingly. By default, all features are upgraded.

**Examples:**

Example 1 (unknown):
```unknown
pixi upgrade [OPTIONS] [PACKAGES]...
```

Example 2 (unknown):
```unknown
pixi upgrade # (1)!
pixi upgrade numpy # (2)!
pixi upgrade numpy pandas # (3)!
pixi upgrade --manifest-path ~/myworkspace/pixi.toml numpy # (4)!
pixi upgrade --feature lint python # (5)!
pixi upgrade --json # (6)!
pixi upgrade --dry-run # (7)!
```

---

## pixi exec#

**URL:** https://pixi.sh/latest/reference/cli/pixi/exec/

**Contents:**
- pixi exec#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Description#
- Examples#

Run a command and install it in a temporary environment

Run a command and install it in a temporary environment.

Remove the temporary environments with pixi clean cache --exec.

**Examples:**

Example 1 (unknown):
```unknown
pixi exec [OPTIONS] [COMMAND]...
```

Example 2 (unknown):
```unknown
pixi exec python

# Run ipython and include the py-rattler and numpy packages in the environment
pixi exec --with py-rattler --with numpy ipython

# Specify the specs of the environment
pixi exec --spec python=3.9 --spec numpy python

# Force reinstall to recreate the environment and get the latest package versions
pixi exec --force-reinstall --with py-rattler ipython
```

---

## pixi global remove#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/remove/

**Contents:**
- pixi global remove#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Description#
- Examples#

Removes dependencies from an environment

Removes dependencies from an environment

Use pixi global uninstall to remove the whole environment

Example: pixi global remove --environment python numpy

**Examples:**

Example 1 (unknown):
```unknown
pixi global remove [OPTIONS] <PACKAGE>...
```

Example 2 (unknown):
```unknown
pixi global remove -e my-env package1 package2
```

---

## pixi global list#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/list/

**Contents:**
- pixi global list#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Description#
- Examples#

Lists global environments with their dependencies and exposed commands. Can also display all packages within a specific global environment when using the --environment flag.

Lists global environments with their dependencies and exposed commands. Can also display all packages within a specific global environment when using the --environment flag.

We'll only show the dependencies and exposed binaries of the environment if they differ from the environment name. Here is an example of a few installed packages:

pixi global list Results in: Global environments at /home/user/.pixi: ├── gh: 2.57.0 ├── pixi-pack: 0.1.8 ├── python: 3.11.0 │ └─ exposes: 2to3, 2to3-3.11, idle3, idle3.11, pydoc, pydoc3, pydoc3.11, python, python3, python3-config, python3.1, python3.11, python3.11-config ├── rattler-build: 0.22.0 ├── ripgrep: 14.1.0 │ └─ exposes: rg ├── vim: 9.1.0611 │ └─ exposes: ex, rview, rvim, view, vim, vimdiff, vimtutor, xxd └── zoxide: 0.9.6

Here is an example of list of a single environment: pixi g list -e pixi-pack Results in: The 'pixi-pack' environment has 8 packages: Package Version Build Size _libgcc_mutex 0.1 conda_forge 2.5 KiB _openmp_mutex 4.5 2_gnu 23.1 KiB ca-certificates 2024.8.30 hbcca054_0 155.3 KiB libgcc 14.1.0 h77fa898_1 826.5 KiB libgcc-ng 14.1.0 h69a702a_1 50.9 KiB libgomp 14.1.0 h77fa898_1 449.4 KiB openssl 3.3.2 hb9d3cd8_0 2.8 MiB pixi-pack 0.1.8 hc762bcd_0 4.3 MiB Package Version Build Size Exposes: pixi-pack Channels: conda-forge Platform: linux-64

**Examples:**

Example 1 (unknown):
```unknown
pixi global list [OPTIONS] [REGEX]
```

Example 2 (unknown):
```unknown
pixi global list
```

Example 3 (unknown):
```unknown
Global environments at /home/user/.pixi:
├── gh: 2.57.0
├── pixi-pack: 0.1.8
├── python: 3.11.0
│   └─ exposes: 2to3, 2to3-3.11, idle3, idle3.11, pydoc, pydoc3, pydoc3.11, python, python3, python3-config, python3.1, python3.11, python3.11-config
├── rattler-build: 0.22.0
├── ripgrep: 14.1.0
│   └─ exposes: rg
├── vim: 9.1.0611
│   └─ exposes: ex, rview, rvim, view, vim, vimdiff, vimtutor, xxd
└── zoxide: 0.9.6
```

Example 4 (unknown):
```unknown
pixi g list -e pixi-pack
```

---

## pixi config set#

**URL:** https://pixi.sh/latest/reference/cli/pixi/config/set/

**Contents:**
- pixi config set#
- About#
- Usage#
- Arguments#
- Config Options#
- Global Options#
- Description#
- Examples#

Set a configuration value

Set a configuration value

Example: pixi config set default-channels '["conda-forge", "bioconda"]'

**Examples:**

Example 1 (unknown):
```unknown
pixi config set [OPTIONS] <KEY> [VALUE]
```

Example 2 (unknown):
```unknown
pixi config set default-channels '["conda-forge", "bioconda"]'
pixi config set --global mirrors '{"https://conda.anaconda.org/conda-forge": ["https://prefix.dev/conda-forge"]}'
pixi config set repodata-config.disable-zstd true --system
pixi config set --global detached-environments "/opt/pixi/envs"
pixi config set detached-environments false
pixi config set s3-options.my-bucket '{"endpoint-url": "http://localhost:9000", "force-path-style": true, "region": "auto"}'
```

---

## pixi info#

**URL:** https://pixi.sh/latest/reference/cli/pixi/info/

**Contents:**
- pixi info#
- About#
- Usage#
- Options#
- Global Options#
- Examples#

Information about the system, workspace and environments for the current machine

More information here.

**Examples:**

Example 1 (unknown):
```unknown
pixi info [OPTIONS]
```

Example 2 (unknown):
```unknown
pixi info
pixi info --json
pixi info --extended
```

---

## pixi auth#

**URL:** https://pixi.sh/latest/reference/cli/pixi/auth/

**Contents:**
- pixi auth#
- About#
- Usage#
- Subcommands#

Login to prefix.dev or anaconda.org servers to access private channels

**Examples:**

Example 1 (unknown):
```unknown
pixi auth <COMMAND>
```

---

## pixi workspace#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/

**Contents:**
- pixi workspace#
- About#
- Usage#
- Subcommands#
- Global Options#

Modify the workspace configuration file through the command line

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace [OPTIONS] <COMMAND>
```

---

## pixi remove#

**URL:** https://pixi.sh/latest/reference/cli/pixi/remove/

**Contents:**
- pixi remove#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Git Options#
- Update Options#
- Global Options#
- Description#

Removes dependencies from the workspace

If the project manifest is a pyproject.toml, removing a pypi dependency with the --pypi flag will remove it from either

Removes dependencies from the workspace.

If the workspace manifest is a pyproject.toml, removing a pypi dependency with the --pypi flag will remove it from either

**Examples:**

Example 1 (unknown):
```unknown
pixi remove [OPTIONS] <SPEC>...
```

Example 2 (unknown):
```unknown
pixi remove numpy
pixi remove numpy pandas pytorch
pixi remove --manifest-path ~/myworkspace/pixi.toml numpy
pixi remove --host python
pixi remove --build cmake
pixi remove --pypi requests
pixi remove --platform osx-64 --build clang
pixi remove --feature featurex clang
pixi remove --feature featurex --platform osx-64 clang
pixi remove --feature featurex --platform osx-64 --build clang
pixi remove --no-install numpy
```

---

## pixi init#

**URL:** https://pixi.sh/latest/reference/cli/pixi/init/

**Contents:**
- pixi init#
- About#
- Usage#
- Arguments#
- Options#
- Description#
- Examples#

Creates a new workspace

Importing an environment.yml

When importing an environment, the pixi.toml will be created with the dependencies from the environment file. The pixi.lock will be created when you install the environment. We don't support git+ urls as dependencies for pip packages and for the defaults channel we use main, r and msys2 as the default channels.

Creates a new workspace

This command is used to create a new workspace. It prepares a manifest and some helpers for the user to start working.

As pixi can both work with pixi.toml and pyproject.toml files, the user can choose which one to use with --format.

You can import an existing conda environment file with the --import flag.

**Examples:**

Example 1 (unknown):
```unknown
pixi init [OPTIONS] [PATH]
```

Example 2 (unknown):
```unknown
pixi init myproject  # (1)!
pixi init ~/myproject  # (2)!
pixi init  # (3)!
pixi init --channel conda-forge --channel bioconda myproject  # (4)!
pixi init --platform osx-64 --platform linux-64 myproject  # (5)!
pixi init --import environment.yml  # (6)!
pixi init --format pyproject  # (7)!
pixi init --format pixi --scm gitlab  # (8)!
```

---

## pixi workspace description#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/description/

**Contents:**
- pixi workspace description#
- About#
- Usage#
- Subcommands#
- Global Options#

Commands to manage workspace description

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace description [OPTIONS] <COMMAND>
```

---

## pixi global expose add#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/expose/add/

**Contents:**
- pixi global expose add#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Description#
- Examples#

Add exposed binaries from an environment to your global environment

Add exposed binaries from an environment to your global environment

**Examples:**

Example 1 (unknown):
```unknown
pixi global expose add [OPTIONS] --environment <ENVIRONMENT> [MAPPING]...
```

Example 2 (unknown):
```unknown
pixi global expose add python --environment my-env
pixi global expose add py310=python3.10 --environment python
```

---

## pixi global edit#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/edit/

**Contents:**
- pixi global edit#
- About#
- Usage#
- Arguments#
- Description#
- Examples#

Edit the global manifest file

Edit the global manifest file

Opens your editor to edit the global manifest file.

**Examples:**

Example 1 (unknown):
```unknown
pixi global edit [EDITOR]
```

Example 2 (unknown):
```unknown
pixi global edit
pixi global edit code
pixi global edit vim
```

---

## pixi global#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/

**Contents:**
- pixi global#
- About#
- Usage#
- Subcommands#
- Description#

Subcommand for global package management actions

All commands in this section are used to manage global installations of packages and environments through the global manifest. More info on the global manifest can be found here.

Binaries and environments installed globally are stored in ~/.pixi by default, this can be changed by setting the PIXI_HOME environment variable.

Subcommand for global package management actions.

Install packages on the user level. Into to the [$PIXI_HOME] directory, which defaults to ~/.pixi.

**Examples:**

Example 1 (unknown):
```unknown
pixi global <COMMAND>
```

---

## pixi workspace platform remove#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/platform/remove/

**Contents:**
- pixi workspace platform remove#
- About#
- Usage#
- Arguments#
- Options#

Remove platform(s) from the workspace file and updates the lockfile

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace platform remove [OPTIONS] <PLATFORM>...
```

---

## pixi global add#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/add/

**Contents:**
- pixi global add#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Git Options#
- Description#
- Examples#

Adds dependencies to an environment

Adds dependencies to an environment

**Examples:**

Example 1 (unknown):
```unknown
pixi global add [OPTIONS] --environment <ENVIRONMENT> [PACKAGE]...
```

Example 2 (unknown):
```unknown
pixi global add python=3.9.* --environment my-env
pixi global add python=3.9.* --expose py39=python3.9 --environment my-env
pixi global add numpy matplotlib --environment my-env
pixi global add numpy matplotlib --expose np=python3.9 --environment my-env
```

---

## pixi import#

**URL:** https://pixi.sh/latest/reference/cli/pixi/import/

**Contents:**
- pixi import#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Global Options#
- Description#

Imports a file into an environment in an existing workspace.

Imports a file into an environment in an existing workspace.

If --format isn't provided, import will try each format in turn

**Examples:**

Example 1 (unknown):
```unknown
pixi import [OPTIONS] <FILE>
```

---

## pixi auth login#

**URL:** https://pixi.sh/latest/reference/cli/pixi/auth/login/

**Contents:**
- pixi auth login#
- About#
- Usage#
- Arguments#
- Options#
- Examples#

Store authentication information for a given host

**Examples:**

Example 1 (unknown):
```unknown
pixi auth login [OPTIONS] <HOST>
```

Example 2 (unknown):
```unknown
pixi auth login repo.prefix.dev --token pfx_JQEV-m_2bdz-D8NSyRSaAndHANx0qHjq7f2iD
pixi auth login anaconda.org --conda-token ABCDEFGHIJKLMNOP
pixi auth login https://myquetz.server --username john --password xxxxxx
pixi auth login s3://my-bucket --s3-access-key-id $AWS_ACCESS_KEY_ID --s3-access-key-id $AWS_SECRET_KEY_ID
```

---

## pixi upload#

**URL:** https://pixi.sh/latest/reference/cli/pixi/upload/

**Contents:**
- pixi upload#
- About#
- Usage#
- Arguments#
- Description#

Upload a conda package

Upload a conda package

With this command, you can upload a conda package to a channel. Example: pixi upload https://prefix.dev/api/v1/upload/my_channel my_package.conda

Use pixi auth login to authenticate with the server.

**Examples:**

Example 1 (unknown):
```unknown
pixi upload <HOST> <PACKAGE_FILE>
```

---

## pixi shell#

**URL:** https://pixi.sh/latest/reference/cli/pixi/shell

**Contents:**
- pixi shell#
- About#
- Usage#
- Options#
- Config Options#
- Update Options#
- Global Options#
- Examples#

Start a shell in a pixi environment, run exit to leave the shell

**Examples:**

Example 1 (unknown):
```unknown
pixi shell [OPTIONS]
```

Example 2 (unknown):
```unknown
pixi shell
pixi shell --manifest-path ~/myworkspace/pixi.toml
pixi shell --frozen
pixi shell --locked
pixi shell --environment cuda
exit
```

---

## pixi workspace channel#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/channel/

**Contents:**
- pixi workspace channel#
- About#
- Usage#
- Subcommands#

Commands to manage workspace channels

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace channel <COMMAND>
```

---

## pixi#

**URL:** https://pixi.sh/latest/reference/cli/pixi/

**Contents:**
- pixi#
- Description#
- Usage#
- Subcommands#
- Global Options#

The pixi command is the main entry point for the Pixi CLI.

**Examples:**

Example 1 (unknown):
```unknown
pixi [OPTIONS] [COMMAND]
```

---

## pixi workspace export#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/export/

**Contents:**
- pixi workspace export#
- About#
- Usage#
- Subcommands#

Commands to export workspaces to other formats

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace export <COMMAND>
```

---

## pixi self-update#

**URL:** https://pixi.sh/latest/reference/cli/pixi/self-update/

**Contents:**
- pixi self-update#
- About#
- Usage#
- Options#
- Examples#

Update pixi to the latest version or a specific version

**Examples:**

Example 1 (unknown):
```unknown
pixi self-update [OPTIONS]
```

Example 2 (unknown):
```unknown
pixi self-update
pixi self-update --version 0.46.0
```

---

## The Configuration of Pixi Itself#

**URL:** https://pixi.sh/latest/reference/pixi_configuration/

**Contents:**
- The Configuration of Pixi Itself#
- Configuration options#
  - default-channels#
  - shell#
  - tls-no-verify#
  - authentication-override-file#
  - detached-environments#
  - pinning-strategy#
  - mirrors#
  - proxy-config#

Apart from the workspace specific configuration Pixi supports configuration options which are not required for the workspace to work but are local to the machine. The configuration is loaded in the following order:

The highest priority wins. If a configuration file is found in a higher priority location, the values from the configuration read from lower priority locations are overwritten.

To find the locations where pixi looks for configuration files, run pixi info -vvv.

In Pixi 0.20.1 and older the global configuration options used snake_case which we've changed to kebab-case for consistency with the rest of the configuration. For backwards compatibility, the following configuration options can still be written in snake_case:

The following reference describes all available configuration options.

The default channels to select when running pixi init or pixi global install. This defaults to only conda-forge.

The default-channels are only used when initializing a new workspace. Once initialized the channels are used from the workspace manifest.

When set to true, the TLS certificates are not verified.

This is a security risk and should only be used for testing purposes or internal networks.

You can override this from the CLI with --tls-no-verify.

Override from where the authentication information is loaded. Usually, we try to use the keyring to load authentication data from, and only use a JSON file as a fallback. This option allows you to force the use of a JSON file. Read more in the authentication section.

The directory where Pixi stores the workspace environments, what would normally be placed in the .pixi/envs folder in a workspace's root. It doesn't affect the environments built for pixi global. The location of environments created for a pixi global installation can be controlled using the PIXI_HOME environment variable.

We recommend against using this because any environment created for a workspace is no longer placed in the same folder as the workspace. This creates a disconnect between the workspace and its environments and manual cleanup of the environments is required when deleting the workspace.

However, in some cases, this option can still be very useful, for instance to:

This field can consist of two types of input.

The environments will be stored in the cache directory when this option is true. When you specify a custom path the environments will be stored in that directory.

The resulting directory structure will look like this:

The strategy to use for pinning dependencies when running pixi add. The default is semver but you can set the following:

Configuration for conda channel-mirrors, more info below.

pixi respects the proxy environments such as https_proxy with the highest priority. Also we can set the proxies in proxy-config table of the pixi config, which affect all the pixi network actions, such as resolve, self-update, download, etc. Now proxy-config table supports the following options:

Configuration for repodata fetching.

The above settings can be overridden on a per-channel basis by specifying a channel prefix in the configuration.

To setup a certain number of defaults for the usage of PyPI registries. You can use the following configuration options:

index-url and extra-index-urls are not globals

Unlike pip, these settings, with the exception of keyring-provider will only modify the pixi.toml/pyproject.toml file and are not globally interpreted when not present in the manifest. This is because we want to keep the manifest file as complete and reproducible as possible.

Configuration for S3 authentication. This will lead to Pixi not using AWS's default credentials but instead use the credentials from the Pixi authentication storage, see the S3 section for more information.

Configure multiple settings to limit or extend the concurrency of pixi.

Set them through the CLI with:

Configure whether pixi should execute post-link and pre-unlink scripts or not.

Some packages contain post-link scripts (bat or sh files) that are executed after a package is installed. We deem these scripts as insecure because they can contain arbitrary code that is executed on the user's machine without the user's consent. By default, the value of run-post-link-scripts is set to false which prevents the execution of these scripts.

However, you can opt-in on a global (or workspace) basis by setting the value to insecure (e.g. by running pixi config set --local run-post-link-scripts insecure).

In the future we are planning to add a sandbox mode to execute these scripts in a controlled environment.

Defines the platform used when installing "tools" like build backends. By default pixi uses the platform of the current system, but you can override it to use a different platform. This can be useful if you are running pixi on an architecture for which there is fewer support for certain build backends.

The virtual packages for the tool platform are detected from the current system. If the tool platform is for a different operating system than the current system, no virtual packages will be used.

This allows the user to set specific experimental features that are not yet stable.

Please write a GitHub issue and add the flag experimental to the issue if you find issues with the feature you activated.

Turn this feature on from configuration with the following command:

This will cache the environment activation in the .pixi/activation-env-v0 folder in the workspace root. It will create a json file for each environment that is activated, and it will be used to activate the environment in the future.

You can ignore the cache by running:

Set the configuration with:

Why is this experimental?

This feature is experimental because the cache invalidation is very tricky, and we don't want to disturb users that are not affected by activation times.

You can configure mirrors for conda channels. We expect that mirrors are exact copies of the original channel. The implementation will look for the mirror key (a URL) in the mirrors section of the configuration file and replace the original URL with the mirror URL.

To also include the original URL, you have to repeat it in the list of mirrors.

The mirrors are prioritized based on the order of the list. We attempt to fetch the repodata (the most important file) from the first mirror in the list. The repodata contains all the SHA256 hashes of the individual packages, so it is important to get this file from a trusted source.

You can also specify mirrors for an entire "host", e.g.

This will forward all request to channels on anaconda.org to prefix.dev. Channels that are not currently mirrored on prefix.dev will fail in the above example. You can override the behavior for specific channels (like conda-forge's label channels) by providing a longer prefix that points to itself.

You can also specify mirrors on the OCI registry. There is a public mirror on the Github container registry (ghcr.io) that is maintained by the conda-forge team. You can use it like this:

The GHCR mirror also contains bioconda packages. You can search the available packages on Github.

The mirrors also affect the PyPi resolving and downloading steps of uv. You can set mirrors for the main pypi index and extra indices. But the base part of downloading urls may vary from their index urls. For example, the default pypi index is https://pypi.org/simple, and the package downloading urls are in the form of https://files.pythonhosted.org/packages/<h1>/<h2>/<hash>/<package>.whl. You need two mirror config entries for https://pypi.org/simple and https://files.pythonhosted.org/packages.

**Examples:**

Example 1 (unknown):
```unknown
- `default_channels`
- `change_ps1`
- `tls_no_verify`
- `authentication_override_file`
- `mirrors` and its sub-options
- `repodata_config` and its sub-options
```

Example 2 (unknown):
```unknown
default-channels = ["conda-forge"]
```

Example 3 (unknown):
```unknown
[shell]
change-ps1 = false
force-activate = true
source-completion-scripts = false
```

Example 4 (unknown):
```unknown
tls-no-verify = false
```

---

## pixi workspace name#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/name/

**Contents:**
- pixi workspace name#
- About#
- Usage#
- Subcommands#
- Global Options#

Commands to manage workspace name

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace name [OPTIONS] <COMMAND>
```

---

## pixi tree#

**URL:** https://pixi.sh/latest/reference/cli/pixi/tree/

**Contents:**
- pixi tree#
- About#
- Usage#
- Arguments#
- Options#
- Update Options#
- Global Options#
- Description#
- Examples#

Show a tree of workspace dependencies

Show a tree of workspace dependencies

Dependency names highlighted in green are directly specified in the manifest. Yellow version numbers are conda packages, PyPI version numbers are blue.

Output will look like this, where direct packages in the manifest file will be green. Once a package has been displayed once, the tree won't continue to recurse through its dependencies (compare the first time python appears, vs the rest), and it will instead be marked with a star (*).

Version numbers are colored by the package type, yellow for Conda packages and blue for PyPI.

A regex pattern can be specified to filter the tree to just those that show a specific direct, or transitive dependency:

Additionally, the tree can be inverted, and it can show which packages depend on a regex pattern. The packages specified in the manifest will also be highlighted (in this case cffconvert and pre-commit would be).

Use -v to show which pypi packages are not yet parsed correctly. The extras and markers parsing is still under development.

**Examples:**

Example 1 (unknown):
```unknown
pixi tree [OPTIONS] [REGEX]
```

Example 2 (unknown):
```unknown
pixi tree
pixi tree pre-commit
pixi tree -i yaml
pixi tree --environment docs
pixi tree --platform win-64
```

Example 3 (unknown):
```unknown
➜ pixi tree
├── pre-commit v3.3.3
│   ├── cfgv v3.3.1
│   │   └── python v3.12.2
│   │       ├── bzip2 v1.0.8
│   │       ├── libexpat v2.6.2
│   │       ├── libffi v3.4.2
│   │       ├── libsqlite v3.45.2
│   │       │   └── libzlib v1.2.13
│   │       ├── libzlib v1.2.13 (*)
│   │       ├── ncurses v6.4.20240210
│   │       ├── openssl v3.2.1
│   │       ├── readline v8.2
│   │       │   └── ncurses v6.4.20240210 (*)
│   │       ├── tk v8.6.13
│   │       │   └── libzlib v1.2.13 (*)
│   │       └── xz v5.2.6
│   ├── identify v2.5.35
│   │   └── python v3.12.2 (*)
...
└── tbump v6.9.0
...
    └── tomlkit v0.12.4
        └── python v3.12.2 (*)
```

Example 4 (unknown):
```unknown
➜ pixi tree pre-commit
└── pre-commit v3.3.3
    ├── virtualenv v20.25.1
    │   ├── filelock v3.13.1
    │   │   └── python v3.12.2
    │   │       ├── libexpat v2.6.2
    │   │       ├── readline v8.2
    │   │       │   └── ncurses v6.4.20240210
    │   │       ├── libsqlite v3.45.2
    │   │       │   └── libzlib v1.2.13
    │   │       ├── bzip2 v1.0.8
    │   │       ├── libzlib v1.2.13 (*)
    │   │       ├── libffi v3.4.2
    │   │       ├── tk v8.6.13
    │   │       │   └── libzlib v1.2.13 (*)
    │   │       ├── xz v5.2.6
    │   │       ├── ncurses v6.4.20240210 (*)
    │   │       └── openssl v3.2.1
    │   ├── platformdirs v4.2.0
    │   │   └── python v3.12.2 (*)
    │   ├── distlib v0.3.8
    │   │   └── python v3.12.2 (*)
    │   └── python v3.12.2 (*)
    ├── pyyaml v6.0.1
...
```

---

## pixi install#

**URL:** https://pixi.sh/latest/reference/cli/pixi/install/

**Contents:**
- pixi install#
- About#
- Usage#
- Options#
- Config Options#
- Update Options#
- Global Options#
- Description#
- Examples#

Install an environment, both updating the lockfile and installing the environment

Install an environment, both updating the lockfile and installing the environment.

This command installs an environment, if the lockfile is not up-to-date it will be updated.

pixi install only installs one environment at a time, if you have multiple environments you can select the right one with the --environment flag. If you don't provide an environment, the default environment will be installed.

If you want to install all environments, you can use the --all flag.

Running pixi install is not required before running other commands like pixi run or pixi shell. These commands will automatically install the environment if it is not already installed.

You can use pixi reinstall to reinstall all environments, one environment or just some packages of an environment.

**Examples:**

Example 1 (unknown):
```unknown
pixi install [OPTIONS]
```

Example 2 (unknown):
```unknown
pixi install  # (1)!
pixi install --manifest-path ~/myworkspace/pixi.toml # (2)!
pixi install --frozen # (3)!
pixi install --locked # (4)!
pixi install --environment lint # (5)!
pixi install -e lint # (5)!
```

---

## pixi global install#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/install/

**Contents:**
- pixi global install#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Git Options#
- Description#
- Examples#

Installs the defined packages in a globally accessible location and exposes their command line applications.

Running osx-64 on Apple Silicon will install the Intel binary but run it using Rosetta pixi global install --platform osx-64 ruff

When you pass --path with a local .conda archive, Pixi copies the file into PIXI_HOME/conda-files and installs from that managed copy. Supplying any other kind of path keeps the original location unchanged.

After using global install, you can use the package you installed anywhere on your system.

Installs the defined packages in a globally accessible location and exposes their command line applications.

**Examples:**

Example 1 (unknown):
```unknown
pixi global install --platform osx-64 ruff
```

Example 2 (unknown):
```unknown
pixi global install [OPTIONS] [PACKAGE]...
```

Example 3 (unknown):
```unknown
pixi global install ruff
# Multiple packages can be installed at once
pixi global install starship rattler-build
# Specify the channel(s)
pixi global install --channel conda-forge --channel bioconda trackplot
# Or in a more concise form
pixi global install -c conda-forge -c bioconda trackplot

# Support full conda matchspec
pixi global install python=3.9.*
pixi global install "python [version='3.11.0', build_number=1]"
pixi global install "python [version='3.11.0', build=he550d4f_1_cpython]"
pixi global install python=3.11.0=h10a6764_1_cpython

# Install for a specific platform, only useful on osx-arm64
pixi global install --platform osx-64 ruff

# Install a package with all its executables exposed, together with additional packages that don't expose anything
pixi global install ipython --with numpy --with scipy

# Install into a specific environment name and expose all executables
pixi global install --environment data-science ipython jupyterlab numpy matplotlib

# Expose the binary under a different name
pixi global install --expose "py39=python3.9" "python=3.9.*"
```

---

## pixi workspace platform add#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/platform/add/

**Contents:**
- pixi workspace platform add#
- About#
- Usage#
- Arguments#
- Options#

Adds a platform(s) to the workspace file and updates the lockfile

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace platform add [OPTIONS] <PLATFORM>...
```

---

## pixi config#

**URL:** https://pixi.sh/latest/reference/cli/pixi/config/

**Contents:**
- pixi config#
- About#
- Usage#
- Subcommands#

Configuration management

**Examples:**

Example 1 (unknown):
```unknown
pixi config <COMMAND>
```

---

## pixi config list#

**URL:** https://pixi.sh/latest/reference/cli/pixi/config/list/

**Contents:**
- pixi config list#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Global Options#
- Description#
- Examples#

List configuration values

List configuration values

Example: pixi config list default-channels

**Examples:**

Example 1 (unknown):
```unknown
pixi config list [OPTIONS] [KEY]
```

Example 2 (unknown):
```unknown
pixi config list default-channels
pixi config list --json
pixi config list --system
pixi config list -g
```

---

## 

**URL:** https://pixi.sh/latest/reference/cli/

---

## pixi workspace version#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/version/

**Contents:**
- pixi workspace version#
- About#
- Usage#
- Subcommands#
- Global Options#

Commands to manage workspace version

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace version [OPTIONS] <COMMAND>
```

---

## pixi workspace platform#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/platform/

**Contents:**
- pixi workspace platform#
- About#
- Usage#
- Subcommands#
- Global Options#

Commands to manage workspace platforms

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace platform [OPTIONS] <COMMAND>
```

---

## pixi global expose#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/expose/

**Contents:**
- pixi global expose#
- About#
- Usage#
- Subcommands#
- Description#

Interact with the exposure of binaries in the global environment

Interact with the exposure of binaries in the global environment

pixi global expose add python310=python3.10 --environment myenv will expose the python3.10 executable as python310 from the environment myenv

pixi global expose remove python310 --environment myenv will remove the exposed name python310 from the environment myenv

**Examples:**

Example 1 (unknown):
```unknown
pixi global expose <COMMAND>
```

---

## pixi global shortcut#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/shortcut/

**Contents:**
- pixi global shortcut#
- About#
- Usage#
- Subcommands#

Interact with the shortcuts on your machine

**Examples:**

Example 1 (unknown):
```unknown
pixi global shortcut <COMMAND>
```

---

## pixi update#

**URL:** https://pixi.sh/latest/reference/cli/pixi/update/

**Contents:**
- pixi update#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Global Options#
- Description#
- Examples#

The update command checks if there are newer versions of the dependencies and updates the pixi.lock file and environments accordingly

The update command checks if there are newer versions of the dependencies and updates the pixi.lock file and environments accordingly.

It will only update the lock file if the dependencies in the manifest file are still compatible with the new versions.

**Examples:**

Example 1 (unknown):
```unknown
pixi update [OPTIONS] [PACKAGES]...
```

Example 2 (unknown):
```unknown
pixi update numpy # (1)!
pixi update numpy pandas # (2)!
pixi update --manifest-path ~/myworkspace/pixi.toml numpy # (3)!
pixi update --environment lint python # (4)!
pixi update -e lint -e schema -e docs pre-commit # (5)!
pixi update --platform osx-arm64 mlx # (6)!
pixi update -p linux-64 -p osx-64 numpy  # (7)!
pixi update --dry-run numpy # (8)!
pixi update --no-install boto3 # (9)!
```

---

## pixi search#

**URL:** https://pixi.sh/latest/reference/cli/pixi/search/

**Contents:**
- pixi search#
- About#
- Usage#
- Arguments#
- Options#
- Global Options#
- Description#
- Examples#

Search a conda package

Search a conda package

Its output will list the latest version of package.

**Examples:**

Example 1 (unknown):
```unknown
pixi search [OPTIONS] <PACKAGE>
```

Example 2 (unknown):
```unknown
pixi search pixi
pixi search --limit 30 "py*"
# search in a different channel and for a specific platform
pixi search -c robostack --platform linux-64 "*plotjuggler*"
# search for a specific version of a package
pixi search "rattler-build<=0.35.4"
pixi search "rattler-build[build_number=h2d22210_0]" --platform linux-64
```

---

## pixi workspace platform list#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/platform/list/

**Contents:**
- pixi workspace platform list#
- About#
- Usage#

List the platforms in the workspace file

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace platform list
```

---

## pixi config unset#

**URL:** https://pixi.sh/latest/reference/cli/pixi/config/unset/

**Contents:**
- pixi config unset#
- About#
- Usage#
- Arguments#
- Config Options#
- Global Options#
- Description#
- Examples#

Unset a configuration value

Unset a configuration value

Example: pixi config unset default-channels

**Examples:**

Example 1 (unknown):
```unknown
pixi config unset [OPTIONS] <KEY>
```

Example 2 (unknown):
```unknown
pixi config unset default-channels
pixi config unset --global mirrors
pixi config unset repodata-config.disable-zstd --system
```

---

## 

**URL:** https://pixi.sh/latest/reference/project_configuration/

---

## pixi auth logout#

**URL:** https://pixi.sh/latest/reference/cli/pixi/auth/logout/

**Contents:**
- pixi auth logout#
- About#
- Usage#
- Arguments#
- Examples#

Remove authentication information for a given host

**Examples:**

Example 1 (unknown):
```unknown
pixi auth logout <HOST>
```

Example 2 (unknown):
```unknown
pixi auth logout <HOST>
pixi auth logout repo.prefix.dev
pixi auth logout anaconda.org
pixi auth logout s3://my-bucket
```

---

## pixi config append#

**URL:** https://pixi.sh/latest/reference/cli/pixi/config/append/

**Contents:**
- pixi config append#
- About#
- Usage#
- Arguments#
- Config Options#
- Global Options#
- Description#
- Examples#

Append a value to a list configuration key

Append a value to a list configuration key

Example: pixi config append default-channels bioconda

**Examples:**

Example 1 (unknown):
```unknown
pixi config append [OPTIONS] <KEY> <VALUE>
```

Example 2 (unknown):
```unknown
pixi config append default-channels robostack
pixi config append default-channels bioconda --global
```

---

## pixi workspace system-requirements#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/system-requirements/

**Contents:**
- pixi workspace system-requirements#
- About#
- Usage#
- Subcommands#
- Global Options#

Commands to manage workspace system requirements

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace system-requirements [OPTIONS] <COMMAND>
```

---

## pixi workspace requires-pixi#

**URL:** https://pixi.sh/latest/reference/cli/pixi/workspace/requires-pixi/

**Contents:**
- pixi workspace requires-pixi#
- About#
- Usage#
- Subcommands#
- Global Options#

Commands to manage the pixi minimum version requirement

**Examples:**

Example 1 (unknown):
```unknown
pixi workspace requires-pixi [OPTIONS] <COMMAND>
```

---

## pixi shell-hook#

**URL:** https://pixi.sh/latest/reference/cli/pixi/shell-hook/

**Contents:**
- pixi shell-hook#
- About#
- Usage#
- Options#
- Config Options#
- Update Options#
- Global Options#
- Description#
- Examples#

Print the pixi environment activation script

Print the pixi environment activation script.

You can source the script to activate the environment without needing pixi itself.

Example use-case, when you want to get rid of the pixi executable in a Docker container.

**Examples:**

Example 1 (unknown):
```unknown
pixi shell-hook [OPTIONS]
```

Example 2 (unknown):
```unknown
pixi shell-hook
pixi shell-hook --shell bash
pixi shell-hook --shell zsh
pixi shell-hook -s powershell
pixi shell-hook --manifest-path ~/myworkspace/pixi.toml
pixi shell-hook --frozen
pixi shell-hook --locked
pixi shell-hook --environment cuda
pixi shell-hook --json
```

Example 3 (unknown):
```unknown
pixi shell-hook --shell bash > /etc/profile.d/pixi.sh
rm ~/.pixi/bin/pixi # Now the environment will be activated without the need for the pixi executable.
```

---

## pixi config prepend#

**URL:** https://pixi.sh/latest/reference/cli/pixi/config/prepend/

**Contents:**
- pixi config prepend#
- About#
- Usage#
- Arguments#
- Config Options#
- Global Options#
- Description#
- Examples#

Prepend a value to a list configuration key

Prepend a value to a list configuration key

Example: pixi config prepend default-channels bioconda

**Examples:**

Example 1 (unknown):
```unknown
pixi config prepend [OPTIONS] <KEY> <VALUE>
```

Example 2 (unknown):
```unknown
pixi config prepend default-channels conda-forge
```

---

## pixi global sync#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/sync/

**Contents:**
- pixi global sync#
- About#
- Usage#
- Config Options#

Sync global manifest with installed environments

**Examples:**

Example 1 (unknown):
```unknown
pixi global sync [OPTIONS]
```

---

## pixi global tree#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/tree/

**Contents:**
- pixi global tree#
- About#
- Usage#
- Arguments#
- Options#
- Description#

Show a tree of dependencies for a specific global environment

Show a tree of a global environment dependencies

Dependency names highlighted in green are directly specified in the manifest.

**Examples:**

Example 1 (unknown):
```unknown
pixi global tree [OPTIONS] --environment <ENVIRONMENT> [REGEX]
```

---

## pixi config edit#

**URL:** https://pixi.sh/latest/reference/cli/pixi/config/edit/

**Contents:**
- pixi config edit#
- About#
- Usage#
- Arguments#
- Config Options#
- Global Options#
- Examples#

Edit the configuration file

**Examples:**

Example 1 (unknown):
```unknown
pixi config edit [OPTIONS] [EDITOR]
```

Example 2 (unknown):
```unknown
pixi config edit --system
pixi config edit --local
pixi config edit -g
pixi config edit --global code
pixi config edit --system vim
```

---

## pixi reinstall#

**URL:** https://pixi.sh/latest/reference/cli/pixi/reinstall/

**Contents:**
- pixi reinstall#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Update Options#
- Global Options#
- Description#

Re-install an environment, both updating the lockfile and re-installing the environment

Re-install an environment, both updating the lockfile and re-installing the environment.

This command reinstalls an environment, if the lockfile is not up-to-date it will be updated. If packages are specified, only those packages will be reinstalled. Otherwise the whole environment will be reinstalled.

pixi reinstall only re-installs one environment at a time, if you have multiple environments you can select the right one with the --environment flag. If you don't provide an environment, the default environment will be re-installed.

If you want to re-install all environments, you can use the --all flag.

**Examples:**

Example 1 (unknown):
```unknown
pixi reinstall [OPTIONS] [PACKAGE]...
```

---

## pixi global update#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/update/

**Contents:**
- pixi global update#
- About#
- Usage#
- Arguments#
- Config Options#
- Examples#

Updates environments in the global environment

**Examples:**

Example 1 (unknown):
```unknown
pixi global update [OPTIONS] [ENVIRONMENTS]...
```

Example 2 (unknown):
```unknown
pixi global update
pixi global update pixi-pack
pixi global update bat rattler-build
```

---

## pixi completion#

**URL:** https://pixi.sh/latest/reference/cli/pixi/completion/

**Contents:**
- pixi completion#
- About#
- Usage#
- Options#

Generates a completion script for a shell

**Examples:**

Example 1 (unknown):
```unknown
pixi completion --shell <SHELL>
```

---

## pixi clean#

**URL:** https://pixi.sh/latest/reference/cli/pixi/clean/

**Contents:**
- pixi clean#
- About#
- Usage#
- Subcommands#
- Options#
- Global Options#
- Description#

Cleanup the environments

Cleanup the environments.

This command removes the information in the .pixi folder. You can specify the environment to remove with the --environment flag.

Use the cache subcommand to clean the cache.

**Examples:**

Example 1 (unknown):
```unknown
pixi clean [OPTIONS] [COMMAND]
```

---
