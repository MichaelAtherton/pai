# Pixi - Building

**Pages:** 18

---

## pixi global uninstall#

**URL:** https://pixi.sh/latest/reference/cli/pixi/global/uninstall/

**Contents:**
- pixi global uninstall#
- About#
- Usage#
- Arguments#
- Config Options#
- Description#
- Examples#

Uninstalls environments from the global environment.

Uninstalls environments from the global environment.

Example: pixi global uninstall pixi-pack rattler-build

**Examples:**

Example 1 (unknown):
```unknown
pixi global uninstall [OPTIONS] <ENVIRONMENT>...
```

Example 2 (unknown):
```unknown
pixi global uninstall my-env
pixi global uninstall pixi-pack rattler-build
```

---

## pixi build#

**URL:** https://pixi.sh/latest/reference/cli/pixi/build/

**Contents:**
- pixi build#
- About#
- Usage#
- Options#
- Config Options#
- Global Options#

Workspace configuration

**Examples:**

Example 1 (unknown):
```unknown
pixi build [OPTIONS]
```

---

## Packaging Pixi

**URL:** https://pixi.sh/latest/misc/packaging/

**Contents:**
- Packaging Pixi
- Building#
  - Build-time Options#
    - TLS#
    - Self-Update#
    - Custom version#
- Shell completion#

This is a guide for distribution maintainers wanting to package Pixi for a different package manager. Users of Pixi can ignore this page.

Pixi is written in Rust and compiled using Cargo, which are needed as compile-time dependencies. At runtime Pixi needs no dependencies in other than the runtime it was compiled against (libc, ...).

To build Pixi run cargo build --locked --profile dist Instead of using the predefined dist profile, which is optimized for binary size, you can also pass other options to let cargo optimize the binary for other metrics.

Pixi provides some compile-time options, which can influence the build

By default, Pixi is built with Rustls TLS implementation. You can compile Pixi using the platform native TLS implementation using by adding --no-default-features --feature native-tls to the build command. Note that this might add additional runtime dependencies, such as OpenSSL on Linux.

Pixi has a self-update functionality. When Pixi is installed using another package manager one usually doesn't want pixi to try to update itself and instead let it be updated by the package manager. For this reason the self-update feature is disabled by default. It can be enabled by adding --feature self_update to the build command.

When the self-update feature is disabled and a user tries to run pixi self-update an error message is displayed. This message can be customized by setting the PIXI_SELF_UPDATE_DISABLED_MESSAGE environment variable at build time to point the user to the package manager they should be using to update pixi. PIXI_SELF_UPDATE_DISABLED_MESSAGE="`self-update` has been disabled for this build. Run `brew upgrade pixi` instead" cargo build --locked --profile dist

You can specify a custom version string to be used in the --version output by setting the PIXI_VERSION environment variable during the build.

After building Pixi you can generate shell autocompletion scripts by running pixi completion --shell <SHELL> and saving the output to a file. Currently supported shells are bash, elvish, fish, nushell, powershell and zsh.

**Examples:**

Example 1 (unknown):
```unknown
cargo build --locked --profile dist
```

Example 2 (unknown):
```unknown
PIXI_SELF_UPDATE_DISABLED_MESSAGE="`self-update` has been disabled for this build. Run `brew upgrade pixi` instead" cargo build --locked --profile dist
```

Example 3 (unknown):
```unknown
PIXI_VERSION="HEAD-123456" cargo build --locked --profile dist
```

Example 4 (unknown):
```unknown
pixi completion --shell <SHELL>
```

---

## Container

**URL:** https://pixi.sh/latest/deployment/container/

**Contents:**
- Container
  - Example Usage#

One way to bring a Pixi package into production is to containerize it using tools like Docker or Podman.

We provide a simple docker image at pixi-docker that contains the Pixi executable on top of different base images.

The images are available on ghcr.io/prefix-dev/pixi.

There are different tags for different base images available:

For all tags, take a look at the build script.

Best practices for docker with pixi

@pavelzw wrote a blog post about shipping conda environments to production using pixi. If you want to know more about best practices using docker with pixi, feel free to check out their blog post.

The following example uses the Pixi docker image as a base image for a multi-stage build. It also makes use of pixi shell-hook to not rely on Pixi being installed in the production container.

For more examples, take a look at pavelzw/pixi-docker-example.

**Examples:**

Example 1 (unknown):
```unknown
FROM ghcr.io/prefix-dev/pixi:0.41.4 AS build

# copy source code, pixi.toml and pixi.lock to the container
WORKDIR /app
COPY . .
# install dependencies to `/app/.pixi/envs/prod`
# use `--locked` to ensure the lockfile is up to date with pixi.toml
RUN pixi install --locked -e prod
# create the shell-hook bash script to activate the environment
RUN pixi shell-hook -e prod -s bash > /shell-hook
RUN echo "#!/bin/bash" > /app/entrypoint.sh
RUN cat /shell-hook >> /app/entrypoint.sh
# extend the shell-hook script to run the command passed to the container
RUN echo 'exec "$@"' >> /app/entrypoint.sh

FROM ubuntu:24.04 AS production
WORKDIR /app
# only copy the production environment into prod container
# please note that the "prefix" (path) needs to stay the same as in the build container
COPY --from=build /app/.pixi/envs/prod /app/.pixi/envs/prod
COPY --from=build --chmod=0755 /app/entrypoint.sh /app/entrypoint.sh
# copy your project code into the container as well
COPY ./my_project /app/my_project

EXPOSE 8000
ENTRYPOINT [ "/app/entrypoint.sh" ]
# run your app inside the pixi environment
CMD [ "uvicorn", "my_project:app", "--host", "0.0.0.0" ]
```

---

## Multiple Packages in Workspace

**URL:** https://pixi.sh/latest/build/workspace/

**Contents:**
- Multiple Packages in Workspace
- Why is This Useful?#
- Let's Get Started#
- Conclusion#

In this tutorial, we will show you how to integrate multiple Pixi packages into a single workspace.

pixi-build is a preview feature, and will change until it is stabilized. Please keep that in mind when you use it for your projects.

The packages coming from conda channels are already built and ready to use. If you want to depend on a package you therefore typically get that package from such a channel. However, there are situations where you want to depend on the source of a package. This is the case for example if you want to develop on multiple packages within the same repository. Or if you need the changes of an unreleased version of one of your dependencies.

