# Firecrawl - Features

**Pages:** 13

---

## Authenticated Scraping

**URL:** llms-txt#authenticated-scraping

**Contents:**
- Overview
- Setup
- Method 1: Cookie-Based Authentication
  - Step 1: Extract Cookies from DevTools
  - Step 2: Use Cookies with Firecrawl
- Best Practices
- Troubleshooting

Source: https://docs.firecrawl.dev/developer-guides/advanced-guides/authenticated-scraping

Learn how to scrape content behind authentication using cookies

<Warning>
  **Important:** Only use authenticated scraping on systems where you have explicit permission from both parties (yourself and the platform owner), such as internal, self-hosted tools or resources you fully control. Do not use authentication on platforms unless you are certain it abides by the site's Terms and Conditions and get written permission when in doubt. Using session cookies improperly can violate terms of service or laws; always confirm you are authorized to access protected content in this way.
</Warning>

The recommended approach for authenticated scraping is **cookie-based authentication**, where you:

1. Login manually to your application
2. Extract the session cookie from DevTools
3. Use the cookie with Firecrawl to access protected pages

<Note>
  **Cookie Expiration Times:**

* **Internal tools**: Often 7-30 days or longer
  * **Other tools**: Often hours or minutes

Internal tools typically have longer cookie lifespans, making this method ideal for recurring scraping tasks.
</Note>

