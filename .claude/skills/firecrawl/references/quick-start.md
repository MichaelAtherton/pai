# Firecrawl Quick Start Examples

Additional code examples for common Firecrawl use cases.

For the 4 most essential examples, see SKILL.md Quick Reference section.

---

## Authenticated Scraping (Cookie-Based)

Scrape content behind authentication using cookies extracted from browser DevTools.

**Important:** Only use on systems with explicit permission.

```python
from firecrawl import FirecrawlApp
import os

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

# Extract cookie from DevTools first (F12 → Application → Cookies)
result = app.scrape_url('https://example.com/protected', params={
    'headers': {
        'Cookie': 'auth-token=YOUR_TOKEN_HERE'
    },
    'formats': ['markdown']
})
```

**Cookie Extraction Steps:**
1. Login to website manually
2. Open DevTools (F12)
3. Go to Application (Chrome) or Storage (Firefox)
4. Expand Cookies → Select domain
5. Find auth cookie (e.g., `auth-token`, `session-id`)
6. Copy cookie value

**Security:**
- Store in environment variables: `os.getenv('AUTH_COOKIE')`
- Never commit cookies to version control
- Monitor expiration (check DevTools "Expires" field)

---

## Browser Actions (Click/Scroll/Input)

Automate browser interactions before scraping dynamic content.

```python
result = app.scrape_url('https://google.com', params={
    'actions': [
        {'type': 'wait', 'milliseconds': 2000},
        {'type': 'write', 'selector': 'input[name="q"]', 'text': 'Firecrawl'},
        {'type': 'click', 'selector': 'button[type="submit"]'},
        {'type': 'wait', 'milliseconds': 3000},
        {'type': 'screenshot'}
    ],
    'formats': ['markdown', {'type': 'screenshot'}]
})
```

**Supported Actions:**
- `wait` - Wait for page load
- `click` - Click element by selector
- `write` - Type text into input field
- `press` - Press keyboard key
- `scroll` - Scroll up/down
- `executeJavascript` - Run custom JavaScript
- `screenshot` - Capture screenshot

**Best Practices:**
- Always use `wait` before and after actions
- Test selectors in browser DevTools first
- Keep action sequences under 10 steps
- Use 2-3 second waits for page loads

---

## Fast Mode (Caching)

Speed up scraping by 500% using cached results.

```python
# Use cached version if less than 1 hour old
result = app.scrape_url('https://example.com', params={
    'maxAge': 3600000  # 1 hour in milliseconds
})
```

**Common maxAge Values:**
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
- ✓ Product catalogs (static content)
- ✓ Historical data
- ✓ Development/testing
- ✓ Bulk processing

**When NOT to Cache:**
- ✗ Real-time data (stock prices, live scores)
- ✗ Frequently updated content
- ✗ Time-sensitive applications

**Disable Caching:**
```python
result = app.scrape_url('https://example.com', params={
    'storeInCache': False  # Don't cache this request
})
```

---

## Map Website URLs

Quickly discover all URLs from a website without scraping content.

**Much faster and cheaper than crawling when you only need URL lists.**

```python
# Get all URLs from a website (very fast: 1-5 seconds)
result = app.map_url('https://example.com', params={
    'search': 'blog',  # Optional: filter URLs containing 'blog'
    'limit': 100,
    'sitemap': 'include'  # Use sitemap if available
})

urls = result['links']
print(f"Found {len(urls)} URLs")

# Filter URLs
blog_urls = [url for url in urls if '/blog/' in url]
```

**Map vs. Crawl:**
- **Map**: Returns URLs only (fast, 1 credit)
- **Crawl**: Returns URLs + content (slower, 1 credit per page)

**Workflow: Map First, Then Selective Scrape**
```python
# Step 1: Map to get all URLs (1 credit)
map_result = app.map_url('https://example.com', params={'limit': 500})

# Step 2: Filter URLs you want
important_urls = [url for url in map_result['links'] if '/docs/' in url]

# Step 3: Batch scrape only what you need (N credits)
batch_result = app.batch_scrape_urls(important_urls[:20], params={
    'formats': ['markdown']
})
```

**Cost Savings Example:**
- Map entire site: 1 credit
- Scrape 20 specific pages: 20 credits
- **Total: 21 credits**
- vs. Crawling 500 pages: 500 credits
- **Savings: 479 credits (96% reduction)**

---

## Search Web + Scrape Results

Search the web and scrape result pages in one operation.