In this tutorial we will showcase how to develop two packages in one workspace. For that we will use the python_rich Python package developed in chapter Building a Python package and let it depend on the cpp_math C++ package developed in chapter Building a C++ package.

We will start with the original setup of python_rich and copy cpp_math into a folder called packages. The source directory structure now looks like this:

Within a Pixi manifest, you can manage a workspace and/or describe a package. In the case of python_rich we choose to do both, so the only thing we have to add cpp_math as a run dependency of python_rich.

We only want to use the workspace table of the top-level manifest. Therefore, we can remove the workspace section in the manifest of cpp_math.

There is actually one problem with python_rich. The age of every person is off by one year!

We need to add one year to the age of every person. Luckily cpp_math exposes a function add which allows us to do exactly that.

If you run pixi run start, the age of each person should now be accurate:

In this tutorial, we created a Pixi workspace containing two packages. The manifest of python_rich describes the workspace as well as the package, with cpp_math only the package section is used. Feel free to add more packages, written in different languages to this workspace!

Thanks for reading! Happy Coding 🚀

Any questions? Feel free to reach out or share this tutorial on X, join our Discord, send us an e-mail or follow our GitHub.

**Examples:**

Example 1 (unknown):
```unknown
.
├── packages
│   └── cpp_math
│       ├── CMakeLists.txt
│       ├── pixi.toml
│       └── src
│           └── math.cpp
├── pixi.lock
├── pixi.toml
├── pyproject.toml
└── src
    └── python_rich
        └── __init__.py
```

Example 2 (unknown):
```unknown
[package.run-dependencies]
cpp_math = { path = "packages/cpp_math" }
rich = "13.9.*"
```

Example 3 (unknown):
```unknown
-[workspace]
-channels = ["https://prefix.dev/conda-forge"]
-platforms = ["osx-arm64", "osx-64", "linux-64", "win-64"]
-preview = ["pixi-build"]
-
-[dependencies]
-cpp_math = { path = "." }
-
-[tasks]
-start = "python -c 'import cpp_math as b; print(b.add(1, 2))'"
```

Example 4 (unknown):
```unknown
┏━━━━━━━━━━━━━━┳━━━━━┳━━━━━━━━━━━━━┓
┃ name         ┃ age ┃ city        ┃
┡━━━━━━━━━━━━━━╇━━━━━╇━━━━━━━━━━━━━┩
│ John Doe     │ 30  │ New York    │
│ Jane Smith   │ 25  │ Los Angeles │
│ Tim de Jager │ 35  │ Utrecht     │
└──────────────┴─────┴─────────────┘
```

---

## Package Source

**URL:** https://pixi.sh/latest/build/package_source/

**Contents:**
- Package Source
- Path#

By default, the package definition assumes the location of the source to be in the root of the package definition.

For example if your package has the following structure: my_package ├── pixi.toml ├── src │ └── my_code.cpp └── include └── my_code.h Build backends are expected to have reasonable defaults from where to take the source code. Apart from the pixi-build-rattler-build backend where you specify the source in the recipe.yaml, the build backend will default to the directory where the package manifest is located

Alternatively, you can specify where the source is located.

If your source is located somewhere else, you can specify the location of the source using the package.build.source.path field.

For example if your package has the following structure: my_package ├── pixi.toml └── source ├── src │ └── my_code.cpp └── include └── my_code.h You can specify the location of the source like this: [package.build.source] path = "source"

This will also work with relative paths: [package.build.source] path = "../my_other_source_directory"

This works great in combination with git submodules.

**Examples:**

Example 1 (unknown):
```unknown
my_package
├── pixi.toml
├── src
│   └── my_code.cpp
└── include
    └── my_code.h
```

Example 2 (unknown):
```unknown
my_package
├── pixi.toml
└── source
    ├── src
    │   └── my_code.cpp
    └── include
        └── my_code.h
```

Example 3 (unknown):
```unknown
[package.build.source]
path = "source"
```

Example 4 (unknown):
```unknown
[package.build.source]
path = "../my_other_source_directory"
```

---

## Advanced Building Using rattler-build

**URL:** https://pixi.sh/latest/build/advanced_cpp/

**Contents:**
- Advanced Building Using rattler-build
- Workspace structure#
  - The pixi.toml file#
- The recipe.yaml file#
- Testing if everything works#
- Conclusion#

In this tutorial, we will show you how to build the same C++ package as from Building a C++ Package tutorial using rattler-build. In this tutorial we assume that you've read the Building a C++ Package tutorial. If you haven't read it yet, we recommend you to do so before continuing. You might also want to check out the documentation for the pixi-build-rattler-build backend. The project structure and the source code will be the same as in the previous tutorial, so we may skip explicit explanations of some parts.

This approach may be useful when no build backend for your language or build system exists. Another reason to use it is when you would like to have more control over the build process.

To illustrate this, we will use the same C++ package as in the previous tutorial, but this time we will use rattler-build to build it. This will unveil the hidden complexity of the build process, and give you a better grasp of how backends work.

pixi-build is a preview feature, and will change until it is stabilized. Please keep that in mind when you use it for your workspaces.

Prefer using a backend if it exists. This will give you a more streamlined and unified build experience.

To get started, please recreate the structure of the workspace from the previous tutorial Building a C++ Package.

We are now using the pixi-build-rattler-build backend instead of the pixi-build-cmake backend.

Next lets add the recipe.yaml file that describes how rattler-build builds the package. You can find the reference on the rattler-build documentation web page.

Now that we've defined a pixi task which allows us to check that our package can properly add 1 and 2:

Executing the tasks works as expected

This command builds the bindings, installs them and then runs the test task.

In this tutorial, we created a Pixi package using rattler-build and a recipe.yaml file. Using this approach, we had more control over the build process. For example, we could changed the build type to Debug using CMAKE_BUILD_TYPE, use Make instead of Ninja by removing the -GNinja configuration. Or we could use make -j$(nproc) to specify the number of jobs to run in parallel when building the package.

At the same time, we lost all the benefit of heavy lifting that is done by language build backend.

Thanks for reading! Happy Coding 🚀

Any questions? Feel free to reach out or share this tutorial on X, join our Discord, e-mail us or follow our GitHub.

**Examples:**

Example 1 (unknown):
```unknown
[workspace]
channels = ["https://prefix.dev/conda-forge"]
platforms = ["osx-arm64", "osx-64", "linux-64", "win-64"]
preview = ["pixi-build"]

[dependencies]
cpp_math = { path = "." }
python = "3.12.*"

[tasks]
start = "python -c 'import cpp_math as b; print(b.add(1, 2))'"

[package]
name = "cpp_math"
version = "0.1.0"

[package.build]
backend = { name = "pixi-build-rattler-build", version = "0.3.*" }
```