<Steps>
  <Step title="Get API Key">
    Get your Firecrawl API key from [firecrawl.dev/app](https://firecrawl.dev/app)
  </Step>

<Step title="Install Dependencies">

<Note>
      **Node.js \< v20**: If you're using Node.js version 19 or earlier, you'll also need to install `dotenv`:

And import it with `import 'dotenv/config'` at the top of your file.
    </Note>
  </Step>

<Step title="Configure Environment">
    Create a `.env` file:

## Method 1: Cookie-Based Authentication

### Step 1: Extract Cookies from DevTools

<Note>
  **Demo Application**: You can practice with our demo app at [https://firecrawl-auth.vercel.app](https://firecrawl-auth.vercel.app)

* Email: `test@example.com`
  * Password: `password123`
</Note>

<Steps>
  <Step title="Login to Your Application">
    Navigate to [https://firecrawl-auth.vercel.app](https://firecrawl-auth.vercel.app) and login with the credentials above
  </Step>

<Step title="Open DevTools">
    Press `F12` or right-click → "Inspect"
  </Step>

<Step title="Navigate to Application Tab">
    Click the **Application** tab (Chrome) or **Storage** tab (Firefox)
  </Step>

<Step title="Find and Copy Cookie">
    1. Expand **Cookies** in the sidebar
    2. Click on your domain
    3. Find the `auth-token` cookie
    4. Double-click the **Value** and copy it

<img src="https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=8dea208fd9512430bce8f1063706b49c" alt="DevTools Cookies View" data-og-width="1992" width="1992" data-og-height="1226" height="1226" data-path="images/guides/dev-tools-cookie.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?w=280&fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=7deb61ef88a1db102c4846ce75c2a68e 280w, https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?w=560&fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=5d4ff7787fef1281daf2d33e7f994acb 560w, https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?w=840&fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=190086435afa1689a222a5a60c088a22 840w, https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?w=1100&fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=c716c9ebd526302c35ed2337a25ddcbb 1100w, https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?w=1650&fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=6b13bbbbace05a5f2e31640949d63899 1650w, https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?w=2500&fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=316b0b9e399cc8d86f228856ebd1d90a 2500w" />
  </Step>
</Steps>

For the demo app, the cookie looks like:

<Warning>
  **Important:** Cookies are sensitive credentials. Never share them publicly or commit them to version control. Treat them like passwords.
</Warning>

### Step 2: Use Cookies with Firecrawl

<CardGroup cols={2}>
  <Card title="Cookie Security" icon="lock">
    * Store cookies in environment variables
    * Never commit cookies to git
    * Rotate cookies regularly
    * Use `.gitignore` for `.env` files
  </Card>

<Card title="Cookie Expiration" icon="clock">
    * Check expiration times in DevTools
    * Set up alerts before expiration
    * Re-extract cookies when they expire
    * Consider using form-based auth for short-lived cookies
  </Card>

<Card title="Rate Limiting" icon="gauge">
    * Respect the application's rate limits
    * Add delays between requests
    * Monitor for 429 (Too Many Requests) errors
    * Use exponential backoff for retries
  </Card>

<Card title="Error Handling" icon="shield">
    * Check for 401/403 errors (expired cookies)
    * Validate response content
    * Log authentication failures
    * Have fallback authentication methods
  </Card>
</CardGroup>

<AccordionGroup>
  <Accordion title="Getting 401 Unauthorized Errors" icon="ban">
    **Possible causes:**

* Cookie has expired
    * Cookie was copied incorrectly
    * Application requires additional headers
    * Session was invalidated on the server

* Re-extract cookies from DevTools after a fresh login
    * Check if you need multiple cookies (session + CSRF token)
    * Verify the cookie domain matches your target URL
  </Accordion>

<Accordion title="Cookie Not Working" icon="cookie-bite">
    **Check these:**

* Is the cookie name correct?
    * Did you copy the entire cookie value?
    * Does the cookie have the correct domain?
    * Is there a `Path` restriction on the cookie?
    * Are there multiple cookies required?

**Pro tip:** Copy all cookies from DevTools and test with all of them, then remove one by one to find which are required.
  </Accordion>

<Accordion title="Session Expires Too Quickly" icon="hourglass">
    **For short-lived sessions:**

* Use form-based authentication instead
    * Automate the login process with actions
    * Set up a cron job to refresh cookies
    * Consider requesting longer session times from your internal tool's admin
  </Accordion>
</AccordionGroup>

<Note>
  **Cookie Lifespan for Internal Tools:** Many internal tools set cookies with 7-30 day expiration times, making them ideal for recurring scraping tasks. Check your cookie's `Expires` field in DevTools to see how long it's valid.
</Note>

**Examples:**

Example 1 (unknown):
```unknown
<Note>
      **Node.js \< v20**: If you're using Node.js version 19 or earlier, you'll also need to install `dotenv`:
```

Example 2 (unknown):
```unknown
And import it with `import 'dotenv/config'` at the top of your file.
    </Note>
  </Step>

  <Step title="Configure Environment">
    Create a `.env` file:
```

Example 3 (unknown):
```unknown
</Step>
</Steps>

***

## Method 1: Cookie-Based Authentication

### Step 1: Extract Cookies from DevTools

<Note>
  **Demo Application**: You can practice with our demo app at [https://firecrawl-auth.vercel.app](https://firecrawl-auth.vercel.app)

  * Email: `test@example.com`
  * Password: `password123`
</Note>

<Steps>
  <Step title="Login to Your Application">
    Navigate to [https://firecrawl-auth.vercel.app](https://firecrawl-auth.vercel.app) and login with the credentials above
  </Step>

  <Step title="Open DevTools">
    Press `F12` or right-click → "Inspect"
  </Step>

  <Step title="Navigate to Application Tab">
    Click the **Application** tab (Chrome) or **Storage** tab (Firefox)
  </Step>

  <Step title="Find and Copy Cookie">
    1. Expand **Cookies** in the sidebar
    2. Click on your domain
    3. Find the `auth-token` cookie
    4. Double-click the **Value** and copy it

    <img src="https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=8dea208fd9512430bce8f1063706b49c" alt="DevTools Cookies View" data-og-width="1992" width="1992" data-og-height="1226" height="1226" data-path="images/guides/dev-tools-cookie.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?w=280&fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=7deb61ef88a1db102c4846ce75c2a68e 280w, https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?w=560&fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=5d4ff7787fef1281daf2d33e7f994acb 560w, https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?w=840&fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=190086435afa1689a222a5a60c088a22 840w, https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?w=1100&fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=c716c9ebd526302c35ed2337a25ddcbb 1100w, https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?w=1650&fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=6b13bbbbace05a5f2e31640949d63899 1650w, https://mintcdn.com/firecrawl/NR4iESBjjsDFYTef/images/guides/dev-tools-cookie.png?w=2500&fit=max&auto=format&n=NR4iESBjjsDFYTef&q=85&s=316b0b9e399cc8d86f228856ebd1d90a 2500w" />
  </Step>
</Steps>

For the demo app, the cookie looks like:
```

Example 4 (unknown):
```unknown
<Warning>
  **Important:** Cookies are sensitive credentials. Never share them publicly or commit them to version control. Treat them like passwords.
</Warning>

### Step 2: Use Cookies with Firecrawl
```

---

## Scraping Amazon

**URL:** llms-txt#scraping-amazon

**Contents:**
- Setup
- Overview
- Scrape with JSON Mode
- Search
- Scrape
- Map
- Crawl
- Batch Scrape

Source: https://docs.firecrawl.dev/developer-guides/common-sites/amazon

Extract product data, prices, and reviews from Amazon using Firecrawl

<Info>
  Amazon is one of the most scraped e-commerce sites. This guide shows you how to effectively extract product data, pricing, reviews, and search results using Firecrawl's powerful features.
</Info>

When scraping Amazon, you'll typically want to:

* Extract product information (title, price, availability)
* Get customer reviews and ratings
* Monitor price changes
* Search for products programmatically
* Track competitor listings

## Scrape with JSON Mode

Extract structured product data using Zod schemas.

Find products on Amazon.

Scrape a single Amazon product page.

Discover all available URLs on Amazon product or category pages. Note: Map returns URLs only, without content.

Crawl multiple pages from Amazon category or search results.

Scrape multiple Amazon product URLs simultaneously.

**Examples:**

Example 1 (unknown):
```unknown
## Overview

When scraping Amazon, you'll typically want to:

* Extract product information (title, price, availability)
* Get customer reviews and ratings
* Monitor price changes
* Search for products programmatically
* Track competitor listings

## Scrape with JSON Mode

Extract structured product data using Zod schemas.
```

Example 2 (unknown):
```unknown
## Search

Find products on Amazon.
```

Example 3 (unknown):
```unknown
## Scrape

Scrape a single Amazon product page.
```

Example 4 (unknown):
```unknown
## Map

Discover all available URLs on Amazon product or category pages. Note: Map returns URLs only, without content.
```

---

## Scraping GitHub

**URL:** llms-txt#scraping-github

**Contents:**
- Setup
- Scrape with JSON Mode
- Search
- Scrape
- Map
- Crawl
- Batch Scrape
- Batch Scrape with JSON Mode

Source: https://docs.firecrawl.dev/developer-guides/common-sites/github

Learn how to scrape GitHub using Firecrawl's core features

Learn how to use Firecrawl's core features to scrape GitHub repositories, issues, and documentation.

## Scrape with JSON Mode

Extract structured data from repositories using Zod schemas.

Find repositories, issues, or documentation on GitHub.

Scrape a single GitHub page - repository, issue, or file.

Discover all available URLs in a repository or documentation site. Note: Map returns URLs only, without content.

Crawl multiple pages from a repository or documentation.

Scrape multiple GitHub URLs simultaneously.

## Batch Scrape with JSON Mode

Extract structured data from multiple repositories at once.

**Examples:**

Example 1 (unknown):
```unknown
## Scrape with JSON Mode

Extract structured data from repositories using Zod schemas.
```

Example 2 (unknown):
```unknown
## Search

Find repositories, issues, or documentation on GitHub.
```

Example 3 (unknown):
```unknown
## Scrape

Scrape a single GitHub page - repository, issue, or file.
```

Example 4 (unknown):
```unknown
## Map

Discover all available URLs in a repository or documentation site. Note: Map returns URLs only, without content.
```

---

## Faster Scraping

**URL:** llms-txt#faster-scraping

**Contents:**
- How It Works
- When to Use This
- Usage
- Common maxAge values
- Performance impact
- Important notes
- Faster crawling

Source: https://docs.firecrawl.dev/features/fast-scraping

Speed up your scrapes by 500% with the maxAge parameter

Firecrawl caches previously scraped pages and, by default, returns a recent copy when available.

* **Default freshness**: `maxAge = 172800000` ms (2 days). If the cached copy is newer than this, it’s returned instantly; otherwise, Firecrawl scrapes fresh and updates the cache.
* **Force fresh**: Set `maxAge: 0` to always scrape.
* **Skip caching**: Set `storeInCache: false` if you don’t want to store results for a request.

Get your results **up to 500% faster** when you don’t need the absolute freshest data. Control freshness via `maxAge`:

1. **Return instantly** if we have a recent version of the page
2. **Scrape fresh** only if our version is older than your specified age
3. **Save you time** - results come back in milliseconds instead of seconds

* Documentation, articles, product pages
* Bulk processing jobs
* Development and testing
* Building knowledge bases

* Real-time data (stock prices, live scores, breaking news)
* Frequently updated content
* Time-sensitive applications

Add `maxAge` to your scrape request. Values are in milliseconds (e.g., `3600000` = 1 hour).

## Common maxAge values

Here are some helpful reference values:

* **5 minutes**: `300000` - For semi-dynamic content
* **1 hour**: `3600000` - For content that updates hourly
* **1 day**: `86400000` - For daily-updated content
* **1 week**: `604800000` - For relatively static content

## Performance impact

With `maxAge` enabled:

* **500% faster response times** for recent content
* **Instant results** instead of waiting for fresh scrapes

* **Default**: `maxAge` is `172800000` (2 days)
* **Fresh when needed**: If our data is older than `maxAge`, we scrape fresh automatically
* **No stale data**: You'll never get data older than your specified `maxAge`

The same speed benefits apply when crawling multiple pages. Use `maxAge` within `scrapeOptions` to get cached results for pages we’ve seen recently.

When crawling with `maxAge`, each page in your crawl will benefit from the 500% speed improvement if we have recent cached data for that page.

Start using `maxAge` today for dramatically faster scrapes and crawls!

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

## Common maxAge values

Here are some helpful reference values:

* **5 minutes**: `300000` - For semi-dynamic content
* **1 hour**: `3600000` - For content that updates hourly
* **1 day**: `86400000` - For daily-updated content
* **1 week**: `604800000` - For relatively static content

## Performance impact

With `maxAge` enabled:

* **500% faster response times** for recent content
* **Instant results** instead of waiting for fresh scrapes

## Important notes

* **Default**: `maxAge` is `172800000` (2 days)
* **Fresh when needed**: If our data is older than `maxAge`, we scrape fresh automatically
* **No stale data**: You'll never get data older than your specified `maxAge`

## Faster crawling

The same speed benefits apply when crawling multiple pages. Use `maxAge` within `scrapeOptions` to get cached results for pages we’ve seen recently.

<CodeGroup>
```

Example 3 (unknown):
```unknown

```

Example 4 (unknown):
```unknown

```

---

## Firecrawl MCP Server

**URL:** llms-txt#firecrawl-mcp-server

**Contents:**
- Features
- Installation
  - Remote hosted URL
  - Running with npx
  - Manual Installation
  - Running on Cursor
  - Running on Windsurf
  - Running with Streamable HTTP Mode
  - Installing via Smithery (Legacy)
  - Running on VS Code

Source: https://docs.firecrawl.dev/mcp-server

Use Firecrawl's API through the Model Context Protocol

A Model Context Protocol (MCP) server implementation that integrates [Firecrawl](https://github.com/mendableai/firecrawl) for web scraping capabilities. Our MCP server is open-source and available on [GitHub](https://github.com/mendableai/firecrawl-mcp-server).

* Web scraping, crawling, and discovery
* Search and content extraction
* Deep research and batch scraping
* Cloud and self-hosted support
* Streamable HTTP support

You can either use our remote hosted URL or run the server locally. Get your API key from [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)

### Remote hosted URL

### Manual Installation

### Running on Cursor

<a href="cursor://anysphere.cursor-deeplink/mcp/install?name=firecrawl&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImZpcmVjcmF3bC1tY3AiXSwiZW52Ijp7IkZJUkVDUkFXTF9BUElfS0VZIjoiWU9VUi1BUEktS0VZIn19">
  <img src="https://cursor.com/deeplink/mcp-install-dark.png" alt="Add Firecrawl MCP server to Cursor" style={{ maxHeight: 32 }} />
</a>

#### Manual Installation

Configuring Cursor 🖥️
Note: Requires Cursor version 0.45.6+
For the most up-to-date configuration instructions, please refer to the official Cursor documentation on configuring MCP servers:
[Cursor MCP Server Configuration Guide](https://docs.cursor.com/context/model-context-protocol#configuring-mcp-servers)

To configure Firecrawl MCP in Cursor **v0.48.6**

1. Open Cursor Settings
2. Go to Features > MCP Servers
3. Click "+ Add new global MCP server"
4. Enter the following code:

To configure Firecrawl MCP in Cursor **v0.45.6**

1. Open Cursor Settings
2. Go to Features > MCP Servers
3. Click "+ Add New MCP Server"
4. Enter the following:
   * Name: "firecrawl-mcp" (or your preferred name)
   * Type: "command"
   * Command: `env FIRECRAWL_API_KEY=your-api-key npx -y firecrawl-mcp`

> If you are using Windows and are running into issues, try `cmd /c "set FIRECRAWL_API_KEY=your-api-key && npx -y firecrawl-mcp"`

Replace `your-api-key` with your Firecrawl API key. If you don't have one yet, you can create an account and get it from [https://www.firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)

After adding, refresh the MCP server list to see the new tools. The Composer Agent will automatically use Firecrawl MCP when appropriate, but you can explicitly request it by describing your web scraping needs. Access the Composer via Command+L (Mac), select "Agent" next to the submit button, and enter your query.

### Running on Windsurf

Add this to your `./codeium/windsurf/model_config.json`:

### Running with Streamable HTTP Mode

To run the server using streamable HTTP transport locally instead of the default stdio transport:

Use the url: [http://localhost:3000/v2/mcp](http://localhost:3000/v2/mcp) or [https://mcp.firecrawl.dev/\{FIRECRAWL\_API\_KEY}/v2/mcp](https://mcp.firecrawl.dev/\{FIRECRAWL_API_KEY}/v2/mcp)

### Installing via Smithery (Legacy)

To install Firecrawl for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@mendableai/mcp-server-firecrawl):

### Running on VS Code

For one-click installation, click one of the install buttons below\...

[![Install with NPX in VS Code](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl\&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D\&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D) [![Install with NPX in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-NPM-24bfa5?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl\&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D\&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D\&quality=insiders)

For manual installation, add the following JSON block to your User Settings (JSON) file in VS Code. You can do this by pressing `Ctrl + Shift + P` and typing `Preferences: Open User Settings (JSON)`.

Optionally, you can add it to a file called `.vscode/mcp.json` in your workspace. This will allow you to share the configuration with others:

**Note:** Some users have reported issues when adding the MCP server to VS Code due to how it validates JSON with an outdated schema format ([microsoft/vscode#155379](https://github.com/microsoft/vscode/issues/155379)).
This affects several MCP tools, including Firecrawl.

**Workaround:** Disable JSON validation in VS Code to allow the MCP server to load properly.\
See reference: [directus/directus#25906 (comment)](https://github.com/directus/directus/issues/25906#issuecomment-3369169513).

The MCP server still works fine when invoked via other extensions, but the issue occurs specifically when registering it directly in the MCP server list. We plan to add guidance once VS Code updates their schema validation.

### Running on Claude Desktop

Add this to the Claude config file:

### Running on Claude Code

Add the Firecrawl MCP server using the Claude Code CLI:

To connect the Firecrawl MCP server in n8n:

1. Get your Firecrawl API key from [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)
2. In your n8n workflow, add an **AI Agent** node
3. In the AI Agent configuration, add a new **Tool**
4. Select **MCP Client Tool** as the tool type
5. Enter the MCP server Endpoint (replace `{YOUR_FIRECRAWL_API_KEY}` with your actual API key):

6. Set **Server Transport** to **HTTP Streamable**
7. Set **Authentication** to **None**
8. For **Tools to include**, you can select **All**, **Selected**, or **All Except** - this will expose the Firecrawl tools (scrape, crawl, map, search, extract, etc.)

For self-hosted deployments, run the MCP server with npx and enable HTTP transport mode:

This will start the server on `http://localhost:3000/v2/mcp` which you can use in your n8n workflow as Endpoint. The `HTTP_STREAMABLE_SERVER=true` environment variable is required since n8n needs HTTP transport.

### Environment Variables

#### Required for Cloud API

* `FIRECRAWL_API_KEY`: Your Firecrawl API key
  * Required when using cloud API (default)
  * Optional when using self-hosted instance with `FIRECRAWL_API_URL`
* `FIRECRAWL_API_URL` (Optional): Custom API endpoint for self-hosted instances
  * Example: `https://firecrawl.your-domain.com`
  * If not provided, the cloud API will be used (requires API key)

#### Optional Configuration

##### Retry Configuration

* `FIRECRAWL_RETRY_MAX_ATTEMPTS`: Maximum number of retry attempts (default: 3)
* `FIRECRAWL_RETRY_INITIAL_DELAY`: Initial delay in milliseconds before first retry (default: 1000)
* `FIRECRAWL_RETRY_MAX_DELAY`: Maximum delay in milliseconds between retries (default: 10000)
* `FIRECRAWL_RETRY_BACKOFF_FACTOR`: Exponential backoff multiplier (default: 2)

##### Credit Usage Monitoring

* `FIRECRAWL_CREDIT_WARNING_THRESHOLD`: Credit usage warning threshold (default: 1000)
* `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD`: Credit usage critical threshold (default: 100)

### Configuration Examples

For cloud API usage with custom retry and credit monitoring:

```bash  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
### Running with npx
```

Example 2 (unknown):
```unknown
### Manual Installation
```

Example 3 (unknown):
```unknown
### Running on Cursor

<a href="cursor://anysphere.cursor-deeplink/mcp/install?name=firecrawl&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImZpcmVjcmF3bC1tY3AiXSwiZW52Ijp7IkZJUkVDUkFXTF9BUElfS0VZIjoiWU9VUi1BUEktS0VZIn19">
  <img src="https://cursor.com/deeplink/mcp-install-dark.png" alt="Add Firecrawl MCP server to Cursor" style={{ maxHeight: 32 }} />
</a>

#### Manual Installation

Configuring Cursor 🖥️
Note: Requires Cursor version 0.45.6+
For the most up-to-date configuration instructions, please refer to the official Cursor documentation on configuring MCP servers:
[Cursor MCP Server Configuration Guide](https://docs.cursor.com/context/model-context-protocol#configuring-mcp-servers)

To configure Firecrawl MCP in Cursor **v0.48.6**

1. Open Cursor Settings
2. Go to Features > MCP Servers
3. Click "+ Add new global MCP server"
4. Enter the following code:
```

Example 4 (unknown):
```unknown
To configure Firecrawl MCP in Cursor **v0.45.6**

1. Open Cursor Settings
2. Go to Features > MCP Servers
3. Click "+ Add New MCP Server"
4. Enter the following:
   * Name: "firecrawl-mcp" (or your preferred name)
   * Type: "command"
   * Command: `env FIRECRAWL_API_KEY=your-api-key npx -y firecrawl-mcp`

> If you are using Windows and are running into issues, try `cmd /c "set FIRECRAWL_API_KEY=your-api-key && npx -y firecrawl-mcp"`

Replace `your-api-key` with your Firecrawl API key. If you don't have one yet, you can create an account and get it from [https://www.firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)

After adding, refresh the MCP server list to see the new tools. The Composer Agent will automatically use Firecrawl MCP when appropriate, but you can explicitly request it by describing your web scraping needs. Access the Composer via Command+L (Mac), select "Agent" next to the submit button, and enter your query.

### Running on Windsurf

Add this to your `./codeium/windsurf/model_config.json`:
```

---

## Advanced Scraping Guide

**URL:** llms-txt#advanced-scraping-guide

**Contents:**
- Basic scraping with Firecrawl
- Scraping PDFs
- Scrape options
  - Formats (`formats`)
  - Full page content vs main content (`onlyMainContent`)
  - Include tags (`includeTags`)
  - Exclude tags (`excludeTags`)
  - Wait for page readiness (`waitFor`)
  - Freshness and cache (`maxAge`)
  - Request timeout (`timeout`)

Source: https://docs.firecrawl.dev/advanced-scraping-guide

Learn how to improve your Firecrawl scraping with advanced options.

This guide will walk you through the different endpoints of Firecrawl and how to use them fully with all its parameters.

## Basic scraping with Firecrawl

To scrape a single page and get clean markdown content, you can use the `/scrape` endpoint.

Firecrawl supports PDFs. Use the `parsers` option (e.g., `parsers: ["pdf"]`) when you want to ensure PDF parsing.

When using the `/scrape` endpoint, you can customize scraping with the options below.

### Formats (`formats`)

* **Type**: `array`
* **Strings**: `["markdown", "links", "html", "rawHtml", "summary", "images"]`
* **Object formats**:
  * JSON: `{ type: "json", prompt, schema }`
  * Screenshot: `{ type: "screenshot", fullPage?, quality?, viewport? }`
  * Change tracking: `{ type: "changeTracking", modes?, prompt?, schema?, tag? }` (requires `markdown`)
* **Default**: `["markdown"]`

### Full page content vs main content (`onlyMainContent`)

* **Type**: `boolean`
* **Description**: By default the scraper returns only the main content. Set to `false` to return full page content.
* **Default**: `true`

### Include tags (`includeTags`)

* **Type**: `array`
* **Description**: HTML tags/classes/ids to include in the scrape.

### Exclude tags (`excludeTags`)

* **Type**: `array`
* **Description**: HTML tags/classes/ids to exclude from the scrape.

### Wait for page readiness (`waitFor`)

* **Type**: `integer`
* **Description**: Milliseconds to wait before scraping (use sparingly).
* **Default**: `0`

### Freshness and cache (`maxAge`)

* **Type**: `integer` (milliseconds)
* **Description**: If a cached version of the page is newer than `maxAge`, Firecrawl returns it instantly; otherwise it scrapes fresh and updates the cache. Set `0` to always fetch fresh.
* **Default**: `172800000` (2 days)

### Request timeout (`timeout`)

* **Type**: `integer`
* **Description**: Max duration in milliseconds before aborting.
* **Default**: `30000` (30 seconds)

### PDF parsing (`parsers`)

* **Type**: `array`
* **Description**: Control parsing behavior. To parse PDFs, set `parsers: ["pdf"]`.

### Actions (`actions`)

When using the /scrape endpoint, Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.

* **Type**: `array`
* **Description**: Sequence of browser steps to run before scraping.
* **Supported actions**:
  * `wait` `{ milliseconds }`
  * `click` `{ selector }`
  * `write` `{ selector, text }`
  * `press` `{ key }`
  * `scroll` `{ direction: "up" | "down" }`
  * `scrape` `{ selector }` (scrape a sub-element)
  * `executeJavascript` `{ script }`
  * `pdf` (trigger PDF render in some flows)

In this example, the scraper will:

* Return the full page content as markdown.
* Include the markdown, raw HTML, HTML, links, and a screenshot in the response.
* Include only the HTML tags `<h1>`, `<p>`, `<a>`, and elements with the class `.main-content`, while excluding any elements with the IDs `#ad` and `#footer`.
* Wait for 1000 milliseconds (1 second) before scraping to allow the page to load.
* Set the maximum duration of the scrape request to 15000 milliseconds (15 seconds).
* Parse PDFs explicitly via `parsers: ["pdf"]`.

Here is the API Reference: [Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)

## JSON extraction via formats

Use the JSON format object in `formats` to extract structured data in one pass:

Use the dedicated extract job API when you want asynchronous extraction with status polling.

## Crawling multiple pages

To crawl multiple pages, use the `/v2/crawl` endpoint.

Used to check the status of a crawl job and get its result.

#### Pagination/Next URL

If the content is larger than 10MB or if the crawl job is still running, the response may include a `next` parameter, a URL to the next page of results.

### Crawl prompt and params preview

You can provide a natural-language `prompt` to let Firecrawl derive crawl settings. Preview them first:

When using the `/v2/crawl` endpoint, you can customize the crawling behavior with:

* **Type**: `array`
* **Description**: Regex patterns to include.
* **Example**: `["^/blog/.*$", "^/docs/.*$"]`

* **Type**: `array`
* **Description**: Regex patterns to exclude.
* **Example**: `["^/admin/.*$", "^/private/.*$"]`

#### maxDiscoveryDepth

* **Type**: `integer`
* **Description**: Max discovery depth for finding new URLs.

* **Type**: `integer`
* **Description**: Max number of pages to crawl.
* **Default**: `10000`

#### crawlEntireDomain

* **Type**: `boolean`
* **Description**: Explore across siblings/parents to cover the entire domain.
* **Default**: `false`

#### allowExternalLinks

* **Type**: `boolean`
* **Description**: Follow links to external domains.
* **Default**: `false`

* **Type**: `boolean`
* **Description**: Follow subdomains of the main domain.
* **Default**: `false`

* **Type**: `number`
* **Description**: Delay in seconds between scrapes.
* **Default**: `undefined`

* **Type**: `object`
* **Description**: Options for the scraper (see Formats above).
* **Example**: `{ "formats": ["markdown", "links", {"type": "screenshot", "fullPage": true}], "includeTags": ["h1", "p", "a", ".main-content"], "excludeTags": ["#ad", "#footer"], "onlyMainContent": false, "waitFor": 1000, "timeout": 15000}`
* **Defaults**: `formats: ["markdown"]`, caching enabled by default (maxAge \~ 2 days)

## Mapping website links

The `/v2/map` endpoint identifies URLs related to a given website.

* **Type**: `string`
* **Description**: Filter links containing text.

* **Type**: `integer`
* **Description**: Maximum number of links to return.
* **Default**: `100`

* **Type**: `"only" | "include" | "skip"`
* **Description**: Control sitemap usage during mapping.
* **Default**: `"include"`

#### includeSubdomains

* **Type**: `boolean`
* **Description**: Include subdomains of the website.
* **Default**: `true`

Here is the API Reference for it: [Map Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/map)

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown

```

Example 3 (unknown):
```unknown
</CodeGroup>

## Scraping PDFs

Firecrawl supports PDFs. Use the `parsers` option (e.g., `parsers: ["pdf"]`) when you want to ensure PDF parsing.

## Scrape options

When using the `/scrape` endpoint, you can customize scraping with the options below.

### Formats (`formats`)

* **Type**: `array`
* **Strings**: `["markdown", "links", "html", "rawHtml", "summary", "images"]`
* **Object formats**:
  * JSON: `{ type: "json", prompt, schema }`
  * Screenshot: `{ type: "screenshot", fullPage?, quality?, viewport? }`
  * Change tracking: `{ type: "changeTracking", modes?, prompt?, schema?, tag? }` (requires `markdown`)
* **Default**: `["markdown"]`

### Full page content vs main content (`onlyMainContent`)

* **Type**: `boolean`
* **Description**: By default the scraper returns only the main content. Set to `false` to return full page content.
* **Default**: `true`

### Include tags (`includeTags`)

* **Type**: `array`
* **Description**: HTML tags/classes/ids to include in the scrape.

### Exclude tags (`excludeTags`)

* **Type**: `array`
* **Description**: HTML tags/classes/ids to exclude from the scrape.

### Wait for page readiness (`waitFor`)

* **Type**: `integer`
* **Description**: Milliseconds to wait before scraping (use sparingly).
* **Default**: `0`

### Freshness and cache (`maxAge`)

* **Type**: `integer` (milliseconds)
* **Description**: If a cached version of the page is newer than `maxAge`, Firecrawl returns it instantly; otherwise it scrapes fresh and updates the cache. Set `0` to always fetch fresh.
* **Default**: `172800000` (2 days)

### Request timeout (`timeout`)

* **Type**: `integer`
* **Description**: Max duration in milliseconds before aborting.
* **Default**: `30000` (30 seconds)

### PDF parsing (`parsers`)

* **Type**: `array`
* **Description**: Control parsing behavior. To parse PDFs, set `parsers: ["pdf"]`.

### Actions (`actions`)

When using the /scrape endpoint, Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.

* **Type**: `array`
* **Description**: Sequence of browser steps to run before scraping.
* **Supported actions**:
  * `wait` `{ milliseconds }`
  * `click` `{ selector }`
  * `write` `{ selector, text }`
  * `press` `{ key }`
  * `scroll` `{ direction: "up" | "down" }`
  * `scrape` `{ selector }` (scrape a sub-element)
  * `executeJavascript` `{ script }`
  * `pdf` (trigger PDF render in some flows)

<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## Scraping Etsy

**URL:** llms-txt#scraping-etsy

**Contents:**
- Setup
- Overview
- Scrape with JSON Mode
- Search
- Scrape
- Map
- Crawl
- Batch Scrape

Source: https://docs.firecrawl.dev/developer-guides/common-sites/etsy

Extract handmade products, shop data, and pricing from Etsy marketplace

<Info>
  Etsy is a global marketplace for unique and creative goods. This guide shows you how to extract product listings, shop information, reviews, and trending items using Firecrawl.
</Info>

When scraping Etsy, you'll typically want to:

* Extract product listings and variations
* Get shop information and ratings
* Monitor trending items and categories
* Track pricing and sales data
* Extract customer reviews

## Scrape with JSON Mode

Extract structured listing data using Zod schemas.

Find products on Etsy marketplace.

Scrape a single Etsy product listing.

Discover all available URLs in an Etsy shop or category. Note: Map returns URLs only, without content.

Crawl multiple pages from Etsy shop or category.

Scrape multiple Etsy listing URLs simultaneously.

**Examples:**

Example 1 (unknown):
```unknown
## Overview

When scraping Etsy, you'll typically want to:

* Extract product listings and variations
* Get shop information and ratings
* Monitor trending items and categories
* Track pricing and sales data
* Extract customer reviews

## Scrape with JSON Mode

Extract structured listing data using Zod schemas.
```

Example 2 (unknown):
```unknown
## Search

Find products on Etsy marketplace.
```

Example 3 (unknown):
```unknown
## Scrape

Scrape a single Etsy product listing.
```

Example 4 (unknown):
```unknown
## Map

Discover all available URLs in an Etsy shop or category. Note: Map returns URLs only, without content.
```

---

## Scraping Wikipedia

**URL:** llms-txt#scraping-wikipedia

**Contents:**
- Setup
- Use Cases
- Scrape with JSON Mode
- Search
- Scrape
- Map
- Crawl
- Batch Scrape

Source: https://docs.firecrawl.dev/developer-guides/common-sites/wikipedia

Extract articles, infoboxes, and build knowledge graphs from Wikipedia

Learn how to effectively scrape Wikipedia for research, knowledge extraction, and building AI applications.

* Research automation and fact-checking
* Building knowledge graphs
* Multi-language content extraction
* Educational content aggregation
* Entity information extraction

## Scrape with JSON Mode

Extract structured data from Wikipedia articles using Zod schemas.

Find articles on Wikipedia.

Scrape a single Wikipedia article.

Discover all available URLs in a Wikipedia portal or category. Note: Map returns URLs only, without content.

Crawl multiple pages from Wikipedia documentation or categories.

Scrape multiple Wikipedia URLs simultaneously.

**Examples:**

Example 1 (unknown):
```unknown
## Use Cases

* Research automation and fact-checking
* Building knowledge graphs
* Multi-language content extraction
* Educational content aggregation
* Entity information extraction

## Scrape with JSON Mode

Extract structured data from Wikipedia articles using Zod schemas.
```

Example 2 (unknown):
```unknown
## Search

Find articles on Wikipedia.
```

Example 3 (unknown):
```unknown
## Scrape

Scrape a single Wikipedia article.
```

Example 4 (unknown):
```unknown
## Map

Discover all available URLs in a Wikipedia portal or category. Note: Map returns URLs only, without content.
```

---

## Get Batch Scrape Status

**URL:** llms-txt#get-batch-scrape-status

Source: https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get

v2-openapi GET /batch/scrape/{id}

---

## Get Batch Scrape Errors

**URL:** llms-txt#get-batch-scrape-errors

Source: https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get-errors

v2-openapi GET /batch/scrape/{id}/errors

---

## Cancel Batch Scrape

**URL:** llms-txt#cancel-batch-scrape

Source: https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-delete

v2-openapi DELETE /batch/scrape/{id}

---

## Batch Scrape

**URL:** llms-txt#batch-scrape

**Contents:**
- Batch scraping multiple URLs
  - How it works
  - Usage
  - Response
- Batch scrape with structured extraction
  - Response
- Batch scrape with webhooks
  - Quick Reference

Source: https://docs.firecrawl.dev/features/batch-scrape

Batch scrape multiple URLs

## Batch scraping multiple URLs

You can now batch scrape multiple URLs at the same time. It takes the starting URLs and optional parameters as arguments. The params argument allows you to specify additional options for the batch scrape job, such as the output formats.

It is very similar to how the `/crawl` endpoint works. You can either start the batch and wait for completion, or start it and handle completion yourself.

* `batchScrape` (JS) / `batch_scrape` (Python): starts a batch job and waits for it to complete, returning the results.
* `startBatchScrape` (JS) / `start_batch_scrape` (Python): starts a batch job and returns the job ID so you can poll or use webhooks.

Calling `batchScrape`/`batch_scrape` returns the full results when the batch completes.

Calling `startBatchScrape`/`start_batch_scrape` returns
a job ID you can track via `getBatchScrapeStatus`/`get_batch_scrape_status`, using
the API endpoint `/batch/scrape/{id}`, or webhooks. This endpoint is intended for
in-progress checks or immediately after completion, **as batch jobs expire after
24 hours**.

## Batch scrape with structured extraction

You can also use the batch scrape endpoint to extract structured data from the pages. This is useful if you want to get the same structured data from a list of URLs.

`batchScrape`/`batch_scrape` returns full results:

`startBatchScrape`/`start_batch_scrape` returns a job ID:

## Batch scrape with webhooks

You can configure webhooks to receive real-time notifications as each URL in your batch is scraped. This allows you to process results immediately instead of waiting for the entire batch to complete.

For comprehensive webhook documentation including event types, payload structure, and implementation examples, see the [Webhooks documentation](/webhooks/overview).

* `batch_scrape.started` - When the batch scrape begins
* `batch_scrape.page` - For each URL successfully scraped
* `batch_scrape.completed` - When all URLs are processed
* `batch_scrape.failed` - If the batch scrape encounters an error

<Note>
  For detailed webhook configuration, security best practices, and
  troubleshooting, visit the [Webhooks documentation](/webhooks/overview).
</Note>

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown

```

Example 3 (unknown):
```unknown
</CodeGroup>

### Response

Calling `batchScrape`/`batch_scrape` returns the full results when the batch completes.
```

Example 4 (unknown):
```unknown
Calling `startBatchScrape`/`start_batch_scrape` returns
a job ID you can track via `getBatchScrapeStatus`/`get_batch_scrape_status`, using
the API endpoint `/batch/scrape/{id}`, or webhooks. This endpoint is intended for
in-progress checks or immediately after completion, **as batch jobs expire after
24 hours**.
```

---

## Use the agent

**URL:** llms-txt#use-the-agent

**Contents:**
- Best Practices
- Related Resources

response = research_agent.run("What are the latest features in Python 3.13?")
print(response)
```

1. **Use the right tool for the job**:
   * `firecrawl_search` when you need to find relevant pages first
   * `firecrawl_scrape` for single pages
   * `firecrawl_batch_scrape` for multiple known URLs
   * `firecrawl_crawl` for discovering and scraping entire sites

2. **Monitor your usage**: Configure credit thresholds to avoid unexpected usage

3. **Handle errors gracefully**: Configure retry settings based on your use case

4. **Optimize performance**: Use batch operations when scraping multiple URLs

<CardGroup cols={2}>
  <Card title="Comprehensive Guide to Building AI Agents Using Google Agent Development Kit (ADK) and Firecrawl" href="https://www.firecrawl.dev/blog/google-adk-multi-agent-tutorial">
    Learn how to build powerful multi-agent AI systems using Google's ADK framework with Firecrawl for web scraping capabilities.
  </Card>

<Card title="MCP Server Documentation" href="https://docs.firecrawl.dev/mcp-server">
    Learn more about Firecrawl's Model Context Protocol (MCP) server integration and capabilities.
  </Card>

<Card title="Google ADK Official Documentation" href="https://google.github.io/adk-docs/">
    Explore the official Google Agent Development Kit documentation for comprehensive guides and API references.
  </Card>
</CardGroup>

---
