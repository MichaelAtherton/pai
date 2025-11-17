---
description: Actions/automation workflow - Lucy automates browser interactions before scraping (click, scroll, input)
globs: ""
alwaysApply: false
---

# ⚡ ACTIONS AUTOMATION WORKFLOW

**YOU (Lucy) are reading this to automate browser interactions before scraping.**

## 🎯 WHEN TO USE

**User says:**
- "Click then scrape"
- "Fill form and scrape results"
- "Search and scrape first result"
- "Scroll then capture"

## 📋 MISSION

Automate browser interactions (click, scroll, input) before scraping content.

## ⚡ SUPPORTED ACTIONS

```python
actions = [
    # Wait for page load
    {'type': 'wait', 'milliseconds': 2000},

    # Click element
    {'type': 'click', 'selector': 'button.load-more'},

    # Type text
    {'type': 'write', 'selector': 'input[name="q"]', 'text': 'search query'},

    # Press key
    {'type': 'press', 'key': 'Enter'},

    # Scroll
    {'type': 'scroll', 'direction': 'down'},  # or 'up'

    # Execute JavaScript
    {'type': 'executeJavascript', 'script': 'window.scrollTo(0, 1000)'},

    # Screenshot
    {'type': 'screenshot'}
]
```

## ⚡ COMMON PATTERNS

### Pattern 1: Search → Click → Scrape

```python
from firecrawl import FirecrawlApp
import os

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

result = app.scrape_url('https://google.com', params={
    'actions': [
        {'type': 'wait', 'milliseconds': 2000},
        {'type': 'write', 'selector': 'input[name="q"]', 'text': 'Firecrawl'},
        {'type': 'press', 'key': 'Enter'},
        {'type': 'wait', 'milliseconds': 3000},
        {'type': 'click', 'selector': 'h3'},  # Click first result
        {'type': 'wait', 'milliseconds': 2000}
    ],
    'formats': ['markdown']
})
```

### Pattern 2: Infinite Scroll → Load All → Scrape

```python
result = app.scrape_url('https://example.com/products', params={
    'actions': [
        {'type': 'wait', 'milliseconds': 2000},
        {'type': 'scroll', 'direction': 'down'},
        {'type': 'wait', 'milliseconds': 2000},
        {'type': 'scroll', 'direction': 'down'},
        {'type': 'wait', 'milliseconds': 2000},
        {'type': 'scroll', 'direction': 'down'},
        {'type': 'wait', 'milliseconds': 2000}
    ],
    'formats': ['markdown']
})
```

### Pattern 3: Load More Button → Click Multiple Times

```python
result = app.scrape_url('https://example.com', params={
    'actions': [
        {'type': 'wait', 'milliseconds': 2000},
        {'type': 'click', 'selector': '.load-more'},
        {'type': 'wait', 'milliseconds': 2000},
        {'type': 'click', 'selector': '.load-more'},
        {'type': 'wait', 'milliseconds': 2000},
        {'type': 'click', 'selector': '.load-more'},
        {'type': 'wait', 'milliseconds': 2000}
    ],
    'formats': ['markdown']
})
```

## 🎯 COMPLETE EXAMPLE

```python
from firecrawl import FirecrawlApp
import os

def scrape_with_actions(url: str, actions: list):
    """Scrape with custom browser actions."""
    app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    result = app.scrape_url(url, params={
        'actions': actions,
        'formats': ['markdown', {'type': 'screenshot'}]
    })

    return result

# Usage: Search Google and scrape first result
actions = [
    {'type': 'wait', 'milliseconds': 2000},
    {'type': 'write', 'selector': 'input[name="q"]', 'text': 'Firecrawl API'},
    {'type': 'press', 'key': 'Enter'},
    {'type': 'wait', 'milliseconds': 3000}
]

result = scrape_with_actions('https://google.com', actions)
print(result['markdown'][:500])
```

## 💡 BEST PRACTICES

1. **Always use `wait` before and after actions**
2. **Test selectors in DevTools** first
3. **Keep action sequences short** (< 10 actions)
4. **Use appropriate wait times** (2-3 seconds for most pages)

---

**END OF WORKFLOW**
