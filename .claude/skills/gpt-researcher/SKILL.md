---
name: gpt-researcher
description: |
  GPT Researcher - Autonomous AI research agent that conducts deep research and generates comprehensive reports with citations.
  USE WHEN user says "research", "do research", "investigate", "write report", "analyze topic", "deep research", "multi-agent research".
  Supports web scraping, local documents, multi-agent workflows, and automated research generation.
---

# GPT Researcher Skill

Comprehensive assistance with gpt-researcher - an autonomous LLM agent for deep research with citations and multi-format report generation.

## When to Use This Skill

This skill activates when user says:
- "Do research on [topic]"
- "Investigate [subject]"
- "Write a research report about [topic]"
- "Analyze the latest developments in [field]"
- "Deep research on [topic]"
- "Multi-agent research"
- "Research local documents"
- "Generate research report with citations"
- "Hybrid research" (web + local documents)
- "MCP research" (using Model Context Protocol)
- Working with GPT Researcher API
- Setting up autonomous research workflows

## Quick Reference

### Basic Research Patterns

**Simple Research:**
```python
from gpt_researcher import GPTResearcher
import asyncio

async def main():
    researcher = GPTResearcher(
        query="What are the latest developments in quantum computing?",
        report_type="research_report"
    )
    research_data = await researcher.conduct_research()
    report = await researcher.write_report()
    print(report)

if __name__ == "__main__":
    asyncio.run(main())
```

**Deep Research (NEW - Tree-Like Exploration):**
```python
# Takes ~5 minutes, costs ~$0.4 using o3-mini
researcher = GPTResearcher(
    query="What are the latest developments in quantum computing?",
    report_type="deep",  # Enables deep research mode
)
research_data = await researcher.conduct_research()
report = await researcher.write_report()
```

**Configuration for Deep Research:**
```bash
# Environment variables
export DEEP_RESEARCH_BREADTH=4      # Parallel paths at each level
export DEEP_RESEARCH_DEPTH=2        # How many levels deep
export DEEP_RESEARCH_CONCURRENCY=4  # Max concurrent operations
export TOTAL_WORDS=2500             # Total words in report
```

### Research Sources

**Web Research (Default):**
```bash
# Set retriever
export RETRIEVER=tavily  # Default

# Multiple retrievers
export RETRIEVER=tavily,arxiv,google
```

**Research on Specific URLs:**
```python
researcher = GPTResearcher(
    query="What are the biggest trends in AI lately?",
    report_type="research_report",
    source_urls=[
        "https://en.wikipedia.org/wiki/Artificial_intelligence",
        "https://www.ibm.com/think/insights/artificial-intelligence-trends"
    ],
    complement_source_urls=False  # Only use provided URLs
)
```

**Local Document Research:**
```bash
# Step 1: Set document path
export DOC_PATH="./my-docs"
```

```python
# Step 2: Use local report source
researcher = GPTResearcher(
    query="What can you tell me about my documents?",
    report_source="local"  # "local", "web", or "hybrid"
)
```

**Hybrid Research (Web + Local):**
```python
researcher = GPTResearcher(
    query="How does our product compare to market trends?",
    report_type="research_report",
    report_source="hybrid"  # Combines web + local docs
)
```

**LangChain Documents:**
```python
from langchain_core.documents import Document

# Use documents from LangChain retriever
researcher = GPTResearcher(
    query="What can you tell me about blue cheese?",
    report_type="research_report",
    report_source="langchain_documents",
    documents=langchain_documents  # List[Document]
)
```

### MCP Integration (Model Context Protocol)

**Enable MCP:**
```bash
# CRITICAL: Must set RETRIEVER to enable MCP
export RETRIEVER=mcp              # Pure MCP research
export RETRIEVER=tavily,mcp       # Hybrid (recommended)
```

**Basic MCP Configuration:**
```python
import os
os.environ["RETRIEVER"] = "tavily,mcp"

researcher = GPTResearcher(
    query="How does React's useState hook work?",
    mcp_configs=[
        {
            "name": "github_api",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"],
            "env": {"GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")}
        }
    ]
)
```

**Multi-Server MCP (Comprehensive Research):**
```python
os.environ["RETRIEVER"] = "tavily,google,mcp"

researcher = GPTResearcher(
    query="Analyze Tesla's Q4 2024 performance",
    mcp_configs=[
        # Financial data
        {
            "name": "financial_data",
            "command": "python",
            "args": ["financial_mcp_server.py"],
            "env": {"ALPHA_VANTAGE_KEY": os.getenv("ALPHA_VANTAGE_KEY")}
        },
        # News research
        {
            "name": "tavily",
            "command": "npx",
            "args": ["-y", "tavily-mcp@0.1.2"],
            "env": {"TAVILY_API_KEY": os.getenv("TAVILY_API_KEY")}
        },
        # GitHub/technical
        {
            "name": "github",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"],
            "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_TOKEN")}
        }
    ]
)
```