```python
result = app.search('latest AI developments', params={
    'formats': ['markdown'],
    'limit': 5,
    'source': 'web',  # or 'news', 'images'
    'location': 'us'
})

for item in result['data']:
    title = item['metadata']['title']
    url = item['metadata']['url']
    content = item['markdown']
    print(f"{title}: {url}")
```

**Parameters:**
- `limit` - Number of results to scrape (default: 5)
- `source` - 'web', 'news', or 'images'
- `location` - Search location (e.g., 'us', 'uk')
- `scrapeOptions` - Options for each result page

**Performance:** 5-15 seconds for 5 results

**Cost:** Search + N scrapes (varies by plan)

---

## Extract with AI (No Schema)

Extract structured data using prompts instead of schemas.

```python
# Schemaless extraction with prompt
result = app.scrape_url('https://example.com', params={
    'formats': [{
        'type': 'json',
        'prompt': 'Extract all product names, prices, and ratings from this page'
    }]
})

data = result['data']
# Returns: {'products': [{'name': '...', 'price': '...', 'rating': '...'}]}
```

**Schema vs. Prompt:**

**With Schema (Recommended):**
- More reliable structure
- Type validation
- Predictable output format

**With Prompt (Flexible):**
- No schema definition needed
- LLM determines structure
- Good for exploration/prototyping

**Example Prompts:**
```python
# Contact information
prompt = 'Extract all email addresses, phone numbers, and social media links'

# Event details
prompt = 'Extract event name, date, time, location, and ticket price'

# Company info
prompt = 'Extract company name, industry, founding year, and headquarters location'
```

---

## Advanced: Hybrid Extraction

Combine multiple formats in one request.

```python
result = app.scrape_url('https://example.com/product', params={
    'formats': [
        'markdown',
        'links',
        {'type': 'screenshot', 'fullPage': True},
        {
            'type': 'json',
            'schema': ProductSchema.model_json_schema()
        }
    ],
    'onlyMainContent': True
})

# Access each format
markdown = result['markdown']
links = result['links']
screenshot = result['screenshot']  # base64 encoded
product_data = result['data']  # structured JSON
```

**Use Cases:**
- Content + screenshot for archival
- Text + links for analysis
- Structure + images for cataloging
- Multi-format export for downstream processing

---

## Performance Optimization

Optimize for speed and cost.

**1. Use Targeted Scraping:**
```python
params = {
    'includeTags': ['.article-content', 'article', 'main'],
    'excludeTags': ['#ads', '.sidebar', 'nav', '.comments'],
    'onlyMainContent': True
}
```

**2. Aggressive Caching:**
```python
params = {'maxAge': 604800000}  # 1 week
```

**3. Map Before Crawl:**
```python
# Don't crawl blindly
urls = app.map_url('https://example.com')['links']
filtered = [u for u in urls if '/important/' in u]
app.batch_scrape_urls(filtered)
```

**4. Batch Instead of Sequential:**
```python
# Parallel processing (fast)
app.batch_scrape_urls(urls)

# vs. Sequential (slow)
for url in urls:
    app.scrape_url(url)
```

---

## Error Handling Patterns

Robust error handling for production use.

```python
import time

def scrape_with_retry(url, max_retries=3):
    """Scrape with automatic retry on failure."""
    for attempt in range(max_retries):
        try:
            result = app.scrape_url(url, params={
                'formats': ['markdown'],
                'timeout': 30000
            })

            if result.get('success'):
                return result
            else:
                print(f"Attempt {attempt + 1} failed")

        except Exception as e:
            if '429' in str(e):
                # Rate limited - wait longer
                wait = (attempt + 1) * 5
                print(f"Rate limited. Waiting {wait}s...")
                time.sleep(wait)
            elif '401' in str(e) or '403' in str(e):
                # Auth error - don't retry
                raise Exception("Authentication failed")
            else:
                print(f"Error: {e}")

        if attempt < max_retries - 1:
            time.sleep(2)

    raise Exception(f"Failed after {max_retries} attempts")

# Usage
result = scrape_with_retry('https://example.com')
```

---

## Related Documentation

- **SKILL.md** - 4 essential examples and quick reference
- **references/parameters.md** - Detailed parameter documentation
- **scripts/** - Runnable example scripts
- **workflows/** - Step-by-step execution guides
- **CLAUDE.md** - Comprehensive deep context

---

This file contains supplementary examples. For core usage, always start with SKILL.md.