Example 2 (unknown):
```unknown
package:
  name: cpp_math
  version: 0.1.0

source:
  path: .
  use_gitignore: true # (1)!

build:
  number: 0
  script: | # (2)!
    cmake $CMAKE_ARGS \
      -GNinja \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=$PREFIX \
      -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
      -DBUILD_SHARED_LIBS=ON \
      -B $SRC_DIR/../build \
      -S .

    cmake --build $SRC_DIR/../build --target install

requirements:
  build: # (3)!
    - ${{ compiler('cxx') }}
    - cmake
    - ninja

  host: # (4)!
    - python 3.12.*
    - nanobind
```

Example 3 (unknown):
```unknown
[tasks]
start = "python -c 'import cpp_math as b; print(b.add(1, 2))'"
```

Example 4 (unknown):
```unknown
$ pixi run start
3
```

---

## The Global Manifest#

**URL:** https://pixi.sh/latest/global_tools/manifest/

**Contents:**
- The Global Manifest#
- Manifest locations#
- Channels#
- Dependencies#
- Exposed executables#
  - Automatically Exposed Executables#
- Shortcuts#

This global manifest contains the list of environments that are installed globally, their dependencies and exposed binaries. It can be edited, synced, checked in to a version control system, and shared with others.

Running the commands from the section before results in the following manifest: version = 1 [envs.rattler-build] channels = ["conda-forge"] dependencies = { rattler-build = "*" } exposed = { rattler-build = "rattler-build" } [envs.ipython] channels = ["conda-forge"] dependencies = { ipython = "*", numpy = "*", matplotlib = "*" } exposed = { ipython = "ipython", ipython3 = "ipython3" } [envs.python] channels = ["conda-forge"] dependencies = { python = "3.12.*" } # (1)! exposed = { py3 = "python" } # (2)!

The manifest can be found at the following locations depending on your operating system. Run pixi info, to find the currently used manifest on your system.

If multiple locations exist, the manifest with the highest priority will be used.

The channels key describes the Conda channels that will be used to download the packages. There is a priority to these, so the first one will have the highest priority. If a package is not found in that channel the next one will be used. For example, running: pixi global install --channel conda-forge --channel bioconda snakemake Results in the following entry in the manifest: [envs.snakemake] channels = ["conda-forge", "bioconda"] dependencies = { snakemake = "*" } exposed = { snakemake = "snakemake" }

More information on channels can be found here.

Dependencies are the Conda packages that will be installed into your environment. For example, running: pixi global install "python<3.12" creates the following entry in the manifest: [envs.vim] channels = ["conda-forge"] dependencies = { python = "<3.12" } # ... Typically, you'd specify just the tool you're installing, but you can add more packages if needed. Defining the environment to install into will allow you to add multiple dependencies at once. For example, running: pixi global install --environment my-env git vim python will create the following entry in the manifest:

You can add dependencies to an existing environment by running: pixi global add --environment my-env package-a package-b

They will be added as dependencies to the my-env environment but won't auto expose the binaries from the new packages.

You can remove dependencies by running:

One can instruct pixi global install, under which name it will expose executables:

The manifest is modified like this:

This means that executable bat will be exposed under the name bird.

There is some added automatic behavior, if you install a package with the same name as the environment, it will be exposed with the same name. Even if the binary name is only exposed through dependencies of the package For example, running: pixi global install ansible will create the following entry in the manifest: [envs.ansible] channels = ["conda-forge"] dependencies = { ansible = "*" } exposed = { ansible = "ansible" } # (1)!

It's also possible to expose an executable which is located in a nested directory. For example dotnet.exe executable is located in a dotnet folder, to expose dotnet you must specify its relative path :

Which will create the following entry in the manifest: [envs.dotnet] channels = ["conda-forge"] dependencies = { dotnet = "*" } exposed = { dotnet = 'dotnet\dotnet' }

Especially for graphical user interfaces it is useful to add shortcuts. This way the application shows up in the start menu or is suggested when you want to open a file type the application supports. If the package supports shortcuts, nothing has to be done from your side. Simply executing pixi global install will do the trick. For example, pixi global install mss will lead to the following manifest:

Note the shortcuts entry. If it's present, pixi will install the shortcut for the mss package. This means, the application will show up in the start menu. If you want to package an application yourself that would benefit from this, you can check out the corresponding documentation.

**Examples:**

Example 1 (unknown):
```unknown
version = 1

[envs.rattler-build]
channels = ["conda-forge"]
dependencies = { rattler-build = "*" }
exposed = { rattler-build = "rattler-build" }

[envs.ipython]
channels = ["conda-forge"]
dependencies = { ipython = "*", numpy = "*", matplotlib = "*" }
exposed = { ipython = "ipython", ipython3 = "ipython3" }

[envs.python]
channels = ["conda-forge"]
dependencies = { python = "3.12.*" } # (1)!
exposed = { py3 = "python" } # (2)!
```

Example 2 (unknown):
```unknown
pixi global install --channel conda-forge --channel bioconda snakemake
```

Example 3 (unknown):
```unknown
[envs.snakemake]
channels = ["conda-forge", "bioconda"]
dependencies = { snakemake = "*" }
exposed = { snakemake = "snakemake" }
```

Example 4 (unknown):
```unknown
pixi global install "python<3.12"
```

---

## Variants

**URL:** https://pixi.sh/latest/build/variants/

**Contents:**
- Variants
- Why is This Useful?#
- Let's Get Started#
- Conclusion#

In this tutorial, we will show you how to use variants in order to build a Pixi package against different versions of a dependency. Some might call this functionality, build matrix, build configurations or parameterized builds, in the conda ecosystem this is referred to as a variant.

pixi-build is a preview feature, and will change until it is stabilized. Please keep that in mind when you use it for your projects.

When we depend on a Pixi package, the dependency versions of the package itself are already set. For example, in the C++ tutorial the cpp_math package we built depended on Python 3.12. Pixi would report a version conflict, if we'd add use both Python 3.11 and cpp_math to our workspace. By using variants, we can add a set of allowed versions for a specific dependency. Pixi will then resolve the package with all the different variants.

In this tutorial we will continue with the result of the workspace tutorial so we can test it against multiple Python versions. As a reminder, we ended up with a top-level pixi.toml containing the workspace and the Python package python_rich. Our workspace then depended on python_rich and cpp_math.

