# Pixi - Tutorials

**Pages:** 8

---

## ROS 2

**URL:** https://pixi.sh/latest/tutorials/ros2/

**Contents:**
- ROS 2
- Prerequisites#
- Create a Pixi workspace#
- Add ROS 2 dependencies#
- Add a custom Python node#
- Simplify the user experience#
- Build a C++ node#
- Conclusion#
- Show Off Your Work!#
- Frequently asked questions#

In this tutorial, we will show you how to develop a ROS 2 package using pixi. The tutorial is written to be executed from top to bottom, missing steps might result in errors.

The audience for this tutorial is developers who are familiar with ROS 2 and how are interested to try Pixi for their development workflow.

It should have created a directory structure like this:

The pixi.toml file is the manifest file for your workspace. It should look like this:

The channels you added to the init command are repositories of packages, you can search in these repositories through our prefix.dev website. The platforms are the systems you want to support, in Pixi you can support multiple platforms, but you have to define which platforms, so Pixi can test if those are supported for your dependencies. For the rest of the fields, you can fill them in as you see fit.

To use a Pixi workspace you don't need any dependencies on your system, all the dependencies you need should be added through pixi, so other users can use your workspace without any issues.

Let's start with the turtlesim example

This will add the ros-humble-desktop and ros-humble-turtlesim packages to your manifest. Depending on your internet speed this might take a minute, as it will also install ROS in your workspace folder (.pixi).

Now run the turtlesim example.

Or use the shell command to start an activated environment in your terminal.

Congratulations you have ROS 2 running on your machine with pixi!

To control the turtle you can run the following command in a new terminal cd my_ros2_project pixi run ros2 run turtlesim turtle_teleop_key Now you can control the turtle with the arrow keys on your keyboard.

As ros works with custom nodes, let's add a custom node to our project.

To build the package we need some more dependencies:

Add the created initialization script for the ros workspace to your manifest file.

Then run the build command

This will create a sourceable script in the install folder, you can source this script through an activation script to use your custom node. Normally this would be the script you add to your .bashrc but instead you tell Pixi to use it by adding the following to pixi.toml:

You can add multiple activation scripts for different platforms, so you can support multiple platforms with one workspace. Use the following example to add support for both Linux and Windows, using the target syntax.

Now you can run your custom node with the following command

In pixi we have a feature called tasks, this allows you to define a task in your manifest file and run it with a simple command. Let's add a task to run the turtlesim example and the custom node.

Now you can run these task by simply running

Tasks are a powerful feature in pixi.

To build a C++ node you need to add the ament_cmake and some other build dependencies to your manifest file.

Now you can create a C++ node with the following command

Now you can build it again and run it with the following commands

Add the cpp task to the manifest file to simplify the user experience.

In this tutorial, we showed you how to create a Python & CMake ROS2 project using pixi. We also showed you how to add dependencies to your project using pixi, and how to run your project using pixi run. This way you can make sure that your project is reproducible on all your machines that have pixi installed.

Finished with your project? We'd love to see what you've created! Share your work on social media using the hashtag #pixi and tag us @prefix_dev. Let's inspire the community together!

Currently, we don't support rosdep in a Pixi environment, so you'll have to add the packages using pixi add. rosdep will call conda install which isn't supported in a Pixi environment.

You can find more documentation on RoboStack channels in the RoboStack documentation.

ROS 2 Humble on macOS,Simulating differential drive using Gazebo.

**Examples:**

Example 1 (unknown):
```unknown
pixi init my_ros2_project -c robostack-humble -c conda-forge
cd my_ros2_project
```

Example 2 (unknown):
```unknown
my_ros2_project
├── .gitattributes
├── .gitignore
└── pixi.toml
```

Example 3 (unknown):
```unknown
[workspace]
name = "my_ros2_project"
version = "0.1.0"
description = "Add a short description here"
authors = ["User Name <user.name@email.url>"]
channels = ["robostack-humble", "conda-forge"]
# Your project can support multiple platforms, the current platform will be automatically added.
platforms = ["linux-64"]

[tasks]

[dependencies]
```

Example 4 (unknown):
```unknown
pixi add ros-humble-desktop ros-humble-turtlesim
```

---

## 

**URL:** https://pixi.sh/latest/tutorials/python/

---

## Rust

**URL:** https://pixi.sh/latest/tutorials/rust/

**Contents:**
- Rust
- Prerequisites#
- Create a Pixi workspace#
- Add Rust dependencies#
- Add a cargo project#
- Next steps, why is this useful when there is rustup?#
- Extra: Add more tasks#
- Conclusion#
- Show Off Your Work!#

In this tutorial, we will show you how to develop a Rust package using pixi. The tutorial is written to be executed from top to bottom, missing steps might result in errors.

The audience for this tutorial is developers who are familiar with Rust and cargo and how are interested to try Pixi for their development workflow. The benefit would be within a rust workflow that you lock both rust and the C/System dependencies your project might be using. For example tokio users might depend on openssl for linux.

It should have created a directory structure like this:

The pixi.toml file is the manifest file for your workspace. It should look like this:

