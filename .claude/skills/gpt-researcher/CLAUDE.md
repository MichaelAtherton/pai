# GPT Researcher - Comprehensive Deep Context

**This is the comprehensive context file for the GPT Researcher skill. Load this when you need deep understanding of GPT Researcher's architecture, methodologies, and advanced usage patterns.**

---

## 🎯 PURPOSE & PHILOSOPHY

GPT Researcher is an autonomous AI research agent that conducts comprehensive research by:
1. Breaking down complex topics into manageable sub-queries
2. Gathering information from multiple sources in parallel
3. Synthesizing findings into coherent, cited reports
4. Optimizing for depth, accuracy, and objectivity

**Core Principles:**
- **Autonomy**: Minimal human intervention required
- **Parallelization**: Multiple research paths executed concurrently
- **Source Diversity**: Aggregates 20+ sources for objective conclusions
- **Citation Integrity**: All claims backed by verifiable sources
- **Privacy-First**: Local document processing never sends raw data externally

---

## 🏗️ ARCHITECTURE & COMPONENTS

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     USER QUERY                              │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│              GPTResearcher Instance                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Query Analyzer & Sub-Query Generator                │  │
│  └─────────────────┬────────────────────────────────────┘  │
│                    │                                        │
│    ┌───────────────┴───────────────┐                       │
│    │                               │                       │
│    ▼                               ▼                       │
│  ┌─────────────┐            ┌──────────────┐              │
│  │   WEB       │            │  LOCAL/MCP   │              │
│  │  RETRIEVER  │            │  RETRIEVER   │              │
│  └──────┬──────┘            └──────┬───────┘              │
│         │                          │                       │
│         │    ┌────────────────────┐│                       │
│         └────▶  SCRAPER/FETCHER   ◀┘                       │
│              └─────────┬──────────┘                        │
│                        │                                    │
│                        ▼                                    │
│              ┌──────────────────┐                          │
│              │  CONTEXT BUILDER │                          │
│              └─────────┬────────┘                          │
│                        │                                    │
│                        ▼                                    │
│              ┌──────────────────┐                          │
│              │   LLM PROCESSOR  │                          │
│              │  (SMART/FAST)    │                          │
│              └─────────┬────────┘                          │
│                        │                                    │
│                        ▼                                    │
│              ┌──────────────────┐                          │
│              │  REPORT WRITER   │                          │
│              └─────────┬────────┘                          │
└────────────────────────┼────────────────────────────────────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ FINAL REPORT  │
                 │ (MD/PDF/DOCX) │
                 └───────────────┘
```

### Core Components

#### 1. **GPTResearcher Class**
Main orchestrator that coordinates all research activities.

**Key Methods:**
- `conduct_research()` - Main research execution
- `write_report()` - Report generation with optional custom prompts
- `get_costs()` - Cost tracking

**Key Parameters:**
- `query` - Research question
- `report_type` - Output format type
- `report_source` - Data source selection
- `source_urls` - Specific URLs (optional)
- `document_urls` - Online documents (optional)
- `documents` - LangChain documents (optional)
- `mcp_configs` - MCP server configurations
- `config_path` - Custom configuration file
- `verbose` - Logging level

#### 2. **Retriever System**
Fetches information from various sources.

**Available Retrievers:**
- **tavily** - Default web search (recommended)
- **google** - Google Search API
- **bing** - Bing Search API
- **arxiv** - Academic papers
- **semantic_scholar** - Academic research
- **pubmed_central** - Medical/health research
- **exa** - Deep web search
- **searx** - Privacy-focused metasearch
- **duckduckgo** - Privacy-focused search
- **mcp** - Model Context Protocol servers
- **custom** - Enterprise custom retrievers

**Retriever Strategy:**
```python
# Single retriever
RETRIEVER="tavily"

# Multiple retrievers (hybrid)
RETRIEVER="tavily,arxiv,semantic_scholar"

