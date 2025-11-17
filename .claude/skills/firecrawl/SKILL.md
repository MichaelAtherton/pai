---
name: firecrawl
description: |
  This skill provides comprehensive web scraping and data extraction using the Firecrawl API.
  It should activate when the user requests scraping websites, crawling entire sites, extracting structured data,
  or converting web content to LLM-ready formats. The skill supports five core features: Scrape (single URLs),
  Crawl (multi-page discovery), Map (URL listing), Search (web search + scrape), and Extract (AI-powered
  structured data). It handles authenticated scraping, batch operations, browser automation, and MCP integration.
---

# Firecrawl Skill

Comprehensive assistance with Firecrawl - the Web Data API for AI that converts entire websites into LLM-ready markdown or structured data.

## When to Use This Skill

Activate this skill when the user requests:
- Scraping websites or extracting data from URLs
- Crawling entire websites or getting all pages from a site
- Searching the web and scraping results
- Mapping website structure or discovering URLs
- Extracting structured data or converting websites to JSON
- Batch scraping multiple pages
- Authenticated scraping or scraping behind login
- PDF scraping or extracting from PDFs
- Taking webpage screenshots
- Monitoring price/content changes
- MCP web scraping (Claude Code integration)
- Converting websites to markdown/LLM format
- Browser actions on websites (click, scroll, input before scraping)
- Working with Firecrawl features or APIs
- Debugging Firecrawl code

## Quick Reference

### Essential Patterns

**1. Basic Single URL Scrape:**
```python
from firecrawl import FirecrawlApp
import os

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
result = app.scrape_url('https://example.com', params={
    'formats': ['markdown', 'html']
})
print(result['markdown'])
```

**2. Crawl Entire Site:**
```python
# Crawl and wait for completion
result = app.crawl_url('https://example.com', params={
    'limit': 100,
    'scrapeOptions': {'formats': ['markdown']}
})

# Or start crawl and poll status
crawl_id = app.start_crawl_url('https://example.com', params={'limit': 100})
status = app.get_crawl_status(crawl_id)
```

**3. Extract Structured Data (JSON Mode):**
```python
from pydantic import BaseModel

class ProductInfo(BaseModel):
    name: str
    price: float
    availability: str

result = app.scrape_url('https://example.com/product', params={
    'formats': [{'type': 'json', 'schema': ProductInfo.model_json_schema()}]
})
```

**4. Batch Scrape Multiple URLs:**
```python
urls = ["https://url1.com", "https://url2.com", "https://url3.com"]
result = app.batch_scrape_urls(urls, params={
    'formats': ['markdown']
})
```

### Additional Examples

Load `references/quick-start.md` for 6 additional code examples:
- Authenticated scraping (cookie-based)
- Browser actions (click/scroll/input)
- Fast mode (caching)
- Map website URLs
- Search web + scrape results
- Extract with AI (no schema)

## Output Formats

Available formats: `markdown`, `html`, `rawHtml`, `links`, `images`, `summary`, `branding`

Object formats: `{'type': 'json', 'schema': {...}}`, `{'type': 'screenshot', ...}`

Load `references/parameters.md` for complete format documentation.

## Reference Files

Access comprehensive documentation in `references/`:

### Core Concepts & Architecture
- **getting_started.md** - Installation, quickstart, API setup (13 KB)
  - Search: "Installation", "Authentication", "Basic scraping", "API key"
- **features.md** - All 5 features + MCP + advanced capabilities (44 KB)
  - Search: "Authenticated Scraping", "MCP Server", "Actions", "Batch", "Caching"
- **api_reference.md** - Complete API endpoints and parameters (33 KB)
  - Search: "Scrape endpoint", "Crawl endpoint", "Parameters", "Response"

### Integration & SDKs
- **sdks.md** - Python/Node SDKs + LLM frameworks (LangChain, LlamaIndex) (27 KB)
  - Search: "LangChain", "LlamaIndex", "AI SDK", "Gemini"
- **advanced.md** - Authenticated scraping, MCP server, self-hosting (10 KB)
  - Search: "Cookie", "DevTools", "Self-host", "MCP config"

