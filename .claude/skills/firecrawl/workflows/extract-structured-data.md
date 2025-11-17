---
description: Extract structured data workflow - Lucy uses AI to extract structured data with or without schemas
globs: ""
alwaysApply: false
---

# 🎯 EXTRACT STRUCTURED DATA WORKFLOW

**YOU (Lucy) are reading this to extract structured data from websites.**

## 🎯 WHEN TO USE

**User says:**
- "Extract product data from this page"
- "Get structured data from [URL]"
- "Extract contact information"
- "Get JSON from this website"

## 📋 MISSION

Extract structured data using AI-powered extraction with schemas.

## ⚡ STEPS

### Step 1: Define Schema (Recommended)

```python
from pydantic import BaseModel
from firecrawl import FirecrawlApp
import os

class ProductInfo(BaseModel):
    name: str
    price: float
    availability: str
    rating: float | None

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
```

### Step 2: Extract with Schema

```python
result = app.scrape_url('https://example.com/product', params={
    'formats': [{
        'type': 'json',
        'schema': ProductInfo.model_json_schema()
    }]
})

product_data = result['data']
```

### Step 3: OR Extract with Prompt (No Schema)

```python
result = app.scrape_url('https://example.com', params={
    'formats': [{
        'type': 'json',
        'prompt': 'Extract all product names, prices, and ratings'
    }]
})
```

## 🎯 COMPLETE EXAMPLE

```python
from pydantic import BaseModel
from firecrawl import FirecrawlApp
import os

class Product(BaseModel):
    name: str
    price: float
    description: str
    in_stock: bool

def extract_product(url: str):
    """Extract structured product data."""
    app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    result = app.scrape_url(url, params={
        'formats': [{
            'type': 'json',
            'schema': Product.model_json_schema()
        }]
    })

    return result['data']

# Usage
product = extract_product('https://example.com/product/123')
print(f"Product: {product['name']}")
print(f"Price: ${product['price']}")
print(f"In Stock: {product['in_stock']}")
```

---

**END OF WORKFLOW**