# MCP integration
RETRIEVER="tavily,mcp"
```

#### 3. **LLM Configuration**
Three-tier LLM strategy for optimal performance/cost:

**FAST_LLM** - Quick operations:
- Sub-query generation
- Source filtering
- Quick summaries
- Default: `gpt-4o-mini`

**SMART_LLM** - Complex analysis:
- Report writing
- Synthesis
- Citation generation
- Default: `gpt-4o`

**STRATEGIC_LLM** - Planning:
- Research strategy
- Topic decomposition
- Outline generation
- Default: `o4-mini` (reasoning model)

#### 4. **Document Processing**
Handles local and online documents.

**Supported Formats:**
- PDF (.pdf) - Most common, OCR supported
- Text (.txt) - Plain text
- Word (.docx, .doc) - Microsoft Word
- CSV (.csv) - Structured data
- Excel (.xlsx, .xls) - Spreadsheets
- Markdown (.md) - Formatted text
- PowerPoint (.pptx, .ppt) - Presentations

**Processing Pipeline:**
```
Document → Loader → Chunker → Embedder → Vector Store → Retriever
```

---

## 📊 RESEARCH MODES & METHODOLOGIES

### 1. **Standard Research (Web Only)**

**When to Use:**
- General topic research
- Current events
- Market trends
- Industry analysis

**Workflow:**
```python
researcher = GPTResearcher(
    query="Your research question",
    report_type="research_report",
    report_source="web"
)
await researcher.conduct_research()
report = await researcher.write_report()
```

**Process:**
1. Query analysis and decomposition
2. Sub-query generation (typically 3-5)
3. Parallel web search execution
4. Source scraping and extraction
5. Context aggregation (20+ sources)
6. LLM synthesis
7. Report generation with citations

**Performance:**
- Duration: 1-3 minutes
- Cost: $0.05 - $0.15
- Sources: 20-30 typically

---

### 2. **Deep Research (Tree Exploration)**

**When to Use:**
- Complex topics requiring thorough analysis
- Academic research
- Strategic decision-making
- Comprehensive market analysis

**Unique Features:**
- Tree-like exploration pattern
- Multiple breadth levels
- Recursive depth exploration
- Smart context management

**Configuration:**
```bash
export DEEP_RESEARCH_BREADTH=4      # Parallel paths per level
export DEEP_RESEARCH_DEPTH=2        # Depth levels
export DEEP_RESEARCH_CONCURRENCY=4  # Max concurrent ops
export TOTAL_WORDS=2500             # Report length
```

**Workflow:**
```python
researcher = GPTResearcher(
    query="Complex research question",
    report_type="deep"  # Activates deep research mode
)
await researcher.conduct_research()
report = await researcher.write_report()
```

**Process Flow:**
```
Level 0: Main Query
    ├─ Breadth 1: Sub-query A
    │   ├─ Depth 1: Follow-up A1
    │   │   └─ Depth 2: Deep-dive A1.1
    │   └─ Depth 1: Follow-up A2
    ├─ Breadth 2: Sub-query B
    │   └─ Depth 1: Follow-up B1
    ├─ Breadth 3: Sub-query C
    └─ Breadth 4: Sub-query D
```

**Performance:**
- Duration: 5-10 minutes
- Cost: $0.30 - $0.50 (using o3-mini)
- Sources: 50+ typically
- Depth: Highly comprehensive

**Best Practices:**
- Start with breadth=4, depth=2
- Increase breadth for wider coverage
- Increase depth for deeper insights
- Monitor costs with verbose mode

---

### 3. **Hybrid Research (Web + Local Documents)**

**When to Use:**
- Combining internal documents with market research
- Product roadmap vs. industry trends
- Policy review with industry standards
- Competitive analysis with proprietary data

**Setup:**
```bash
# Set document path
export DOC_PATH="./my-docs"
```

**Workflow:**
```python
researcher = GPTResearcher(
    query="How does our strategy compare to market trends?",
    report_type="research_report",
    report_source="hybrid"  # Web + local docs
)
await researcher.conduct_research()
report = await researcher.write_report()
```

**Process:**
1. **Local Document Phase:**
   - Load documents from DOC_PATH
   - Chunk and embed documents
   - Create vector store
   - Extract relevant passages

2. **Web Research Phase:**
   - Generate complementary queries
   - Execute web searches
   - Scrape and extract content

3. **Synthesis Phase:**
   - Combine local and web insights
   - Reconcile conflicting information
   - Prioritize recent/authoritative sources
   - Generate unified report

**Privacy Model:**
- Documents processed **locally only**
- Vector embeddings created on your machine
- **Only synthesized insights** sent to LLM
- Raw document data **never** transmitted
- Full GDPR/compliance safe

**Performance:**
- Duration: 2-5 minutes
- Cost: $0.15 - $0.30
- Sources: Local docs + 20+ web sources

---

### 4. **MCP Integration (Model Context Protocol)**

**When to Use:**
- Specialized data sources (GitHub, databases, APIs)
- Enterprise knowledge bases
- Custom tool integrations
- Multi-domain research

**Critical Configuration:**
```bash
# MUST set RETRIEVER to enable MCP
export RETRIEVER=mcp              # Pure MCP
export RETRIEVER=tavily,mcp       # Hybrid (recommended)
```

**Architecture:**
```
┌──────────────┐
│ GPTResearcher│
└──────┬───────┘
       │
       ▼
