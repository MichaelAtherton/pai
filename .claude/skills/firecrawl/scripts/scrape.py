#!/usr/bin/env python3
"""
Simple Scrape Example

Demonstrates basic single URL scraping with Firecrawl.
Returns clean markdown perfect for LLMs.
"""

from firecrawl import FirecrawlApp
import os
import sys

def main():
    # Get API key from environment
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        print("Error: FIRECRAWL_API_KEY environment variable not set")
        print("Get your API key from: https://firecrawl.dev/app/api-keys")
        print("Then run: export FIRECRAWL_API_KEY=fc-your-key")
        sys.exit(1)

    # Initialize Firecrawl
    app = FirecrawlApp(api_key=api_key)

    # URL to scrape (use argument if provided)
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://firecrawl.dev'

    print(f"Scraping: {url}")
    print("-" * 60)

    try:
        # Scrape URL with multiple formats
        result = app.scrape_url(url, params={
            'formats': ['markdown', 'links'],
            'onlyMainContent': True,
            'maxAge': 86400000  # 1-day cache
        })

        # Check success
        if result.get('success'):
            # Extract data
            markdown = result.get('markdown', '')
            links = result.get('links', [])
            metadata = result.get('metadata', {})

            # Display results
            print(f"✓ Scrape successful!")
            print(f"\nTitle: {metadata.get('title', 'N/A')}")
            print(f"Description: {metadata.get('description', 'N/A')[:100]}...")
            print(f"Content length: {len(markdown)} characters")
            print(f"Links found: {len(links)}")

            # Show first 500 chars of markdown
            print(f"\nContent preview:")
            print("-" * 60)
            print(markdown[:500] + "...")

            # Show first 5 links
            if links:
                print(f"\nFirst 5 links:")
                for link in links[:5]:
                    print(f"  - {link}")

        else:
            print(f"✗ Scrape failed")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