To use a Pixi workspace you don't need any dependencies on your system, all the dependencies you need should be added through pixi, so other users can use your workspace without any issues. pixi add rust

This will add the rust package to your pixi.toml file under [dependencies]. Which includes the rust toolchain, and cargo.

Now that you have rust installed, you can create a cargo project in your pixi workspace. pixi run cargo init

pixi run is pixi's way to run commands in the pixi environment, it will make sure that the environment is set up correctly for the command to run. It runs its own cross-platform shell, if you want more information checkout the tasks documentation. You can also activate the environment in your own shell by running pixi shell, after that you don't need pixi run ... anymore.

Now we can build a cargo project using pixi. pixi run cargo build To simplify the build process, you can add a build task to your pixi.toml file using the following command: pixi task add build "cargo build" Which creates this field in the pixi.toml file: pixi.toml[tasks] build = "cargo build"

And now you can build your project using: pixi run build

You can also run your project using: pixi run cargo run Which you can simplify with a task again. pixi task add start "cargo run"

So you should get the following output: pixi run start Hello, world!

Congratulations, you have a Rust project running on your machine with pixi!

Cargo is not a binary package manager, but a source-based package manager. This means that you need to have the Rust compiler installed on your system to use it. And possibly other dependencies that are not included in the cargo package manager. For example, you might need to install openssl or libssl-dev on your system to build a package. This is the case for pixi as well, but pixi will install these dependencies in your workspace folder, so you don't have to worry about them.

Add the following dependencies to your cargo project: pixi run cargo add git2

If your system is not preconfigured to build C and have the libssl-dev package installed you will not be able to build the project: pixi run build ... Could not find directory of OpenSSL installation, and this `-sys` crate cannot proceed without this knowledge. If OpenSSL is installed and this crate had trouble finding it, you can set the `OPENSSL_DIR` environment variable for the compilation process. Make sure you also have the development packages of openssl installed. For example, `libssl-dev` on Ubuntu or `openssl-devel` on Fedora. If you're in a situation where you think the directory *should* be found automatically, please open a bug at https://github.com/sfackler/rust-openssl and include information about your system as well as this message. $HOST = x86_64-unknown-linux-gnu $TARGET = x86_64-unknown-linux-gnu openssl-sys = 0.9.102 It looks like you're compiling on Linux and also targeting Linux. Currently this requires the `pkg-config` utility to find OpenSSL but unfortunately `pkg-config` could not be found. If you have OpenSSL installed you can likely fix this by installing `pkg-config`. ... You can fix this, by adding the necessary dependencies for building git2, with pixi: pixi add openssl pkg-config compilers

Now you should be able to build your project again: pixi run build ... Compiling git2 v0.18.3 Compiling my_rust_project v0.1.0 (/my_rust_project) Finished dev [unoptimized + debuginfo] target(s) in 7.44s Running `target/debug/my_rust_project`

You can add more tasks to your pixi.toml file to simplify your workflow.

For example, you can add a test task to run your tests: pixi task add test "cargo test"

And you can add a clean task to clean your project: pixi task add clean "cargo clean"

You can add a formatting task to your project: pixi task add fmt "cargo fmt"

You can extend these tasks to run multiple commands with the use of the depends-on field. pixi task add lint "cargo clippy" --depends-on fmt

In this tutorial, we showed you how to create a Rust project using pixi. We also showed you how to add dependencies to your project using pixi. This way you can make sure that your project is reproducible on any system that has pixi installed.

Finished with your project? We'd love to see what you've created! Share your work on social media using the hashtag #pixi and tag us @prefix_dev. Let's inspire the community together!

**Examples:**

Example 1 (unknown):
```unknown
pixi init my_rust_project
cd my_rust_project
```

Example 2 (unknown):
```unknown
my_rust_project
├── .gitattributes
├── .gitignore
└── pixi.toml
```

Example 3 (unknown):
```unknown
[workspace]
name = "my_rust_project"
version = "0.1.0"
description = "Add a short description here"
authors = ["User Name <user.name@email.url>"]
channels = ["conda-forge"]
platforms = ["linux-64"] # (1)!

[tasks]

[dependencies]
```

Example 4 (unknown):
```unknown
pixi add rust
```

---

## pyproject.toml

**URL:** https://pixi.sh/latest/python/pyproject_toml/

**Contents:**
- pyproject.toml
- Initial setup of the pyproject.toml file#
- Python dependency#
- Dependency section#
- Optional dependencies#
- Dependency groups#
- Example#
- Build-system section#
- Development dependencies with [tool.uv.sources]#
  - Why is this useful?#

We support the use of the pyproject.toml as our manifest file in pixi. This allows the user to keep one file with all configuration. The pyproject.toml file is a standard for Python projects. We don't advise to use the pyproject.toml file for anything else than python projects, the pixi.toml is better suited for other types of projects.

When you already have a pyproject.toml file in your project, you can run pixi init in a that folder. Pixi will automatically

If you do not have an existing pyproject.toml file , you can run pixi init --format pyproject in your project folder. In that case, Pixi will create a pyproject.toml manifest from scratch with some sane defaults.

The pyproject.toml file supports the requires_python field. Pixi understands that field and automatically adds the version to the dependencies.