┌──────────────────────────────┐
│ MCP Integration Layer        │
│ ┌────────────────────────┐  │
│ │ Stage 1: Tool Selection│  │  LLM analyzes query
│ └──────────┬─────────────┘  │  Selects relevant MCP tools
│            │                 │
│            ▼                 │
│ ┌────────────────────────┐  │
│ │ Stage 2: Execution     │  │  LLM generates args
│ └──────────┬─────────────┘  │  Executes selected tools
└────────────┼────────────────┘
             │
             ▼
    ┌────────────────┐
    │  MCP Servers   │
    ├────────────────┤
    │ • GitHub       │
    │ • Tavily       │
    │ • Financial DB │
    │ • Custom APIs  │
    └────────────────┘
```

**MCP Configuration Structure:**
```python
mcp_configs = [
    {
        "name": "server_identifier",
        "command": "npx",  # or "python"
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
            "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")
        }
    }
]
```

**Multi-Server Example:**
```python
os.environ["RETRIEVER"] = "tavily,google,mcp"

researcher = GPTResearcher(
    query="Comprehensive Tesla Q4 analysis",
    mcp_configs=[
        # Financial data
        {
            "name": "financial",
            "command": "python",
            "args": ["financial_server.py"],
            "env": {"ALPHA_VANTAGE_KEY": os.getenv("ALPHA_KEY")}
        },
        # News/sentiment
        {
            "name": "tavily",
            "command": "npx",
            "args": ["-y", "tavily-mcp@0.1.2"],
            "env": {"TAVILY_API_KEY": os.getenv("TAVILY_KEY")}
        },
        # Code/technical
        {
            "name": "github",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"],
            "env": {"GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")}
        }
    ]
)
```

**MCP Strategies:**
- `fast` - Run MCP once with main query (default)
- `deep` - Run MCP for all sub-queries (comprehensive)
- `disabled` - Skip MCP entirely

**Performance:**
- Fast strategy: Similar to standard research
- Deep strategy: 2-3x longer, much more comprehensive
- Tool selection: Automatic (LLM-driven)

---

### 5. **Multi-Agent Research (LangGraph)**

**When to Use:**
- Publication-quality reports
- Academic research papers
- Business intelligence reports
- Multi-stakeholder analysis

**The 7-Agent Team:**

1. **Chief Editor** - Orchestrates the entire process
2. **Researcher** (GPT Researcher) - Conducts deep research
3. **Editor** - Plans outline and structure
4. **Reviewer** - Validates correctness and quality
5. **Revisor** - Revises based on feedback
6. **Writer** - Compiles final report
7. **Publisher** - Exports to multiple formats

**Workflow:**
```
┌──────────────┐
│ Chief Editor │ ← Orchestrator
└──────┬───────┘
       │
       ▼
┌──────────────┐      ┌──────────┐
│   Browser    │──────▶│  Editor  │ Plans outline
│(GPTResearcher)│      └────┬─────┘
└──────────────┘           │
                           ▼
       ┌───────────────────────────────┐
       │   For each outline section:   │
       │                               │
       │  ┌──────────┐  ┌──────────┐  │
       │  │Researcher│→ │ Reviewer │  │
       │  └────┬─────┘  └────┬─────┘  │
       │       │             │         │
       │       ▼             ▼         │
       │  ┌──────────┐  ┌──────────┐  │
       │  │  Draft   │→ │ Revisor  │  │
       │  └──────────┘  └────┬─────┘  │
       │                     │         │
       └─────────────────────┼─────────┘
                             │
                             ▼
                      ┌──────────┐
                      │  Writer  │ Compiles
                      └────┬─────┘
                           │
                           ▼
                      ┌──────────┐
                      │Publisher │ PDF/DOCX/MD
                      └──────────┘
```

**Configuration (task.json):**
```json
{
  "query": "Is AI in a hype cycle?",
  "model": "gpt-4o",
  "max_sections": 3,
  "publish_formats": {
    "markdown": true,
    "pdf": true,
    "docx": true
  },
  "include_human_feedback": false,
  "source": "web",
  "follow_guidelines": true,
  "guidelines": [
    "The report MUST fully answer the original question",
    "The report MUST be written in APA format",
    "The report MUST be written in English"
  ],
  "verbose": true
}
```

**Running:**
```bash
# Install
pip install langgraph-cli

