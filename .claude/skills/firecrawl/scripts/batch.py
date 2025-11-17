#!/usr/bin/env python3
"""
Batch Scrape Example

Demonstrates scraping multiple URLs in parallel.
"""

from firecrawl import FirecrawlApp
import os
import sys

def main():
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        print("Error: FIRECRAWL_API_KEY not set")
        sys.exit(1)

    app = FirecrawlApp(api_key=api_key)

    # URLs to scrape
    urls = [
        "https://firecrawl.dev",
        "https://docs.firecrawl.dev",
        "https://firecrawl.dev/blog"
    ]

    print(f"Batch scraping {len(urls)} URLs...")
    print("-" * 60)

    try:
        # Batch scrape
        result = app.batch_scrape_urls(urls, params={
            'formats': ['markdown', 'links'],
            'onlyMainContent': True
        })

        if result.get('success'):
            pages = result.get('data', [])

            print(f"✓ Batch scrape complete!")
            print(f"Pages scraped: {len(pages)}")
            print(f"\nResults:")
            print("-" * 60)

            for i, page in enumerate(pages, 1):
                title = page.get('metadata', {}).get('title', 'No title')
                url = page['url']
                content_length = len(page.get('markdown', ''))
                links_count = len(page.get('links', []))

                print(f"{i}. {title}")
                print(f"   URL: {url}")
                print(f"   Content: {content_length} chars")
                print(f"   Links: {links_count}")
                print()

        else:
            print("✗ Batch scrape failed")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