### Retriever Configuration

**Available Retrievers:**
- `tavily` - Default web search (requires TAVILY_API_KEY)
- `google` - Google search (requires GOOGLE_API_KEY)
- `bing` - Bing search (requires BING_API_KEY)
- `arxiv` - Academic papers
- `semantic_scholar` - Academic research
- `pubmed_central` - Medical research
- `exa` - Deep web search
- `searx` - Privacy-focused metasearch
- `duckduckgo` - Privacy-focused search
- `mcp` - Model Context Protocol servers

**Multiple Retrievers (Hybrid Strategy):**
```bash
export RETRIEVER=tavily,arxiv,semantic_scholar,mcp
```

### LLM Configuration

**Supported LLMs:**
```bash
# OpenAI (default)
export FAST_LLM=openai:gpt-4o-mini
export SMART_LLM=openai:gpt-4o
export STRATEGIC_LLM=openai:o4-mini

# Anthropic
export ANTHROPIC_API_KEY=[Your Key]
export FAST_LLM=anthropic:claude-2.1
export SMART_LLM=anthropic:claude-3-opus-20240229

# Azure OpenAI
export AZURE_OPENAI_API_KEY=[Your Key]
export FAST_LLM=azure_openai:gpt-4o-mini
export SMART_LLM=azure_openai:gpt-4o

# Ollama (local)
export OLLAMA_BASE_URL=http://localhost:11434
export FAST_LLM=ollama:llama3
export SMART_LLM=ollama:llama3
export EMBEDDING=ollama:nomic-embed-text

# Groq (fast inference)
export GROQ_API_KEY=[Your Key]
export FAST_LLM=groq:Mixtral-8x7b-32768
export SMART_LLM=groq:Mixtral-8x7b-32768
```

### Custom Agent Prompts

**Specify Custom Research Instructions:**
```python
researcher = GPTResearcher(
    query="Research the latest advancements in AI and provide a detailed report in APA format including sources.",
    report_type="custom_report"  # Use custom_report type
)
```

### Report Types

- `research_report` - Comprehensive research report
- `outline_report` - Research outline
- `resource_report` - List of resources
- `custom_report` - Custom prompt-based report
- `deep` - Deep research with tree exploration (NEW)

## Multi-Agent Research (LangGraph)

GPT Researcher supports multi-agent workflows using LangGraph for enhanced depth and quality.

**The Research Team (7 AI Agents):**
1. **Chief Editor** - Oversees process and manages team
2. **Researcher** (gpt-researcher) - Conducts deep research
3. **Editor** - Plans outline and structure
4. **Reviewer** - Validates correctness
5. **Revisor** - Revises based on feedback
6. **Writer** - Compiles final report
7. **Publisher** - Publishes to multiple formats

**Quick Start:**
```bash
pip install gpt-researcher langgraph-cli

# Configure task.json
{
  "query": "Is AI in a hype cycle?",
  "model": "gpt-4o",
  "max_sections": 3,
  "publish_formats": {
    "markdown": true,
    "pdf": true,
    "docx": true
  },
  "follow_guidelines": true
}

# Run multi-agent research
python main.py
```

## Installation

```bash
pip install gpt-researcher

# Required API keys
export OPENAI_API_KEY=[Your Key]
export TAVILY_API_KEY=[Your Key]
```

## Key Environment Variables

```bash
# Essential
OPENAI_API_KEY=[Your Key]
TAVILY_API_KEY=[Your Key]
RETRIEVER=tavily,mcp              # Enable retrievers
DOC_PATH=./my-docs                # Local documents path

# Deep Research
DEEP_RESEARCH_BREADTH=4           # Parallel research paths
DEEP_RESEARCH_DEPTH=2             # Depth levels
DEEP_RESEARCH_CONCURRENCY=4       # Max concurrent ops
TOTAL_WORDS=2500                  # Report word count

# MCP Advanced
MCP_STRATEGY=fast                 # "fast" or "deep"
MCP_AUTO_TOOL_SELECTION=true      # Auto tool selection
```

## Common Troubleshooting

**"No retriever specified" or "MCP not working":**
- Solution: Set `RETRIEVER=mcp` or `RETRIEVER=tavily,mcp`
- Verify: `echo $RETRIEVER`