The file tree looks like this:

In order to allow multiple Python versions we first have to change the Python version requirement of cpp_math from 3.12.* to *.

Now, we have to specify the Python versions we want to allow. We do that in workspace.build-variants:

If we'd run pixi install now, we'd leave it up to Pixi whether to use Python 3.11 or 3.12. In practice, you'll want to create multiple environments specifying a different dependency version. In our case this allows us to test our setup against both Python 3.11 and 3.12.

By running pixi list we can see the Python version used in each environment. You can also see that the Build string of cpp_math differ between py311 and py312. That means that a different package has been built for each variant. Since python_rich only contains Python source code, a single build can be used for multiple Python versions. The package is noarch. Therefore, the build string is the same.

In this tutorial, we showed how to use variants to build multiple versions of a single package. We built cpp_math for Python 3.12 and 3.13, which allows us to test whether it works properly on both Python versions. Variants are not limited to a single dependency, you could for example try to test multiple versions of nanobind.

On top of adding variants inline, they can also be included as files. Check out the reference to learn more!

Thanks for reading! Happy Coding 🚀

Any questions? Feel free to reach out or share this tutorial on X, join our Discord, send us an e-mail or follow our GitHub.

**Examples:**

Example 1 (unknown):
```unknown
[dependencies]
python_rich = { path = "." }
```

Example 2 (unknown):
```unknown
.
├── packages
│   └── cpp_math
│       ├── CMakeLists.txt
│       ├── pixi.toml
│       └── src
│           └── math.cpp
├── pixi.lock
├── pixi.toml
├── pyproject.toml
└── src
    └── python_rich
        └── __init__.py
```

Example 3 (unknown):
```unknown
[package.host-dependencies]
cmake = ">=3.20, <3.27"
nanobind = ">=2.4.0, <2.5.0"
python = "*"                 # (1)!
```

Example 4 (unknown):
```unknown
[workspace.build-variants]
python = ["3.11.*", "3.12.*"]
```

---

## pixi add#

**URL:** https://pixi.sh/latest/reference/cli/pixi/add/

**Contents:**
- pixi add#
- About#
- Usage#
- Arguments#
- Options#
- Config Options#
- Git Options#
- Update Options#
- Global Options#
- Description#

Adds dependencies to the workspace

Adds dependencies to the workspace

The dependencies should be defined as MatchSpec for conda package, or a PyPI requirement for the --pypi dependencies. If no specific version is provided, the latest version compatible with your workspace will be chosen automatically or a * will be used.

Adding multiple dependencies at once is also supported:

The --platform and --build/--host flags make the dependency target specific.

Mixing --platform and --build/--host flags is supported

The --pypi option will add the package as a pypi dependency. This cannot be mixed with the conda dependencies

If the workspace manifest is a pyproject.toml, adding a pypi dependency will add it to the native pyproject project.dependencies array or to the native dependency-groups table if a feature is specified:

Note that if --platform or --editable are specified, the pypi dependency will be added to the tool.pixi.pypi-dependencies table instead as native arrays have no support for platform-specific or editable dependencies.

These dependencies will then be read by pixi as if they had been added to the pixi pypi-dependencies tables of the default or of a named feature.

The versions will be automatically added with a pinning strategy based on semver or the pinning strategy set in the config. There is a list of packages that are not following the semver versioning scheme but will use the minor version by default: Python, Rust, Julia, GCC, GXX, GFortran, NodeJS, Deno, R, R-Base, Perl

If you want to use a non default pinning strategy, you can set it using pixi's configuration. pixi config set pinning-strategy no-pin --global The default is semver which will pin the dependencies to the latest major version or minor for v0 versions.

There is an exception to this rule when you add a package we defined as non semver, then we'll use the minor strategy. These are the packages we defined as non semver: Python, Rust, Julia, GCC, GXX, GFortran, NodeJS, Deno, R, R-Base, Perl

**Examples:**

Example 1 (unknown):
```unknown
pixi add [OPTIONS] <SPEC>...
```

Example 2 (unknown):
```unknown
pixi add numpy # (1)!
pixi add numpy pandas "pytorch>=1.8" # (2)!
pixi add "numpy>=1.22,<1.24" # (3)!
pixi add --manifest-path ~/myworkspace/pixi.toml numpy # (4)!
pixi add --host "python>=3.9.0" # (5)!
pixi add --build cmake # (6)!
pixi add --platform osx-64 clang # (7)!
pixi add --no-install numpy # (8)!
pixi add --no-lockfile-update numpy # (9)!
pixi add --feature featurex numpy # (10)!
pixi add --git https://github.com/wolfv/pixi-build-examples boost-check # (11)!
pixi add --git https://github.com/wolfv/pixi-build-examples --branch main --subdir boost-check boost-check # (12)!
pixi add --git https://github.com/wolfv/pixi-build-examples --tag v0.1.0 boost-check # (13)!
pixi add --git https://github.com/wolfv/pixi-build-examples --rev e50d4a1 boost-check # (14)!

# Add a pypi dependency
pixi add --pypi requests[security] # (15)!
pixi add --pypi Django==5.1rc1 # (16)!
pixi add --pypi "boltons>=24.0.0" --feature lint # (17)!
pixi add --pypi "boltons @ https://files.pythonhosted.org/packages/46/35/e50d4a115f93e2a3fbf52438435bb2efcf14c11d4fcd6bdcd77a6fc399c9/boltons-24.0.0-py3-none-any.whl" # (18)!
pixi add --pypi "exchangelib @ git+https://github.com/ecederstrand/exchangelib" # (19)!
pixi add --pypi "project @ file:///absolute/path/to/project" # (20)!
pixi add --pypi "project@file:///absolute/path/to/project" --editable # (21)!
pixi add --git https://github.com/mahmoud/boltons.git boltons --pypi # (22)!
pixi add --git https://github.com/mahmoud/boltons.git boltons --branch main --pypi # (23)!
pixi add --git https://github.com/mahmoud/boltons.git boltons --rev e50d4a1 --pypi # (24)!
pixi add --git https://github.com/mahmoud/boltons.git boltons --tag v0.1.0 --pypi # (25)!
pixi add --git https://github.com/mahmoud/boltons.git boltons --tag v0.1.0 --pypi --subdir boltons # (26)!
```

Example 3 (unknown):
```unknown
pixi config set pinning-strategy no-pin --global
```

---