# Deploy
langgraph up

# Or run locally
python main.py
```

**Performance:**
- Duration: 10-20 minutes
- Output: 5-6 page reports
- Formats: MD, PDF, DOCX
- Quality: Publication-ready

---

## ⚙️ ADVANCED CONFIGURATION

### Environment Variables (Complete Reference)

#### LLM Configuration
```bash
# Provider selection
FAST_LLM="openai:gpt-4o-mini"
SMART_LLM="openai:gpt-4o"
STRATEGIC_LLM="openai:o4-mini"
EMBEDDING="openai:text-embedding-3-small"

# API Keys
OPENAI_API_KEY="your_key"
ANTHROPIC_API_KEY="your_key"
GROQ_API_KEY="your_key"
AZURE_OPENAI_API_KEY="your_key"
```

#### Retriever Configuration
```bash
RETRIEVER="tavily,mcp"              # Multiple retrievers
TAVILY_API_KEY="your_key"
GOOGLE_API_KEY="your_key"
BING_API_KEY="your_key"
```

#### Deep Research
```bash
DEEP_RESEARCH_BREADTH=4             # Parallel paths (1-10)
DEEP_RESEARCH_DEPTH=2               # Depth levels (1-5)
DEEP_RESEARCH_CONCURRENCY=4         # Max concurrent (1-10)
TOTAL_WORDS=2500                    # Report length
```

#### Local Documents
```bash
DOC_PATH="./my-docs"                # Local docs directory
```

#### MCP Configuration
```bash
MCP_STRATEGY="fast"                 # fast, deep, disabled
MCP_AUTO_TOOL_SELECTION=true        # Auto tool selection
```

#### Performance Tuning
```bash
MAX_ITERATIONS=3                    # Research iterations
MAX_SEARCH_RESULTS=10               # Results per query
MAX_TOKENS=4000                     # LLM response tokens
TEMPERATURE=0.7                     # Generation temperature
ENABLE_CACHE=true                   # Query caching
```

### Custom Configuration File

**config.yaml structure:**
```yaml
# LLM Settings
fast_llm: "openai:gpt-4o-mini"
smart_llm: "openai:gpt-4o"
strategic_llm: "openai:o4-mini"

# Research Settings
retriever: "tavily,mcp"
max_iterations: 3
report_type: "research_report"
total_words: 1500

# Deep Research
deep_research_breadth: 4
deep_research_depth: 2

# Behavior
verbose: true
tone: "OBJECTIVE"
```

**Usage:**
```python
researcher = GPTResearcher(
    query="Your query",
    config_path="path/to/config.yaml"
)
```

---

## 🎯 REPORT TYPES & CUSTOMIZATION

### Report Types

#### 1. **research_report** (Default)
- Standard comprehensive report
- Balanced depth and breadth
- Includes citations
- 1000-2000 words typical

#### 2. **outline_report**
- Structured outline only
- Hierarchical organization
- Section headers with brief descriptions
- Good for planning

#### 3. **resource_report**
- List of sources and resources
- Minimal synthesis
- URLs and citations
- Quick reference

#### 4. **custom_report**
- Custom prompt-driven
- Full control over format
- Specify exact requirements
- Example:
```python
researcher = GPTResearcher(
    query="Research AI trends and provide APA format report",
    report_type="custom_report"
)
```

#### 5. **deep**
- Activates deep research mode
- Tree-like exploration
- Most comprehensive
- 2500+ words typical

### Custom Prompts

**Flexibility in output format:**
```python
# Standard report
report = await researcher.write_report()

# Concise summary
report = await researcher.write_report(
    custom_prompt="Provide 2-paragraph summary without citations"
)

# Executive brief
report = await researcher.write_report(
    custom_prompt="""
    Create executive brief with:
    1. Executive Summary (2-3 sentences)
    2. Key Findings (3-5 bullets)
    3. Strategic Implications
    4. Recommended Actions
    Keep under 500 words.
    """
)

# Technical analysis
report = await researcher.write_report(
    custom_prompt="""
    Write detailed technical analysis with:
    - Methodology
    - Data sources assessment
    - Detailed findings
    - Technical conclusions
    - Full APA citations
    """
)
```

### Tone Configuration

Available tones:
- OBJECTIVE (default)
- FORMAL
- ANALYTICAL
- PERSUASIVE
- INFORMATIVE
- EXPLANATORY
- DESCRIPTIVE
- CRITICAL
- COMPARATIVE
- SPECULATIVE

**Usage:**
```python
from gpt_researcher.utils.enum import Tone

