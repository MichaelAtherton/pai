#!/usr/bin/env python3
"""
Actions Example

Demonstrates browser automation before scraping.
Shows how to click, scroll, and input text before extracting content.
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

    print("Actions Example: Search Google and scrape results")
    print("-" * 60)

    try:
        # Example 1: Search Google
        result = app.scrape_url('https://google.com', params={
            'actions': [
                {'type': 'wait', 'milliseconds': 2000},
                {'type': 'write', 'selector': 'input[name="q"]', 'text': 'Firecrawl API'},
                {'type': 'press', 'key': 'Enter'},
                {'type': 'wait', 'milliseconds': 3000}
            ],
            'formats': ['markdown']
        })

        if result.get('success'):
            markdown = result.get('markdown', '')

            print("✓ Action sequence successful!")
            print(f"Content length: {len(markdown)} characters")
            print(f"\nSearch results preview:")
            print("-" * 60)
            print(markdown[:500] + "...")

        else:
            print("✗ Actions failed")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Example 2: Scroll to load dynamic content
    print(f"\n\n{'='*60}")
    print("Example 2: Scroll to load dynamic content")
    print("=" * 60)

    url = sys.argv[1] if len(sys.argv) > 1 else 'https://firecrawl.dev'

    try:
        result = app.scrape_url(url, params={
            'actions': [
                {'type': 'wait', 'milliseconds': 2000},
                {'type': 'scroll', 'direction': 'down'},
                {'type': 'wait', 'milliseconds': 2000},
                {'type': 'scroll', 'direction': 'down'},
                {'type': 'wait', 'milliseconds': 2000}
            ],
            'formats': ['markdown', {'type': 'screenshot'}]
        })

        if result.get('success'):
            print("✓ Scroll actions complete!")
            markdown = result.get('markdown', '')
            screenshot = result.get('screenshot', '')

            print(f"Content: {len(markdown)} chars")
            print(f"Screenshot: {'Captured' if screenshot else 'Not captured'}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