This is an example of a pyproject.toml file with the requires_python field, which will be used as the python dependency:

Which is equivalent to:

The pyproject.toml file supports the dependencies field. Pixi understands that field and automatically adds the dependencies to the workspace as [pypi-dependencies].

This is an example of a pyproject.toml file with the dependencies field:

Which is equivalent to:

You can overwrite these with conda dependencies by adding them to the dependencies field:

This would result in the conda dependencies being installed and the pypi dependencies being ignored. As Pixi takes the conda dependencies over the pypi dependencies.

If your python project includes groups of optional dependencies, Pixi will automatically interpret them as Pixi features of the same name with the associated pypi-dependencies.

You can add them to Pixi environments manually, or use pixi init to setup the workspace, which will create one environment per feature. Self-references to other groups of optional dependencies are also handled.

For instance, imagine you have a project folder with a pyproject.toml file similar to:

Running pixi init in that project folder will transform the pyproject.toml file into:

In this example, three environments will be created by pixi:

All environments will be solved together, as indicated by the common solve-group, and added to the lock file. You can edit the [tool.pixi.environments] section manually to adapt it to your use case (e.g. if you do not need a particular environment).

If your python project includes dependency groups, Pixi will automatically interpret them as Pixi features of the same name with the associated pypi-dependencies.

You can add them to Pixi environments manually, or use pixi init to setup the workspace, which will create one environment per dependency group.

For instance, imagine you have a project folder with a pyproject.toml file similar to:

Running pixi init in that project folder will transform the pyproject.toml file into:

In this example, four environments will be created by pixi:

All environments will be solved together, as indicated by the common solve-group, and added to the lock file. You can edit the [tool.pixi.environments] section manually to adapt it to your use case (e.g. if you do not need a particular environment).

As the pyproject.toml file supports the full Pixi spec with [tool.pixi] prepended an example would look like this:

The pyproject.toml file normally contains a [build-system] section. Pixi will use this section to build and install the project if it is added as a pypi path dependency.

If the pyproject.toml file does not contain any [build-system] section, Pixi will fall back to uv's default, which is equivalent to the below:

Including a [build-system] section is highly recommended. If you are not sure of the build-backend you want to use, including the [build-system] section below in your pyproject.toml is a good starting point. pixi init --format pyproject defaults to hatchling. The advantages of hatchling over setuptools are outlined on its website.

Because pixi is using uv for building its pypi-dependencies, one can use the tool.uv.sources section to specify sources for any pypi-dependencies referenced from the main pixi manifest.

When you are setting up a monorepo of some sort and you want to be able for source dependencies to reference each other, you need to use the [tool.uv.sources] section to specify the sources for those dependencies. This is because uv handles both the resolution of PyPI dependencies and the building of any source dependencies.

Concretely what this looks like in the pyproject.toml for main_project:

Then the pyproject.toml for a should contain a [tool.uv.sources] section.

More information about what is allowed in this sections is available in the uv docs

The main pixi.toml or pyproject.toml is parsed directly by pixi and not processed by uv. This means that you cannot use the [tool.uv.sources] section in the main pixi.toml or pyproject.toml. This is a limitation we are aware of, feel free to open an issue if you would like support for this.

**Examples:**

Example 1 (unknown):
```unknown
[project]
name = "my_project"
requires-python = ">=3.9"

[tool.pixi.workspace]
channels = ["conda-forge"]
platforms = ["linux-64", "osx-arm64", "osx-64", "win-64"]
```

Example 2 (unknown):
```unknown
[workspace]
name = "my_project"
channels = ["conda-forge"]
platforms = ["linux-64", "osx-arm64", "osx-64", "win-64"]

[dependencies]
python = ">=3.9"
```

Example 3 (unknown):
```unknown
[project]
name = "my_project"
requires-python = ">=3.9"
dependencies = [
    "numpy",
    "pandas",
    "matplotlib",
]

[tool.pixi.workspace]
channels = ["conda-forge"]
platforms = ["linux-64", "osx-arm64", "osx-64", "win-64"]
```

Example 4 (unknown):
```unknown
[workspace]
name = "my_project"
channels = ["conda-forge"]
platforms = ["linux-64", "osx-arm64", "osx-64", "win-64"]

[pypi-dependencies]
numpy = "*"
pandas = "*"
matplotlib = "*"

[dependencies]
python = ">=3.9"
```

---

## Multi Environment

**URL:** https://pixi.sh/latest/tutorials/multi_environment/

**Contents:**
- Multi Environment
- Why Is This Useful?#
- Glossary#
    - Feature#
    - Environment#
    - Default#
- Let's Get Started#
  - Adding a feature#
  - Adding an environment#
  - Running a task#

In this tutorial we will show you how to use multiple environments in one Pixi workspace.

When developing a workspace you often need different tools, libraries or test environments. With Pixi you can define multiple environments in one workspace and switch between them easily. A developer often needs all the tools they can get, whereas your testing infrastructure might not require all those tools, and your production environment might require even less. Setting up different environments for these different use cases can be a hassle, but with Pixi it's easy.

This tutorial possibly uses some new terms, here is a quick overview:

