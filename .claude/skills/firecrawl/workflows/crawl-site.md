---
description: Crawl workflow - Lucy crawls entire websites, discovering and scraping multiple pages automatically
globs: ""
alwaysApply: false
---

# 🕷️ CRAWL SITE WORKFLOW

**YOU (Lucy) are reading this because the user requested to crawl a website.**

## 🎯 WHEN TO USE

**User says:**
- "Crawl this website"
- "Get all pages from [site]"
- "Scrape entire documentation"
- "Extract all blog posts"

## 📋 MISSION

Discover and scrape multiple pages from a website automatically.

## ⚡ STEPS

### Step 1: Setup

```python
from firecrawl import FirecrawlApp
import os
import time

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
```

### Step 2: Configure Crawl Parameters

```python
params = {
    'limit': 100,                          # Max pages to crawl
    'maxDiscoveryDepth': 3,                # How deep to discover
    'includeUrlPatterns': ['^/docs/.*$'],  # Only /docs/* pages
    'excludeUrlPatterns': ['^/admin/.*$'], # Skip /admin/*
    'scrapeOptions': {
        'formats': ['markdown'],
        'onlyMainContent': True,
        'maxAge': 86400000  # 1-day cache
    }
}
```

**Common patterns:**
```python
# Blog posts only
'includeUrlPatterns': ['^/blog/.*$', '^/posts/.*$']

# Exclude admin/auth pages
'excludeUrlPatterns': ['^/admin/.*$', '^/auth/.*$', '^/login.*$']

# Entire domain
'crawlEntireDomain': True
```

### Step 3: Start Crawl (Two Methods)

**Method 1: Wait for completion (SDK handles polling)**
```python
result = app.crawl_url('https://example.com', params=params)
# Returns when complete
```

**Method 2: Start and poll manually**
```python
# Start crawl
crawl_id = app.start_crawl_url('https://example.com', params=params)

# Poll status
while True:
    status = app.get_crawl_status(crawl_id)

    print(f"Status: {status['status']}")
    print(f"Progress: {status['completed']}/{status['total']}")

    if status['status'] == 'completed':
        break

    time.sleep(5)  # Wait 5s before next check

# Get results
results = status['data']
```

### Step 4: Handle Pagination

```python
# If results > 10MB, they're paginated
if 'next' in status:
    print(f"More results at: {status['next']}")
    # Use the 'next' URL to get more results
```

### Step 5: Process Results

```python
for page in result['data']:
    url = page['url']
    markdown = page['markdown']
    metadata = page['metadata']

    print(f"Page: {metadata.get('title', url)}")
    print(f"Length: {len(markdown)} chars")
```

## 🎯 COMPLETE EXAMPLE

```python
from firecrawl import FirecrawlApp
import os

def crawl_website(base_url: str, limit: int = 100, url_patterns: list = None):
    """
    Crawl a website and return all pages.

    Args:
        base_url: Starting URL
        limit: Max pages to crawl
        url_patterns: Regex patterns to include

    Returns:
        list: Crawled pages
    """
    app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    params = {
        'limit': limit,
        'maxDiscoveryDepth': 3,
        'scrapeOptions': {
            'formats': ['markdown'],
            'onlyMainContent': True
        }
    }

    if url_patterns:
        params['includeUrlPatterns'] = url_patterns

    # Crawl and wait for completion
    result = app.crawl_url(base_url, params=params)

    if result.get('success'):
        return result['data']
    else:
        raise Exception("Crawl failed")

# Usage
if __name__ == "__main__":
    pages = crawl_website(
        'https://docs.example.com',
        limit=50,
        url_patterns=['^/docs/.*$']
    )

    print(f"Crawled {len(pages)} pages")
    for page in pages[:5]:  # Show first 5
        print(f"- {page['metadata'].get('title')}: {page['url']}")
```

## ⚠️ ERROR HANDLING

### Error 1: Too Many Pages

**Solution:** Set strict limit and patterns
```python
params = {
    'limit': 50,
    'includeUrlPatterns': ['^/blog/2024/.*$']
}
```

### Error 2: Crawl Stuck/Slow

**Solution:** Check status, cancel if needed
```python
status = app.get_crawl_status(crawl_id)
if status['status'] == 'failed':
    print("Crawl failed, check errors")
```

---

**END OF WORKFLOW**
