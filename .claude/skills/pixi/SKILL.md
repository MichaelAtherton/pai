---
name: pixi
description: |
  Pixi package manager expertise - Fast, modern, reproducible package management for Python, Rust, Node.js, ROS2.
  USE WHEN user says "install pixi", "pixi command", "manage environments with pixi", "pixi tasks", "pixi global install".
  This is Michael's PRIMARY package manager for both Python and JS/TS projects.
---

# Pixi Package Manager Skill

Comprehensive assistance with pixi development and package management, generated from official documentation.

## When to Use This Skill

This skill activates when user says:
- "Install/add packages with pixi"
- "Create pixi environment"
- "Run pixi tasks"
- "Set up pixi project"
- "Pixi global install"
- "Manage conda/PyPI packages"
- "Pixi configuration"
- "Debug pixi issues"
- "Pixi best practices"
- Working with pixi.toml or pixi.lock files
- Cross-platform environment setup

## Quick Reference

### Common Patterns

**Global Package Management:**
```bash
# Install global tools
pixi global install python

# Uninstall global packages
pixi global uninstall pixi-pack rattler-build

# Remove from specific environment
pixi global remove --environment python numpy

# Expose commands with custom names
pixi global expose add python310=python3.10 python3=python3 --environment myenv
```

**Project Package Management:**
```bash
# Add dependencies
pixi add python=3.9

# Add PyPI packages
pixi add --pypi requests

# Add to specific feature/environment
pixi add --feature test pytest
```

**Configuration:**
```bash
# Set default channels
pixi config set default-channels '["conda-forge", "bioconda"]'
```

**Virtual Packages:**
In the Conda ecosystem, virtual packages represent system capabilities:
- `__cuda` - CUDA drivers present on host
- `__glibc` - System glibc version
- `__osx` - macOS version
- These aren't installed but used in dependency resolution

**PyPI Configuration:**
```toml
[pypi-options]
index-url = "https://pypi.org/simple"
extra-index-urls = ["https://example.com/simple"]
find-links = [{path = './links'}]
```

**Channel to PyPI Mapping:**
Map conda package names to PyPI equivalents in JSON format:
```json
{
  "conda_name": "pypi_package_name"
}
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **building.md** - Building and packaging workflows
- **concepts.md** - Core pixi concepts and architecture
- **getting_started.md** - Installation and first steps
- **integration.md** - IDE and tool integration
- **other.md** - Additional features and utilities
- **reference.md** - Complete CLI and config reference
- **tutorials.md** - Step-by-step guides

**Access reference files:**
```
Read /Users/michaelatherton/Documents/condaEnv/AIRL/PAI/.claude/skills/pixi/references/[filename].md
```

## Working with This Skill

### For Beginners
Start with `getting_started.md` or `tutorials.md` for foundational concepts.

### For Specific Features
Use the appropriate category reference file for detailed information:
- Commands → `reference.md`
- Concepts → `concepts.md`
- Integration → `integration.md`

### For Code Examples
The quick reference section above contains common patterns extracted from official docs.

## Important Notes

- **Michael's Primary Package Manager**: Pixi is the preferred tool for all Python and JS/TS projects
- **Mixed Dependencies**: Can handle both conda and PyPI packages in same environment
- **Cross-Platform**: Same pixi.toml works across macOS, Linux, Windows
- **Reproducible**: pixi.lock ensures exact same environment everywhere
- **Fast**: Uses rattler (Rust-based) for blazing fast solves

## Updating This Skill

To refresh with updated documentation:
1. Re-run the scraper with same configuration
2. Skill rebuilds with latest information

## Resources

### references/
Organized documentation extracted from official sources containing:
- Detailed explanations
- Code examples with syntax highlighting
- Links to original documentation
- Table of contents for navigation

### Future Enhancements
- `scripts/` - Helper scripts for common automation
- `assets/` - Templates, boilerplate, example projects