A feature defines a part of an environment, but are not useful without being part of an environment. You can define multiple features in one workspace. A feature can contain tasks, dependencies, platforms, channels and more. You can mix multiple features to create an environment. Features are defined by adding [feature.<name>.*] to a table in the manifest file.

An environment is a collection of features. Environments can actually be installed and activated to run tasks in. You can define multiple environments in one workspace. Defining environments is done by adding them to the [environments] table in the manifest file.

Instead of specifying [feature.<name>.dependencies], one can populate [dependencies] directly. These top level table, are added to the "default" feature, which is added to every environment, unless you specifically opt-out.

We'll simply start with a new workspace, you can skip this step if you already have a Pixi workspace.

Now we have a new Pixi workspace with the following structure: ├── .pixi │ └── envs │ └── default ├── pixi.lock └── pixi.toml

Note the .pixi/envs/default directory, this is where the default environment is stored. If no environment is specified, Pixi will create or use the default environment.

Let's start adding a simple test feature to our workspace. We can do this through the command line, or by editing the pixi.toml file. Here we will use the command line, and add a pytest dependency to the test feature in our workspace. pixi add --feature test pytest This will add the following to our pixi.toml file: [feature.test.dependencies] pytest = "*" This table acts exactly the same as a normal dependencies table, but it is only used when the test feature is part of an environment.

We will add the test environment to our workspace to add some testing tools. We can do this through the command line, or by editing the pixi.toml file. Here we will use the command line: pixi workspace environment add test --feature test This will add the following to our pixi.toml file: [environments] test = ["test"]

We can now run a task in our new environment. pixi run --environment test pytest --version This has created the test environment, and run the pytest --version command in it. You can see the environment will be added to the .pixi/envs directory. ├── .pixi │ └── envs │ ├── default │ └── test If you want to see the environment, you can use the pixi list command. pixi list --environment test

If you have special test commands that always fit with the test environment you can add them to the test feature. # Adding the 'test' task to the 'test' feature and setting it to run `pytest` pixi task add test --feature test pytest This will add the following to our pixi.toml file: [feature.test.tasks] test = "pytest" Now you don't have to specify the environment when running the test command. pixi run test In this example similar to running pixi run --environment test pytest

This works as long as there is only one of the environments that has the test task.

In this example we will use multiple environments to test a package against multiple versions of Python. This is a common use-case when developing a python library. This workflow can be translated to any setup where you want to have multiple environments to test against a different dependency setups.

For this example we assume you have run the commands in the previous example, and have a workspace with a test environment. To allow python being flexible in the new environments we need to set it to a more flexible version e.g. *.

We will start by setting up two features, py311 and py312. pixi add --feature py311 python=3.11 pixi add --feature py312 python=3.12

We'll add the test and Python features to the corresponding environments. pixi workspace environment add test-py311 --feature py311 --feature test pixi workspace environment add test-py312 --feature py312 --feature test

This should result in adding the following to the pixi.toml: [feature.py311.dependencies] python = "3.11.*" [feature.py312.dependencies] python = "3.12.*" [environments] test-py311 = ["py311", "test"] test-py312 = ["py312", "test"]

Now we can run the test command in both environments. pixi run --environment test-py311 test pixi run --environment test-py312 test # Or using the task directly, which will spawn a dialog to select the environment of choice pixi run test

These could now run in CI to test separate environments: .github/workflows/test.ymltest: runs-on: ubuntu-latest strategy: matrix: environment: [test-py311, test-py312] steps: - uses: actions/checkout@v4 - uses: prefix-dev/setup-pixi@v0 with: environments: ${{ matrix.environment }} - run: pixi run -e ${{ matrix.environment }} test More info on that in the GitHub actions documentation.

This assumes a clean workspace, so if you have been following along, you might want to start a new workspace. pixi init production_project cd production_project

Like before we'll start with creating multiple features. pixi add numpy python # default feature pixi add --feature dev jupyterlab pixi add --feature test pytest

Now we'll add the environments. To accommodate the different use-cases we'll add a production, test and default environment.

We make this the default environment as it will be the easiest to run locally, as it avoids the need to specify the environment when running tasks.

We'll also add the solve-group prod to the environments, this will make sure that the dependencies are solved as if they were in the same environment. This will result in the production environment having the exact same versions of the dependencies as the default and test environment. This way we can be sure that the project will run in the same way in all environments.

If we run pixi list -x for the environments we can see that the different environments have the exact same dependency versions. # Default environment Package Version Build Size Kind Source jupyterlab 4.3.4 pyhd8ed1ab_0 6.9 MiB conda jupyterlab numpy 2.2.1 py313ha4a2180_0 6.2 MiB conda numpy pytest 8.3.4 pyhd8ed1ab_1 253.1 KiB conda pytest python 3.13.1 h4f43103_105_cp313 12.3 MiB conda python Environment: test Package Version Build Size Kind Source numpy 2.2.1 py313ha4a2180_0 6.2 MiB conda numpy pytest 8.3.4 pyhd8ed1ab_1 253.1 KiB conda pytest python 3.13.1 h4f43103_105_cp313 12.3 MiB conda python Environment: production Package Version Build Size Kind Source numpy 2.2.1 py313ha4a2180_0 6.2 MiB conda numpy python 3.13.1 h4f43103_105_cp313 12.3 MiB conda python

