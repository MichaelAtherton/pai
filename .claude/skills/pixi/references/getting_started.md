# Pixi - Getting Started

**Pages:** 2

---

## Pytorch Installation

**URL:** https://pixi.sh/latest/python/pytorch/

**Contents:**
- Pytorch Installation
- Overview#
- System requirements#
- Installing from Conda-forge#
- Installing from PyPi#
  - Pytorch index#
  - Mixing MacOS and CUDA with pypi-dependencies#
- Installing from PyTorch channel#
- Troubleshooting#
    - Testing the pytorch installation#

This guide explains how to integrate PyTorch with pixi, it supports multiple ways of installing PyTorch.

With these options you can choose the best way to install PyTorch based on your requirements.

In the context of PyTorch, system requirements help Pixi understand whether it can install and use CUDA-related packages. These requirements ensure compatibility during dependency resolution.

The key mechanism here is the use of virtual packages like __cuda. Virtual packages signal the available system capabilities (e.g., CUDA version). By specifying system-requirements.cuda = "12", you are telling Pixi that CUDA version 12 is available and can be used during resolution.

Without setting the appropriate system-requirements.cuda, Pixi will default to installing the CPU-only versions of PyTorch and its dependencies.

A more in-depth explanation of system requirements can be found here.

You can install PyTorch using the conda-forge channel. These are the conda-forge community maintained builds of PyTorch. You can make direct use of the Nvidia provided packages to make sure the packages can work together.

To deliberately install a specific version of the cuda packages you can depend on the cuda-version package which will then be interpreted by the other packages during resolution. The cuda-version package constraints the version of the __cuda virtual package and cudatoolkit package. This ensures that the correct version of the cudatoolkit package is installed and the tree of dependencies is resolved correctly.

With conda-forge you can also install the cpu version of PyTorch. A common use-case is having two environments, one for CUDA machines and one for non-CUDA machines.

Running these environments then can be done with the pixi run command. pixi run --environment cpu python -c "import torch; print(torch.cuda.is_available())" pixi run -e gpu python -c "import torch; print(torch.cuda.is_available())"

Now you should be able to extend that with your dependencies and tasks.

Here are some links to notable packages:

Thanks to the integration with uv we can also install PyTorch from pypi.

Mixing [dependencies] and [pypi-dependencies]

When using this approach for the torch package, you should also install the packages that depend on torch from pypi. Thus, not mix the PyPI packages with Conda packages if there are dependencies from the Conda packages to the PyPI ones.

The reason for this is that our resolving is a two step process, first resolve the Conda packages and then the PyPI packages. Thus this can not succeed if we require a Conda package to depend on a PyPI package.

PyTorch packages are provided through a custom index, these are similar to Conda channels, which are maintained by the PyTorch team. To install PyTorch from the PyTorch index, you need to add the indexes to manifest. Best to do this per dependency to force the index to be used.

You can tell Pixi to use multiple environment for the multiple versions of PyTorch, either cpu or gpu.

Running these environments then can be done with the pixi run command. pixi run --environment cpu python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())" pixi run -e gpu python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"

When using pypi-dependencies, Pixi creates a “solve” environment to resolve the PyPI dependencies. This process involves installing the Conda dependencies first and then resolving the PyPI packages within that environment.

This can become problematic if you’re on a macOS machine and trying to resolve the CUDA version of PyTorch for Linux or Windows. Since macOS doesn’t support those environments, the Conda dependencies for CUDA will fail to install, preventing proper resolution.

Current Status: The Pixi maintainers are aware of this limitation and are actively working on a solution to enable cross-platform dependency resolution for such cases.

In the meantime, you may need to run the resolution process on a machine that supports CUDA, such as a Linux or Windows host.

This depends on the non-free main channel from Anaconda and mixing it with conda-forge can lead to conflicts.

This is the legacy way of installing pytorch, this will not be updated to later versions as pytorch has discontinued their channel.

When you had trouble figuring out why your PyTorch installation is not working, please share your solution or tips with the community by creating a PR to this documentation.

You can verify your PyTorch installation with this command: pixi run python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"

To check which CUDA version Pixi detects on your machine, run: pixi info

Example output: ... Virtual packages: __unix=0=0 : __linux=6.5.9=0 : __cuda=12.5=0 ...

If __cuda is missing, you can verify your system’s CUDA version using NVIDIA tools: nvidia-smi

To check the version of the CUDA toolkit installed in your environment: pixi run nvcc --version

Broken installations often result from mixing incompatible channels or package sources:

Mixing Conda Channels

Using both conda-forge and the legacy pytorch channel can cause conflicts. Choose one channel and stick with it to avoid issues in the installed environment.

Mixing Conda and PyPI Packages

If you install PyTorch from pypi, all packages that depend on torch must also come from PyPI. Mixing Conda and PyPI packages within the same dependency chain leads to conflicts.

If you see an error like this: ABI tag mismatch ├─▶ failed to resolve pypi dependencies ╰─▶ Because only the following versions of torch are available: torch<=2.5.1 torch==2.5.1+cpu and torch==2.5.1 has no wheels with a matching Python ABI tag, we can conclude that torch>=2.5.1,<2.5.1+cpu cannot be used. And because torch==2.5.1+cpu has no wheels with a matching platform tag and you require torch>=2.5.1, we can conclude that your requirements are unsatisfiable. This happens when the Python ABI tag (Application Binary Interface) doesn’t match the available PyPI wheels.

Platform tag mismatch ├─▶ failed to resolve pypi dependencies ╰─▶ Because only the following versions of torch are available: torch<=2.5.1 torch==2.5.1+cu124 and torch>=2.5.1 has no wheels with a matching platform tag, we can conclude that torch>=2.5.1,<2.5.1+cu124 cannot be used. And because you require torch>=2.5.1, we can conclude that your requirements are unsatisfiable. This occurs when the platform tag doesn’t match the PyPI wheels available to be installed.