## Conda/Mamba

**URL:** https://pixi.sh/latest/switching_from/conda/

**Contents:**
- Conda/Mamba
- Why Pixi?#
- Key Differences at a Glance#
- Environment vs Workspace#
- Global environments#
- Automated switching#
- Troubleshooting#

Welcome to the guide designed to ease your transition from conda or mamba to pixi. This document compares key commands and concepts between these tools, highlighting pixi's unique approach to managing environments and packages. With pixi, you'll experience a workspace-based workflow, enhancing your development process, and allowing for easy sharing of your work.

Pixi builds upon the foundation of the conda ecosystem, introducing a workspace-centric approach rather than focusing solely on environments. This shift towards workspaces offers a more organized and efficient way to manage dependencies and run code, tailored to modern development practices.

Conda has a base environment, which is the default environment when you start a new shell. Pixi does not have a base environment. And requires you to install the tools you need in the workspace or globally. Using pixi global install bat will install bat in a global environment, which is not the same as the base environment in conda.

For some advanced use-cases, you can activate the environment in the current shell. This uses the pixi shell-hook which prints the activation script, which can be used to activate the environment in the current shell without pixi itself. ~/myenv > eval "$(pixi shell-hook)"

Conda and mamba focus on managing environments, while pixi emphasizes workspaces. In pixi, a workspace is a folder containing a manifest(pixi.toml/pyproject.toml) file that describes the workspace, a pixi.lock lock-file that describes the exact dependencies, and a .pixi folder that contains the environment.

This workspace-centric approach allows for easy sharing and collaboration, as the workspace folder contains all the necessary information to recreate the environment. It manages more than one environment for more than one platform in a single workspace, and allows for easy switching between them. (See multiple environments)

conda installs all environments in one global location. When this is important to you for filesystem reasons, you can use the detached-environments feature of pixi. pixi config set detached-environments true # or a specific location pixi config set detached-environments /path/to/envs This doesn't allow you to activate the environments using pixi shell -n but it will make the installation of the environments go to the same folder.

pixi does have the pixi global command to install tools on your machine. (See global) This is not a replacement for conda but works the same as pipx and condax. It creates a single isolated environment for the given requirement and installs the binaries into the global path. pixi global install bat bat pixi.toml

Never install pip with pixi global

Installations with pixi global get their own isolated environment. Installing pip with pixi global will create a new isolated environment with its own pip binary. Using that pip binary will install packages in the pip environment, making it unreachable form anywhere as you can't activate it.

You can import environment.yml files into a Pixi workspace — see our import tutorial.

If you are working with Conda users or systems, you can export your environment to a environment.yml file to share them. pixi workspace export conda-environment Additionally you can export a conda explicit specification.

Encountering issues? Here are solutions to some common problems when being used to the conda workflow:

**Examples:**

Example 1 (unknown):
```unknown
~/myenv > eval "$(pixi shell-hook)"
```

Example 2 (unknown):
```unknown
pixi config set detached-environments true
# or a specific location
pixi config set detached-environments /path/to/envs
```

Example 3 (unknown):
```unknown
pixi global install bat
bat pixi.toml
```

Example 4 (unknown):
```unknown
pixi workspace export conda-environment
```

---

## Building a C++ Package

**URL:** https://pixi.sh/latest/build/cpp/

**Contents:**
- Building a C++ Package
- Creating a New Workspace#
- Creating the workspace files#
  - The pixi.toml file#
  - The CMakeLists.txt file#
  - The src/math.cpp file#
- Testing if everything works#
- Conclusion#

This example shows how to build a C++ package with CMake and use it together with pixi-build. To read more about how building packages work with Pixi see the Getting Started guide. You might also want to check out the documentation for the pixi-build-cmake backend.

We'll start off by creating a workspace that use nanobind to build Python bindings. That we can also test using pixi. We'll later combine this example together with a Python package.

pixi-build is a preview feature, and will change until it is stabilized. Please keep that in mind when you use it for your workspaces.

To get started, create a new workspace with pixi:

This should give you the basic pixi.toml to get started.

We'll now create the following source directory structure: cpp_math/ ├── CMakeLists.txt ├── pixi.toml ├── .gitignore └── src └── math.cpp

Next up we'll create the:

Use the following pixi.toml file, you can hover over the annotations to see why each step was added.

Next lets add the CMakeList.txt file: cmake_minimum_required(VERSION 3.20...3.27) project(cpp_math) find_package(Python 3.8 COMPONENTS Interpreter Development.Module REQUIRED) # (1)! execute_process( COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE nanobind_ROOT ) # (2)! execute_process( COMMAND ${Python_EXECUTABLE} -c "import sysconfig; print(sysconfig.get_path('purelib'))" OUTPUT_VARIABLE PYTHON_SITE_PACKAGES OUTPUT_STRIP_TRAILING_WHITESPACE ) # (3)! find_package(nanobind CONFIG REQUIRED) # (4)! nanobind_add_module(${PROJECT_NAME} src/math.cpp) # (5)! install( # (6)! TARGETS ${PROJECT_NAME} EXPORT ${PROJECT_NAME}Targets LIBRARY DESTINATION ${PYTHON_SITE_PACKAGES} ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR} RUNTIME DESTINATION ${BINDIR} )

Next lets add the src/math.cpp file, this one is quite simple:

Now that we have created the files we can test if everything works:

This command builds the bindings, installs them and then runs the test task.

In this tutorial, we created a Pixi package using C++. It can be used as-is, to upload to a conda channel. In another tutorial we will learn how to add multiple Pixi packages to the same workspace and let one Pixi package use another.

Thanks for reading! Happy Coding 🚀

Any questions? Feel free to reach out or share this tutorial on X, join our Discord, e-mail us or follow our GitHub.

**Examples:**

Example 1 (unknown):
```unknown
pixi init cpp_math
```

Example 2 (unknown):
```unknown
cpp_math/
├── CMakeLists.txt
├── pixi.toml
├── .gitignore
└── src
    └── math.cpp
```

Example 3 (unknown):
```unknown
[workspace]
channels = ["https://prefix.dev/conda-forge"]
platforms = ["osx-arm64", "linux-64", "osx-64", "win-64"]
preview = ["pixi-build"]                                  # (1)!

[dependencies] # (2)!
cpp_math = { path = "." }
python = "*"

[tasks]
start = "python -c 'import cpp_math as b; print(b.add(1, 2))'" # (3)!

[package] # (4)!
name = "cpp_math"
version = "0.1.0"

[package.build]
backend = { name = "pixi-build-cmake", version = "0.3.*" }

[package.build.config]
extra-args = ["-DCMAKE_BUILD_TYPE=Release"] # (9)!

[package.host-dependencies]
cmake = "3.20.*"   # (8)!
nanobind = "2.4.*" # (6)!
python = "3.12.*"  # (7)!
```