When you want to have an environment that doesn't have the default feature, you can use the --no-default-feature flag. This will result in the environment not having the default feature, and only the features you specify.

A common use-case of this would be having an environment that can generate your documentation.

Let's add the mkdocs dependency to the docs feature. pixi add --feature docs mkdocs

Now we can add the docs environment without the default feature. pixi workspace environment add docs --feature docs --no-default-feature

If we run pixi list -x -e docs we can see that it only has the mkdocs dependency. Environment: docs Package Version Build Size Kind Source mkdocs 1.6.1 pyhd8ed1ab_1 3.4 MiB conda mkdocs

The multiple environment feature is extremely powerful and can be used in many different ways. There is much more to explore in the reference and advanced sections. If there are any questions, or you know how to improve this tutorial, feel free to reach out to us on GitHub.

**Examples:**

Example 1 (unknown):
```unknown
pixi init workspace
cd workspace
pixi add python
```

Example 2 (unknown):
```unknown
├── .pixi
│   └── envs
│       └── default
├── pixi.lock
└── pixi.toml
```

Example 3 (unknown):
```unknown
pixi add --feature test pytest
```

Example 4 (unknown):
```unknown
[feature.test.dependencies]
pytest = "*"
```

---

## Building a Python Package

**URL:** https://pixi.sh/latest/build/python/

**Contents:**
- Building a Python Package
- Why is This Useful?#
- Let's Get Started#
  - Adding a pixi.toml#
- Conclusion#

In this tutorial, we will show you how to create a simple Python package with pixi. To read more about how building packages work with Pixi see the Getting Started guide. You might also want to check out the documentation for the pixi-build-python backend.

pixi-build is a preview feature, and will change until it is stabilized. Please keep that in mind when you use it for your projects.

Pixi builds upon the conda ecosystem, which allows you to create a Python environment with all the dependencies you need. Unlike PyPI, the conda ecosystem is cross-language and also offers packages written in Rust, R, C, C++ and many other languages.

By building a Python package with pixi, you can:

In this tutorial we will focus on point 1.

First, we create a simple Python package with a pyproject.toml and a single Python file. The package will be called python_rich, so we will create the following structure:

The Python package has a single function main. Calling that, will print a table containing the name, age and city of three people.

The metadata of the Python package is defined in pyproject.toml.

What we have in the moment, constitutes a full Python package. It could be uploaded to PyPI as-is.

However, we still need a tool to manage our environments and if we want other Pixi projects to depend on our tool, we need to include more information. We will do exactly that by creating a pixi.toml.

The Pixi manifest can be in its own pixi.toml file or integrated in pyproject.toml In this tutorial, we will use pixi.toml. If you want everything integrated in pyproject.toml just copy the content of pixi.toml in this tutorial to your pyproject.toml and prepend tool.pixi. to each table.

Let's initialize a Pixi project.

We pass --format pixi in order to communicate to pixi, that we want a pixi.toml rather than extending pyproject.toml.

This is the content of the pixi.toml:

When we now run pixi run start, we get the following output:

In this tutorial, we created a Pixi package based on Python. It can be used as-is, to upload to a conda channel or to PyPI. In another tutorial we will learn how to add multiple Pixi packages to the same workspace and let one Pixi package use another.

Thanks for reading! Happy Coding 🚀

Any questions? Feel free to reach out or share this tutorial on X, join our Discord, send us an e-mail or follow our GitHub.

**Examples:**

Example 1 (unknown):
```unknown
├── src # (1)!
│   └── python_rich
│       └── __init__.py
└── pyproject.toml
```

Example 2 (python):
```python
from dataclasses import dataclass, fields
from rich.console import Console
from rich.table import Table


@dataclass
class Person:
    name: str
    age: int
    city: str


def main() -> None:
    console = Console()

    people = [
        Person("John Doe", 30, "New York"),
        Person("Jane Smith", 25, "Los Angeles"),
        Person("Tim de Jager", 35, "Utrecht"),
    ]

    table = Table()

    for column in fields(Person):
        table.add_column(column.name)

    for person in people:
        table.add_row(person.name, str(person.age), person.city)

    console.print(table)
```

Example 3 (unknown):
```unknown
[project]
dependencies = ["rich"]                              # (1)!
name = "python_rich"
requires-python = ">= 3.11"
scripts = { rich-example-main = "python_rich:main" } # (2)!
version = "0.1.0"

[build-system] # (3)!
build-backend = "hatchling.build"
requires = ["hatchling"]
```

Example 4 (unknown):
```unknown
pixi init --format pixi
```

---

## Basic Usage

**URL:** https://pixi.sh/latest/python/tutorial/

**Contents:**
- Basic Usage
- Why is this useful?#
- pixi.toml and pyproject.toml#
- Let's get started#
  - What's in the pyproject.toml?#
  - Managing both Conda and PyPI dependencies#
  - Installation: pixi install#