researcher = GPTResearcher(
    query="Your query",
    tone=Tone.FORMAL
)
```

---

## 🔧 TROUBLESHOOTING GUIDE

### Common Issues & Solutions

#### 1. **"No retriever specified" or "MCP not working"**

**Symptoms:**
- MCP configs provided but not used
- Only web search running

**Root Cause:**
- RETRIEVER environment variable not set

**Solution:**
```bash
export RETRIEVER=mcp
# or
export RETRIEVER=tavily,mcp
```

**Verification:**
```bash
echo $RETRIEVER
# Should output: tavily,mcp
```

---

#### 2. **"Invalid retriever(s) found"**

**Symptoms:**
- Error on initialization
- Retriever name rejected

**Root Cause:**
- Typo in retriever name
- Unsupported retriever

**Valid Retrievers:**
`tavily`, `mcp`, `google`, `bing`, `arxiv`, `semantic_scholar`, `pubmed_central`, `exa`, `searx`, `duckduckgo`, `custom`

**Solution:**
```bash
# Check for typos
export RETRIEVER=tavily,arxiv  # ✓ Correct
export RETRIEVER=tavilly,arxiv # ✗ Wrong (typo)
```

---

#### 3. **"No MCP server configurations found"**

**Symptoms:**
- RETRIEVER=mcp set
- But no MCP servers used

**Root Cause:**
- Empty or missing mcp_configs parameter

**Solution:**
```python
# Ensure mcp_configs is provided
researcher = GPTResearcher(
    query="Your query",
    mcp_configs=[
        {
            "name": "server_name",
            "command": "npx",
            "args": ["-y", "package-name"],
            "env": {"API_KEY": os.getenv("KEY")}
        }
    ]
)
```

---

#### 4. **"MCP server connection failed"**

**Symptoms:**
- Server timeout
- Connection refused

**Diagnosis Steps:**
1. Check server command is correct
2. Verify environment variables are set
3. Test server independently
4. Check network connectivity

**Solution:**
```bash
# Test MCP server independently
npx -y @modelcontextprotocol/server-github

# Check env vars
echo $GITHUB_TOKEN

# Verify network
curl -I https://api.github.com
```

---

#### 5. **"No tools available from MCP server"**

**Symptoms:**
- Server connects but no tools found
- Empty tool list

**Root Cause:**
- Server not exposing tools correctly
- Tool selection issue

**Solution:**
```bash
# Enable auto tool selection
export MCP_AUTO_TOOL_SELECTION=true
```

```python
# Or in code
os.environ["MCP_AUTO_TOOL_SELECTION"] = "true"
```

---

#### 6. **Rate Limiting / API Errors**

**Symptoms:**
- 429 errors
- "Rate limit exceeded"

**Solutions:**

**Option 1: Switch to cheaper model**
```bash
export FAST_LLM="openai:gpt-4o-mini"
export SMART_LLM="openai:gpt-4o-mini"
```

**Option 2: Reduce iterations**
```bash
export MAX_ITERATIONS=2
```

**Option 3: Add delays**
```python
# In custom implementation
import asyncio
await asyncio.sleep(1)  # Between requests
```

**Option 4: Use different provider**
```bash
# Groq for fast inference
export GROQ_API_KEY="your_key"
export FAST_LLM="groq:mixtral-8x7b-32768"
```

---

#### 7. **Document Loading Errors**

**Symptoms:**
- "Failed to load document"
- "Unsupported format"

**Diagnosis:**
```bash
# Check file exists
ls -la ./my-docs/

# Check file format
file ./my-docs/document.pdf

