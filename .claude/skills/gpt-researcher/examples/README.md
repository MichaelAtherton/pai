# GPT Researcher - Example Scripts

This directory contains runnable example scripts demonstrating various GPT Researcher capabilities.

## Available Examples

### 1. Simple Run (`simple_run.py`)

The most basic example - demonstrates straightforward research workflow.

**What it does:**
- Initializes GPTResearcher
- Conducts web research
- Generates a research report

**Usage:**
```bash
python simple_run.py
```

**Best for:**
- Getting started with GPT Researcher
- Quick research tasks
- Understanding basic workflow

---

### 2. Custom Prompts (`custom_prompt.py`)

Demonstrates how to customize report formatting and style using custom prompts.

**What it does:**
- Generates standard research reports
- Creates concise summaries
- Produces bullet-point reports
- Makes executive briefs
- Generates technical analyses
- Creates comparison reports

**Usage:**
```bash
python custom_prompt.py
```

**Best for:**
- Tailoring report format to specific needs
- Creating different output styles
- Executive summaries vs. detailed reports

---

### 3. Detailed Report (`detailed_report.py`)

Shows how to generate comprehensive, multi-section reports on complex topics.

**What it does:**
- Breaks down complex topics into subtopics
- Conducts focused research on each section
- Prevents content duplication
- Generates table of contents automatically
- Includes proper citations

**Usage:**
```bash
python detailed_report.py
```

**Best for:**
- Academic research papers
- Business intelligence reports
- Market analysis documents
- Technical documentation
- Industry trend reports

---

### 4. Hybrid Research - Local Documents (`hybrid_local.py`)

Combines web search with local document analysis for comprehensive research.

**What it does:**
- Analyzes documents from `./my-docs` directory
- Conducts web research
- Synthesizes insights from both sources
- Processes documents locally (privacy-safe)

**Usage:**
```bash
# Prepare documents
mkdir -p my-docs
cp /path/to/your/documents/*.pdf my-docs/

# Run research
python hybrid_local.py
```

**Best for:**
- Combining internal documents with market research
- Product roadmap vs. market trends analysis
- Internal policy review with industry standards
- Competitive analysis using proprietary data

---

### 5. Hybrid Research - Online Documents (`hybrid_online.py`)

Combines web search with specific online document URLs.

**What it does:**
- Fetches and analyzes online documents from URLs
- Conducts additional web research
- Synthesizes findings from all sources

**Usage:**
```bash
python hybrid_online.py
```

**Best for:**
- Research using public company reports
- Academic research from published papers
- Market analysis using industry whitepapers
- Technical research from documentation sites

---

## Prerequisites

### Installation

```bash
pip install gpt-researcher
```

### API Keys

Set required environment variables:

```bash
# OpenAI (or other LLM provider)
export OPENAI_API_KEY=your_openai_api_key

# Tavily (or other search provider)
export TAVILY_API_KEY=your_tavily_api_key
```

### Optional Configuration

For advanced configuration, see `../templates/config.yaml`

---

## Quick Start Guide

### 1. Set Up Environment

```bash
# Clone or navigate to skill directory
cd .claude/skills/gpt-researcher

# Install dependencies
pip install gpt-researcher

# Set API keys
export OPENAI_API_KEY=your_key
export TAVILY_API_KEY=your_key
```

### 2. Run Your First Example

```bash
cd examples
python simple_run.py
```

### 3. Explore Other Examples

```bash
# Try custom prompts
python custom_prompt.py

# Generate detailed report
python detailed_report.py

# Test hybrid research
python hybrid_local.py
```

---

## Example Comparison

| Example | Complexity | Duration | Output | Best Use Case |
|---------|-----------|----------|--------|---------------|
| `simple_run.py` | ⭐ Basic | 1-2 min | Standard report | Quick research |
| `custom_prompt.py` | ⭐⭐ Intermediate | 1-3 min | Custom format | Tailored outputs |
| `detailed_report.py` | ⭐⭐⭐ Advanced | 3-5 min | Multi-section | Comprehensive analysis |
| `hybrid_local.py` | ⭐⭐⭐ Advanced | 2-5 min | Hybrid report | Internal + external |
| `hybrid_online.py` | ⭐⭐⭐ Advanced | 2-5 min | Hybrid report | Specific sources |