- What's in the environment?#
  - Multiple environments#
- Getting code to run#

In this tutorial, we will show you how to create a simple Python project with Pixi. We will show some of the features that Pixi provides, that are currently not a part of pdm, poetry etc.

Pixi builds upon the conda ecosystem, which allows you to create a Python environment with all the dependencies you need. This is especially useful when you are working with multiple Python interpreters and bindings to C and C++ libraries. For example, GDAL from PyPI does not have binary C dependencies, but the conda package does. On the other hand, some packages are only available through PyPI, which pixi can also install for you. Best of both world, let's give it a go!

We support two manifest formats: pyproject.toml and pixi.toml. In this tutorial, we will use the pyproject.toml format because it is the most common format for Python projects.

Let's start out by creating a new project that uses a pyproject.toml file.

This creates a project directory with the following structure:

The pyproject.toml for the project looks like this:

This project uses a src-layout, but Pixi supports both flat- and src-layouts.

Okay, so let's have a look at what sections have been added and how we can modify the pyproject.toml.

These first entries were added to the pyproject.toml file:

The channels and platforms are added to the [tool.pixi.workspace] section. Channels like conda-forge manage packages similar to PyPI but allow for different packages across languages. The keyword platforms determines which platforms the workspace supports.

The pixi_py package itself is added as an editable dependency. This means that the package is installed in editable mode, so you can make changes to the package and see the changes reflected in the environment, without having to re-install the environment.

In pixi, unlike other package managers, this is explicitly stated in the pyproject.toml file. The main reason being so that you can choose which environment this package should be included in.

Our projects usually depend on other packages.

This will add the black package as a Conda package to the pyproject.toml file. Which will result in the following addition to the pyproject.toml:

But we can also be strict about the version that should be used. pixi add black=25 resulting in:

Sometimes there are packages that aren't available on conda channels but are published on PyPI.

which results in the addition to the dependencies key in the pyproject.toml

When using the pypi-dependencies you can make use of the optional-dependencies that other packages make available as extras. For example, flask makes the async dependencies option, which can be added with the --pypi keyword:

which updates the dependencies entry to

This tutorial focuses on the use of the pyproject.toml, but in case you're curious, the pixi.toml would contain the following entry after the installation of a PyPI package including an optional dependency: [pypi-dependencies] flask = { version = "==3.1.0", extras = ["async"] }

Pixi always ensures the environment is up-to-date with the pyproject.toml file when running the environment. If you want to do it manually, you can run:

We now have a new directory called .pixi in the workspace root. The environment is a Conda environment with all the Conda and PyPI dependencies installed into it.

The environment is always a result of the pixi.lock file, which is generated from the pyproject.toml file. This file contains the exact versions of the dependencies that were installed in the environment across platforms.

Using pixi list, you can see what's in the environment, this is essentially a nicer view on the lock file (pixi.lock):

Package Version Build Size Kind Source asgiref 3.8.1 68.5 KiB pypi asgiref-3.8.1-py3-none-any.whl black 24.10.0 py313h8f79df9_0 388.7 KiB conda black blinker 1.9.0 23.9 KiB pypi blinker-1.9.0-py3-none-any.whl bzip2 1.0.8 h99b78c6_7 120 KiB conda bzip2 ca-certificates 2024.12.14 hf0a4a13_0 153.4 KiB conda ca-certificates click 8.1.8 pyh707e725_0 82.7 KiB conda click flask 3.1.0 335.9 KiB pypi flask-3.1.0-py3-none-any.whl itsdangerous 2.2.0 45.8 KiB pypi itsdangerous-2.2.0-py3-none-any.whl jinja2 3.1.5 484.8 KiB pypi jinja2-3.1.5-py3-none-any.whl libexpat 2.6.4 h286801f_0 63.2 KiB conda libexpat libffi 3.4.2 h3422bc3_5 38.1 KiB conda libffi liblzma 5.6.3 h39f12f2_1 96.8 KiB conda liblzma libmpdec 4.0.0 h99b78c6_0 67.6 KiB conda libmpdec libsqlite 3.48.0 h3f77e49_1 832.8 KiB conda libsqlite libzlib 1.3.1 h8359307_2 45.3 KiB conda libzlib markupsafe 3.0.2 73 KiB pypi markupsafe-3.0.2-cp313-cp313-macosx_11_0_arm64.whl mypy_extensions 1.0.0 pyha770c72_1 10.6 KiB conda mypy_extensions ncurses 6.5 h5e97a16_3 778.3 KiB conda ncurses openssl 3.4.0 h81ee809_1 2.8 MiB conda openssl packaging 24.2 pyhd8ed1ab_2 58.8 KiB conda packaging pathspec 0.12.1 pyhd8ed1ab_1 40.1 KiB conda pathspec pixi_py 0.1.0 pypi (editable) platformdirs 4.3.6 pyhd8ed1ab_1 20 KiB conda platformdirs python 3.13.1 h4f43103_105_cp313 12.3 MiB conda python python_abi 3.13 5_cp313 6.2 KiB conda python_abi readline 8.2 h92ec313_1 244.5 KiB conda readline tk 8.6.13 h5083fa2_1 3 MiB conda tk tzdata 2025a h78e105d_0 120 KiB conda tzdata werkzeug 3.1.3 743 KiB pypi werkzeug-3.1.3-py3-none-any.whl Here, you can see the different conda and Pypi packages listed. As you can see, the pixi-py package that we are working on is installed in editable mode. Every environment in Pixi is isolated but reuses files that are hard-linked from a central cache directory. This means that you can have multiple environments with the same packages but only have the individual files stored once on disk.