**"MCP server connection failed":**
- Verify server command and arguments
- Check environment variables are set
- Test MCP server independently

**"No tools available from MCP server":**
- Enable `MCP_AUTO_TOOL_SELECTION=true`
- Check server startup logs

## Best Practices

1. **Always set RETRIEVER environment variable** for MCP functionality
2. **Use hybrid strategies** (`tavily,mcp`) for comprehensive research
3. **Store sensitive data** in environment variables
4. **Test MCP servers independently** before integration
5. **Enable verbose mode** during development
6. **Choose appropriate retriever combinations** based on research domain
7. **Use deep research** for complex topics requiring thorough analysis
8. **Leverage multi-agent workflows** for publication-quality reports

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **core_concepts.md** - Architecture, retrievers, LLMs, MCP integration (98 KB)
- **examples.md** - Code examples and usage patterns
- **features.md** - Feature descriptions and capabilities
- **getting_started.md** - Installation and quick start
- **other.md** - Additional utilities and tools

**Access reference files:**
```
Read /Users/michaelatherton/Documents/condaEnv/AIRL/PAI/.claude/skills/gpt-researcher/references/[filename].md
```

## Working with This Skill

### For Beginners
Start with `getting_started.md` for installation and basic usage.

### For Specific Features
- Deep Research → `core_concepts.md` (Deep Research section)
- MCP Integration → `core_concepts.md` (MCP Integration section)
- Multi-Agent → `examples.md` (LangGraph section)
- LLM Configuration → `core_concepts.md` (LLM Providers section)

### For Code Examples
The quick reference section above contains essential patterns. For advanced examples, see `examples.md`.

## Important Notes

- **Deep Research** uses reasoning models (o3-mini) and takes ~5 minutes
- **MCP Integration** requires `RETRIEVER=mcp` or hybrid strategy
- **Multi-Agent Workflows** generate 5-6 page reports in multiple formats
- **Hybrid Research** combines web + local documents for comprehensive insights
- **Cost Optimization** - Use `FAST_LLM` for speed, `SMART_LLM` for quality
- **Local LLMs Supported** - Can run entirely offline with Ollama

## Available Workflows

**For step-by-step execution instructions, see workflows/ directory:**

### Essential Workflows
- **quick-research.md** - Standard web-only research (1-3 min, $0.05-$0.15)
- **deep-research.md** - Comprehensive tree exploration (5-10 min, $0.30-$0.50)
- **hybrid-research.md** - Web + local/online documents (2-5 min, $0.15-$0.30)

### Advanced Workflows
- **mcp-integration.md** - Model Context Protocol sources
- **custom-report.md** - Custom format generation (executive, bullets, APA, etc.)
- **multi-agent.md** - LangGraph 7-agent publication-quality reports
- **cost-optimization.md** - Budget-conscious research ($0.03-$0.05)
- **troubleshooting.md** - Debug and fix common issues

**To execute a workflow:**
```
Read /Users/michaelatherton/Documents/condaEnv/AIRL/PAI/.claude/skills/gpt-researcher/workflows/[workflow-name].md
```

Each workflow provides executable step-by-step instructions for Lucy to follow.

## Related Skills

- Use with **perplexity-researcher** skill for web-first research
- Use with **fabric** skill to process/extract from research outputs
- Combine with **MCP servers** for specialized domain research
- Integrate with **LangChain** for custom retrieval workflows

## Supplementary Resources

**For Comprehensive Deep Context:**
```
Read /Users/michaelatherton/Documents/condaEnv/AIRL/PAI/.claude/skills/gpt-researcher/CLAUDE.md
```

CLAUDE.md contains:
- Complete architecture and component documentation
- Detailed methodology for all 5 research modes
- Advanced configuration guide
- Comprehensive troubleshooting decision trees
- Cost optimization strategies
- Performance tuning guide
- Integration patterns
- Security and privacy best practices
- Learning path from beginner to advanced

**For Runnable Examples:**
```
See /Users/michaelatherton/Documents/condaEnv/AIRL/PAI/.claude/skills/gpt-researcher/examples/
```

**For Configuration Templates:**
```
See /Users/michaelatherton/Documents/condaEnv/AIRL/PAI/.claude/skills/gpt-researcher/templates/config.yaml
```

**For Reference Documentation:**
```
See /Users/michaelatherton/Documents/condaEnv/AIRL/PAI/.claude/skills/gpt-researcher/references/
```

## Updating This Skill

To refresh with updated documentation:
1. Re-run the scraper with same configuration
2. Skill rebuilds with latest information

---

This skill was automatically generated from official GPT Researcher documentation and enhanced for PAI integration.