Example 4 (unknown):
```unknown
cmake_minimum_required(VERSION 3.20...3.27)
project(cpp_math)

find_package(Python 3.8 COMPONENTS Interpreter Development.Module REQUIRED) # (1)!

execute_process(
  COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
  OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE nanobind_ROOT
) # (2)!

execute_process(
    COMMAND ${Python_EXECUTABLE} -c "import sysconfig; print(sysconfig.get_path('purelib'))"
    OUTPUT_VARIABLE PYTHON_SITE_PACKAGES
    OUTPUT_STRIP_TRAILING_WHITESPACE
) # (3)!

find_package(nanobind CONFIG REQUIRED) # (4)!

nanobind_add_module(${PROJECT_NAME} src/math.cpp) # (5)!

install( # (6)!
    TARGETS ${PROJECT_NAME}
    EXPORT ${PROJECT_NAME}Targets
    LIBRARY DESTINATION ${PYTHON_SITE_PACKAGES}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${BINDIR}
)
```

---

## Pixi Vision

**URL:** https://pixi.sh/latest/misc/vision/

**Contents:**
- Pixi Vision
- Pixi values#
- Conda#
- Target languages#

We created pixi because we want to have a cargo/npm/yarn like package management experience for conda. We really love what the conda packaging ecosystem achieves, but we think that the user experience can be improved a lot. Modern package managers like cargo have shown us, how great a package manager can be. We want to bring that experience to the conda ecosystem.

We want to make Pixi a great experience for everyone, so we have a few values that we want to uphold:

We are building on top of the conda packaging ecosystem, this means that we have a huge number of packages available for different platforms on conda-forge. We believe the conda packaging ecosystem provides a solid base to manage your dependencies. Conda-forge is community maintained and very open to contributions. It is widely used in data science and scientific computing, robotics and other fields. And has a proven track record.

More info: Conda & Pypi

Essentially, we are language agnostics, we are targeting any language that can be installed with conda. Including: C++, Python, Rust, Zig etc. But we do believe the python ecosystem can benefit from a good package manager that is based on conda. So we are trying to provide an alternative to existing solutions there. We also think we can provide a good solution for C++ projects, as there are a lot of libraries available on conda-forge today. Pixi also truly shines when using it for multi-language projects e.g. a mix of C++ and Python, because we provide a nice way to build everything up to and including system level packages.

---

## Build Backends

**URL:** https://pixi.sh/latest/build/backends/

**Contents:**
- Build Backends
  - Installation#
  - Overriding the Build Backend#

To decouple the building of a conda package from Pixi we provide something what are called build backends. These are essentially executables following a specific protocol that is implemented for both Pixi and the build backend. This also allows for decoupling of the build backend from Pixi and it's manifest specification.

The Prefix.dev managed backends are being developed in the pixi-build-backends repository, and have their own documentation.

Install a certain build backend by adding it to the package.build section of the manifest file.:

For custom backend channels, you can add the channel to the channels section of the manifest file: [package.build] backend = { name = "pixi-build-python", version = "==0.4.0" } channels = [ "https://prefix.dev/pixi-build-backends", "https://prefix.dev/conda-forge", ]

Sometimes you want to override the build backend that is used by pixi. Meaning overriding the backend that is specified in the [package.build]. We currently have two environment variables that allow for this:

**Examples:**

Example 1 (unknown):
```unknown
[package.build.backend]
channels = [
  "https://prefix.dev/pixi-build-backends",
  "https://prefix.dev/conda-forge",
]
name = "pixi-build-python"
version = "0.1.*"
```

Example 2 (unknown):
```unknown
[package.build]
backend = { name = "pixi-build-python", version = "==0.4.0" }
channels = [
  "https://prefix.dev/pixi-build-backends",
  "https://prefix.dev/conda-forge",
]
```

---

## Dependency Types

**URL:** https://pixi.sh/latest/build/dependency_types/

**Contents:**
- Dependency Types
  - Build Dependencies#
  - Host Dependencies#
    - Python Code#
    - Native Code#
    - Run-Exports#
  - Dependencies (Run Dependencies)#

If you add a package to the dependency table of a feature that dependency will be available in all environments that include that feature. The dependencies of a package that is being built are a bit more granular. Here you can see the three types of dependencies for a simple C++ package.

Each dependency is used at a different step of the package building process. cxx-compiler is used to build the package, catch will be linked into the package and git will be available during runtime.

Let's delve deeper into the various types of package dependencies and their specific roles in the build process.

When using the pixi-build-cmake backend you do not need to specify cmake or the compiler as a dependency. The backend will install cmake, ninja and the C++ compilers by default.

This table contains dependencies that are needed to build the workspace. Different from dependencies and host-dependencies these packages are installed for the architecture of the build machine. This enables cross-compiling from one machine architecture to another.

Typical examples of build dependencies are:

The build target refers to the machine that will execute the build. Programs and libraries installed by these dependencies will be executed on the build machine.

For example, if you compile on a MacBook with an Apple Silicon chip but target Linux x86_64 then your build platform is osx-arm64 and your host platform is linux-64.

Host dependencies are the dependencies needed during build/link time that are specific to the host machine. The difference to build dependencies becomes for example important during cross compilation. The compiler is a build dependency since it is specific to your machine. In contrast, the libraries you link to are host dependencies since they are specific to the host machine. Typical examples of host dependencies are:

Because of the way building currently works, dependencies like hatchling,pip,uv etc. are host dependencies. Otherwise, it would use the wrong python prefix during the build process.

This is more of a technical limitation, and we are looking into ways to make this less of a hassle. But for now, you will need to add these dependencies to the host-dependencies section.

So as an example, say we want to use hatchling and uv as to build a python package. You need to use, something like this in your manifest file:

When cross-compiling, you might need to specify host dependencies that should have the target machine architecture, and are used during the build process. When linking a library, for example. Let's recap an explanation that can be found here A Master Guide To Linux Cross-Compiling

Let's say we are using a Linux PC (linux-64) to cross compile a CMake application called Awesome to run on a Linux ARM target machine (linux-aarch64). We would get the following table:

