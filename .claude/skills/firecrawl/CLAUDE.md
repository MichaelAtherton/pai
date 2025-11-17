# Firecrawl - Comprehensive Deep Context

**Version:** 2.0.0
**Last Updated:** 2025-11-16
**Purpose:** Anti-hallucination comprehensive reference for Firecrawl web scraping API

---

## Table of Contents

1. [Purpose & Philosophy](#purpose--philosophy)
2. [Architecture & Components](#architecture--components)
3. [Five Core Features](#five-core-features)
4. [Advanced Features](#advanced-features)
5. [Output Formats](#output-formats)
6. [Integration Patterns](#integration-patterns)
7. [Platform-Specific Guides](#platform-specific-guides)
8. [Cost & Performance](#cost--performance)
9. [Troubleshooting](#troubleshooting)
10. [Security & Privacy](#security--privacy)
11. [Learning Path](#learning-path)
12. [Workflow Execution Guide](#workflow-execution-guide)

---

## Purpose & Philosophy

### What is Firecrawl?

Firecrawl is an **API service** that converts websites into **LLM-ready formats** (markdown, JSON, screenshots). Unlike traditional web scraping libraries, Firecrawl is a managed cloud service that handles the complex infrastructure:

- **Proxies & Anti-Bot Mechanisms**: Bypass bot detection automatically
- **Dynamic Content**: Render JavaScript, handle single-page apps
- **Rate Limiting**: Built-in intelligent rate limiting
- **Caching**: Automatic caching for 500% speed improvements
- **Format Conversion**: Clean markdown optimized for LLMs

### Firecrawl vs. Traditional Scraping

| Aspect | Traditional Libraries | Firecrawl API |
|--------|----------------------|---------------|
| **Infrastructure** | You manage proxies, browsers | Fully managed |
| **Bot Detection** | Manual bypass needed | Automatic handling |
| **Dynamic Content** | Requires Selenium/Playwright | Built-in JS rendering |
| **Output Format** | Raw HTML | LLM-ready markdown/JSON |
| **Scaling** | Manual scaling | Automatic scaling |
| **Pricing** | Server costs | Credit-based API |

### Philosophy

1. **LLM-First Design**: Outputs optimized for AI consumption
2. **Reliability**: Built to get data even from difficult sites
3. **Speed**: Intelligent caching and parallel processing
4. **Simplicity**: One API call instead of managing infrastructure

---

## Architecture & Components

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      USER REQUEST                           │
│         (URL, URLs, Search Query, or Map Request)          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  FIRECRAWL API GATEWAY                      │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              FEATURE ROUTER                          │  │
│  │  ┌──────────────────────────────────────────────┐   │  │
│  │  │ /scrape     → Single URL scraping           │   │  │
│  │  │ /crawl      → Multi-page discovery + scrape │   │  │
│  │  │ /map        → URL discovery only            │   │  │
│  │  │ /search     → Web search + scrape results   │   │  │
│  │  │ /extract    → AI-powered data extraction    │   │  │
│  │  │ /batch      → Multiple URLs simultaneously  │   │  │
│  │  └──────────────────────────────────────────────┘   │  │
│  └──────────────────────┬──────────────────────────────────┘  │
│                         │                                   │
│         ┌───────────────┴──────────────┐                   │
│         │                               │                   │
│         ▼                               ▼                   │
│  ┌──────────────┐              ┌───────────────┐           │
│  │   BROWSER    │              │   SCRAPER     │           │
│  │   ENGINE     │◄────────────►│   ENGINE      │           │
│  │              │              │               │           │
│  │ - Chromium   │              │ - HTML Parser │           │
│  │ - JS Render  │              │ - Content     │           │
│  │ - Actions    │              │   Extraction  │           │
│  │ - Screenshots│              │ - PDF Parser  │           │
│  └──────┬───────┘              └───────┬───────┘           │
│         │                               │                   │
│         └───────────────┬───────────────┘                   │
│                         │                                   │
│                         ▼                                   │
│              ┌─────────────────────┐                        │
│              │ FORMAT CONVERTERS   │                        │
│              │                     │                        │
│              │ • Markdown Conv.    │                        │
│              │ • HTML Cleaner      │                        │
│              │ • JSON Generator    │                        │
│              │ • Screenshot Cap.   │                        │
│              │ • Link Extractor    │                        │
│              │ • Image Extractor   │                        │
│              │ • Brand Analyzer    │                        │
│              └──────────┬──────────┘                        │
│                         │                                   │
│                         ▼                                   │
│                ┌────────────────┐                           │
│                │  CACHE LAYER   │                           │
│                │  (maxAge ctrl) │                           │
│                └────────┬───────┘                           │
└─────────────────────────┼───────────────────────────────────┘
                          │
                          ▼
                ┌──────────────────┐
                │  OUTPUT FORMATS  │
                │                  │
                │  • Markdown      │
                │  • JSON/Schema   │
                │  • HTML/Raw HTML │
                │  • Screenshots   │
                │  • Links/Images  │
                │  • Branding Data │
                └──────────────────┘
```

### Components

1. **API Gateway**: Routes requests to appropriate feature
2. **Browser Engine**: Chromium-based for JS rendering and actions
3. **Scraper Engine**: Extracts and cleans content
4. **Format Converters**: Transform to LLM-ready formats
5. **Cache Layer**: Stores results with configurable `maxAge`

---

## Five Core Features

### 1. Scrape (Single URL)

**Purpose**: Extract content from a single webpage

**When to Use:**
- Single page data extraction
- Product pages, articles, documentation
- API endpoint testing
- Screenshot capture

**Key Parameters:**
```python
params = {
    'formats': ['markdown', 'html', {'type': 'screenshot'}],
    'onlyMainContent': True,           # Main content vs full page
    'includeTags': ['h1', 'p', '.content'],
    'excludeTags': ['#ads', '.footer'],
    'waitFor': 2000,                   # Wait ms before scraping
    'maxAge': 86400000,                # 1 day cache
    'timeout': 30000,                  # 30s timeout
    'parsers': ['pdf'],                # PDF parsing
    'headers': {'Cookie': 'token=...'},# Authentication
    'actions': []                      # Browser actions
}
```

**Performance:**
- **Cached**: < 500ms (if within maxAge)
- **Fresh**: 2-10 seconds (depending on page complexity)

**Cost**: 1 credit per scrape

**Response Structure:**
```python
{
    'success': True,
    'markdown': '# Page Title\n\nContent...',
    'html': '<h1>Page Title</h1>...',
    'screenshot': 'base64_encoded_image',
    'metadata': {
        'title': 'Page Title',
        'description': '...',
        'ogImage': 'https://...'
    }
}
```

**Example:**
```python
result = app.scrape_url('https://example.com', params={
    'formats': ['markdown', 'links'],
    'onlyMainContent': True,
    'maxAge': 3600000  # 1 hour cache
})
```

---

### 2. Crawl (Multi-Page)

**Purpose**: Discover and scrape multiple pages from a website

**When to Use:**
- Documentation sites (get all docs)
- E-commerce categories (all products)
- Blog archives (all posts)
- Knowledge base extraction

**Discovery Strategy:**
Firecrawl starts from the given URL and:
1. Extracts all links from the page
2. Filters by `includeUrlPatterns` / `excludeUrlPatterns`
3. Respects `maxDiscoveryDepth`
4. Discovers new URLs up to `limit`
5. Scrapes each discovered page with `scrapeOptions`

**Key Parameters:**
```python
params = {
    'limit': 100,                          # Max pages to crawl
    'maxDiscoveryDepth': 3,                # How deep to discover
    'includeUrlPatterns': ['^/blog/.*$'],  # Regex include
    'excludeUrlPatterns': ['^/admin/.*$'], # Regex exclude
    'crawlEntireDomain': False,            # Explore entire domain
    'allowExternalLinks': False,           # Follow external links
    'allowSubdomains': False,              # Follow subdomains
    'delayBetweenScrapes': 1,              # Delay in seconds
    'scrapeOptions': {
        'formats': ['markdown'],
        'onlyMainContent': True,
        'maxAge': 86400000
    }
}
```

**Async Job Flow:**
```python
# Method 1: Wait for completion (SDK handles polling)
result = app.crawl_url('https://example.com', params={'limit': 50})

# Method 2: Start and poll manually
crawl_id = app.start_crawl_url('https://example.com', params={'limit': 50})

# Poll status
while True:
    status = app.get_crawl_status(crawl_id)
    if status['status'] == 'completed':
        break
    time.sleep(5)

# Get results (paginated if > 10MB)
results = status['data']
if 'next' in status:
    # More results available at status['next']
    pass
```

**Performance:**
- **Small sites** (10-20 pages): 30 seconds - 1 minute
- **Medium sites** (50-100 pages): 1-5 minutes
- **Large sites** (500+ pages): 5-30 minutes

**Cost**: 1 credit per page crawled

**Response Structure:**
```python
{
    'success': True,
    'id': 'crawl-abc123',
    'status': 'completed',
    'total': 47,
    'completed': 47,
    'data': [
        {
            'markdown': '...',
            'html': '...',
            'metadata': {...},
            'url': 'https://example.com/page1'
        },
        # ... more pages
    ],
    'next': None  # or URL to next batch if > 10MB
}
```

---

### 3. Map (URL Discovery)

**Purpose**: Quickly discover all URLs on a website without scraping content

**When to Use:**
- Site structure analysis
- URL list generation for selective scraping
- Sitemap verification
- Pre-crawl planning

**Key Difference from Crawl:**
- **Map**: Returns URLs only (very fast, cheap)
- **Crawl**: Returns URLs + scraped content (slower, more expensive)

**Key Parameters:**
```python
params = {
    'search': 'blog',        # Filter URLs containing 'blog'
    'limit': 100,            # Max URLs to return
    'sitemap': 'include',    # 'only', 'include', 'skip'
    'includeSubdomains': True
}
```

**Performance:**
- **Typical**: 1-5 seconds (extremely fast)
- Works with sitemaps when available for instant results

**Cost**: 1 credit per map request

**Response Structure:**
```python
{
    'success': True,
    'links': [
        'https://example.com/page1',
        'https://example.com/page2',
        'https://example.com/blog/post1',
        # ... more URLs
    ]
}
```

**Example Workflow:**
```python
# Step 1: Map to get all URLs
map_result = app.map_url('https://example.com', params={'limit': 500})

# Step 2: Filter URLs you want
blog_urls = [url for url in map_result['links'] if '/blog/' in url]

# Step 3: Batch scrape only the URLs you need
batch_result = app.batch_scrape_urls(blog_urls[:20], params={'formats': ['markdown']})
```

---

### 4. Search (Web Search + Scrape)

**Purpose**: Search the web and scrape results in one operation

**When to Use:**
- Research tasks (find + extract info)
- Competitive analysis
- News monitoring
- Content aggregation

**Key Parameters:**
```python
params = {
    'formats': ['markdown'],
    'limit': 5,                  # Number of results to scrape
    'location': 'us',            # Search location
    'source': 'web',             # 'web', 'news', 'images'
    'scrapeOptions': {           # Options for each result
        'formats': ['markdown'],
        'onlyMainContent': True
    }
}
```

**Performance:**
- **Typical**: 5-15 seconds for 5 results
- Performs search + scrapes each result

**Cost**: Varies (search + scrapes combined)

**Response Structure:**
```python
{
    'success': True,
    'data': [
        {
            'markdown': '...',
            'metadata': {
                'title': '...',
                'description': '...',
                'url': 'https://...'
            }
        },
        # ... more results
    ]
}
```

**Example:**
```python
result = app.search('latest developments in quantum computing', params={
    'formats': ['markdown'],
    'limit': 5
})

for item in result['data']:
    print(f"Title: {item['metadata']['title']}")
    print(f"Content: {item['markdown'][:200]}...")
```

---

### 5. Extract (AI-Powered Structured Data)

**Purpose**: Extract structured data using AI (with or without schema)

**When to Use:**
- Product data extraction
- Contact information gathering
- Event details extraction
- Custom structured data needs

**Two Modes:**

**Mode 1: Schema-Based (Recommended)**
```python
from pydantic import BaseModel

class ProductInfo(BaseModel):
    name: str
    price: float
    availability: str
    rating: float | None

result = app.scrape_url('https://example.com/product', params={
    'formats': [{
        'type': 'json',
        'schema': ProductInfo.model_json_schema()
    }]
})
```

**Mode 2: Prompt-Based (Schemaless)**
```python
result = app.scrape_url('https://example.com', params={
    'formats': [{
        'type': 'json',
        'prompt': 'Extract all product names, prices, and availability status'
    }]
})
```

**Multi-Page Extraction:**
```python
# Extract from entire website
extract_id = app.start_extract_url('https://example.com', params={
    'schema': schema,
    'limit': 50  # Max pages to extract from
})

# Poll status
status = app.get_extract_status(extract_id)
```

**Performance:**
- **Single page**: 10-30 seconds (LLM processing)
- **Multi-page**: Varies based on pages

**Cost**: Token-based (LLM API costs)

**Response Structure:**
```python
{
    'success': True,
    'data': {
        'name': 'Product Name',
        'price': 29.99,
        'availability': 'In Stock',
        'rating': 4.5
    }
}
```

---

## Advanced Features

### 1. Actions (Browser Automation)

**Purpose**: Interact with pages before scraping (click, scroll, input, wait)

**Supported Actions:**

```python
actions = [
    # Wait for page load
    {'type': 'wait', 'milliseconds': 2000},

    # Click element
    {'type': 'click', 'selector': 'button.load-more'},

    # Type text
    {'type': 'write', 'selector': 'input[name="search"]', 'text': 'query'},

    # Press key
    {'type': 'press', 'key': 'Enter'},

    # Scroll
    {'type': 'scroll', 'direction': 'down'},  # or 'up'

    # Scrape sub-element
    {'type': 'scrape', 'selector': '.results'},

    # Execute JavaScript
    {'type': 'executeJavascript', 'script': 'window.scrollTo(0, document.body.scrollHeight)'},

    # Take screenshot
    {'type': 'screenshot'}
]
```

**Best Practices:**
1. **Always use `wait`** before and after actions
2. **Chain actions logically** (wait → click → wait → scrape)
3. **Use selectors carefully** (test in DevTools first)
4. **Limit action complexity** (keep sequences short)

**Example Workflow:**
```python
# Search Google, click first result, scrape
result = app.scrape_url('https://google.com', params={
    'actions': [
        {'type': 'wait', 'milliseconds': 2000},
        {'type': 'write', 'selector': 'input[name="q"]', 'text': 'Firecrawl'},
        {'type': 'press', 'key': 'Enter'},
        {'type': 'wait', 'milliseconds': 3000},
        {'type': 'click', 'selector': 'h3'},
        {'type': 'wait', 'milliseconds': 2000}
    ],
    'formats': ['markdown']
})
```

---

### 2. Authenticated Scraping (Cookie-Based)

⚠️ **Legal Warning**: Only use authenticated scraping on systems where you have explicit permission from both parties (yourself and the platform owner). Using session cookies improperly can violate terms of service or laws.

**Process:**

**Step 1: Extract Cookies from DevTools**
1. Login to the website manually
2. Open DevTools (F12)
3. Go to Application (Chrome) or Storage (Firefox) tab
4. Expand Cookies → Click domain
5. Find authentication cookie (e.g., `auth-token`, `session-id`)
6. Copy the cookie value

**Step 2: Use Cookie with Firecrawl**
```python
result = app.scrape_url('https://example.com/protected', params={
    'headers': {
        'Cookie': 'auth-token=YOUR_COOKIE_VALUE_HERE'
    }
})
```

**Cookie Expiration:**
- **Internal tools**: Often 7-30 days
- **Public sites**: Often hours or minutes

**Best Practices:**
1. **Store cookies securely** (environment variables)
2. **Never commit cookies** to version control
3. **Rotate cookies regularly**
4. **Monitor for 401/403 errors** (expired cookies)
5. **Use `.env` files** with `.gitignore`

**Example with Environment Variables:**
```python
import os

result = app.scrape_url('https://internal-tool.com/dashboard', params={
    'headers': {
        'Cookie': os.getenv('INTERNAL_TOOL_COOKIE')
    }
})
```

---

### 3. Caching (maxAge Parameter)

**Purpose**: Speed up scraping by 500% using cached results

**How It Works:**
- Firecrawl caches all scrape results
- If cached version is newer than `maxAge`, returns instantly
- Otherwise, scrapes fresh and updates cache

**Default**: `maxAge = 172800000` (2 days)

**Common Values:**
```python
# Always fresh (no cache)
maxAge = 0

# 5 minutes
maxAge = 300000

# 1 hour
maxAge = 3600000

# 1 day
maxAge = 86400000

# 1 week
maxAge = 604800000

# 2 days (default)
maxAge = 172800000
```

**When to Use Caching:**
- ✓ Documentation sites
- ✓ Product catalogs (static)
- ✓ Historical data
- ✓ Development/testing
- ✓ Bulk processing

**When NOT to Use Caching:**
- ✗ Real-time data (stock prices, live scores)
- ✗ Frequently updated content
- ✗ Time-sensitive applications

**Example:**
```python
# Use 1-hour cache for documentation
result = app.scrape_url('https://docs.example.com', params={
    'maxAge': 3600000,
    'formats': ['markdown']
})
```

**Disable Caching for Specific Request:**
```python
result = app.scrape_url('https://example.com', params={
    'storeInCache': False  # Don't cache this result
})
```

---

### 4. Batch Operations

**Purpose**: Scrape multiple URLs simultaneously

**When to Use vs. Crawl:**
- **Batch**: Known URLs, parallel scraping
- **Crawl**: Unknown URLs, discovery + scraping

**Two Methods:**

**Method 1: Wait for Completion**
```python
urls = ["url1.com", "url2.com", "url3.com"]
result = app.batch_scrape_urls(urls, params={'formats': ['markdown']})
```

**Method 2: Start and Poll**
```python
batch_id = app.start_batch_scrape_urls(urls, params={'formats': ['markdown']})

# Poll status
status = app.get_batch_scrape_status(batch_id)

# Get errors (if any)
errors = app.get_batch_scrape_errors(batch_id)
```

**Performance:**
- Parallel processing (much faster than sequential)
- **Typical**: 1-3 minutes for 20-50 URLs

**Cost**: 1 credit per URL

**Response Structure:**
```python
{
    'success': True,
    'id': 'batch-abc123',
    'status': 'completed',
    'total': 3,
    'completed': 3,
    'data': [
        {'markdown': '...', 'metadata': {...}, 'url': 'url1.com'},
        {'markdown': '...', 'metadata': {...}, 'url': 'url2.com'},
        {'markdown': '...', 'metadata': {...}, 'url': 'url3.com'}
    ]
}
```

**Handling Partial Failures:**
```python
# Some URLs may fail (404, timeout, etc.)
errors = app.get_batch_scrape_errors(batch_id)
for error in errors:
    print(f"Failed: {error['url']} - {error['error']}")
```

---

### 5. MCP Server Integration

**What is MCP?**
Model Context Protocol - a standard for connecting AI assistants to data sources.

**Firecrawl MCP Server** allows you to use Firecrawl directly from:
- Claude Code
- Cursor
- VSCode
- Windsurf
- n8n
- Claude Desktop

**Installation Patterns:**

**For Cursor:**
```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "your-api-key"
      }
    }
  }
}
```

**For Claude Code:**
```bash
claude code mcp add firecrawl --key your-api-key
```

**For n8n (Streamable HTTP):**
```bash
# Start MCP server in HTTP mode
HTTP_STREAMABLE_SERVER=true npx -y firecrawl-mcp

# Use endpoint: http://localhost:3000/v2/mcp
```

**Available Tools via MCP:**
- `firecrawl_scrape` - Scrape single URL
- `firecrawl_crawl` - Crawl website
- `firecrawl_map` - Map URLs
- `firecrawl_search` - Search web
- `firecrawl_batch_scrape` - Batch scrape

**Example Usage in Claude Code:**
```
User: "Use Firecrawl to scrape https://example.com"
Claude: [Automatically calls firecrawl_scrape via MCP]
```

---

## Output Formats

### 1. Markdown (Default)
Clean markdown optimized for LLMs
```python
{'formats': ['markdown']}
```

### 2. HTML
Cleaned HTML (ads/scripts removed)
```python
{'formats': ['html']}
```

### 3. Raw HTML
Original HTML with no modifications
```python
{'formats': ['rawHtml']}
```

### 4. Links
All links from the page
```python
{'formats': ['links']}
```

### 5. Images
All image URLs from the page
```python
{'formats': ['images']}
```

### 6. Summary
AI-generated summary
```python
{'formats': ['summary']}
```

### 7. JSON (Structured Data)

**With Schema:**
```python
{'formats': [{
    'type': 'json',
    'schema': {
        'type': 'object',
        'properties': {
            'title': {'type': 'string'},
            'price': {'type': 'number'}
        }
    }
}]}
```

**Without Schema (Prompt):**
```python
{'formats': [{
    'type': 'json',
    'prompt': 'Extract product names and prices'
}]}
```

### 8. Screenshot

**Basic:**
```python
{'formats': [{'type': 'screenshot'}]}
```

**Full Page:**
```python
{'formats': [{
    'type': 'screenshot',
    'fullPage': True,
    'quality': 100,
    'viewport': {'width': 1920, 'height': 1080}
}]}
```

### 9. Branding
Extract brand identity (colors, fonts, spacing, components)
```python
{'formats': ['branding']}
```

**Response:**
```python
{
    'branding': {
        'colorScheme': 'light',
        'logo': 'https://...',
        'colors': {
            'primary': '#FF713C',
            'secondary': '#...',
            'background': '#fff'
        },
        'fonts': ['Inter', 'Roboto'],
        'typography': {...},
        'spacing': {...},
        'components': {...}
    }
}
```

---

## Integration Patterns

### 1. LangChain (Python)

```python
from langchain_community.document_loaders import FireCrawlLoader

loader = FireCrawlLoader(
    url="https://example.com",
    mode="scrape",  # or "crawl"
    api_key="your-api-key",
    params={'formats': ['markdown']}
)

docs = loader.load()
```

### 2. LlamaIndex

```python
from llama_index.readers.web import FirecrawlWebReader

reader = FirecrawlWebReader(api_key="your-api-key")
documents = reader.load_data(url="https://example.com")
```

### 3. AI SDK (Vercel)

```typescript
import { FirecrawlApp } from 'firecrawl';
import { openai } from '@ai-sdk/openai';
import { generateText } from 'ai';

const app = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Scrape
const scrapeResult = await app.scrapeUrl('https://example.com');

// Send to LLM
const result = await generateText({
  model: openai('gpt-4'),
  prompt: `Summarize: ${scrapeResult.markdown}`
});
```

### 4. Gemini

```python
from firecrawl import FirecrawlApp
import google.generativeai as genai

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Scrape
result = app.scrape_url('https://example.com')

# Analyze with Gemini
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(f"Analyze: {result['markdown']}")
```

### 5. n8n Workflow

1. Add AI Agent node
2. Add Tool → MCP Client Tool
3. Endpoint: `http://localhost:3000/v2/mcp` (or hosted)
4. Server Transport: HTTP Streamable
5. Authentication: None
6. Select Firecrawl tools

---

## Platform-Specific Guides

### Amazon

**Product Scraping:**
```python
# With schema
class AmazonProduct(BaseModel):
    title: str
    price: float
    rating: float
    availability: str

result = app.scrape_url('https://amazon.com/product/...', params={
    'formats': [{'type': 'json', 'schema': AmazonProduct.model_json_schema()}]
})
```

**Search Products:**
```python
result = app.search('laptop under $1000 site:amazon.com', params={
    'formats': ['markdown'],
    'limit': 5
})
```

### GitHub

**Repository Scraping:**
```python
# Scrape README
result = app.scrape_url('https://github.com/user/repo')

# Crawl all docs
result = app.crawl_url('https://github.com/user/repo/tree/main/docs', params={
    'limit': 50,
    'scrapeOptions': {'formats': ['markdown']}
})
```

### Wikipedia

**Article Extraction:**
```python
class WikipediaInfo(BaseModel):
    title: str
    summary: str
    infobox: dict

result = app.scrape_url('https://en.wikipedia.org/wiki/Artificial_intelligence', params={
    'formats': [{'type': 'json', 'schema': WikipediaInfo.model_json_schema()}]
})
```

### Documentation Sites

**Crawl Entire Docs:**
```python
result = app.crawl_url('https://docs.example.com', params={
    'limit': 500,
    'includeUrlPatterns': ['^/docs/.*$'],
    'scrapeOptions': {
        'formats': ['markdown'],
        'onlyMainContent': True,
        'maxAge': 86400000  # 1 day cache
    }
})
```

---

## Cost & Performance

### Rate Limits by Plan

| Plan | Concurrent Browsers | Requests/Min | Requests/Hour |
|------|---------------------|--------------|---------------|
| Free | 2 | 10 | 500 |
| Hobby | 5 | 100 | 5,000 |
| Standard | 50 | 500 | 25,000 |
| Growth | 100 | 5,000 | 250,000 |

### Credit Costs

| Operation | Cost |
|-----------|------|
| Scrape | 1 credit |
| Crawl | 1 credit/page |
| Map | 1 credit |
| Search | Varies |
| Extract | Token-based |
| Batch | 1 credit/URL |

### Performance Benchmarks

| Operation | Cached | Fresh | Notes |
|-----------|--------|-------|-------|
| Scrape | < 500ms | 2-10s | Simple pages faster |
| Crawl (10 pages) | N/A | 30s-1min | Parallel processing |
| Crawl (100 pages) | N/A | 1-5min | Depends on site |
| Map | N/A | 1-5s | Very fast |
| Search (5 results) | N/A | 5-15s | Search + scrapes |
| Extract | N/A | 10-30s | LLM processing |
| Batch (20 URLs) | Mixed | 1-3min | Parallel |

### Cost Optimization Strategies

1. **Use `maxAge` for caching** (500% speed improvement)
2. **Map before crawl** (discover URLs first, then selective scrape)
3. **Batch instead of sequential** (parallel processing)
4. **Use `onlyMainContent: true`** (reduces data transfer)
5. **Filter with `includeTags`/`excludeTags`** (targeted extraction)
6. **Set appropriate `limit`** on crawls (don't over-crawl)
7. **Use `includeUrlPatterns`** to limit crawl scope

**Example:**
```python
# INEFFICIENT: Crawl entire site, then filter
result = app.crawl_url('https://example.com', params={'limit': 500})
blog_posts = [p for p in result['data'] if '/blog/' in p['url']]

# EFFICIENT: Use URL patterns to crawl only blog
result = app.crawl_url('https://example.com', params={
    'limit': 100,
    'includeUrlPatterns': ['^/blog/.*$'],
    'scrapeOptions': {
        'onlyMainContent': True,
        'maxAge': 86400000
    }
})
```

---

## Troubleshooting

### Issue 1: Rate Limiting (429 Errors)

**Symptoms:**
- `429 Too Many Requests` errors
- Scrapes failing intermittently

**Diagnosis:**
```python
try:
    result = app.scrape_url('https://example.com')
except Exception as e:
    if '429' in str(e):
        print("Rate limited!")
```

**Solutions:**

1. **Check your plan limits** (see Rate Limits table above)
2. **Add delays between requests**
```python
import time
for url in urls:
    result = app.scrape_url(url)
    time.sleep(1)  # 1 second delay
```
3. **Use batch operations** (built-in rate limiting)
4. **Upgrade plan** if hitting limits regularly

---

### Issue 2: Authentication Failures (401/403)

**Symptoms:**
- 401 Unauthorized or 403 Forbidden errors
- Authenticated pages showing login screen

**Diagnosis:**
```python
result = app.scrape_url('https://example.com/protected', params={
    'headers': {'Cookie': cookie}
})

# Check if login page appears in response
if 'login' in result['markdown'].lower():
    print("Cookie expired or invalid")
```

**Solutions:**

1. **Re-extract cookie** from DevTools after fresh login
2. **Check cookie expiration** in DevTools (Application → Cookies → Expires)
3. **Verify cookie name** (might be multiple cookies needed)
4. **Include all required cookies**
```python
headers = {
    'Cookie': f'session-id={session}; auth-token={token}; csrf={csrf}'
}
```

---

### Issue 3: Dynamic Content Not Loading

**Symptoms:**
- Content appears in browser but not in scraped result
- JavaScript-rendered content missing

**Diagnosis:**
- Open page in browser
- Disable JavaScript
- If content disappears, it's dynamic

**Solutions:**

1. **Add `waitFor` delay**
```python
result = app.scrape_url('https://example.com', params={
    'waitFor': 5000  # Wait 5 seconds for JS to load
})
```

2. **Use actions to trigger loading**
```python
result = app.scrape_url('https://example.com', params={
    'actions': [
        {'type': 'wait', 'milliseconds': 3000},
        {'type': 'scroll', 'direction': 'down'},
        {'type': 'wait', 'milliseconds': 2000}
    ]
})
```

3. **Scroll to load lazy content**
```python
actions = [
    {'type': 'scroll', 'direction': 'down'},
    {'type': 'wait', 'milliseconds': 2000},
    {'type': 'scroll', 'direction': 'down'},
    {'type': 'wait', 'milliseconds': 2000}
]
```

---

### Issue 4: Parsing Failures / Incomplete Data

**Symptoms:**
- Missing content sections
- Ads/footers included when not wanted

**Solutions:**

1. **Use `onlyMainContent: true`** (default)
```python
params = {'onlyMainContent': True}
```

2. **Specify `includeTags`**
```python
params = {
    'includeTags': ['article', '.content', 'h1', 'h2', 'p']
}
```

3. **Specify `excludeTags`**
```python
params = {
    'excludeTags': ['#ads', '.footer', 'nav', '.sidebar']
}
```

4. **Combine both for precision**
```python
params = {
    'includeTags': ['.article-content'],
    'excludeTags': ['.related-posts', '.comments']
}
```

---

### Issue 5: MCP Connection Issues

**Symptoms:**
- MCP server not appearing in tool list
- Connection refused errors

**Solutions:**

1. **Verify API key is set**
```bash
echo $FIRECRAWL_API_KEY
```

2. **Check MCP server config** (Cursor/VSCode)
```json
{
  "firecrawl": {
    "command": "npx",
    "args": ["-y", "firecrawl-mcp"],
    "env": {
      "FIRECRAWL_API_KEY": "fc-YOUR-KEY"
    }
  }
}
```

3. **Test server independently**
```bash
FIRECRAWL_API_KEY=fc-your-key npx -y firecrawl-mcp
```

4. **For HTTP mode (n8n), start server manually**
```bash
HTTP_STREAMABLE_SERVER=true FIRECRAWL_API_KEY=fc-your-key npx -y firecrawl-mcp
```

---

### Issue 6: Cost Overruns

**Symptoms:**
- Unexpected high credit usage
- Crawls consuming more credits than expected

**Diagnosis:**
```python
# Check crawl status to see actual pages crawled
status = app.get_crawl_status(crawl_id)
print(f"Total pages: {status['total']}")
```

**Solutions:**

1. **Set strict `limit`**
```python
params = {'limit': 50}  # Max 50 pages
```

2. **Use URL patterns to narrow scope**
```python
params = {
    'limit': 100,
    'includeUrlPatterns': ['^/blog/2024/.*$']  # Only 2024 blog posts
}
```

3. **Map first, then selective scrape**
```python
# Map (1 credit)
map_result = app.map_url('https://example.com')

# Filter URLs
important_urls = [url for url in map_result['links'] if is_important(url)]

# Batch scrape only important (N credits)
batch_result = app.batch_scrape_urls(important_urls[:20])
```

4. **Enable caching with appropriate `maxAge`**
```python
params = {
    'scrapeOptions': {
        'maxAge': 86400000  # Use 1-day cache
    }
}
```

---

## Security & Privacy

### Best Practices

1. **Never commit API keys** to version control
```bash
# .env file
FIRECRAWL_API_KEY=fc-your-key

# .gitignore
.env
```

2. **Store cookies securely**
```python
import os
cookie = os.getenv('INTERNAL_TOOL_COOKIE')  # From .env
```

3. **Respect robots.txt** (check manually)
```bash
curl https://example.com/robots.txt
```

4. **Follow site Terms of Service**

5. **Rate limit your requests** (be respectful)

6. **Use `onlyMainContent`** to minimize data collection

7. **Delete unused data** (don't hoard scraped content)

### Compliance

**Legal Considerations:**
- ✓ Public data (publicly accessible URLs)
- ✓ Internal tools (with permission)
- ✗ Bypassing paywalls (illegal in most jurisdictions)
- ✗ Scraping personal data without consent (GDPR violation)
- ✗ Violating site ToS (potential legal action)

**When in Doubt:**
- Get written permission
- Consult legal counsel
- Use public APIs when available

---

## Learning Path

### Beginner (Start Here)

1. **Read** `getting_started.md` reference
2. **Try** basic scrape workflow: `workflows/basic-scrape.md`
3. **Run** `scripts/scrape.py`
4. **Learn** output formats (markdown, html, json)

### Intermediate

1. **Try** crawl workflow: `workflows/crawl-site.md`
2. **Run** `scripts/crawl.py`
3. **Learn** URL patterns (includeUrlPatterns, excludeUrlPatterns)
4. **Try** batch scrape workflow: `workflows/batch-scrape.md`
5. **Learn** caching (`maxAge` parameter)

### Advanced

1. **Try** extract workflow: `workflows/extract-structured-data.md`
2. **Run** `scripts/extract.py`
3. **Learn** schema design (Pydantic, JSON Schema)
4. **Try** authenticated scrape: `workflows/authenticated-scrape.md`
5. **Run** `scripts/auth_scrape.py`
6. **Learn** actions: `workflows/actions-automation.md`

### Expert

1. **Setup** MCP integration: `workflows/mcp-integration.md`
2. **Integrate** with LangChain/LlamaIndex
3. **Build** custom workflows (n8n, Zapier)
4. **Optimize** for cost and performance
5. **Handle** edge cases and errors gracefully

---

## Workflow Execution Guide

For executable step-by-step instructions, load workflows from the `workflows/` directory.

### Available Workflows

#### Essential Workflows (Core Features)

1. **basic-scrape.md** - Single URL scraping
   - Duration: 5-10 seconds
   - Cost: 1 credit
   - Use: Product pages, articles, documentation

2. **crawl-site.md** - Multi-page website crawling
   - Duration: 30s-5min (depends on site size)
   - Cost: 1 credit per page
   - Use: Documentation sites, blog archives, e-commerce categories

3. **batch-scrape.md** - Scrape multiple URLs simultaneously
   - Duration: 1-3 minutes
   - Cost: 1 credit per URL
   - Use: Known URL lists, parallel processing

4. **map-urls.md** - Fast URL discovery
   - Duration: 1-5 seconds
   - Cost: 1 credit
   - Use: Site structure analysis, pre-crawl planning

5. **extract-structured-data.md** - AI-powered data extraction
   - Duration: 10-30 seconds
   - Cost: Token-based
   - Use: Product data, contact info, custom schemas

#### Advanced Workflows

6. **authenticated-scrape.md** - Scraping behind authentication
   - Duration: 10-20 seconds
   - Cost: 1 credit
   - Use: Internal tools, authenticated content

7. **mcp-integration.md** - Using Firecrawl via MCP servers
   - Duration: Varies
   - Cost: API-based
   - Use: Claude Code, Cursor, VSCode integration

8. **actions-automation.md** - Browser interactions before scraping
   - Duration: 15-30 seconds
   - Cost: 1 credit
   - Use: Dynamic content, form filling, click-then-scrape

### Workflow Selection Guide

| User Request | Workflow | Rationale |
|--------------|----------|-----------|
| "Scrape this URL" | basic-scrape.md | Single page extraction |
| "Crawl website" | crawl-site.md | Multi-page discovery |
| "Scrape these 20 URLs" | batch-scrape.md | Known URLs, parallel |
| "Get all URLs from site" | map-urls.md | URL discovery only |
| "Extract product data" | extract-structured-data.md | Structured extraction |
| "Scrape behind login" | authenticated-scrape.md | Requires authentication |
| "Use in Cursor/VSCode" | mcp-integration.md | MCP integration |
| "Click then scrape" | actions-automation.md | Browser automation |

### How to Load Workflows

```
Read /Users/michaelatherton/Documents/condaEnv/AIRL/PAI/.claude/skills/firecrawl/workflows/[workflow-name].md
```

Each workflow contains:
- **Mission**: What to accomplish
- **When to Use**: Activation conditions
- **Steps**: Executable procedures
- **Code Examples**: Copy-paste ready
- **Error Handling**: Common issues and solutions
- **Complete Example**: Full working code

---

**End of CLAUDE.md** - For quick reference, see SKILL.md. For executable workflows, see workflows/ directory.
