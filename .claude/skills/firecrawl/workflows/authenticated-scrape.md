---
description: Authenticated scraping workflow - Lucy scrapes content behind authentication using cookies
globs: ""
alwaysApply: false
---

# 🔐 AUTHENTICATED SCRAPE WORKFLOW

**YOU (Lucy) are reading this to scrape authenticated/protected content.**

⚠️ **LEGAL WARNING**: Only use on systems with explicit permission. Never violate Terms of Service.

## 🎯 WHEN TO USE

**User says:**
- "Scrape this page behind login"
- "Extract from authenticated page"
- "Scrape internal tool"

## 📋 MISSION

Scrape content requiring authentication using cookie-based auth.

## ⚡ STEPS

### Step 1: Extract Cookie (Manual Process)

**Guide user through DevTools:**

1. Login to the website manually
2. Open DevTools (F12)
3. Go to Application (Chrome) or Storage (Firefox) tab
4. Expand Cookies → Click domain
5. Find auth cookie (e.g., `auth-token`, `session-id`)
6. Copy cookie value

### Step 2: Store Cookie Securely

```bash
# In .env file (NEVER commit to git)
INTERNAL_TOOL_COOKIE=your_cookie_value_here
```

### Step 3: Scrape with Cookie

```python
from firecrawl import FirecrawlApp
import os

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

result = app.scrape_url('https://internal-tool.com/dashboard', params={
    'headers': {
        'Cookie': os.getenv('INTERNAL_TOOL_COOKIE')
    },
    'formats': ['markdown']
})
```

### Step 4: Handle Cookie Expiration

```python
# Check if login page appears
if 'login' in result['markdown'].lower():
    print("⚠️ Cookie expired. Re-extract from DevTools")
```

## 🎯 COMPLETE EXAMPLE

```python
from firecrawl import FirecrawlApp
import os

def scrape_authenticated(url: str, cookie_env_var: str):
    """Scrape authenticated page using cookie."""
    app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    cookie = os.getenv(cookie_env_var)
    if not cookie:
        raise ValueError(f"{cookie_env_var} not set in environment")

    result = app.scrape_url(url, params={
        'headers': {'Cookie': cookie},
        'formats': ['markdown']
    })

    # Check for login page (cookie expired)
    if 'login' in result['markdown'].lower():
        raise Exception("Cookie expired - re-extract from DevTools")

    return result['markdown']

# Usage
try:
    content = scrape_authenticated(
        'https://internal-tool.com/dashboard',
        'INTERNAL_TOOL_COOKIE'
    )
    print("Scrape successful!")
except Exception as e:
    print(f"Error: {e}")
```

## ⚠️ SECURITY BEST PRACTICES

1. **Never commit cookies** to version control
2. **Use environment variables** for storage
3. **Rotate cookies regularly**
4. **Monitor expiration** (check DevTools "Expires" field)
5. **Delete when done** (don't hoard credentials)

---

**END OF WORKFLOW**
