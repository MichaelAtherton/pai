#!/usr/bin/env python3
"""
Authenticated Scrape Example

Demonstrates scraping behind authentication using cookies.

IMPORTANT: Only use on systems with explicit permission!
"""

from firecrawl import FirecrawlApp
import os
import sys

def main():
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        print("Error: FIRECRAWL_API_KEY not set")
        sys.exit(1)

    # Get cookie from environment (NEVER hardcode!)
    auth_cookie = os.getenv("AUTH_COOKIE")
    if not auth_cookie:
        print("Error: AUTH_COOKIE not set")
        print("\nTo extract cookie:")
        print("1. Login to the site manually")
        print("2. Open DevTools (F12)")
        print("3. Go to Application/Storage → Cookies")
        print("4. Copy cookie value")
        print("5. Export AUTH_COOKIE=your_cookie_value")
        sys.exit(1)

    app = FirecrawlApp(api_key=api_key)

    # URL to scrape (protected page)
    url = sys.argv[1] if len(sys.argv) > 1 else input("Enter protected URL: ")

    print(f"Scraping authenticated page: {url}")
    print("-" * 60)

    try:
        # Scrape with cookie
        result = app.scrape_url(url, params={
            'headers': {
                'Cookie': auth_cookie
            },
            'formats': ['markdown']
        })

        if result.get('success'):
            markdown = result.get('markdown', '')

            # Check if we got login page (cookie expired)
            if 'login' in markdown.lower() or 'sign in' in markdown.lower():
                print("⚠️  Warning: Got login page - cookie may be expired")
                print("Re-extract cookie from DevTools and update AUTH_COOKIE")
            else:
                print("✓ Authenticated scrape successful!")
                print(f"Content length: {len(markdown)} characters")
                print(f"\nPreview:")
                print("-" * 60)
                print(markdown[:500] + "...")

        else:
            print("✗ Scrape failed")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