The Python interpreter is also installed in the environment. This is because the Python interpreter version is read from the requires-python field in the pyproject.toml file. This is used to determine the Python version to install in the environment. This way, Pixi automatically manages/bootstraps the Python interpreter for you, so no more brew, apt or other system install steps.

If you want to use a free-threaded Python interpreter, you can add the python-freethreading dependency with: pixi add python-freethreading This ensures that a free-threaded version of Python is installed in the environment. This might not work with other packages that are not thread-safe yet. You can read more about free-threaded Python here.

Pixi can also create multiple environments, this works well together with the dependency-groups feature in the pyproject.toml file.

Let's add a dependency-group, which Pixi calls a feature, named test. And add the pytest package to this group.

This results in the package being added to the dependency-groups following the PEP 735.

After we have added the dependency-groups to the pyproject.toml, Pixi sees these as a feature, which can contain a collection of dependencies, tasks, channels, and more.

Solve groups are a way to group dependencies together. This is useful when you have multiple environments that share the same dependencies. For example, maybe pytest is a dependency that influences the dependencies of the default environment. By putting these in the same solve group, you ensure that the versions in test and default are exactly the same.

Without specifying the environment name, Pixi will default to the default environment. If you want to install or run the test environment, you can specify the environment with the --environment flag.

Let's add some code to the pixi_py package. We will add a new function to the src/pixi_py/__init__.py file:

Now add the rich dependency from PyPI pixi add --pypi rich

Let's see if this works by running:

pixi run python -c 'import pixi_py; pixi_py.say_hello()' Which should output:

This might be slow the first time because Pixi installs the project, but it will be near instant the second time.

Pixi runs the self installed Python interpreter. Then, we are importing the pixi_py package, which is installed in editable mode. The code calls the say_hello function that we just added. And it works! Cool!

Okay, so let's add a test for this function. Let's add a tests/test_me.py file in the root of the project.

Giving us the following project structure:

Let's add an easy task for running the tests.

So Pixi has a task system to make it easy to run commands. Similar to npm scripts or something you would specify in a Justfile.

Tasks are a cool Pixi feature that is powerful and runs in a cross-platform shell. You can do caching, dependencies and more. Read more about tasks in the tasks section.

pixi run test results in the following output: ✨ Pixi task (test): pytest . ================================================================================================= test session starts ================================================================================================= platform darwin -- Python 3.12.2, pytest-8.1.1, pluggy-1.4.0 rootdir: /private/tmp/pixi-py configfile: pyproject.toml collected 1 item test_me.py . [100%] ================================================================================================== 1 passed in 0.00s =================================================================================================

The test task was added to the test feature/environment. When you run the test task, Pixi automatically switches to the test environment. Because that is the only environment that has the task.

Neat! It seems to be working!

Let's compare the output of the test and default environments. We add the --explicit flag to show the explicit dependencies in the environment.

We see that the test environment has:

However, the default environment is missing the pytest package. This way, you can finetune your environments to only have the packages that are needed for that environment. E.g. you could also have a dev environment that has pytest and ruff installed, but you could omit these from the prod environment. There is a docker example that shows how to set up a minimal prod environment and copy from there.

Last thing, Pixi provides the ability for pypi packages to depend on conda packages. Let's confirm this with: pixi list pygments Note that it was installed as a pypi package: Package Version Build Size Kind Source pygments 2.17.2 4.1 MiB pypi pygments-2.17.2-py3-none-any.http.whl

This is a dependency of the rich package. As you can see by running: pixi tree --invert pygments

Let's explicitly add pygments to the pyproject.toml file.

This will add the following to the pyproject.toml file:

We can now see that the pygments package is now installed as a conda package.

pixi list pygments Now results in: Package Version Build Size Kind Source pygments 2.19.1 pyhd8ed1ab_0 867.8 KiB conda pygments

This way, PyPI dependencies and conda dependencies can be mixed and matched to seamlessly interoperate.

In this tutorial, you've seen how easy it is to use a pyproject.toml to manage your Pixi dependencies and environments. We have also explored how to use PyPI and conda dependencies seamlessly together in the same workspace and install optional dependencies to manage Python packages.

Hopefully, this provides a flexible and powerful way to manage your Python projects and a fertile base for further exploration with Pixi.

Thanks for reading! Happy Coding 🚀

Any questions? Feel free to reach out or share this tutorial on X, join our Discord, send us an e-mail or follow our GitHub.

**Examples:**

Example 1 (unknown):
```unknown
pixi init pixi-py --format pyproject
```

Example 2 (unknown):
```unknown
pixi-py
├── pyproject.toml
└── src
    └── pixi_py
        └── __init__.py
```

