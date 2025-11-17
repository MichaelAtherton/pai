---
description: Batch scrape workflow - Lucy scrapes multiple known URLs simultaneously in parallel
globs: ""
alwaysApply: false
---

# 📦 BATCH SCRAPE WORKFLOW

**YOU (Lucy) are reading this because the user wants to scrape multiple URLs.**

## 🎯 WHEN TO USE

**User says:**
- "Scrape these URLs"
- "Batch scrape these pages"
- "Scrape multiple URLs"
- Has a list of specific URLs to scrape

## 📋 MISSION

Scrape multiple known URLs in parallel for fast processing.

## ⚡ STEPS

### Step 1: Prepare URL List

```python
from firecrawl import FirecrawlApp
import os

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]
```

### Step 2: Configure Batch Options

```python
params = {
    'formats': ['markdown'],
    'onlyMainContent': True,
    'maxAge': 86400000  # 1-day cache
}
```

### Step 3: Execute Batch Scrape (Two Methods)

**Method 1: Wait for completion**
```python
result = app.batch_scrape_urls(urls, params=params)
# Returns when all URLs scraped
```

**Method 2: Start and poll**
```python
import time

batch_id = app.start_batch_scrape_urls(urls, params=params)

while True:
    status = app.get_batch_scrape_status(batch_id)
    print(f"Progress: {status['completed']}/{status['total']}")

    if status['status'] == 'completed':
        break
    time.sleep(3)

result = status['data']
```

### Step 4: Handle Partial Failures

```python
# Check for errors
errors = app.get_batch_scrape_errors(batch_id)

for error in errors:
    print(f"Failed: {error['url']} - {error['error']}")
```

## 🎯 COMPLETE EXAMPLE

```python
from firecrawl import FirecrawlApp
import os

def batch_scrape(urls: list, formats: list = None):
    """Batch scrape multiple URLs."""
    app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    params = {
        'formats': formats or ['markdown'],
        'onlyMainContent': True
    }

    result = app.batch_scrape_urls(urls, params=params)

    if result.get('success'):
        return result['data']
    else:
        raise Exception("Batch scrape failed")

# Usage
urls = [
    "https://firecrawl.dev",
    "https://docs.firecrawl.dev",
    "https://firecrawl.dev/blog"
]

pages = batch_scrape(urls, formats=['markdown', 'links'])
print(f"Scraped {len(pages)} pages")
```

---

**END OF WORKFLOW**