So if I need to use a library like SDL2, I would need to add it to the host-dependencies table. As the machine running Awesome will have a different host architecture than the build architecture.

Giving you something like this in your manifest file:

Conda packages, can define run-exports, that are dependencies that when specified in the host-dependencies section, will be implicitly be added to the run-dependencies section. This is useful to avoid having to specify the same dependencies in both sections. As most packages on conda-forge will have these run-exports defined. When using something like zlib, you would only need to specify it in the host-dependencies section, and it will be used as a run-dependency automatically.

These are the dependencies that are required to when running the package, they are the most common dependencies. And are what you would usually use in a workspace.

**Examples:**

Example 1 (unknown):
```unknown
[package.build-dependencies]
cxx-compiler = "*"

[package.host-dependencies]
catch = "*"

[package.run-dependencies]
git = "*"
```

Example 2 (unknown):
```unknown
[host-dependencies]
hatchling = "*"
uv = "*"
```

Example 3 (unknown):
```unknown
# in our example these dependencies will use the aarch64 binaries
[host-dependencies]
sdl2 = "*"
```

---

## Global Tools#

**URL:** https://pixi.sh/latest/global_tools/introduction/

**Contents:**
- Global Tools#
- Basic Usage#
- Install Dependencies From Source#
- Shell Completions#
- Adding a Series of Tools at Once#
- Creating a Data Science Sandbox Environment#
- Install Packages For a Different Platform#
- Packaging#
  - Opt Out of CONDA_PREFIX#

With pixi global, users can manage globally installed tools in a way that makes them available from any directory. This means that the Pixi environment will be placed in a global location, and the tools will be exposed to the system PATH, allowing you to run them from the command line. Some packages, especially those with graphical user interfaces, will also add start menu entries.

Running the following command installs rattler-build on your system.

What's great about pixi global is that, by default, it isolates each package in its own environment, exposing only the necessary entry points. This means you don't have to worry about removing a package and accidentally breaking seemingly unrelated packages. This behavior is quite similar to that of pipx.

However, there are times when you may want multiple dependencies in the same environment. For instance, while ipython is really useful on its own, it becomes much more useful when numpy and matplotlib are available when using it.

Let's execute the following command:

numpy exposes executables, but since it's added via --with it's executables are not being exposed.

Importing numpy and matplotlib now works as expected. ipython -c 'import numpy; import matplotlib'

At some point, you might want to install multiple versions of the same package on your system. Since they will be all available on the system PATH, they need to be exposed under different names.

Let's check out the following command: pixi global install --expose py3=python "python=3.12"

By specifying --expose we specified that we want to expose the executable python under the name py3. The package python has more executables, but since we specified --exposed they are not auto-exposed.

You can run py3 to start the python interpreter. py3 -c "print('Hello World')"

Pixi global also allows you to install Pixi packages. Let's assume there's a C++ package we'd like to install globally from source. First, it needs to have a package manifest:

If the source is on your machine, you can install it like this:

If the source resides in a git repository, you can access it like this:

One has to take care if the source contains multiple outputs, see for example this recipe:

In this case, we have to specify which output we want to install:

When you work in a terminal, you are using a shell and shells can process completions of command line tools. The process works like this: you type "git -" in your terminal and press <TAB>. Then, your shell will present you all the flags git offers. However, that only works if you have the completions installed for the tool in question. If the tool you installed via pixi global contains completions they will be automatically installed. At the moment, only Linux and macOS are supported.

First install a tool with pixi global:

The completions can be found under $PIXI_HOME/completions.

You can then load the completions in the startup script of your shell:

Completions of packages are installed as long as their binaries are exposed under the same name: e.g. exposed = { git = "git" }.

Without specifying an environment, you can add multiple tools at once: pixi global install pixi-pack rattler-build This command generates the following entry in the manifest: [envs.pixi-pack] channels = ["conda-forge"] dependencies= { pixi-pack = "*" } exposed = { pixi-pack = "pixi-pack" } [envs.rattler-build] channels = ["conda-forge"] dependencies = { rattler-build = "*" } exposed = { rattler-build = "rattler-build" } Creating two separate non-interfering environments, while exposing only the minimum required binaries.

You can create an environment with multiple tools using the following command: pixi global install --environment data-science --expose jupyter --expose ipython jupyter numpy pandas matplotlib ipython This command generates the following entry in the manifest: [envs.data-science] channels = ["conda-forge"] dependencies = { jupyter = "*", ipython = "*" } exposed = { jupyter = "jupyter", ipython = "ipython" } In this setup, both jupyter and ipython are exposed from the data-science environment, allowing you to run: > ipython # Or > jupyter lab These commands will be available globally, making it easy to access your preferred tools without switching environments.

You can install packages for a different platform using the --platform flag. This is useful when you want to install packages for a different platform, such as osx-64 packages on osx-arm64. For example, running this on osx-arm64: pixi global install --platform osx-64 python will create the following entry in the manifest: [envs.python] channels = ["conda-forge"] platforms = ["osx-64"] dependencies = { python = "*" } # ...

Pixi activates the target environment before running a globally exposed executable, which usually sets CONDA_PREFIX to that environment's path. Some tools inspect CONDA_PREFIX and expect it to point to a standard Conda installation, which can lead to confusing behavior when the tool runs from a Pixi-managed prefix.

Package authors can opt out of exporting CONDA_PREFIX by shipping a marker file at etc/pixi/<executable>/global-ignore-conda-prefix inside the environment (for example etc/pixi/borg/global-ignore-conda-prefix for an executable named borg). When this file is present for the exposed executable, Pixi removes CONDA_PREFIX from the environment variables, letting the tool behave as if no Conda environment is active.

Here's a minimal recipe.yaml snippet that adds the marker while building the package with executable borg:

After installing such a package with pixi global install, the exposed executable no longer sees CONDA_PREFIX and can fall back to its default behavior.

**Examples:**

Example 1 (unknown):
```unknown
pixi global install rattler-build
```

Example 2 (unknown):
```unknown
pixi global install ipython --with numpy --with matplotlib
```

Example 3 (unknown):
```unknown
ipython -c 'import numpy; import matplotlib'
```

Example 4 (unknown):
```unknown
pixi global install --expose py3=python "python=3.12"
```

---

## Getting Started

**URL:** https://pixi.sh/latest/build/getting_started/

**Contents:**
- Getting Started
- Setting up the Manifest#
- CLI Commands#

Next to managing workflows and environments, Pixi can also build packages. This is useful for the following reasons:

