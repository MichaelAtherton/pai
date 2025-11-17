#!/usr/bin/env python3
"""
Map Then Scrape Example

Demonstrates efficient two-step process:
1. Map website to get all URLs (fast, cheap)
2. Filter URLs and selectively scrape (targeted)

This is more efficient than crawling when you know what you want.
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

    url = sys.argv[1] if len(sys.argv) > 1 else 'https://firecrawl.dev'

    print(f"Map-then-scrape workflow for: {url}")
    print("-" * 60)

    try:
        # Step 1: Map website to get all URLs
        print("Step 1: Mapping website...")
        map_result = app.map_url(url, params={
            'limit': 200
        })

        all_urls = map_result.get('links', [])
        print(f"✓ Found {len(all_urls)} URLs")

        # Step 2: Filter URLs
        print("\nStep 2: Filtering URLs...")

        # Example: Find all blog posts
        blog_urls = [u for u in all_urls if '/blog/' in u]
        print(f"Blog posts: {len(blog_urls)}")

        # Example: Find all documentation pages
        doc_urls = [u for u in all_urls if '/docs/' in u]
        print(f"Documentation: {len(doc_urls)}")

        # Show some URLs
        print(f"\nSample blog URLs:")
        for url in blog_urls[:5]:
            print(f"  - {url}")

        # Step 3: Selective scrape (only the URLs we want)
        print(f"\nStep 3: Selectively scraping {min(5, len(blog_urls))} blog posts...")

        if blog_urls:
            batch_result = app.batch_scrape_urls(blog_urls[:5], params={
                'formats': ['markdown'],
                'onlyMainContent': True
            })

            if batch_result.get('success'):
                pages = batch_result.get('data', [])
                print(f"✓ Scraped {len(pages)} pages")

                for i, page in enumerate(pages, 1):
                    title = page.get('metadata', {}).get('title', 'No title')
                    content_length = len(page.get('markdown', ''))
                    print(f"{i}. {title} ({content_length} chars)")

                # Calculate cost savings
                print(f"\nCost comparison:")
                print(f"  Map: 1 credit")
                print(f"  Batch scrape: {len(pages)} credits")
                print(f"  Total: {1 + len(pages)} credits")
                print(f"\n  vs. Crawling all {len(all_urls)} pages: {len(all_urls)} credits")
                print(f"  Savings: {len(all_urls) - (1 + len(pages))} credits")

        else:
            print("No blog URLs found to scrape")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
