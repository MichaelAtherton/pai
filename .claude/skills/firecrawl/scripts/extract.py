#!/usr/bin/env python3
"""
Extract Structured Data Example

Demonstrates AI-powered structured data extraction with Pydantic schemas.
"""

from firecrawl import FirecrawlApp
from pydantic import BaseModel
import os
import sys
import json

# Define schema for product data
class ProductInfo(BaseModel):
    name: str
    price: float | None
    description: str
    availability: str

def main():
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        print("Error: FIRECRAWL_API_KEY not set")
        sys.exit(1)

    app = FirecrawlApp(api_key=api_key)

    # Example product URL (replace with actual product page)
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://firecrawl.dev'

    print(f"Extracting structured data from: {url}")
    print("-" * 60)

    try:
        # Extract with schema
        result = app.scrape_url(url, params={
            'formats': [{
                'type': 'json',
                'schema': ProductInfo.model_json_schema()
            }]
        })

        if result.get('success'):
            data = result.get('data', {})

            print("✓ Extraction successful!")
            print(f"\nExtracted data:")
            print("-" * 60)
            print(json.dumps(data, indent=2))

            # Access structured fields
            print(f"\nProduct Name: {data.get('name', 'N/A')}")
            print(f"Price: ${data.get('price', 0)}")
            print(f"Description: {data.get('description', 'N/A')[:100]}...")
            print(f"Availability: {data.get('availability', 'N/A')}")

        else:
            print("✗ Extraction failed")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Example 2: Extract without schema (using prompt)
    print(f"\n\n{'='*60}")
    print("Example 2: Extract with prompt (no schema)")
    print("=" * 60)

    try:
        result = app.scrape_url(url, params={
            'formats': [{
                'type': 'json',
                'prompt': 'Extract the page title, main heading, and any pricing information'
            }]
        })

        if result.get('success'):
            data = result.get('data', {})
            print("✓ Extraction successful!")
            print(json.dumps(data, indent=2))

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