We've been working to support these use-cases with the build feature in pixi. The vision is to enable building of packages from source, for any language, on any platform.

Currently, the build feature has a number of limitations:

This is an overview of the Pixi manifest using the pixi-build feature.

A more in-depth overview of what is available in the [package] part of the manifest can be found in the Manifest Reference.

Under the [workspace] section, you can specify properties like the name, channels, and platforms. This is currently an alias for [project].

Since the build feature is still in preview, you have to add "pixi-build" to workspace.preview.

In package you specify properties specific to the package you want to build.

Packages are built by using build backends. By specifying package.build.backend and package.build.channels you determine which backend is used and from which channel it will be downloaded.

There are different build backends available.

Pixi backends describe how to build a conda package, for a certain language or build tool. In this example, we are using pixi-build-python backend in order to build a Python package.

We need to add our package python_rich as source dependency to the workspace.

python_rich uses hatchling as Python build backend, so this needs to be mentioned in host-dependencies.

Python PEP517 backends like hatchling know how to build a Python package. So hatchling creates a Python package, and pixi-build-python turns the Python package into a conda package.

Read up on host-dependencies in the dependency types chapter

We add rich as a run dependency to the package. This is necessary because the package uses rich during runtime. You can read up on run-dependencies in the dependency types chapter

Using the preview feature you can now build packages from source.

**Examples:**

Example 1 (unknown):
```unknown
### Specifies properties for the whole workspace ###
[workspace]
preview = ["pixi-build"]
channels = ["https://prefix.dev/conda-forge"]
platforms = ["win-64", "linux-64", "osx-arm64", "osx-64"]

[tasks]
start = "rich-example-main"

[dependencies]
python_rich = { path = "." }

### Specify the package properties ###
[package]
name = "python_rich"
version = "0.1.0"

# We are using `pixi-build-python` in order to build a Python package
[package.build.backend]
name = "pixi-build-python"
version = "==0.4.0"


# The Python package `python_rich` uses `hatchling` as Python build backend
[package.host-dependencies]
hatchling = "*"

# The Python package `python_rich` has a run dependency on `rich`
[package.run-dependencies]
rich = "13.9.*"
```

Example 2 (unknown):
```unknown
[workspace]
preview = ["pixi-build"]
```

Example 3 (unknown):
```unknown
[package]
name = "python_rich"
version = "0.1.0"
```

Example 4 (unknown):
```unknown
[package.build.backend]
name = "pixi-build-python"
version = "==0.4.0"
```

---

## Building a ROS Package

**URL:** https://pixi.sh/latest/build/ros/

**Contents:**
- Building a ROS Package
- Create a Pixi workspace#
- Creating a Python ROS package#
  - Initialize a ROS package#
  - Add Pixi package info to the new package#
  - Add the package to the pixi workspace#
  - Testing your package#
- Create a CMake ROS package#
  - Scaffold a C++ package:#
  - Add the pixi package info#

This guide shows how to build a ROS package into a conda package with Pixi using the pixi-build-ros backend.

To understand the build feature, start with the general Build Getting Started guide. For ROS without Pixi building (not packaging), see the ROS 2 tutorial. You may also want to read the backend documentation for pixi-build-ros.

pixi-build is a preview feature and may change before stabilization. Expect rough edges; please report issues so we can improve it.

Initialize a new workspace and install the ROS 2 CLI so you can scaffold packages via the ros2 cli.

This adds the ros2 cli command to your Pixi environment.

In all examples below, ensure the build preview is enabled in your workspace manifest: ros_ws/pixi.tomlpreview = ["pixi-build"]

Resulting workspace manifest: ros_ws/pixi.toml[workspace] channels = [ "https://prefix.dev/robostack-jazzy", "https://prefix.dev/conda-forge", ] platforms = [ "osx-arm64", "win-64", "linux-64", ] # Your platform here, e.g. "linux-64", "osx-arm64", "win-64" preview = ["pixi-build"] [dependencies] ros-jazzy-ros2run = ">=0.32.4,<0.33"

We'll be creating a normal ROS2 package using ament_python and then adding Pixi support to it. Most of the logic is done by the ROS2 CLI, so you can follow normal ROS 2 package creation steps.

Use the ROS CLI to generate an ament_python package skeleton within the workspace.

You should now have something like:

Create a pixi.toml inside src/my_python_ros_pkg so Pixi can build it using the ROS backend. The backend reads most metadata from package.xml, so you only need to specify the backend and distro.

Tell the root workspace to depend on the package via a path dependency that matches the ROS-prefixed name:

pixi run ros2 run my_python_ros_pkg my_python_node Outputs: Hi from my_python_ros_pkg.

Creating a C++ or mixed package using ament_cmake.

Create a pixi.toml inside src/my_cmake_ros_pkg so Pixi can build it using the ROS backend. The backend reads most metadata from package.xml, so you only need to specify the backend and distro.

Tell the root workspace to depend on the package via a path dependency that matches the ROS-prefixed name:

Now install and run: pixi run ros2 run my_cmake_ros_pkg my_cmake_node Outputs: hello world my_cmake_ros_pkg package

With the package(s) added to the workspace, you can now build them.

You can now upload these artifacts to a conda channel and depend on them from other Pixi workspaces.

You can package ROS projects as conda packages with Pixi using the pixi-build-ros backend. Start simple, keep package.xml truthful, add ROS dependencies as needed, and iterate with the preview build feature. Once built, you can upload artifacts to a conda channel and depend on them from other Pixi workspaces.

**Examples:**

Example 1 (unknown):
```unknown
pixi init ros_ws --channel https://prefix.dev/robostack-jazzy --channel https://prefix.dev/conda-forge
cd ros_ws
pixi add ros-jazzy-ros2run
```

Example 2 (unknown):
```unknown
preview = ["pixi-build"]
```

Example 3 (unknown):
```unknown
[workspace]
channels = [
  "https://prefix.dev/robostack-jazzy",
  "https://prefix.dev/conda-forge",
]
platforms = [
  "osx-arm64",
  "win-64",
  "linux-64",
] # Your platform here, e.g. "linux-64", "osx-arm64", "win-64"
preview = ["pixi-build"]

[dependencies]
ros-jazzy-ros2run = ">=0.32.4,<0.33"
```

Example 4 (unknown):
```unknown
pixi run ros2 pkg create --build-type ament_python --destination-directory src --node-name my_python_node my_python_ros_pkg
```

---
