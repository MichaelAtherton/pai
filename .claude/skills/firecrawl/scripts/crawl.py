#!/usr/bin/env python3
"""
Crawl with Options Example

Demonstrates website crawling with URL pattern filtering.
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

    # URL to crawl
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://firecrawl.dev'

    print(f"Crawling: {url}")
    print("This may take 30s-2min depending on site size...")
    print("-" * 60)

    try:
        # Crawl with options
        result = app.crawl_url(url, params={
            'limit': 20,                           # Max 20 pages
            'maxDiscoveryDepth': 2,                # 2 levels deep
            'excludeUrlPatterns': ['^/admin/.*$'], # Skip admin pages
            'scrapeOptions': {
                'formats': ['markdown'],
                'onlyMainContent': True,
                'maxAge': 86400000  # Use cache
            }
        })

        if result.get('success'):
            pages = result.get('data', [])

            print(f"✓ Crawl complete!")
            print(f"Pages crawled: {len(pages)}")
            print(f"\nCrawled pages:")
            print("-" * 60)

            for i, page in enumerate(pages, 1):
                title = page.get('metadata', {}).get('title', 'No title')
                url = page['url']
                length = len(page.get('markdown', ''))

                print(f"{i}. {title}")
                print(f"   URL: {url}")
                print(f"   Content: {length} chars")

            # Calculate total content
            total_content = sum(len(p.get('markdown', '')) for p in pages)
            print(f"\nTotal content scraped: {total_content} characters")

        else:
            print("✗ Crawl failed")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
