# Firecrawl Parameters Reference

Comprehensive documentation of all parameters for Firecrawl API operations.

---

## Scrape Parameters

Used with `/scrape` endpoint and `scrape_url()` method.

### formats
- **Type**: `array`
- **Default**: `['markdown']`
- **Description**: Output formats to return

**String formats:**
- `'markdown'` - Clean markdown (default)
- `'html'` - Cleaned HTML (ads/scripts removed)
- `'rawHtml'` - Original HTML with no modifications
- `'links'` - All links from the page
- `'images'` - All image URLs
- `'summary'` - AI-generated summary
- `'branding'` - Brand identity (colors, fonts, spacing)

**Object formats:**
```python
# JSON with schema
{'type': 'json', 'schema': {...}}

# JSON with prompt (no schema)
{'type': 'json', 'prompt': 'Extract...'}

# Screenshot
{'type': 'screenshot', 'fullPage': True, 'quality': 100}

# Change tracking
{'type': 'changeTracking', 'modes': [...]}
```

**Example:**
```python
formats = ['markdown', 'links', {'type': 'screenshot', 'fullPage': True}]
```

---

### onlyMainContent
- **Type**: `boolean`
- **Default**: `true`
- **Description**: Extract only main content, skip navigation/ads/footer

**Example:**
```python
# Main content only (clean)
onlyMainContent = True

# Full page including nav/ads/footer
onlyMainContent = False
```

---

### includeTags
- **Type**: `array of strings`
- **Default**: `null`
- **Description**: HTML tags/classes/ids to include in scrape

**Examples:**
```python
# Include specific tags
includeTags = ['article', 'main', '.content']

# Include by class
includeTags = ['.product-info', '.reviews']

# Include by ID
includeTags = ['#main-content', '#description']

# Combination
includeTags = ['article', '.content', 'h1', 'h2', 'p']
```

---

### excludeTags
- **Type**: `array of strings`
- **Default**: `null`
- **Description**: HTML tags/classes/ids to exclude from scrape

**Examples:**
```python
# Exclude common noise
excludeTags = ['#ads', '.footer', 'nav', '.sidebar']

# Exclude specific sections
excludeTags = ['.comments', '.related-posts', '.social-share']

# Combination
excludeTags = ['#ad', '#footer', '.ad-container', 'script', 'style']
```

---

### waitFor
- **Type**: `integer` (milliseconds)
- **Default**: `0`
- **Description**: Wait time before scraping (for page load/JS execution)

**When to use:**
- Dynamic content loads slowly
- JavaScript-heavy pages
- AJAX content

**Examples:**
```python
# Wait 2 seconds
waitFor = 2000

# Wait 5 seconds for heavy JS
waitFor = 5000

# No wait (static content)
waitFor = 0
```

**Best Practice:** Use sparingly. Try without first, add only if content missing.

---

### maxAge
- **Type**: `integer` (milliseconds)
- **Default**: `172800000` (2 days)
- **Description**: Cache freshness. Returns cached if newer than maxAge, otherwise scrapes fresh.

**Common values:**
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

**Performance Impact:** 500% faster when cached

---

### timeout
- **Type**: `integer` (milliseconds)
- **Default**: `30000` (30 seconds)
- **Description**: Maximum duration before aborting request

**Examples:**
```python
# Default timeout
timeout = 30000

# Longer for slow sites
timeout = 60000

# Shorter for fast APIs
timeout = 15000
```

---

### parsers
- **Type**: `array of strings`
- **Default**: `[]` (auto-detect)
- **Description**: Force specific parsers

**Options:**
```python
# Force PDF parsing
parsers = ['pdf']

# Auto-detect (default)
parsers = []
```

---

### headers
- **Type**: `object`
- **Default**: `{}`
- **Description**: Custom HTTP headers (for authentication, etc.)