Example Issue: torch==2.5.1+cu124 (CUDA 12.4) was attempted on an osx machine, but this version is only available for linux-64 and win-64.

Solution: - Use the correct PyPI index for your platform: - CPU-only: Use the cpu index for all platforms. - CUDA versions: Use cu124 for linux-64 and win-64.

Correct Indexes: - CPU: https://download.pytorch.org/whl/cpu - CUDA 12.4: https://download.pytorch.org/whl/cu124

This ensures PyTorch installations are compatible with your system’s platform and Python version.

**Examples:**

Example 1 (unknown):
```unknown
[workspace]
channels = ["https://prefix.dev/conda-forge"]
name = "pytorch-conda-forge"
platforms = ["linux-64", "win-64"]

[system-requirements]
cuda = "12.0"

[dependencies]
pytorch-gpu = "*"
```

Example 2 (unknown):
```unknown
[project]
name = "pytorch-conda-forge"

[tool.pixi.project]
channels = ["https://prefix.dev/conda-forge"]
platforms = ["linux-64"]

[tool.pixi.system-requirements]
cuda = "12.0"

[tool.pixi.dependencies]
pytorch-gpu = "*"
```

Example 3 (unknown):
```unknown
[dependencies]
pytorch-gpu = "*"
cuda-version = "12.6.*"
```

Example 4 (unknown):
```unknown
[tool.pixi.dependencies]
pytorch-gpu = "*"
cuda-version = "12.6.*"
```

---

## Installation

**URL:** https://pixi.sh/latest/installation/

**Contents:**
- Installation
- Update#
- Alternative Installation Methods#
  - Homebrew#
  - Windows Installer#
  - Winget#
  - Scoop#
  - Download From GitHub Releases#
  - Install From Source#
- Installer Script Options#

To install pixi you can run the following command in your terminal:

If your system doesn't have curl, you can use wget:

The above invocation will automatically download the latest version of pixi, extract it, and move the pixi binary to ~/.pixi/bin. The script will also extend the PATH environment variable in the startup script of your shell to include ~/.pixi/bin. This allows you to invoke pixi from anywhere.

The above invocation will automatically download the latest version of pixi, extract it, and move the pixi binary to %UserProfile%\.pixi\bin. The command will also add %UserProfile%\.pixi\bin to your PATH environment variable, allowing you to invoke pixi from anywhere.

Now restart your terminal or shell to make the installation effective.

You can check the installation sh script: download and the ps1: download. The scripts are open source and available on GitHub.

Don't forget to add autocompletion!

After installing Pixi, you can enable autocompletion for your shell. See the Autocompletion section below for instructions.

Updating is as simple as installing, rerunning the installation script gets you the latest version.

pixi self-update Or get a specific Pixi version using: pixi self-update --version x.y.z

If you've used a package manager like brew, mamba, conda, paru etc. to install pixi you must use the built-in update mechanism. e.g. brew upgrade pixi.

Although we recommend installing Pixi through the above method we also provide additional installation methods.

Pixi is available via homebrew. To install Pixi via homebrew simply run:

We provide an msi installer on our GitHub releases page. The installer will download Pixi and add it to the PATH.

Pixi is a single executable and can be run without any external dependencies. That means you can manually download the suitable archive for your architecture and operating system from our GitHub releases, unpack it and then use it as is. If you want pixi itself or the executables installed via pixi global to be available in your PATH, you have to add them manually. The executables are located in PIXI_HOME/bin.

pixi is 100% written in Rust, and therefore it can be installed, built and tested with cargo. To start using Pixi from a source build run:

We don't publish to crates.io anymore, so you need to install it from the repository. The reason for this is that we depend on some unpublished crates which disallows us to publish to crates.io.

or when you want to make changes use:

If you have any issues building because of the dependency on rattler checkout its compile steps.

The installation script has several options that can be manipulated through environment variables.

For example, on Apple Silicon, you can force the installation of the x86 version: curl -fsSL https://pixi.sh/install.sh | PIXI_ARCH=x86_64 bash Or set the version curl -fsSL https://pixi.sh/install.sh | PIXI_VERSION=v0.18.0 bash

The installation script has several options that can be manipulated through environment variables.

For example, set the version: $env:PIXI_VERSION='v0.18.0'; powershell -ExecutionPolicy Bypass -Command "iwr -useb https://pixi.sh/install.ps1 | iex"

To get autocompletion follow the instructions for your shell. Afterwards, restart the shell or source the shell config file.

Add the following to the end of ~/.bashrc: ~/.bashrceval "$(pixi completion --shell bash)"

Add the following to the end of ~/.zshrc:

Add the following to the end of Microsoft.PowerShell_profile.ps1. You can check the location of this file by querying the $PROFILE variable in PowerShell. Typically the path is ~\Documents\PowerShell\Microsoft.PowerShell_profile.ps1 or ~/.config/powershell/Microsoft.PowerShell_profile.ps1 on -Nix.

Add the following to the end of ~/.config/fish/config.fish:

Add the following to your Nushell config file (find it by running $nu.config-path in Nushell):

Add the following to the end of ~/.elvish/rc.elv:

Before un-installation you might want to delete any previous files pixi has installed.

**Examples:**

Example 1 (unknown):
```unknown
curl -fsSL https://pixi.sh/install.sh | sh
```

Example 2 (unknown):
```unknown
wget -qO- https://pixi.sh/install.sh | sh
```

Example 3 (unknown):
```unknown
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

Example 4 (unknown):
```unknown
pixi self-update
```

---