# Check permissions
ls -l ./my-docs/document.pdf
```

**Solutions:**

**Corrupted PDF:**
- Re-download or re-export
- Ensure not password-protected
- Try converting to searchable PDF

**Unsupported Format:**
- Convert to PDF, DOCX, or TXT
- Use OCR for scanned documents

**Permission Issues:**
```bash
chmod 644 ./my-docs/*.pdf
```

---

#### 8. **Memory Issues (Large Documents)**

**Symptoms:**
- Process killed
- Out of memory errors

**Solutions:**

**Option 1: Process fewer documents**
```bash
# Move large files temporarily
mkdir ./my-docs/archive
mv ./my-docs/large-file.pdf ./my-docs/archive/
```

**Option 2: Increase system memory**
```bash
# Docker
docker run --memory=8g ...

# System settings
# Increase swap space
```

**Option 3: Chunk smaller**
```python
# In custom implementation
chunk_size = 500  # Smaller chunks
```

---

## 💰 COST OPTIMIZATION STRATEGIES

### Cost Breakdown

**Typical Costs (GPT-4 based):**

| Research Type | Duration | Cost | Optimization |
|---------------|----------|------|--------------|
| Quick Web | 1-2 min | $0.05-$0.10 | Use gpt-4o-mini |
| Standard | 2-3 min | $0.10-$0.20 | Reduce iterations |
| Deep Research | 5-10 min | $0.30-$0.50 | Use o3-mini |
| Hybrid | 2-5 min | $0.15-$0.30 | Cache enabled |
| Multi-Agent | 10-20 min | $0.50-$1.00 | Batch sections |

### Cost Optimization Techniques

#### 1. **Use Cheaper Models for Fast Operations**
```bash
# Instead of
export FAST_LLM="openai:gpt-4o"  # Expensive

# Use
export FAST_LLM="openai:gpt-4o-mini"  # 10x cheaper
```

**Impact:** 50-70% cost reduction on sub-query generation

#### 2. **Reduce Max Iterations**
```bash
# Default
export MAX_ITERATIONS=3

# Cost-optimized
export MAX_ITERATIONS=2
```

**Impact:** 33% cost reduction, minimal quality loss

#### 3. **Enable Caching**
```bash
export ENABLE_CACHE=true
```

**Impact:** Up to 50% savings on repeated queries

#### 4. **Use Local LLMs for Development**
```bash
# Ollama setup
export OLLAMA_BASE_URL="http://localhost:11434"
export FAST_LLM="ollama:llama3"
export SMART_LLM="ollama:llama3"
```

**Impact:** $0 cost for development/testing

#### 5. **Optimize Retriever Strategy**
```bash
# Expensive (multiple paid APIs)
export RETRIEVER="google,bing,exa"

# Cost-effective (free + cheap)
export RETRIEVER="tavily,duckduckgo"
```

#### 6. **Adjust Report Length**
```bash
# Default
export TOTAL_WORDS=2000

# Shorter (cheaper)
export TOTAL_WORDS=1000
```

**Impact:** ~30% cost reduction

### Cost Monitoring

**Enable cost tracking:**
```python
researcher = GPTResearcher(query="...", verbose=True)
await researcher.conduct_research()
report = await researcher.write_report()

# Get costs
cost = researcher.get_costs()
print(f"Research cost: ${cost:.4f}")
```

**Budget controls:**
```python
# Set max budget
MAX_BUDGET = 0.50  # $0.50

cost = researcher.get_costs()
if cost > MAX_BUDGET:
    print(f"Budget exceeded: ${cost:.4f} > ${MAX_BUDGET}")
    # Take action
```

---

## 🚀 PERFORMANCE OPTIMIZATION

### Speed Optimization

#### 1. **Parallelization**
Already built-in, but you can tune:
```bash
export DEEP_RESEARCH_CONCURRENCY=8  # More parallel operations
```

#### 2. **Faster Models**
```bash
# Groq for blazing fast inference
export GROQ_API_KEY="your_key"
export FAST_LLM="groq:mixtral-8x7b-32768"
export SMART_LLM="groq:mixtral-8x7b-32768"
```

**Impact:** 3-5x faster completion

#### 3. **Reduce Source Count**
```bash
export MAX_SEARCH_RESULTS=5  # Default is 10
```

**Impact:** ~30% faster, slightly less comprehensive

#### 4. **Streaming Mode**
```python
# Enable WebSocket for real-time updates
researcher = GPTResearcher(
    query="...",
    websocket=websocket
)
```

**Impact:** Better UX, perceived performance

### Quality Optimization

#### 1. **Use Better Models**
```bash
export SMART_LLM="anthropic:claude-3-opus-20240229"
```

#### 2. **Increase Iterations**
```bash
export MAX_ITERATIONS=5
```

#### 3. **More Sources**
```bash
export MAX_SEARCH_RESULTS=20
```

#### 4. **Follow Guidelines**
```json
{
  "follow_guidelines": true,
  "guidelines": [
    "Report MUST fully answer question",
    "Report MUST include citations",
    "Report MUST be well-structured"
  ]
}
```

### Balance (Speed + Quality + Cost)

**Recommended Configurations:**

**Development/Testing:**
```bash
FAST_LLM="ollama:llama3"
SMART_LLM="ollama:llama3"
MAX_ITERATIONS=2
MAX_SEARCH_RESULTS=5
```

**Production (Balanced):**
```bash
FAST_LLM="openai:gpt-4o-mini"
SMART_LLM="openai:gpt-4o"
MAX_ITERATIONS=3
MAX_SEARCH_RESULTS=10
ENABLE_CACHE=true
```

**Production (Quality-First):**
```bash
FAST_LLM="openai:gpt-4o"
SMART_LLM="anthropic:claude-3-opus-20240229"
STRATEGIC_LLM="openai:o4-mini"
MAX_ITERATIONS=4
MAX_SEARCH_RESULTS=15
```

---

## 📚 INTEGRATION PATTERNS

### Integration with Other PAI Skills

#### 1. **With research Skill**
```markdown
Use gpt-researcher for:
- Single-topic deep dives
- Detailed report generation
- Custom format requirements

Use research skill for:
- Multi-perspective research (3 different LLMs)
- Parallel research queries
- Fast broad coverage
```

#### 2. **With fabric Skill**
```python
# 1. Generate research report
researcher = GPTResearcher(query="AI trends")
report = await researcher.write_report()

# 2. Process with fabric patterns
# extract_wisdom, summarize, etc.
```

#### 3. **With perplexity-researcher**
```markdown
Combine for comprehensive coverage:
- gpt-researcher: Deep, cited reports
- perplexity-researcher: Quick web searches
- Use both for validation/cross-checking
```

### API Integration

**FastAPI Example:**
```python
from fastapi import FastAPI, WebSocket
from gpt_researcher import GPTResearcher

app = FastAPI()

@app.websocket("/research")
async def research_endpoint(websocket: WebSocket):
    await websocket.accept()

    # Get query
    query = await websocket.receive_text()

    # Research
    researcher = GPTResearcher(
        query=query,
        websocket=websocket
    )
    await researcher.conduct_research()
    report = await researcher.write_report()

    # Send report
    await websocket.send_text(report)
```

### LangChain Integration

```python
from langchain_core.documents import Document
from langchain_postgres.vectorstores import PGVector
from gpt_researcher import GPTResearcher

# Get documents from LangChain retriever
retriever = get_retriever("collection_name")
documents = retriever.invoke("cheese")

# Use with GPT Researcher
researcher = GPTResearcher(
    query="What can you tell me about blue cheese?",
    report_source="langchain_documents",
    documents=documents
)
```

---

## 🎓 LEARNING PATH & RESOURCES

### Beginner Path

1. **Start with simple_run.py**
   - Understand basic workflow
   - See query → report flow
   - Check costs

2. **Try custom_prompt.py**
   - Learn report customization
   - Understand formatting options

3. **Explore hybrid_local.py**
   - Add local documents
   - See privacy model in action

### Intermediate Path

4. **Try detailed_report.py**
   - Multi-section reports
   - Table of contents generation

5. **Experiment with MCP**
   - Add GitHub MCP server
   - Try multi-server research

6. **Use config.yaml**
   - Customize all settings
   - Optimize for your use case

### Advanced Path

7. **Deep Research Mode**
   - Understand tree exploration
   - Tune breadth/depth

8. **Multi-Agent with LangGraph**
   - Publication-quality reports
   - Custom agent workflows

9. **Custom Retrievers**
   - Enterprise integrations
   - Custom data sources

### Official Resources

- **Documentation**: https://docs.gptr.dev
- **GitHub**: https://github.com/assafelovic/gpt-researcher
- **Discord**: https://discord.gg/QgZXvJAccX
- **Examples**: See examples/ directory

---

## 🔐 SECURITY & PRIVACY

### Data Handling

**What's Sent Externally:**
- Research queries (text only)
- Synthesized summaries
- Generated reports
- Source URLs

**What Stays Local:**
- Raw document content
- Document embeddings
- Vector stores
- File paths
- Internal metadata

### Best Practices

1. **API Key Security**
```bash
# Use environment variables
export OPENAI_API_KEY="sk-..."

# Never commit keys
echo "*.env" >> .gitignore
```

2. **Sensitive Documents**
```python
# Create separate directory for sensitive docs
# Don't include in research
```

3. **Audit Logs**
```python
researcher = GPTResearcher(query="...", verbose=True)
# Logs all operations
```

4. **Cost Controls**
```python
# Set budget limits
MAX_BUDGET = 1.00
# Monitor and alert
```

---

## 📁 WORKFLOW EXECUTION GUIDE

For executable step-by-step instructions, load workflows from the `workflows/` directory. Each workflow provides concrete procedures for Lucy to execute specific research modes.

### Available Workflows

**Essential Workflows (Tier 1):**

1. **quick-research.md** - Standard Web Research
   - When: General research requests
   - Duration: 1-3 minutes | Cost: $0.05-$0.15
   - Process: Query → Research → Report
   - Output: 1000-1500 word comprehensive report

2. **deep-research.md** - Comprehensive Tree Exploration
   - When: "Deep research", "comprehensive analysis"
   - Duration: 5-10 minutes | Cost: $0.30-$0.50
   - Process: Strategic planning → Breadth exploration → Depth diving
   - Output: 2500+ word multi-level report with 50+ sources

3. **hybrid-research.md** - Web + Documents
   - When: "Research using our docs", "compare to market"
   - Duration: 2-5 minutes | Cost: $0.15-$0.30
   - Process: Document analysis → Web research → Synthesis
   - Output: Internal + external insights report

**Advanced Workflows (Tier 2):**

4. **mcp-integration.md** - Model Context Protocol
   - When: GitHub, databases, custom APIs needed
   - Process: Two-stage (tool selection → execution)
   - Special: Intelligent tool selection by LLM

5. **custom-report.md** - Format Customization
   - When: "Executive summary", "bullet points", specific formats
   - Process: Research → Custom prompt → Formatted output
   - Formats: Executive, bullets, APA, technical, comparison

**Specialized Workflows (Tier 3):**

6. **multi-agent.md** - LangGraph Publication Quality
   - When: "Publication quality", academic reports
   - Duration: 10-20 minutes | Cost: $0.50-$1.00
   - Team: 7 agents (Editor, Researcher, Reviewer, Writer, etc.)
   - Output: 5-6 page report in MD/PDF/DOCX

7. **cost-optimization.md** - Budget-Conscious
   - When: Cost concerns, budget limits
   - Duration: 1-2 minutes | Cost: $0.03-$0.05
   - Optimizations: Cheaper models, fewer iterations, shorter reports

8. **troubleshooting.md** - Debug & Fix
   - When: Errors, failures, "not working"
   - Content: Diagnostic decision trees, solutions
   - Coverage: 8 common issues with fixes

### How to Use Workflows

**Step 1: User makes request**
```
User: "Do deep research on quantum computing"
```

**Step 2: Lucy identifies workflow**
```
Match: "deep research" → deep-research.md workflow
```

**Step 3: Lucy loads workflow**
```
Read /Users/michaelatherton/Documents/condaEnv/AIRL/PAI/.claude/skills/gpt-researcher/workflows/deep-research.md
```

**Step 4: Lucy executes steps**
- Follows executable instructions
- Runs code examples
- Handles errors per workflow guidance
- Delivers results to user

### Workflow Selection Guide

| User Request | Workflow | Rationale |
|--------------|----------|-----------|
| "Research X" | quick-research.md | Standard request |
| "Deep/comprehensive research" | deep-research.md | Needs depth |
| "Using our docs" | hybrid-research.md | Local documents |
| "GitHub/database" | mcp-integration.md | Specialized sources |
| "Executive summary" | custom-report.md | Format specific |
| "Publication quality" | multi-agent.md | High quality needed |
| "Cheap/budget" | cost-optimization.md | Cost constrained |
| "Not working/error" | troubleshooting.md | Issue diagnosis |

### Workflow Loading Paths

```bash
# Essential
workflows/quick-research.md
workflows/deep-research.md
workflows/hybrid-research.md

# Advanced
workflows/mcp-integration.md
workflows/custom-report.md
workflows/multi-agent.md
workflows/cost-optimization.md
workflows/troubleshooting.md
```

---

## 📝 CONCLUSION

This CLAUDE.md provides comprehensive context for GPT Researcher usage. For quick reference, see SKILL.md. For runnable examples, see examples/ directory. For executable workflows, see workflows/ directory.

**Key Takeaways:**
- GPT Researcher offers multiple research modes for different needs
- Configuration is highly flexible but has sensible defaults
- Cost/quality/speed can be balanced via configuration
- Privacy-first design for local documents
- Extensive integration possibilities

**When to Use Each Mode:**
- **Standard**: General research, current topics
- **Deep**: Complex analysis, comprehensive coverage
- **Hybrid**: Internal + external insights
- **MCP**: Specialized data sources
- **Multi-Agent**: Publication-quality reports

**Next Steps:**
1. Start with examples/simple_run.py
2. Experiment with different modes
3. Optimize for your specific needs
4. Integrate with your workflows

For questions, consult:
- This file (comprehensive context)
- SKILL.md (quick reference)
- examples/README.md (practical examples)
- Official docs (https://docs.gptr.dev)