---

## Cost Estimates

Typical costs using GPT-4:

- **Simple Run**: $0.05 - $0.10 per research
- **Custom Prompt**: $0.05 - $0.15 per research
- **Detailed Report**: $0.20 - $0.40 per research
- **Hybrid Research**: $0.15 - $0.30 per research

*Costs can be reduced significantly by using gpt-4o-mini*

---

## Customization Guide

### Modify Research Query

Edit the `query` variable in any example:

```python
query = "Your custom research question here"
```

### Change Report Type

```python
report_type = "research_report"  # Standard
report_type = "outline_report"   # Outline only
report_type = "resource_report"  # Resources list
report_type = "custom_report"    # Custom format
report_type = "deep"             # Deep research
```

### Adjust Report Source

```python
report_source = "web"      # Web only
report_source = "local"    # Local docs only
report_source = "hybrid"   # Both
```

### Use Custom Configuration

```python
researcher = GPTResearcher(
    query=query,
    report_type=report_type,
    config_path="../templates/config.yaml"
)
```

---

## Troubleshooting

### API Key Not Found

```bash
# Check if variables are set
echo $OPENAI_API_KEY
echo $TAVILY_API_KEY

# Set if missing
export OPENAI_API_KEY=your_key
export TAVILY_API_KEY=your_key
```

### Module Not Found

```bash
# Install or reinstall
pip install --upgrade gpt-researcher
```

### Documents Not Loading (Hybrid Research)

```bash
# Check document path exists
ls -la my-docs/

# Verify DOC_PATH is set
echo $DOC_PATH

# Create if missing
mkdir -p my-docs
```

### Rate Limiting

If you hit rate limits:
- Reduce `max_iterations` in config
- Use `gpt-4o-mini` instead of `gpt-4o`
- Add delays between requests
- Check API usage quotas

---

## Advanced Usage

### Using Different LLMs

```bash
# Anthropic Claude
export ANTHROPIC_API_KEY=your_key
export FAST_LLM="anthropic:claude-3-haiku"
export SMART_LLM="anthropic:claude-3-opus"

# Local Ollama
export OLLAMA_BASE_URL="http://localhost:11434"
export FAST_LLM="ollama:llama3"
export SMART_LLM="ollama:llama3"

# Groq (fast inference)
export GROQ_API_KEY=your_key
export FAST_LLM="groq:mixtral-8x7b-32768"
```

### Using Different Retrievers

```bash
# Google Search
export GOOGLE_API_KEY=your_key
export RETRIEVER="google"

# Academic sources
export RETRIEVER="arxiv,semantic_scholar"

# Multiple sources
export RETRIEVER="tavily,google,arxiv"
```

### Deep Research

Modify any example to use deep research:

```python
researcher = GPTResearcher(
    query=query,
    report_type="deep",  # Enable deep research
)

# Configure depth
os.environ['DEEP_RESEARCH_BREADTH'] = '6'
os.environ['DEEP_RESEARCH_DEPTH'] = '3'
```

---

## Resources

- **Main Documentation**: [docs.gptr.dev](https://docs.gptr.dev)
- **GitHub Repository**: [github.com/assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
- **Discord Community**: [discord.gg/QgZXvJAccX](https://discord.gg/QgZXvJAccX)
- **Skill Reference**: `../references/examples.md`
- **Configuration Template**: `../templates/config.yaml`

---

## Contributing

Found a bug or want to add an example?
1. Check existing examples in this directory
2. Follow the established pattern
3. Add documentation to this README
4. Test thoroughly before sharing

---

## License

These examples are part of the gpt-researcher skill for PAI and follow the same license as GPT Researcher (Apache 2.0).