### Use Cases & Patterns
- **guides.md** - Platform-specific guides (Amazon, GitHub, Etsy, Wikipedia) (4.4 KB)
  - Search: "Amazon", "GitHub", "Product scraping"

### Additional References
- **quick-start.md** - 6 additional code examples with detailed explanations
  - Search: "Authenticated", "Actions", "Caching", "Map", "Search"
- **parameters.md** - Complete parameter documentation for all features
  - Search: "formats", "maxAge", "actions", "includeUrlPatterns"

**Access reference files:**
```
Read references/[filename].md
```

## Getting Started

Load `getting_started.md` for installation and basic scraping patterns.

## Accessing Feature Documentation

Load specific sections from `features.md`:
- Single URL scraping → Scrape section
- Multi-page crawling → Crawl section
- URL discovery → Map section
- Web search → Search section
- Structured data → Extract section
- MCP integration → Firecrawl MCP Server section
- Authenticated scraping → Authenticated Scraping section

## Loading Code Examples

Access runnable Python scripts in `scripts/`:
```
Read scripts/README.md
```

**Available scripts:**
- `scrape.py` - Basic single URL scraping
- `crawl.py` - Crawl with URL pattern filtering
- `batch.py` - Batch scrape multiple URLs
- `auth_scrape.py` - Authenticated scraping
- `extract.py` - Structured data extraction
- `actions.py` - Browser automation
- `map_then_scrape.py` - Map then selective scrape

## Available Workflows

Access step-by-step execution instructions in `workflows/`:

### Essential Workflows (Core Features)
- **basic-scrape.md** - Single URL scraping (5-10s, 1 credit)
- **crawl-site.md** - Multi-page website crawling (30s-5min, 1 credit/page)
- **batch-scrape.md** - Scrape multiple URLs simultaneously (1-3min, 1 credit/URL)
- **map-urls.md** - Fast URL discovery (1-5s, 1 credit)
- **extract-structured-data.md** - AI-powered data extraction (10-30s, token-based)

### Advanced Workflows
- **authenticated-scrape.md** - Scraping behind authentication (10-20s, 1 credit)
- **mcp-integration.md** - Using Firecrawl via MCP servers (varies)
- **actions-automation.md** - Browser interactions before scraping (15-30s, 1 credit)

**Execute a workflow:**
```
Read workflows/[workflow-name].md
```

Each workflow provides executable step-by-step instructions.

## Important Notes

- **Rate Limits**: Free: 10 req/min, Hobby: 100 req/min, Standard: 500 req/min
- **Caching**: Default `maxAge` is 2 days. Use caching for 500% speed improvement
- **Cost**: 1 credit per scrape/page. Extract uses token-based pricing
- **Authentication**: Only use on systems with explicit permission. Follow site ToS
- **MCP Integration**: Requires `FIRECRAWL_API_KEY` environment variable
- **Dynamic Content**: Automatically handles JS-rendered content
- **PDF Support**: Use `parsers: ['pdf']` parameter

## Supplementary Resources

**Load comprehensive deep context:**
```
Read CLAUDE.md
```

CLAUDE.md contains:
- Complete architecture and component documentation
- Detailed methodology for all 5 features (Scrape, Crawl, Map, Search, Extract)
- Advanced configuration guide (actions, authentication, caching)
- Comprehensive troubleshooting decision trees
- Cost optimization strategies
- Performance tuning guide
- Integration patterns (LangChain, LlamaIndex, AI SDK, n8n)
- Security and privacy best practices
- Platform-specific guides (Amazon, GitHub, etc.)
- Learning path from beginner to advanced

**Access runnable scripts:**
```
See scripts/
```

**Access configuration templates:**
```
See templates/config.yaml
```

**Access reference documentation:**
```
See references/
```

## Related Skills

- Use with **gpt-researcher** skill for comprehensive web research workflows
- Use with **fabric** skill to process/extract patterns from scraped content
- Combine with **MCP servers** for specialized data source integration
- Integrate with **LangChain** for custom RAG workflows

## Updating This Skill

Refresh with updated documentation:
1. Re-run the scraper with same configuration
2. Skill rebuilds with latest information from docs.firecrawl.dev

---

This skill was automatically generated from official Firecrawl documentation and enhanced for PAI integration.
