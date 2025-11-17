---
description: MCP integration workflow - Lucy connects GPT Researcher to Model Context Protocol servers for specialized data sources
globs: ""
alwaysApply: false
---

# 🔌 MCP INTEGRATION WORKFLOW

**YOU (Lucy) are reading this because the user needs specialized data sources via MCP.**

## 🎯 YOUR MISSION

Integrate GPT Researcher with MCP servers to access:
- GitHub repositories
- Custom databases
- Enterprise APIs
- Specialized tools
- Multi-source intelligence

## ⚡ WHEN TO USE THIS WORKFLOW

**User mentions:**
- "Research using GitHub"
- "Query our database"
- "Use custom API for research"
- "MCP research"
- Any mention of specialized data sources

**Best for:**
- Code repository analysis
- Enterprise knowledge bases
- Custom tool integrations
- Multi-domain research

## 🏗️ MCP ARCHITECTURE

```
GPTResearcher
     ↓
MCP Integration Layer
     ├─ Stage 1: Tool Selection (LLM analyzes + selects)
     └─ Stage 2: Execution (LLM generates args + executes)
     ↓
MCP Servers
     ├─ GitHub
     ├─ Tavily
     ├─ Custom Database
     └─ Other APIs
```

## 📋 CRITICAL CONFIGURATION

### Step 1: Enable MCP in Environment

**MUST SET RETRIEVER:**
```python
import os

# CRITICAL: MCP won't work without this
os.environ['RETRIEVER'] = 'mcp'          # Pure MCP
# OR
os.environ['RETRIEVER'] = 'tavily,mcp'   # Hybrid (recommended)
```

**Without RETRIEVER=mcp, MCP configs are ignored!**

### Step 2: Configure MCP Servers

**Single MCP Server Example (GitHub):**
```python
mcp_configs = [
    {
        "name": "github",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
            "GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_TOKEN")
        }
    }
]
```

**Multi-Server Example (Comprehensive):**
```python
mcp_configs = [
    # Financial data
    {
        "name": "financial",
        "command": "python",
        "args": ["financial_mcp_server.py"],
        "env": {
            "ALPHA_VANTAGE_KEY": os.getenv("ALPHA_KEY")
        }
    },
    # News/sentiment
    {
        "name": "tavily",
        "command": "npx",
        "args": ["-y", "tavily-mcp@0.1.2"],
        "env": {
            "TAVILY_API_KEY": os.getenv("TAVILY_KEY")
        }
    },
    # Code/technical
    {
        "name": "github",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
            "GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_TOKEN")
        }
    }
]
```

### Step 3: Initialize with MCP

```python
from gpt_researcher import GPTResearcher

researcher = GPTResearcher(
    query="Analyze Tesla's Q4 2024 performance",
    report_type="research_report",
    mcp_configs=mcp_configs,  # Provide MCP configurations
    verbose=True
)
```

### Step 4: Execute MCP Research

```python
print("🔌 Starting MCP-integrated research...")
print(f"   MCP Servers: {len(mcp_configs)}")
print("   Stage 1: LLM selects relevant tools...")
print("   Stage 2: LLM executes with generated args...\n")

await researcher.conduct_research()
```

**Two-Stage Process:**

**Stage 1 - Intelligent Tool Selection:**
- LLM analyzes research query
- LLM reviews available MCP servers
- LLM selects most relevant tools
- Automatic, no manual tool specification needed

**Stage 2 - Contextual Execution:**
- LLM generates query-specific arguments
- LLM executes selected tools
- LLM processes tool outputs
- LLM integrates into research

### Step 5: Generate MCP Report

```python
print("✍️  Synthesizing MCP + web results...\n")

report = await researcher.write_report()

print("=" * 80)
print("MCP RESEARCH REPORT")
print("=" * 80)
print(f"MCP Servers Used: {len(mcp_configs)}")
print("=" * 80)
print(report)
```