**Examples:**
```python
# Cookie authentication
headers = {'Cookie': 'auth-token=abc123'}

# API token
headers = {'Authorization': 'Bearer token123'}

# Multiple headers
headers = {
    'Cookie': 'session=xyz',
    'User-Agent': 'Custom/1.0'
}
```

---

### actions
- **Type**: `array of action objects`
- **Default**: `[]`
- **Description**: Browser automation actions before scraping

**Action types:**
```python
# Wait
{'type': 'wait', 'milliseconds': 2000}

# Click
{'type': 'click', 'selector': 'button.load-more'}

# Write text
{'type': 'write', 'selector': 'input[name="q"]', 'text': 'search term'}

# Press key
{'type': 'press', 'key': 'Enter'}

# Scroll
{'type': 'scroll', 'direction': 'down'}  # or 'up'

# Execute JavaScript
{'type': 'executeJavascript', 'script': 'window.scrollTo(0, 1000)'}

# Screenshot
{'type': 'screenshot'}
```

**Example sequence:**
```python
actions = [
    {'type': 'wait', 'milliseconds': 2000},
    {'type': 'write', 'selector': 'input[name="q"]', 'text': 'Firecrawl'},
    {'type': 'press', 'key': 'Enter'},
    {'type': 'wait', 'milliseconds': 3000}
]
```

---

### storeInCache
- **Type**: `boolean`
- **Default**: `true`
- **Description**: Whether to cache this request's results

**Example:**
```python
# Don't cache (one-time sensitive data)
storeInCache = False
```

---

## Crawl Parameters

Used with `/crawl` endpoint and `crawl_url()` method.

### limit
- **Type**: `integer`
- **Default**: `10000`
- **Description**: Maximum pages to crawl

**Examples:**
```python
# Small site
limit = 20

# Medium site
limit = 100

# Large site
limit = 500

# Very large (max)
limit = 10000
```

---

### maxDiscoveryDepth
- **Type**: `integer`
- **Default**: `null`
- **Description**: How many levels deep to discover URLs

**Example:**
```python
# Only direct links from start URL
maxDiscoveryDepth = 1

# Up to 3 levels deep
maxDiscoveryDepth = 3

# No limit
maxDiscoveryDepth = None
```

---

### includeUrlPatterns
- **Type**: `array of regex strings`
- **Default**: `null`
- **Description**: Regex patterns to include URLs

**Examples:**
```python
# Include only blog posts
includeUrlPatterns = ['^/blog/.*$']

# Include docs and API
includeUrlPatterns = ['^/docs/.*$', '^/api/.*$']

# Include year-specific
includeUrlPatterns = ['^/blog/2024/.*$']
```

---

### excludeUrlPatterns
- **Type**: `array of regex strings`
- **Default**: `null`
- **Description**: Regex patterns to exclude URLs

**Examples:**
```python
# Exclude admin pages
excludeUrlPatterns = ['^/admin/.*$', '^/auth/.*$']

# Exclude assets
excludeUrlPatterns = ['^/assets/.*$', '^/images/.*$']

# Exclude old content
excludeUrlPatterns = ['^/archive/.*$', '^/blog/2020/.*$']
```

---

### crawlEntireDomain
- **Type**: `boolean`
- **Default**: `false`
- **Description**: Navigate up to parent pages to explore entire domain

**Example:**
```python
# Explore entire domain structure
crawlEntireDomain = True

# Stay within starting path
crawlEntireDomain = False
```

---

### allowExternalLinks
- **Type**: `boolean`
- **Default**: `false`
- **Description**: Follow links to external domains

**Example:**
```python
# Follow external links
allowExternalLinks = True

# Stay on same domain
allowExternalLinks = False
```

---

### allowSubdomains
- **Type**: `boolean`
- **Default**: `false`
- **Description**: Follow links to subdomains

**Example:**
```python
# Follow subdomains (docs.example.com, blog.example.com)
allowSubdomains = True

# Stay on main domain only
allowSubdomains = False
```

---

### delayBetweenScrapes
- **Type**: `number` (seconds)
- **Default**: `null`
- **Description**: Delay between scraping each page