Example 3 (unknown):
```unknown
[project]
dependencies = []
name = "pixi-py"
requires-python = ">= 3.11"
version = "0.1.0"

[build-system]
build-backend = "hatchling.build"
requires = ["hatchling"]

[tool.pixi.workspace]
channels = ["conda-forge"]
platforms = ["osx-arm64"]

[tool.pixi.pypi-dependencies]
pixi_py = { path = ".", editable = true }

[tool.pixi.tasks]
```

Example 4 (unknown):
```unknown
# Main pixi entry
[tool.pixi.workspace]
channels = ["conda-forge"]
# This is your machine platform by default
platforms = ["osx-arm64"]
```

---

## Import Environments

**URL:** https://pixi.sh/latest/tutorials/import/

**Contents:**
- Import Environments
- pixi import#
  - conda-env format#
  - pypi-txt format#
- pixi init --import#
- Conclusion#

In this tutorial we will show you how to import existing environments into a Pixi workspace. In case some words used in the tutorial don't make sense to you, you may get value from first reading some of our other tutorials, like our first workspace walthrough and our guide to multi-environment workspaces.

Within any Pixi workspace, you can use pixi import to import an environment from a given file. At the time of writing, we support two import file formats: conda-env and pypi-txt. Running pixi import without providing a format will try each format in turn until one succeeds, or return an error if all formats fail.

If you don't already have a Pixi workspace, you can create one with pixi init.

The conda-env format is for files in the conda ecosystem (typically called environment.yml) following the syntax specified in the conda docs. Suppose our environment to import is specified in this file:

We can then run pixi import --format=conda-env environment.yml to import the environment into our workspace. By default, since our environment.yml has a name field, this creates a feature of the same name (or uses the feature of that name if it already exists), and creates an environment containing that feature (with no-default-feature set):

It is then possible to define tasks for that environment, run commands in that environment, and launch a pixi shell in that environment — see the getting started guide for links to start learning about these topics!

For files without a name field, or to override the default behaviour, you can specify custom --feature and --environment names. This also allows importing into existing features and environments (including the default feature and environment). For example, given this other environment file to import:

Running pixi import --format=conda-env --feature=numpy --environment=simple-env env2.yml will import the environment into a new feature called "numpy", and include that feature in the existing simple-env environment (effectively merging the environments from our two input files):

It is also possible to specify platforms for the feature via the --platform argument. For example, pixi import --format=conda-env --feature=unix --platform=linux-64 --platform=osx-arm64 environment.yml adds the following to our workspace manifest:

The pypi-txt format is for files in the PyPI ecosystem following the requirements file format specification in the pip docs.

Suppose our environment to import is specified in this file:

We can then run pixi import --format=pypi-txt --feature=my-feature1 requirements.txt to import the environment into our workspace. It is necessary to specify a feature or environment name (or both) via the arguments of the same names. If only one of these names is provided, a matching name is used for the other field. Hence, the following lines are added to our workspace manifest:

Any dependencies listed in the file are added as pypi-dependencies. An environment will be created with no-default-feature set if the given environment name does not already exist.

It is then possible to define tasks for that environment, run commands in that environment, and launch a pixi shell in that environment — see the getting started guide for links to start learning about these topics!

Just like the conda-env format, it is possible to import into existing features/environments (including the default feature/environment), and set specific platforms for the feature. See the previous section for details.

It is also possible to combine the steps of pixi init and pixi import into one, via pixi init --import. For example, pixi init --import environment.yml (using the same file from our example above) produces a manifest which looks like this:

Unlike pixi import, this by default uses the default feature and environment. Thus, it achieves a very similar workspace to that obtained by running pixi init and pixi import --feature=default environment.yml.

One difference is that pixi init --import will by default inherit its name from the given import file (if the file specifies the name field), rather than from its working directory.

At the time of writing, only the conda-env format is supported by pixi init --import.

For further details, please see the CLI reference documentation for pixi import and pixi init --import. If there are any questions, or you know how to improve this tutorial, feel free to reach out to us on GitHub.

At the time of writing, there are plans for many potential extensions to our import capabilities — you can follow along with that work at the import roadmap issue on GitHub.

**Examples:**

Example 1 (unknown):
```unknown
name: simple-env
channels: ["conda-forge"]
dependencies:
- python
- pip:
  - httpx
```

Example 2 (unknown):
```unknown
[feature.simple-env]
channels = ["conda-forge"]

[feature.simple-env.dependencies]
python = "*"

[feature.simple-env.pypi-dependencies]
httpx = "*"

[environments]
simple-env = { features = ["simple-env"], no-default-feature = true }
```

Example 3 (unknown):
```unknown
channels: ["conda-forge"]
dependencies:
- numpy
```

Example 4 (unknown):
```unknown
[feature.simple-env]
channels = ["conda-forge"]

[feature.simple-env.dependencies]
python = "*"

[feature.simple-env.pypi-dependencies]
httpx = "*"

[feature.numpy]
channels = ["conda-forge"]

[feature.numpy.dependencies]
numpy = "*"

[environments]
simple-env = { features = ["simple-env", "numpy"], no-default-feature = true }
```

---