## 🎛️ MCP STRATEGIES

### Fast Strategy (Default)

```python
os.environ['MCP_STRATEGY'] = 'fast'
```

- Run MCP once with main query
- Quick results
- Good for most use cases
- Duration similar to standard research

### Deep Strategy

```python
os.environ['MCP_STRATEGY'] = 'deep'
```

- Run MCP for all sub-queries
- Comprehensive coverage
- 2-3x longer duration
- More API calls to MCP servers

### Disabled Strategy

```python
os.environ['MCP_STRATEGY'] = 'disabled'
```

- Skip MCP entirely
- Use for debugging
- Falls back to web-only

## 🔧 MCP CONFIGURATION PATTERNS

### Remote MCP Server

```python
{
    "name": "arxiv_api",
    "connection_url": "wss://mcp.arxiv.org/ws",  # WebSocket URL
    "connection_token": os.getenv("ARXIV_TOKEN")
}
```

### Auto Tool Selection

```python
os.environ['MCP_AUTO_TOOL_SELECTION'] = 'true'

# For servers with multiple tools
# LLM automatically chooses best tool
```

### Connection Types

GPT Researcher auto-detects:
- `wss://` → WebSocket
- `https://` → HTTP
- Command + args → Stdio (default)

## ⚠️ TROUBLESHOOTING MCP

### "No retriever specified"

```python
# SOLUTION: Must set RETRIEVER
os.environ['RETRIEVER'] = 'mcp'
# Verify
assert os.getenv('RETRIEVER') == 'mcp'
```

### "No MCP server configurations found"

```python
# SOLUTION: Ensure mcp_configs is non-empty list
assert isinstance(mcp_configs, list)
assert len(mcp_configs) > 0
```

### "MCP server connection failed"

```python
# Diagnostic steps:
# 1. Test server independently
import subprocess
result = subprocess.run(
    ["npx", "-y", "@modelcontextprotocol/server-github"],
    capture_output=True
)
print(result.stderr)

# 2. Verify env vars
assert os.getenv("GITHUB_TOKEN"), "Missing GITHUB_TOKEN"

# 3. Check network
import requests
response = requests.get("https://api.github.com")
assert response.status_code == 200
```

### "No tools available"

```python
# SOLUTION: Enable auto tool selection
os.environ['MCP_AUTO_TOOL_SELECTION'] = 'true'

# Or verify server exposes tools correctly
```

## 🎯 COMPLETE EXAMPLE

```python
from gpt_researcher import GPTResearcher
import asyncio
import os

async def mcp_research(query: str) -> str:
    """Execute research using MCP servers."""

    # CRITICAL: Enable MCP
    os.environ['RETRIEVER'] = 'tavily,mcp'  # Hybrid
    os.environ['MCP_STRATEGY'] = 'fast'

    # Configure MCP servers
    mcp_configs = [
        {
            "name": "github",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"],
            "env": {
                "GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_TOKEN")
            }
        }
    ]

    # Verify environment
    assert os.getenv("GITHUB_TOKEN"), "Missing GITHUB_TOKEN"

    # Initialize
    researcher = GPTResearcher(
        query=query,
        report_type="research_report",
        mcp_configs=mcp_configs,
        verbose=True
    )

    # Execute
    print("🔌 MCP Research Starting...\n")
    await researcher.conduct_research()

    print("\n✍️  Generating report...\n")
    report = await researcher.write_report()

    # Results
    print("=" * 80)
    print("MCP RESEARCH COMPLETED")
    print("=" * 80)
    print(report)

    return report

# Execute
if __name__ == "__main__":
    query = input("MCP research query: ")
    report = asyncio.run(mcp_research(query))
```

## 📚 RELATED WORKFLOWS

- **quick-research.md** - Add MCP to standard research
- **deep-research.md** - Combine MCP + deep mode
- **hybrid-research.md** - MCP + local docs

---

**END OF WORKFLOW** - MCP integration complete.