**Example:**
```python
# 1 second delay between pages
delayBetweenScrapes = 1

# 2 second delay
delayBetweenScrapes = 2
```

**Use case:** Respectful rate limiting

---

### scrapeOptions
- **Type**: `object`
- **Default**: `{'formats': ['markdown']}`
- **Description**: Options to use for each scraped page (inherits all scrape parameters)

**Example:**
```python
scrapeOptions = {
    'formats': ['markdown', 'links'],
    'onlyMainContent': True,
    'maxAge': 86400000,
    'excludeTags': ['#ads', '.footer']
}
```

---

## Map Parameters

Used with `/map` endpoint and `map_url()` method.

### search
- **Type**: `string`
- **Default**: `null`
- **Description**: Filter URLs containing this text

**Example:**
```python
# Find URLs containing 'blog'
search = 'blog'

# Find URLs containing 'product'
search = 'product'
```

---

### limit
- **Type**: `integer`
- **Default**: `100`
- **Description**: Maximum URLs to return

**Example:**
```python
# Small list
limit = 50

# Large list
limit = 500
```

---

### sitemap
- **Type**: `string`
- **Default**: `'include'`
- **Options**: `'only'`, `'include'`, `'skip'`
- **Description**: How to use sitemap

**Examples:**
```python
# Use sitemap only (fast if available)
sitemap = 'only'

# Use sitemap if available, otherwise discover
sitemap = 'include'

# Ignore sitemap, always discover
sitemap = 'skip'
```

---

### includeSubdomains
- **Type**: `boolean`
- **Default**: `true`
- **Description**: Include subdomains in results

---

## Batch Scrape Parameters

Used with `/batch/scrape` endpoint and `batch_scrape_urls()` method.

Same as scrape parameters, applied to all URLs in batch.

**Example:**
```python
urls = ['url1.com', 'url2.com', 'url3.com']

params = {
    'formats': ['markdown'],
    'onlyMainContent': True,
    'maxAge': 86400000
}

app.batch_scrape_urls(urls, params=params)
```

---

## Extract Parameters

Used with `/extract` endpoint.

### schema
- **Type**: `object` (JSON Schema)
- **Default**: `null`
- **Description**: Schema for structured extraction

**Example:**
```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float

schema = Product.model_json_schema()
```

---

### prompt
- **Type**: `string`
- **Default**: `null`
- **Description**: Natural language extraction instructions (alternative to schema)

**Example:**
```python
prompt = 'Extract all product names, prices, and availability status'
```

---

### limit
- **Type**: `integer`
- **Default**: `50`
- **Description**: Maximum pages to extract from (multi-page extraction)

---

## Parameter Combinations

### Minimal Scrape (Fastest, Cheapest)
```python
params = {
    'formats': ['markdown'],
    'onlyMainContent': True,
    'maxAge': 604800000  # 1 week cache
}
```

### Comprehensive Scrape (Everything)
```python
params = {
    'formats': ['markdown', 'html', 'links', 'images', {'type': 'screenshot'}],
    'onlyMainContent': False,
    'maxAge': 0  # Always fresh
}
```

### Targeted Scrape (Specific Content)
```python
params = {
    'formats': ['markdown'],
    'includeTags': ['.article-content', 'article'],
    'excludeTags': ['#ads', '.sidebar', 'nav'],
    'onlyMainContent': True
}
```

### Dynamic Content Scrape
```python
params = {
    'formats': ['markdown'],
    'waitFor': 3000,
    'actions': [
        {'type': 'scroll', 'direction': 'down'},
        {'type': 'wait', 'milliseconds': 2000}
    ]
}
```

---

## Related Documentation

- **SKILL.md** - Essential examples
- **references/quick-start.md** - Additional examples
- **references/api_reference.md** - Complete API documentation
- **CLAUDE.md** - Comprehensive deep context

---

Use this reference to understand all available parameters and their effects.
