---
description: Map URLs workflow - Lucy quickly discovers all URLs from a website without scraping content
globs: ""
alwaysApply: false
---

# 🗺️ MAP URLS WORKFLOW

**YOU (Lucy) are reading this to quickly discover URLs from a website.**

## 🎯 WHEN TO USE

**User says:**
- "Get all URLs from this site"
- "Map website structure"
- "List all pages on [site]"
- "Find all blog posts URLs"

## 📋 MISSION

Quickly discover all URLs on a website (without scraping content).

## ⚡ STEPS

### Step 1: Execute Map

```python
from firecrawl import FirecrawlApp
import os

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

result = app.map_url('https://example.com', params={
    'search': 'blog',     # Filter URLs containing 'blog'
    'limit': 100,          # Max URLs
    'sitemap': 'include'   # Use sitemap if available
})
```

### Step 2: Process URLs

```python
urls = result['links']
print(f"Found {len(urls)} URLs")

# Filter URLs
blog_urls = [url for url in urls if '/blog/' in url]
```

## 🎯 COMPLETE EXAMPLE

```python
from firecrawl import FirecrawlApp
import os

def map_website(base_url: str, search_term: str = None):
    """Map all URLs from a website."""
    app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    params = {'limit': 500}
    if search_term:
        params['search'] = search_term

    result = app.map_url(base_url, params=params)
    return result['links']

# Usage
urls = map_website('https://example.com', search_term='docs')
print(f"Found {len(urls)} documentation URLs")
```

---

**END OF WORKFLOW**
