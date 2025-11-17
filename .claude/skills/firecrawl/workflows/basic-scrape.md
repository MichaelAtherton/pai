---
description: Basic scraping workflow - Lucy scrapes a single URL and returns clean data in requested formats
globs: ""
alwaysApply: false
---

# 🔬 BASIC SCRAPE WORKFLOW

**YOU (Lucy) are reading this because the user requested to scrape a single URL.**

## 🎯 WHEN TO USE

**User says:**
- "Scrape this URL"
- "Extract data from [URL]"
- "Get content from this page"
- "Screenshot this website"
- "Convert this page to markdown"

## 📋 MISSION

Scrape a single webpage and return clean, LLM-ready data in the requested format(s).

## ⚡ STEPS

### Step 1: Setup

```python
from firecrawl import FirecrawlApp
import os

# Initialize Firecrawl
app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
```

**Verify API key is set:**
```python
api_key = os.getenv("FIRECRAWL_API_KEY")
if not api_key:
    raise ValueError("FIRECRAWL_API_KEY not set. Get one from https://firecrawl.dev")
```

### Step 2: Determine Required Formats

**Ask yourself:** What format does the user need?

- **Default**: `['markdown']` - Clean markdown for LLMs
- **Multiple formats**: `['markdown', 'html', 'links']`
- **Screenshot**: `[{'type': 'screenshot'}]`
- **Structured data**: `[{'type': 'json', 'schema': schema}]`

**Common combinations:**
```python
# Text + links
formats = ['markdown', 'links']

# Text + screenshot
formats = ['markdown', {'type': 'screenshot', 'fullPage': True}]

# Everything
formats = ['markdown', 'html', 'links', 'images']
```

### Step 3: Configure Scrape Options

```python
params = {
    'formats': ['markdown'],           # What to return
    'onlyMainContent': True,           # Skip ads/nav/footer (default: True)
    'waitFor': 0,                      # Wait ms before scraping (if needed)
    'maxAge': 86400000,                # Use 1-day cache (default: 2 days)
    'timeout': 30000,                  # 30s timeout (default)
}
```

**Optional refinements:**
```python
# Include only specific content
params['includeTags'] = ['article', '.content', 'h1', 'h2', 'p']

# Exclude noise
params['excludeTags'] = ['#ads', '.footer', 'nav', '.comments']
```

### Step 4: Execute Scrape

```python
try:
    result = app.scrape_url('https://example.com', params=params)

    # Check success
    if result.get('success'):
        print("✓ Scrape successful!")
    else:
        print("✗ Scrape failed")

except Exception as e:
    print(f"Error: {e}")
```

### Step 5: Extract and Return Data

```python
# Markdown
markdown = result.get('markdown', '')

# HTML (if requested)
html = result.get('html', '')

# Links (if requested)
links = result.get('links', [])

# Metadata (always included)
metadata = result.get('metadata', {})
title = metadata.get('title', '')
description = metadata.get('description', '')

# Screenshot (if requested)
screenshot = result.get('screenshot', '')  # base64 encoded
```

## 🎯 COMPLETE EXAMPLE

```python
from firecrawl import FirecrawlApp
import os

def scrape_url_basic(url: str, formats: list = None):
    """
    Scrape a single URL and return clean data.

    Args:
        url: The URL to scrape
        formats: List of formats to return (default: ['markdown'])

    Returns:
        dict: Scraped data
    """
    # Initialize
    app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    # Default formats
    if formats is None:
        formats = ['markdown']

    # Configure params
    params = {
        'formats': formats,
        'onlyMainContent': True,
        'maxAge': 86400000,  # 1-day cache
    }

    # Scrape
    try:
        result = app.scrape_url(url, params=params)

        if result.get('success'):
            return {
                'markdown': result.get('markdown', ''),
                'html': result.get('html', ''),
                'links': result.get('links', []),
                'metadata': result.get('metadata', {}),
                'screenshot': result.get('screenshot', '')
            }
        else:
            raise Exception("Scrape failed")

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Usage
if __name__ == "__main__":
    result = scrape_url_basic(
        'https://firecrawl.dev',
        formats=['markdown', 'links']
    )

    if result:
        print(f"Title: {result['metadata'].get('title', 'N/A')}")
        print(f"Content length: {len(result['markdown'])} chars")
        print(f"Links found: {len(result['links'])}")
```

## ⚠️ ERROR HANDLING

### Error 1: API Key Missing

**Symptom:** `ValueError: API key required`

**Solution:**
```bash
export FIRECRAWL_API_KEY=fc-your-key
```

### Error 2: Rate Limiting (429)

**Symptom:** `429 Too Many Requests`

**Solution:**
```python
import time

# Add delay between requests
for url in urls:
    result = app.scrape_url(url)
    time.sleep(1)  # 1 second delay
```

### Error 3: Timeout

**Symptom:** Request times out

**Solution:**
```python
params = {
    'timeout': 60000,  # Increase to 60s
    'waitFor': 5000    # Wait longer for page load
}
```

### Error 4: Dynamic Content Missing

**Symptom:** Content appears in browser but not in scrape

**Solution:**
```python
params = {
    'waitFor': 3000,  # Wait 3s for JS to load
    'actions': [
        {'type': 'wait', 'milliseconds': 3000},
        {'type': 'scroll', 'direction': 'down'}
    ]
}
```

## 💡 PRO TIPS

1. **Use caching** for faster results:
   ```python
   params = {'maxAge': 3600000}  # 1-hour cache = 500% faster
   ```

2. **Extract only what you need**:
   ```python
   params = {'includeTags': ['.article-content']}
   ```

3. **Request multiple formats** in one call:
   ```python
   formats = ['markdown', 'links', {'type': 'screenshot'}]
   ```

4. **Check `onlyMainContent` for clean data**:
   ```python
   params = {'onlyMainContent': True}  # Skip ads/nav/footer
   ```

---

**END OF WORKFLOW** - Basic scrape complete.
