# Firecrawl - Other

**Pages:** 84

---

## Rust

**URL:** llms-txt#rust

**Contents:**
- Installation

Source: https://docs.firecrawl.dev/sdks/rust

Firecrawl Rust SDK is a library to help you easily scrape and crawl websites, and output the data in a format ready for use with language models (LLMs).

<Warning>
  This SDK currently uses the **v1** version of the Firecrawl API, which is not the most recent (v2 is available). Some features and improvements may only be available in v2.
</Warning>

To install the Firecrawl Rust SDK, add the following to your `Cargo.toml`:

```yaml Rust theme={null}

---

## Search

**URL:** llms-txt#search

**Contents:**
- Performing a Search with Firecrawl
  - /search endpoint
  - Installation
  - Basic Usage
  - Response
- Search result types
- Search Categories
  - GitHub Category Search
  - Research Category Search
  - Mixed Category Search

Source: https://docs.firecrawl.dev/features/search

Search the web and get full content from results

Firecrawl's search API allows you to perform web searches and optionally scrape the search results in one operation.

* Choose specific output formats (markdown, HTML, links, screenshots)
* Search the web with customizable parameters (location, etc.)
* Optionally retrieve content from search results in various formats
* Control the number of results and set timeouts

For details, see the [Search Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/search).

## Performing a Search with Firecrawl

Used to perform web searches and optionally retrieve content from the results.

SDKs will return the data object directly. cURL will return the complete payload.

## Search result types

In addition to regular web results, Search supports specialized result types via the `sources` parameter:

* `web`: standard web results (default)
* `news`: news-focused results
* `images`: image search results

Filter search results by specific categories using the `categories` parameter:

* `github`: Search within GitHub repositories, code, issues, and documentation
* `research`: Search academic and research websites (arXiv, Nature, IEEE, PubMed, etc.)
* `pdf`: Search for PDFs

### GitHub Category Search

Search specifically within GitHub repositories:

### Research Category Search

Search academic and research websites:

### Mixed Category Search

Combine multiple categories in one search:

### Category Response Format

Each search result includes a `category` field indicating its source:

### HD Image Search with Size Filtering

Use Google Images operators to find high-resolution images:

**Common HD resolutions:**

* `imagesize:1920x1080` - Full HD (1080p)
* `imagesize:2560x1440` - QHD (1440p)
* `imagesize:3840x2160` - 4K UHD
* `larger:1920x1080` - HD and above
* `larger:2560x1440` - QHD and above

## Search with Content Scraping

Search and retrieve content from the search results in one operation.

Every option in scrape endpoint is supported by this search endpoint through the `scrapeOptions` parameter.

### Response with Scraped Content

## Advanced Search Options

Firecrawl's search API supports various parameters to customize your search:

### Location Customization

### Time-Based Search

Use the `tbs` parameter to filter results by time:

* `qdr:h` - Past hour
* `qdr:d` - Past 24 hours
* `qdr:w` - Past week
* `qdr:m` - Past month
* `qdr:y` - Past year

For more precise time filtering, you can specify exact date ranges using the custom date range format:

Set a custom timeout for search operations:

When search results are not scraped (no scrape options specified), the cost is 2 credits per 10 search results. When scraping is enabled, there is no additional charge for basic scrapes of each search result beyond the standard scraping costs.

However, be aware of these cost factors:

* **PDF parsing**: 1 credit per PDF page (can significantly increase costs for multi-page PDFs)
* **Stealth proxy mode**: +4 additional credits per search result
* ***JSON mode***: +4 additional credits per search result

* Set `parsers: []` if you don't need PDF content
* Use `proxy: "basic"` instead of `"stealth"` when possible
* Limit the number of search results with the `limit` parameter

## Advanced Scraping Options

For more details about the scraping options, refer to the [Scrape Feature documentation](https://docs.firecrawl.dev/features/scrape). Everything except for the FIRE-1 Agent and Change-Tracking features are supported by this Search endpoint.

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

### Basic Usage

<CodeGroup>
```

Example 3 (unknown):
```unknown

```

Example 4 (unknown):
```unknown

```

---

## MCP Web Search & Scrape in Cursor

**URL:** llms-txt#mcp-web-search-&-scrape-in-cursor

**Contents:**
- Quick Setup
  - 1. Get Your API Key
  - 2. Add to Cursor
  - 3. Restart Cursor
- Quick Demo

Source: https://docs.firecrawl.dev/developer-guides/mcp-setup-guides/cursor

Add web scraping and search to Cursor in 2 minutes

Add web scraping and search capabilities to Cursor with Firecrawl MCP.

### 1. Get Your API Key

Sign up at [firecrawl.dev/app](https://firecrawl.dev/app) and copy your API key.

Open Settings (`Cmd+,`), search for "MCP", and add:

Replace `your_api_key_here` with your actual Firecrawl API key.

### 3. Restart Cursor

Done! You can now search and scrape the web from Cursor.

Try these in Cursor Chat (`Cmd+K`):

Cursor will automatically use Firecrawl tools.

**Examples:**

Example 1 (unknown):
```unknown
Replace `your_api_key_here` with your actual Firecrawl API key.

### 3. Restart Cursor

Done! You can now search and scrape the web from Cursor.

## Quick Demo

Try these in Cursor Chat (`Cmd+K`):

**Search:**
```

Example 2 (unknown):
```unknown
**Scrape:**
```

Example 3 (unknown):
```unknown
**Get docs:**
```

---

## Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):

**URL:** llms-txt#your-quick-tunnel-has-been-created!-visit-it-at-(it-may-take-some-time-to-be-reachable):

---

## Firecrawl + Dify

**URL:** llms-txt#firecrawl-+-dify

**Contents:**
- Dify Integration Overview
- Firecrawl Tools in Dify
- Getting Started
- Usage Patterns
- Common Use Cases
- Firecrawl Actions
- Best Practices
- Dify vs Other Platforms

Source: https://docs.firecrawl.dev/developer-guides/workflow-automation/dify

Official plugin for Firecrawl + Dify AI workflow automation

<Note>
  **Official Dify Plugin:** [marketplace.dify.ai/plugins/langgenius/firecrawl](https://marketplace.dify.ai/plugins/langgenius/firecrawl)

Official plugin by Dify team • 44,000+ installs • Chatflow & Agent apps • Free to use
</Note>

## Dify Integration Overview

Dify is an open-source LLM app development platform. The official Firecrawl plugin enables web crawling and scraping directly in your AI workflows.

<CardGroup cols={2}>
  <Card title="Chatflow & Workflow Apps" icon="diagram-project">
    Build visual pipelines with Firecrawl nodes for data extraction
  </Card>

<Card title="Agent Applications" icon="robot">
    Give AI agents the power to scrape live web data on demand
  </Card>
</CardGroup>

## Firecrawl Tools in Dify

<AccordionGroup>
  <Accordion title="Scrape" icon="file-code">
    Convert any URL into clean, structured data. Transform raw HTML into actionable insights.

**Use Cases:** Extract product data, scrape article content, get structured data with JSON mode.
  </Accordion>

<Accordion title="Crawl" icon="spider">
    Perform recursive crawls of websites and subdomains to gather extensive content.

**Use Cases:** Full site content extraction, documentation scraping, multi-page data collection.
  </Accordion>

<Accordion title="Map" icon="sitemap">
    Generate a complete map of all URLs present on a website.

**Use Cases:** Site structure analysis, SEO auditing, URL discovery for batch scraping.
  </Accordion>

<Accordion title="Crawl Job" icon="list-check">
    Retrieve scraping results based on a Job ID or cancel ongoing tasks.

**Use Cases:** Monitor long-running crawls, manage async scraping workflows, cancel operations when needed.
  </Accordion>
</AccordionGroup>

<Steps>
  <Step title="Install Firecrawl Plugin">
    Access the [Dify Plugin Marketplace](https://marketplace.dify.ai/plugins/langgenius/firecrawl) and install the Firecrawl tool
  </Step>

<Step title="Get Firecrawl API Key">
    Visit [Firecrawl API Keys](https://www.firecrawl.dev/app/api-keys) and create a new API key
  </Step>

<Step title="Authorize in Dify">
    Navigate to **Plugins > Firecrawl > To Authorize** and input your API key
  </Step>

<Step title="Add to Your Workflow">
    Drag Firecrawl tools into your Chatflow, Workflow, or Agent application
  </Step>

<Step title="Configure & Test">
    Set up parameters and test your workflow
  </Step>
</Steps>

<Tabs>
  <Tab title="Chatflow Apps">
    **Visual Pipeline Integration**

1. Add Firecrawl node to your pipeline
    2. Select action (Map, Crawl, Scrape)
    3. Define input variables
    4. Execute pipeline sequentially

<Tab title="Workflow Apps">
    **Automated Data Processing**

Build multi-step workflows with:

* Scheduled scraping
    * Data transformation
    * Database storage
    * Notifications

<Tab title="Agent Apps">
    **AI-Powered Web Access**

Give agents real-time web scraping capabilities:

1. Add Firecrawl tool to Agent
    2. Agent autonomously decides when to scrape
    3. LLM analyzes extracted content
    4. Agent provides informed responses

**Use Case:** Customer support agents that reference live documentation
  </Tab>
</Tabs>

<CardGroup cols={2}>
  <Card title="AI Chatbot with Live Data" icon="messages">
    Build RAG-powered chatbots that scrape and reference live website content
  </Card>

<Card title="Content Analysis Agent" icon="brain">
    Agents that research topics by scraping and analyzing multiple sources
  </Card>

<Card title="Competitor Monitoring" icon="binoculars">
    Automated workflows that track competitor websites and alert on changes
  </Card>

<Card title="Data Enrichment Pipeline" icon="database">
    Extract and enrich data from websites into structured databases
  </Card>
</CardGroup>

| Tool          | Description                    | Best For                |
| ------------- | ------------------------------ | ----------------------- |
| **Scrape**    | Single-page data extraction    | Quick content capture   |
| **Crawl**     | Multi-page recursive crawling  | Full site extraction    |
| **Map**       | URL discovery and site mapping | SEO analysis, URL lists |
| **Crawl Job** | Async job management           | Long-running operations |

<CardGroup cols={2}>
  <Card title="Agent Apps" icon="robot">
    * Let agents decide when to scrape
    * Use natural language instructions
    * Enable tool calling in LLM settings
    * Monitor token usage with large scrapes
  </Card>

<Card title="Workflow Apps" icon="diagram-project">
    * Use Map before Crawl for large sites
    * Set appropriate crawl limits
    * Add error handling nodes
    * Test with small datasets first
  </Card>
</CardGroup>

## Dify vs Other Platforms

| Feature         | Dify                 | Make                | Zapier              | n8n                 |
| --------------- | -------------------- | ------------------- | ------------------- | ------------------- |
| **Type**        | LLM app platform     | Workflow automation | Workflow automation | Workflow automation |
| **Best For**    | AI agents & chatbots | Visual workflows    | Quick automation    | Developer control   |
| **Pricing**     | Open-source + Cloud  | Operations-based    | Per-task            | Flat monthly        |
| **AI-Native**   | Yes                  | Partial             | Partial             | Partial             |
| **Self-Hosted** | Yes                  | No                  | No                  | Yes                 |

<Tip>
  **Pro Tip:** Dify excels at building AI-native applications where agents need dynamic web access. Perfect for chatbots, research assistants, and AI tools that need live data.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
User Input → Firecrawl (Scrape) → LLM Processing → Response
```

Example 2 (unknown):
```unknown
Schedule Trigger → Firecrawl (Crawl) → Data Processing → Storage
```

---

## Proxies

**URL:** llms-txt#proxies

**Contents:**
- Location-Based Proxy Selection
- How to Specify Proxy Location
- Proxy Types

Source: https://docs.firecrawl.dev/features/proxies

Learn about proxy types, locations, and how Firecrawl selects proxies for your requests.

Firecrawl provides different proxy types to help you scrape websites with varying levels of anti-bot protection. The proxy type can be specified using the `proxy` parameter.

> By default, Firecrawl routes all requests through proxies to help ensure reliability and access, even if you do not specify a proxy type or location.

## Location-Based Proxy Selection

Firecrawl automatically selects the best proxy based on your specified or detected location. This helps optimize scraping performance and reliability. However, not all locations are currently supported. The following locations are available:

| Country Code | Country Name         | Stealth Mode Support |
| ------------ | -------------------- | -------------------- |
| AE           | United Arab Emirates | No                   |
| AU           | Australia            | Yes                  |
| BR           | Brazil               | Yes                  |
| CA           | Canada               | No                   |
| CN           | China                | No                   |
| CZ           | Czechia              | No                   |
| DE           | Germany              | Yes                  |
| FR           | France               | Yes                  |
| GB           | United Kingdom       | No                   |
| IL           | Israel               | No                   |
| IN           | India                | No                   |
| IT           | Italy                | No                   |
| JP           | Japan                | No                   |
| PL           | Poland               | No                   |
| PT           | Portugal             | No                   |
| QA           | Qatar                | No                   |
| TR           | Turkey               | No                   |
| US           | United States        | Yes                  |
| VN           | Vietnam              | No                   |

<Warning>The list of supported proxy locations was last updated on Sep 12, 2025. Availability may change over time.</Warning>

If you need proxies in a location not listed above, please [contact us](mailto:help@firecrawl.com) and let us know your requirements.

If you do not specify a proxy or location, Firecrawl will automatically select the best option based on the target site and your request.

## How to Specify Proxy Location

You can request a specific proxy location by setting the `location.country` parameter in your request. For example, to use a Brazilian proxy, set `location.country` to `BR`.

For full details, see the [API reference for `location.country`](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-location).

<Info>If you request a country where a proxy is not available, Firecrawl will use the closest available region (EU or US) and set the browser location to your requested country.</Info>

Firecrawl supports three types of proxies:

* **basic**: Proxies for scraping sites with none to basic anti-bot solutions. Fast and usually works.
* **stealth**: Stealth proxies for scraping sites with advanced anti-bot solutions, or for sites that block regular proxies. Slower, but more reliable on certain sites. [Learn more about Stealth Mode →](/features/stealth-mode)
* **auto**: Firecrawl will automatically retry scraping with stealth proxies if the basic proxy fails. If the retry with stealth is successful, 5 credits will be billed for the scrape. If the first attempt with basic is successful, only the regular cost will be billed.

> **Note:** For detailed information on using stealth proxies, including credit costs and retry strategies, see the [Stealth Mode documentation](/features/stealth-mode).

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown

```

---

## SEO Platforms

**URL:** llms-txt#seo-platforms

**Contents:**
- Start with a Template
- How It Works
- Why SEO Platforms Choose Firecrawl
  - Optimize for AI Discovery, Not Just Google
  - Complete Site Intelligence at Scale
- What You Can Build
- FAQs
- Related Use Cases

Source: https://docs.firecrawl.dev/use-cases/seo-platforms

Optimize websites for AI assistants and search engines

SEO platforms and consultants use Firecrawl to optimize websites for AI assistants and search engines.

## Start with a Template

<Card title="FireGEO" icon="github" href="https://github.com/mendableai/firegeo">
  GEO-powered SEO monitoring and multi-region rank tracking
</Card>

<Note>
  **Get started with the FireGEO template.** Optimize for both search engines and AI assistants.
</Note>

Prepare your website for the AI-first future. Audit AI readability and ensure your content is discoverable by both traditional search engines and AI assistants.

## Why SEO Platforms Choose Firecrawl

### Optimize for AI Discovery, Not Just Google

The future of search is AI-powered. While competitors focus on traditional SEO, forward-thinking platforms use Firecrawl to increase their clients' visibility in AI assistant responses-the new frontier of organic discovery.

### Complete Site Intelligence at Scale

Analyze entire websites, not just sample pages. Extract every meta tag, header structure, internal link, and content element across thousands of pages simultaneously. Identify optimization opportunities your competitors miss.

## What You Can Build

* **AI Readability Audit**: Optimize for AI comprehension
* **Content Analysis**: Structure and semantic optimization
* **Technical SEO**: Site performance and crawlability
* **SERP Tracking**: Monitor search engine positions

<AccordionGroup>
  <Accordion title="How can I optimize my site for AI assistants?">
    Firecrawl helps you structure content for optimal AI comprehension, extract semantic signals, and ensure your site follows best practices for AI discovery. This includes generating experimental formats like llms.txt (an emerging convention for AI crawler guidance).
  </Accordion>

<Accordion title="How does Firecrawl support SEO audits?">
    Firecrawl extracts complete site structures, meta tags, headers, internal links, and content to perform comprehensive SEO audits. Identify optimization opportunities and track improvements over time.
  </Accordion>

<Accordion title="Can Firecrawl help with competitor SEO analysis?">
    Yes. Analyze competitor site structures, keyword usage, content strategies, and technical SEO implementations. Understand what's working in your industry to inform your strategy.
  </Accordion>

<Accordion title="How can I use Firecrawl for content gap analysis?">
    Crawl competitor sites to identify topics they cover that you don't. Extract their content categories, blog topics, and page structures to find opportunities for new content.
  </Accordion>

<Accordion title="Does Firecrawl help with technical SEO monitoring?">
    Yes. Identify broken links, track redirect chains, extract canonical tags, and monitor meta tag implementation. Regular crawls help identify technical SEO issues across your site.
  </Accordion>
</AccordionGroup>

* [AI Platforms](/use-cases/ai-platforms) - Build AI-powered SEO tools
* [Competitive Intelligence](/use-cases/competitive-intelligence) - Track competitor SEO
* [Content Generation](/use-cases/content-generation) - Create SEO content

---

## Data Migration

**URL:** llms-txt#data-migration

**Contents:**
- Start with a Template
- How It Works
- What You Can Migrate
- Common Migration Use Cases
  - CMS Content Extraction
  - E-commerce Data Extraction
- FAQs
- Related Use Cases

Source: https://docs.firecrawl.dev/use-cases/data-migration

Transfer web data efficiently between platforms and systems

Migration teams use Firecrawl to transfer content between platforms and streamline customer onboarding from competitors.

## Start with a Template

<Card title="Firecrawl Migrator" icon="github" href="https://github.com/mendableai/firecrawl-migrator">
  Efficiently migrate data between platforms and systems
</Card>

<Note>
  **Get started with the Firecrawl Migrator template.** Extract and transform data for platform migrations.
</Note>

Use Firecrawl to extract data from existing websites for migration projects. Pull content, structure, and metadata from your current platform, then transform and import it into your new system using your preferred migration tools.

## What You Can Migrate

* **Content**: Pages, posts, articles, media files, metadata
* **Structure**: Hierarchies, categories, tags, taxonomies
* **Users**: Profiles and user-related data where publicly accessible
* **Settings**: Configurations, custom fields, workflows
* **E-commerce**: Products, catalogs, inventory, orders

## Common Migration Use Cases

Users build migration tools with Firecrawl to extract data from various platforms:

### CMS Content Extraction

* Extract content from WordPress, Drupal, Joomla sites
* Pull data from custom CMS platforms
* Preserve content structure and metadata
* Export for import into new systems like Contentful, Strapi, or Sanity

### E-commerce Data Extraction

* Extract product catalogs from Magento, WooCommerce stores
* Pull inventory and pricing data
* Capture product descriptions and specifications
* Format data for import into Shopify, BigCommerce, or other platforms

<AccordionGroup>
  <Accordion title="How do you handle large-scale migrations?">
    Our infrastructure scales automatically to handle large migrations. We support incremental processing with batching and parallel extraction, allowing you to migrate millions of pages by breaking them into manageable chunks with progress tracking.
  </Accordion>

<Accordion title="Can I preserve SEO value during migration?">
    Yes! Extract all SEO metadata including URLs, titles, descriptions, and implement proper redirects. We help maintain your search rankings through the migration.
  </Accordion>

<Accordion title="What about media files and attachments?">
    Firecrawl can extract and catalog all media files. You can download them for re-upload to your new platform or reference them directly if keeping the same CDN.
  </Accordion>

<Accordion title="How do I validate the migration?">
    We provide detailed extraction reports and support comparison tools. You can verify content completeness, check broken links, and validate data integrity.
  </Accordion>

<Accordion title="Can I migrate user-generated content and comments?">
    Yes, you can extract publicly visible user-generated content including comments, reviews, and forum posts. Private user data requires appropriate authentication and permissions.
  </Accordion>
</AccordionGroup>

* [Product & E-commerce](/use-cases/product-ecommerce) - Catalog migrations
* [Content Generation](/use-cases/content-generation) - Content transformation
* [AI Platforms](/use-cases/ai-platforms) - Knowledge base migration

---

## MCP Web Search & Scrape in Factory AI

**URL:** llms-txt#mcp-web-search-&-scrape-in-factory-ai

**Contents:**
- Quick Setup
  - 1. Get Your API Key
  - 2. Install Factory AI CLI
  - 3. Add Firecrawl MCP Server
  - 4. Done!
- Quick Demo

Source: https://docs.firecrawl.dev/developer-guides/mcp-setup-guides/factory-ai

Add web scraping and search to Factory AI in 2 minutes

Add web scraping and search capabilities to Factory AI with Firecrawl MCP.

### 1. Get Your API Key

Sign up at [firecrawl.dev/app](https://firecrawl.dev/app) and copy your API key.

### 2. Install Factory AI CLI

Install the [Factory AI CLI](https://docs.factory.ai/cli/getting-started/quickstart) if you haven't already:

### 3. Add Firecrawl MCP Server

In the Factory droid CLI, add Firecrawl using the `/mcp add` command:

Replace `your-api-key-here` with your actual Firecrawl API key.

The Firecrawl tools are now available in your Factory AI session!

Try these in Factory AI:

**Get documentation:**

Factory will automatically use Firecrawl's search and scrape tools to get the information.

**Examples:**

Example 1 (unknown):
```unknown
**Windows:**
```

Example 2 (unknown):
```unknown
### 3. Add Firecrawl MCP Server

In the Factory droid CLI, add Firecrawl using the `/mcp add` command:
```

Example 3 (unknown):
```unknown
Replace `your-api-key-here` with your actual Firecrawl API key.

### 4. Done!

The Firecrawl tools are now available in your Factory AI session!

## Quick Demo

Try these in Factory AI:

**Search the web:**
```

Example 4 (unknown):
```unknown
**Scrape a page:**
```

---

## Document Parsing

**URL:** llms-txt#document-parsing

**Contents:**
- Supported Document Formats
- How to Use Document Parsing
  - Example: Scraping an Excel File
  - Example: Scraping a Word Document
- Output Format
- Sheet1
- Sheet2

Source: https://docs.firecrawl.dev/features/document-parsing

Learn about document parsing capabilities.

Firecrawl provides powerful document parsing capabilities, allowing you to extract structured content from various document formats. This feature is particularly useful for processing files like spreadsheets, Word documents, and more.

## Supported Document Formats

Firecrawl currently supports the following document formats:

* **Excel Spreadsheets** (`.xlsx`, `.xls`)
  * Each worksheet is converted to an HTML table
  * Worksheets are separated by H2 headings with the sheet name
  * Preserves cell formatting and data types

* **Word Documents** (`.docx`, `.doc`, `.odt`, `.rtf`)
  * Extracts text content while preserving document structure
  * Maintains headings, paragraphs, lists, and tables
  * Preserves basic formatting and styling

* **PDF Documents** (`.pdf`)
  * Extracts text content with layout information
  * Preserves document structure including sections and paragraphs
  * Handles both text-based and scanned PDFs (with OCR support)
  * Priced at 1 credit per-page. See [Pricing](https://docs.firecrawl.dev/pricing) for details.

## How to Use Document Parsing

Document parsing in Firecrawl works automatically when you provide a URL that points to a supported document type. The system will detect the file type based on the URL extension or content-type header and process it accordingly.

### Example: Scraping an Excel File

### Example: Scraping a Word Document

All supported document types are converted to clean, structured markdown. For example, an Excel file with multiple sheets might be converted to:

**Examples:**

Example 1 (unknown):
```unknown
### Example: Scraping a Word Document
```

Example 2 (unknown):
```unknown
## Output Format

All supported document types are converted to clean, structured markdown. For example, an Excel file with multiple sheets might be converted to:
```

---

## You can specify a SearXNG server with the JSON format enabled, if you'd like to use that instead of direct Google.

**URL:** llms-txt#you-can-specify-a-searxng-server-with-the-json-format-enabled,-if-you'd-like-to-use-that-instead-of-direct-google.

---

## pip install firecrawl-py

**URL:** llms-txt#pip-install-firecrawl-py

**Contents:**
- Usage

from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
python Python theme={null}
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

**Examples:**

Example 1 (unknown):
```unknown
## Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `Firecrawl` class.

Here's an example of how to use the SDK:
```

---

## Other Optionals

**URL:** llms-txt#other-optionals

**Contents:**
  - Installing dependencies

TEST_API_KEY= # use if you've set up authentication and want to test with a real API key
OPENAI_API_KEY= # add for LLM dependednt features (image alt generation, etc.)
BULL_AUTH_KEY= @
PLAYWRIGHT_MICROSERVICE_URL=  # set if you'd like to run a playwright fallback
LLAMAPARSE_API_KEY= #Set if you have a llamaparse key you'd like to use to parse pdfs
SLACK_WEBHOOK_URL= # set if you'd like to send slack server health status messages
POSTHOG_API_KEY= # set if you'd like to send posthog events like job logs
POSTHOG_HOST= # set if you'd like to send posthog events like job logs

**Examples:**

Example 1 (unknown):
```unknown
### Installing dependencies

First, install the dependencies using pnpm.
```

---

## PROXY_PASSWORD=

**URL:** llms-txt#proxy_password=

**Contents:**
- === /search API ===

## === /search API ===

---

## Install dependencies

**URL:** llms-txt#install-dependencies

---

## SUPABASE_ANON_TOKEN=

**URL:** llms-txt#supabase_anon_token=

---

## Crawl

**URL:** llms-txt#crawl

**Contents:**
- Crawling
  - /crawl endpoint
  - Installation
  - Usage
  - Scrape options in crawl
  - API Response
  - Check Crawl Job
  - SDK methods
- Crawl WebSocket
- Crawl Webhook

Source: https://docs.firecrawl.dev/features/crawl

Firecrawl can recursively search through a urls subdomains, and gather the content

Firecrawl efficiently crawls websites to extract comprehensive data while bypassing blockers. The process:

1. **URL Analysis:** Scans sitemap and crawls website to identify links
2. **Traversal:** Recursively follows links to find all subpages
3. **Scraping:** Extracts content from each page, handling JS and rate limits
4. **Output:** Converts data to clean markdown or structured format

This ensures thorough data collection from any starting URL.

Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.

<Warning>
  By default - Crawl will ignore sublinks of a page if they aren't children of
  the url you provide. So, the website.com/other-parent/blog-1 wouldn't be
  returned if you crawled website.com/blogs/. If you want
  website.com/other-parent/blog-1, use the `crawlEntireDomain` parameter. To
  crawl subdomains like blog.website.com when crawling website.com, use the
  `allowSubdomains` parameter.
</Warning>

### Scrape options in crawl

All options from the Scrape endpoint are available in Crawl via `scrapeOptions` (JS) / `scrape_options` (Python). These apply to every page the crawler scrapes: formats, proxy, caching, actions, location, tags, etc. See the full list in the [Scrape API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

If you're using cURL or the starter method, this will return an `ID` to check the status of the crawl.

<Note>
  If you're using the SDK, see methods below for waiter vs starter behavior.
</Note>

Used to check the status of a crawl job and get its result.

<Note>
  This endpoint only works for crawls that are in progress or crawls that have
  completed recently.{' '}
</Note>

#### Response Handling

The response varies based on the crawl's status.

For not completed or large responses exceeding 10MB, a `next` URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the `next` parameter is absent, it indicates the end of the crawl data.

The skip parameter sets the maximum number of results returned for each chunk of results returned.

<Info>
  The skip and next parameter are only relavent when hitting the api directly.
  If you're using the SDK, we handle this for you and will return all the
  results at once.
</Info>

There are two ways to use the SDK:

1. **Crawl then wait** (`crawl`):
   * Waits for the crawl to complete and returns the full response
   * Handles pagination automatically
   * Recommended for most use cases

The response includes the crawl status and all scraped data:

2. **Start then check status** (`startCrawl`/`start_crawl`):
   * Returns immediately with a crawl ID
   * Allows manual status checking
   * Useful for long-running crawls or custom polling logic

Firecrawl's WebSocket-based method, `Crawl URL and Watch`, enables real-time data extraction and monitoring. Start a crawl with a URL and customize it with options like page limits, allowed domains, and output formats, ideal for immediate data processing needs.

You can configure webhooks to receive real-time notifications as your crawl progresses. This allows you to process pages as they're scraped instead of waiting for the entire crawl to complete.

For comprehensive webhook documentation including event types, payload structure, and implementation examples, see the [Webhooks documentation](/webhooks/overview).

* `crawl.started` - When the crawl begins
* `crawl.page` - For each page successfully scraped
* `crawl.completed` - When the crawl finishes
* `crawl.failed` - If the crawl encounters an error

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
</CodeGroup>

### Usage

<CodeGroup>
```

Example 3 (unknown):
```unknown

```

Example 4 (unknown):
```unknown

```

---

## Developers & MCP

**URL:** llms-txt#developers-&-mcp

**Contents:**
- Start with a Template
- How It Works
- Why Developers Choose Firecrawl MCP
  - Build Smarter AI Assistants
  - Zero Infrastructure Required
- Customer Stories
- FAQs
- Related Use Cases

Source: https://docs.firecrawl.dev/use-cases/developers-mcp

Build powerful integrations with Model Context Protocol support

Developers use Firecrawl's MCP server to add web scraping to Claude Desktop, Cursor, and other AI coding assistants.

## Start with a Template

<CardGroup cols={2}>
  <Card title="MCP Server Firecrawl" icon="github" href="https://github.com/mendableai/firecrawl-mcp-server">
    Official MCP server - Add web scraping to Claude Desktop and Cursor
  </Card>

<Card title="Open Lovable" icon="github" href="https://github.com/mendableai/open-lovable">
    Build complete applications from any website instantly
  </Card>
</CardGroup>

<Note>
  **Get started with MCP in minutes.** Follow our [setup guide](https://github.com/mendableai/firecrawl-mcp-server#installation) to integrate Firecrawl into Claude Desktop or Cursor.
</Note>

Integrate Firecrawl directly into your AI coding workflow. Research documentation, fetch API specs, and access web data without leaving your development environment through Model Context Protocol.

## Why Developers Choose Firecrawl MCP

### Build Smarter AI Assistants

Give your AI real-time access to documentation, APIs, and web resources. Reduce outdated information and hallucinations by providing your assistant with the latest data.

### Zero Infrastructure Required

No servers to manage, no crawlers to maintain. Just configure once and your AI assistant can access websites instantly through the Model Context Protocol.

<CardGroup cols={2}>
  <Card href="https://www.firecrawl.dev/blog/how-botpress-enhances-knowledge-base-creation-with-firecrawl">
    **Botpress**

Discover how Botpress uses Firecrawl to streamline knowledge base population and improve developer experience.
  </Card>

<Card href="https://www.firecrawl.dev/blog/how-answer-hq-powers-ai-customer-support-with-firecrawl">
    **Answer HQ**

Learn how Answer HQ uses Firecrawl to help businesses import website data and build intelligent support assistants.
  </Card>
</CardGroup>

<AccordionGroup>
  <Accordion title="Which AI assistants support MCP?">
    Currently, Claude Desktop and Cursor have native MCP support. More AI assistants are adding support regularly. You can also use the MCP SDK to build custom integrations.
  </Accordion>

<Accordion title="Can I use MCP in VS Code or other IDEs?">
    VS Code and other IDEs can use MCP through community extensions or terminal integrations. Native support varies by IDE. Check our [GitHub repository](https://github.com/mendableai/firecrawl-mcp-server) for IDE-specific setup guides.
  </Accordion>

<Accordion title="How do I cache frequently accessed docs?">
    The MCP server automatically caches responses for 15 minutes. You can configure cache duration in your MCP server settings or implement custom caching logic.
  </Accordion>

<Accordion title="Is there a rate limit for MCP requests?">
    MCP requests use your standard Firecrawl API rate limits. We recommend batching related requests and using caching for frequently accessed documentation.
  </Accordion>

<Accordion title="How do I set up MCP with my Firecrawl API key?">
    Follow our [setup guide](https://github.com/mendableai/firecrawl-mcp-server#installation) to configure MCP. You'll need to add your Firecrawl API key to your MCP configuration file. The process takes just a few minutes.
  </Accordion>
</AccordionGroup>

* [AI Platforms](/use-cases/ai-platforms) - Build AI-powered dev tools
* [Deep Research](/use-cases/deep-research) - Complex technical research
* [Content Generation](/use-cases/content-generation) - Generate documentation

---

## JSON mode - Structured result

**URL:** llms-txt#json-mode---structured-result

**Contents:**
- Scrape and extract structured data with Firecrawl
- Extract structured data
  - JSON mode via /scrape
  - Structured data without schema
  - Real-world example: Extracting company information
  - JSON format options

Source: https://docs.firecrawl.dev/features/llm-extract

Extract structured data from pages via LLMs

<Note>
  **v2 API Change:** JSON schema extraction is fully supported in v2, but the API format has changed. In v2, the schema is embedded directly inside the format object as `formats: [{type: "json", schema: {...}}]`. The v1 `jsonOptions` parameter no longer exists in v2.
</Note>

## Scrape and extract structured data with Firecrawl

Firecrawl uses AI to get structured data from web pages in 3 steps:

1. **Set the Schema (optional):**
   Define a JSON schema (using OpenAI's format) to specify the data you want, or just provide a `prompt` if you don't need a strict schema, along with the webpage URL.

2. **Make the Request:**
   Send your URL and schema to our scrape endpoint using JSON mode. See how here:
   [Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)

3. **Get Your Data:**
   Get back clean, structured data matching your schema that you can use right away.

This makes getting web data in the format you need quick and easy.

## Extract structured data

### JSON mode via /scrape

Used to extract structured data from scraped pages.

### Structured data without schema

You can also extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.

### Real-world example: Extracting company information

Here's a comprehensive example extracting structured company information from a website:

### JSON format options

When using JSON mode in v2, include an object in `formats` with the schema embedded directly:

`formats: [{ type: 'json', schema: { ... }, prompt: '...' }]`

* `schema`: JSON Schema describing the structured output you want (required for schema-based extraction).
* `prompt`: Optional prompt to guide extraction (also used for no-schema extraction).

**Important:** Unlike v1, there is no separate `jsonOptions` parameter in v2. The schema must be included directly inside the format object in the `formats` array.

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

Output:
```

Example 4 (unknown):
```unknown
### Structured data without schema

You can also extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.

<CodeGroup>
```

---

## Agent Development Kit (ADK)

**URL:** llms-txt#agent-development-kit-(adk)

**Contents:**
- Overview
- Features
- Prerequisites
- Setup
- Available Tools
- Configuration
  - Required Configuration
  - Optional Configuration
- Example: Web Research Agent

Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/google-adk

Integrate Firecrawl with Google's ADK using MCP for advanced agent workflows

Integrate Firecrawl with Google's Agent Development Kit (ADK) to build powerful AI agents with web scraping capabilities through the Model Context Protocol (MCP).

Firecrawl provides an MCP server that seamlessly integrates with Google's ADK, enabling your agents to efficiently scrape, crawl, and extract structured data from any website. The integration supports both cloud-based and self-hosted Firecrawl instances with streamable HTTP for optimal performance.

* Efficient web scraping, crawling, and content discovery from any website
* Advanced search capabilities and intelligent content extraction
* Deep research and high-volume batch scraping
* Flexible deployment (cloud-based or self-hosted)
* Optimized for modern web environments with streamable HTTP support

* Obtain an API key for Firecrawl from [firecrawl.dev](https://firecrawl.dev)
* Install Google ADK

| Tool               | Name                           | Description                                                                          |
| ------------------ | ------------------------------ | ------------------------------------------------------------------------------------ |
| Scrape Tool        | `firecrawl_scrape`             | Scrape content from a single URL with advanced options                               |
| Batch Scrape Tool  | `firecrawl_batch_scrape`       | Scrape multiple URLs efficiently with built-in rate limiting and parallel processing |
| Check Batch Status | `firecrawl_check_batch_status` | Check the status of a batch operation                                                |
| Map Tool           | `firecrawl_map`                | Map a website to discover all indexed URLs on the site                               |
| Search Tool        | `firecrawl_search`             | Search the web and optionally extract content from search results                    |
| Crawl Tool         | `firecrawl_crawl`              | Start an asynchronous crawl with advanced options                                    |
| Check Crawl Status | `firecrawl_check_crawl_status` | Check the status of a crawl job                                                      |
| Extract Tool       | `firecrawl_extract`            | Extract structured information from web pages using LLM capabilities                 |

### Required Configuration

**FIRECRAWL\_API\_KEY**: Your Firecrawl API key

* Required when using cloud API (default)
* Optional when using self-hosted instance with FIRECRAWL\_API\_URL

### Optional Configuration

**Firecrawl API URL (for self-hosted instances)**:

* `FIRECRAWL_API_URL`: Custom API endpoint
* Example: `https://firecrawl.your-domain.com`
* If not provided, the cloud API will be used

**Retry configuration**:

* `FIRECRAWL_RETRY_MAX_ATTEMPTS`: Maximum retry attempts (default: 3)
* `FIRECRAWL_RETRY_INITIAL_DELAY`: Initial delay in milliseconds (default: 1000)
* `FIRECRAWL_RETRY_MAX_DELAY`: Maximum delay in milliseconds (default: 10000)
* `FIRECRAWL_RETRY_BACKOFF_FACTOR`: Exponential backoff multiplier (default: 2)

**Credit usage monitoring**:

* `FIRECRAWL_CREDIT_WARNING_THRESHOLD`: Warning threshold (default: 1000)
* `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD`: Critical threshold (default: 100)

## Example: Web Research Agent

```python  theme={null}
from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

FIRECRAWL_API_KEY = "YOUR-API-KEY"

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

## Available Tools

| Tool               | Name                           | Description                                                                          |
| ------------------ | ------------------------------ | ------------------------------------------------------------------------------------ |
| Scrape Tool        | `firecrawl_scrape`             | Scrape content from a single URL with advanced options                               |
| Batch Scrape Tool  | `firecrawl_batch_scrape`       | Scrape multiple URLs efficiently with built-in rate limiting and parallel processing |
| Check Batch Status | `firecrawl_check_batch_status` | Check the status of a batch operation                                                |
| Map Tool           | `firecrawl_map`                | Map a website to discover all indexed URLs on the site                               |
| Search Tool        | `firecrawl_search`             | Search the web and optionally extract content from search results                    |
| Crawl Tool         | `firecrawl_crawl`              | Start an asynchronous crawl with advanced options                                    |
| Check Crawl Status | `firecrawl_check_crawl_status` | Check the status of a crawl job                                                      |
| Extract Tool       | `firecrawl_extract`            | Extract structured information from web pages using LLM capabilities                 |

## Configuration

### Required Configuration

**FIRECRAWL\_API\_KEY**: Your Firecrawl API key

* Required when using cloud API (default)
* Optional when using self-hosted instance with FIRECRAWL\_API\_URL

### Optional Configuration

**Firecrawl API URL (for self-hosted instances)**:

* `FIRECRAWL_API_URL`: Custom API endpoint
* Example: `https://firecrawl.your-domain.com`
* If not provided, the cloud API will be used

**Retry configuration**:

* `FIRECRAWL_RETRY_MAX_ATTEMPTS`: Maximum retry attempts (default: 3)
* `FIRECRAWL_RETRY_INITIAL_DELAY`: Initial delay in milliseconds (default: 1000)
* `FIRECRAWL_RETRY_MAX_DELAY`: Maximum delay in milliseconds (default: 10000)
* `FIRECRAWL_RETRY_BACKOFF_FACTOR`: Exponential backoff multiplier (default: 2)

**Credit usage monitoring**:

* `FIRECRAWL_CREDIT_WARNING_THRESHOLD`: Warning threshold (default: 1000)
* `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD`: Critical threshold (default: 100)

## Example: Web Research Agent
```

---

## Set if you'd like to send posthog events like job logs

**URL:** llms-txt#set-if-you'd-like-to-send-posthog-events-like-job-logs

---

## SEARXNG_ENGINES=

**URL:** llms-txt#searxng_engines=

---

## MCP Web Search & Scrape in Windsurf

**URL:** llms-txt#mcp-web-search-&-scrape-in-windsurf

**Contents:**
- Quick Setup
  - 1. Get Your API Key
  - 2. Add to Windsurf
  - 3. Restart Windsurf
- Quick Demo

Source: https://docs.firecrawl.dev/developer-guides/mcp-setup-guides/windsurf

Add web scraping and search to Windsurf in 2 minutes

Add web scraping and search capabilities to Windsurf with Firecrawl MCP.

### 1. Get Your API Key

Sign up at [firecrawl.dev/app](https://firecrawl.dev/app) and copy your API key.

### 2. Add to Windsurf

Add this to your `./codeium/windsurf/model_config.json`:

Replace `YOUR_API_KEY` with your actual Firecrawl API key.

### 3. Restart Windsurf

Done! Windsurf can now search and scrape the web.

Try these in Windsurf:

Windsurf's AI agents will automatically use Firecrawl tools.

**Examples:**

Example 1 (unknown):
```unknown
Replace `YOUR_API_KEY` with your actual Firecrawl API key.

### 3. Restart Windsurf

Done! Windsurf can now search and scrape the web.

## Quick Demo

Try these in Windsurf:

**Search:**
```

Example 2 (unknown):
```unknown
**Scrape:**
```

Example 3 (unknown):
```unknown
**Get docs:**
```

---

## Firecrawl + Make

**URL:** llms-txt#firecrawl-+-make

**Contents:**
- Make Integration Overview
- Firecrawl Modules in Make
- Popular App Integrations
- Common Workflow Patterns
- Getting Started
- Firecrawl Actions Overview
- Best Practices
- Industry Use Cases
- Make vs Zapier vs n8n

Source: https://docs.firecrawl.dev/developer-guides/workflow-automation/make

Official integration and workflow automation for Firecrawl + Make

<Note>
  **Official Make Integration:** [make.com/en/integrations/firecrawl](https://www.make.com/en/integrations/firecrawl)

Connect with 3,000+ apps • Visual workflow builder • Enterprise-grade automation • AI-powered scenarios
</Note>

## Make Integration Overview

Make (formerly Integromat) provides a verified, officially supported Firecrawl integration maintained by Mendable.

<CardGroup cols={2}>
  <Card title="Visual Workflow Builder" icon="diagram-project">
    Design complex automations with Make's intuitive visual interface
  </Card>

<Card title="Enterprise Ready" icon="building">
    Scale securely with enterprise-grade automation and controls
  </Card>
</CardGroup>

## Firecrawl Modules in Make

<AccordionGroup>
  <Accordion title="Actions (7 modules)" icon="bolt">
    ### Crawl a Website

Crawl a URL and get its content from multiple pages

### Extract a Website

Extract structured data from pages using LLMs

Scrape a URL and get its content from a single page

Map multiple URLs based on options

Web search (SERP) with Firecrawl's scraping capabilities

Get the status of a given crawl event ID

### Get Extract Status

Get the status of a given extraction event ID
  </Accordion>

<Accordion title="Search (1 module)" icon="magnifying-glass">
    ### Search a Website

Full-page content retrieval for any search query
  </Accordion>

<Accordion title="Advanced" icon="code">
    ### Make an API Call

Perform arbitrary authorized API calls for custom use cases
  </Accordion>
</AccordionGroup>

## Popular App Integrations

<Tabs>
  <Tab title="Data Storage">
    **Google Sheets** - Track and log scraped data in spreadsheets

**Airtable** - Build structured databases with scraped content

**Google Drive** - Store scraped files and reports

**Notion** - Organize research and web data
  </Tab>

<Tab title="Communication">
    **Slack** - Get alerts for website changes and updates

**Telegram Bot** - Instant notifications for monitoring

**Gmail** - Email reports and digests

**Microsoft 365 Email** - Enterprise email automation
  </Tab>

<Tab title="CRM & Sales">
    **HubSpot CRM** - Enrich leads with web data

**monday.com** - Track competitor intelligence

**ClickUp** - Manage research tasks
  </Tab>

<Tab title="AI Tools">
    **OpenAI (ChatGPT, DALL-E)** - Analyze and summarize scraped content

**Google Gemini AI** - Process and extract insights

**Perplexity AI** - Enhanced research workflows

**Make AI Agents** - Build adaptive AI-powered automations
  </Tab>
</Tabs>

## Common Workflow Patterns

<CardGroup cols={2}>
  <Card title="Competitor Monitoring" icon="binoculars">
    **Schedule** → Firecrawl (Scrape) → Google Sheets (Log) → Slack (Alert)

Track competitor websites and get instant notifications
  </Card>

<Card title="Lead Enrichment" icon="users">
    **Google Forms** → Firecrawl (Scrape company site) → HubSpot CRM (Update)

Automatically enrich leads with company data
  </Card>

<Card title="Content Aggregation" icon="newspaper">
    **Schedule** → Firecrawl (Crawl blog) → OpenAI (Summarize) → Gmail (Send digest)

Automated content curation and distribution
  </Card>

<Card title="Price Monitoring" icon="chart-line">
    **Schedule (Hourly)** → Firecrawl (Scrape) → Filter → Telegram (Alert)

Real-time price tracking and alerts
  </Card>
</CardGroup>

<Steps>
  <Step title="Sign up for Firecrawl">
    Get your API key at [firecrawl.dev](https://firecrawl.dev)
  </Step>

<Step title="Create a Scenario in Make">
    Log into [Make](https://make.com) and click "Create a new scenario"
  </Step>

<Step title="Add Firecrawl Module">
    Search for "Firecrawl" and select your desired action
  </Step>

<Step title="Connect with API Key">
    Add your Firecrawl API key to authenticate
  </Step>

<Step title="Configure & Test">
    Set up your workflow parameters and run a test
  </Step>
</Steps>

## Firecrawl Actions Overview

| Module                | Use Case                         | Best For            |
| --------------------- | -------------------------------- | ------------------- |
| **Scrape a Website**  | Single-page data extraction      | Quick data capture  |
| **Crawl a Website**   | Multi-page content collection    | Full site scraping  |
| **Extract a Website** | AI-powered structured extraction | Complex data needs  |
| **Search a Website**  | SERP + full content              | Research automation |
| **Map a Website**     | URL discovery                    | SEO analysis        |

<CardGroup cols={2}>
  <Card title="Performance" icon="gauge-high">
    * Use **Scrape** for single pages (fastest)
    * Use **Crawl** with limits for large sites
    * Schedule appropriately to avoid rate limits
    * Add error handling modules
  </Card>

<Card title="Cost Optimization" icon="piggy-bank">
    * Schedule strategically (hourly/daily/weekly)
    * Use filters to prevent unnecessary runs
    * Set crawl limits to control API usage
    * Test in Firecrawl playground first
  </Card>
</CardGroup>

## Industry Use Cases

<AccordionGroup>
  <Accordion title="E-commerce" icon="cart-shopping">
    * Competitor price monitoring
    * Product availability tracking
    * Review aggregation and analysis
    * Inventory level monitoring
  </Accordion>

<Accordion title="Real Estate" icon="house">
    * Listing aggregation from multiple sources
    * Market trend analysis
    * Property data enrichment
    * Competitive pricing intelligence
  </Accordion>

<Accordion title="Marketing" icon="bullhorn">
    * Competitor content monitoring
    * SEO performance tracking
    * Backlink analysis
    * Social media mention tracking
  </Accordion>

<Accordion title="Finance" icon="chart-line">
    * Market data collection
    * News and sentiment aggregation
    * Regulatory filing monitoring
    * Stock price tracking
  </Accordion>

<Accordion title="HR & Recruitment" icon="user-tie">
    * Job posting aggregation
    * Company research automation
    * Candidate background enrichment
    * Salary benchmarking
  </Accordion>
</AccordionGroup>

## Make vs Zapier vs n8n

| Feature            | Make                              | Zapier           | n8n                  |
| ------------------ | --------------------------------- | ---------------- | -------------------- |
| **Setup**          | Visual builder, cloud             | No-code, cloud   | Self-hosted or cloud |
| **Pricing**        | Operations-based                  | Per-task pricing | Flat monthly         |
| **Integrations**   | 3,000+ apps                       | 8,000+ apps      | 400+ integrations    |
| **Complexity**     | Advanced workflows                | Simple workflows | Complex workflows    |
| **Best For**       | Visual automation, mid-complexity | Quick automation | Developer control    |
| **Learning Curve** | Moderate                          | Easy             | Moderate-Advanced    |

<Tip>
  **Pro Tip:** Make excels at visual workflow design and complex automations. Perfect for teams that need more control than Zapier but prefer visual building over n8n's code-first approach.
</Tip>

---

## Scrape a website:

**URL:** llms-txt#scrape-a-website:

**Contents:**
  - Crawl a Website
  - Start a Crawl
  - Checking Crawl Status
  - Cancelling a Crawl
  - Map a Website
  - Crawling a Website with WebSockets
  - Pagination
- Error Handling
- Async Class

scrape_result = firecrawl.scrape('firecrawl.dev', formats=['markdown', 'html'])
print(scrape_result)
python Python theme={null}
job = firecrawl.crawl(url="https://docs.firecrawl.dev", limit=5, poll_interval=1, timeout=120)
print(job)
python Python theme={null}
job = firecrawl.start_crawl(url="https://docs.firecrawl.dev", limit=10)
print(job)
python Python theme={null}
status = firecrawl.get_crawl_status("<crawl-id>")
print(status)
python Python theme={null}
ok = firecrawl.cancel_crawl("<crawl-id>")
print("Cancelled:", ok)
python Python theme={null}
res = firecrawl.map(url="https://firecrawl.dev", limit=10)
print(res)
python Python theme={null}
import asyncio
from firecrawl import AsyncFirecrawl

async def main():
    firecrawl = AsyncFirecrawl(api_key="fc-YOUR-API-KEY")

# Start a crawl first
    started = await firecrawl.start_crawl("https://firecrawl.dev", limit=5)

# Watch updates (snapshots) until terminal status
    async for snapshot in firecrawl.watcher(started.id, kind="crawl", poll_interval=2, timeout=120):
        if snapshot.status == "completed":
            print("DONE", snapshot.status)
            for doc in snapshot.data:
                print("DOC", doc.metadata.source_url if doc.metadata else None)
        elif snapshot.status == "failed":
            print("ERR", snapshot.status)
        else:
            print("STATUS", snapshot.status, snapshot.completed, "/", snapshot.total)

asyncio.run(main())
python Python theme={null}
crawl_job = client.start_crawl("https://example.com", limit=100)

status = client.get_crawl_status(crawl_job.id, pagination_config=PaginationConfig(auto_paginate=False))
print("crawl single page:", status.status, "docs:", len(status.data), "next:", status.next)
python Python theme={null}
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=50, max_wait_time=15),
)
print("crawl limited:", status.status, "docs:", len(status.data), "next:", status.next)
python Python theme={null}
batch_job = client.start_batch_scrape(urls)
status = client.get_batch_scrape_status(batch_job.id, pagination_config=PaginationConfig(auto_paginate=False))
print("batch single page:", status.status, "docs:", len(status.data), "next:", status.next)
python Python theme={null}
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=100, max_wait_time=20),
)
print("batch limited:", status.status, "docs:", len(status.data), "next:", status.next)
python Python theme={null}
import asyncio
from firecrawl import AsyncFirecrawl

async def main():
    firecrawl = AsyncFirecrawl(api_key="fc-YOUR-API-KEY")

# Scrape
    doc = await firecrawl.scrape("https://firecrawl.dev", formats=["markdown"])  # type: ignore[arg-type]
    print(doc.get("markdown"))

# Search
    results = await firecrawl.search("firecrawl", limit=2)
    print(results.get("web", []))

# Crawl (start + status)
    started = await firecrawl.start_crawl("https://docs.firecrawl.dev", limit=3)
    status = await firecrawl.get_crawl_status(started.id)
    print(status.status)

# Batch scrape (wait)
    job = await firecrawl.batch_scrape([
        "https://firecrawl.dev",
        "https://docs.firecrawl.dev",
    ], formats=["markdown"], poll_interval=1, timeout=60)
    print(job.status, job.completed, job.total)

asyncio.run(main())
```

**Examples:**

Example 1 (unknown):
```unknown
### Crawl a Website

To crawl a website, use the `crawl` method. It takes the starting URL and optional options as arguments. The options allow you to specify additional settings for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format. See [Pagination](#pagination) for auto/manual pagination and limiting.
```

Example 2 (unknown):
```unknown
### Start a Crawl

<Tip>Prefer non-blocking? Check out the [Async Class](#async-class) section below.</Tip>

Start a job without waiting using `start_crawl`. It returns a job `ID` you can use to check status. Use `crawl` when you want a waiter that blocks until completion. See [Pagination](#pagination) for paging behavior and limits.
```

Example 3 (unknown):
```unknown
### Checking Crawl Status

To check the status of a crawl job, use the `get_crawl_status` method. It takes the job ID as a parameter and returns the current status of the crawl job.
```

Example 4 (unknown):
```unknown
### Cancelling a Crawl

To cancel an crawl job, use the `cancel_crawl` method. It takes the job ID of the `start_crawl` as a parameter and returns the cancellation status.
```

---

## Change Tracking

**URL:** llms-txt#change-tracking

**Contents:**
- Overview
- SDKs
  - Basic Usage
  - Advanced Options
  - Git-Diff Results Example:
  - JSON Comparison Results Example:
  - Data Models
- Change Tracking Modes
  - Git-Diff Mode
  - JSON Mode

Source: https://docs.firecrawl.dev/features/change-tracking

Firecrawl can track changes between the current page and a previous version, and tell you if it updated or not

<img src="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=cc56c24d15e1b2ed4806ddb66d0f5c3f" alt="Change Tracking" data-og-width="2400" width="2400" data-og-height="1350" height="1350" data-path="images/launch-week/lw3d12.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?w=280&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2f46113bc318badaeaf0fb32e7645df8 280w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?w=560&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2fd31b621bcb393815715ce8fe1e5abd 560w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?w=840&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2423ca2755bdb28f4d3e64e1abffebf6 840w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?w=1100&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=cc14d2752f8888824b84ea121fcbbb7d 1100w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?w=1650&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2e8a59b9d8f69c378551f4c5ff20e13d 1650w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?w=2500&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=830c7f2a9465d9f6f3733a5289a5e9fe 2500w" />

Change tracking allows you to monitor and detect changes in web content over time. This feature is available in both the JavaScript and Python SDKs.

Change tracking enables you to:

* Detect if a webpage has changed since the last scrape
* View the specific changes between scrapes
* Get structured data about what has changed
* Control the visibility of changes

Using the `changeTracking` format, you can monitor changes on a website and receive information about:

* `previousScrapeAt`: The timestamp of the previous scrape that the current page is being compared against (`null` if no previous scrape)
* `changeStatus`: The result of the comparison between the two page versions
  * `new`: This page did not exist or was not discovered before (usually has a `null` `previousScrapeAt`)
  * `same`: This page's content has not changed since the last scrape
  * `changed`: This page's content has changed since the last scrape
  * `removed`: This page was removed since the last scrape
* `visibility`: The visibility of the current page/URL
  * `visible`: This page is visible, meaning that its URL was discovered through an organic route (through links on other visible pages or the sitemap)
  * `hidden`: This page is not visible, meaning it is still available on the web, but no longer discoverable via the sitemap or crawling the site. We can only identify invisible links if they had been visible, and captured, during a previous crawl or scrape

To use change tracking, include `'changeTracking'` in the formats when scraping a URL:

You can configure change tracking by passing an object in the `formats` array:

### Git-Diff Results Example:

### JSON Comparison Results Example:

The change tracking feature includes the following data models:

## Change Tracking Modes

The change tracking feature supports two modes:

The `git-diff` mode provides a traditional diff format similar to Git's output. It shows line-by-line changes with additions and deletions marked.

The structured JSON representation of the diff includes:

* `files`: Array of changed files (in web context, typically just one)
* `chunks`: Sections of changes within a file
* `changes`: Individual line changes with type (add, delete, normal)

The `json` mode provides a structured comparison of specific fields extracted from the content. This is useful for tracking changes in specific data points rather than the entire content.

To use JSON mode, you need to provide a schema that defines the fields to extract and compare.

Here are some important details to know when using the change tracking feature:

* **Comparison Method**: Scrapes are always compared via their markdown response.
  * The `markdown` format must also be specified when using the `changeTracking` format. Other formats may also be specified in addition.
  * The comparison algorithm is resistant to changes in whitespace and content order. iframe source URLs are currently ignored for resistance against captchas and antibots with randomized URLs.

* **Matching Previous Scrapes**: Previous scrapes to compare against are currently matched on the source URL, the team ID, the `markdown` format, and the `tag` parameter.
  * For an effective comparison, the input URL should be exactly the same as the previous request for the same content.
  * Crawling the same URLs with different `includePaths`/`excludePaths` will have inconsistencies when using `changeTracking`.
  * Scraping the same URLs with different `includeTags`/`excludeTags`/`onlyMainContent` will have inconsistencies when using `changeTracking`.
  * Compared pages will also be compared against previous scrapes that only have the `markdown` format without the `changeTracking` format.
  * Comparisons are scoped to your team. If you scrape a URL for the first time with your API key, its `changeStatus` will always be `new`, even if other Firecrawl users have scraped it before.

* **Beta Status**: While in Beta, it is recommended to monitor the `warning` field of the resulting document, and to handle the `changeTracking` object potentially missing from the response.
  * This may occur when the database lookup to find the previous scrape to compare against times out.

### Basic Scrape Example

### Tracking Product Price Changes

### Monitoring Content Changes with Git-Diff

The change tracking feature is currently in beta. Using the basic change tracking functionality and `git-diff` mode has no additional cost. However, if you use the `json` mode for structured data comparison, the page scrape will cost 5 credits per page.

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

Example Response:
```

Example 3 (unknown):
```unknown
### Advanced Options

You can configure change tracking by passing an object in the `formats` array:

<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## Add this to your Cargo.toml

**URL:** llms-txt#add-this-to-your-cargo.toml

**Contents:**
- Usage
  - Scraping a URL
  - Scraping with Extract
  - Crawling a Website
  - Map a URL
- Error Handling

[dependencies]
firecrawl = "^1.0"
tokio = { version = "^1", features = ["full"] }
rust Rust theme={null}
use firecrawl::{crawl::{CrawlOptions, CrawlScrapeOptions, CrawlScrapeFormats}, FirecrawlApp, scrape::{ScrapeOptions, ScrapeFormats}};

#[tokio::main]
async fn main() {
    // Initialize the FirecrawlApp with the API key
    let app = FirecrawlApp::new("fc-YOUR_API_KEY").expect("Failed to initialize FirecrawlApp");

// Scrape a URL
    let options = ScrapeOptions {
        formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
        ..Default::default()
    };

let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

match scrape_result {
        Ok(data) => println!("Scrape Result:\n{}", data.markdown.unwrap()),
        Err(e) => eprintln!("Map failed: {}", e),
    }

// Crawl a website
    let crawl_options = CrawlOptions {
        scrape_options: CrawlScrapeOptions {
            formats: vec![ CrawlScrapeFormats::Markdown, CrawlScrapeFormats::HTML ].into(),
            ..Default::default()
        }.into(),
        limit: 100.into(),
        ..Default::default()
    };

let crawl_result = app
        .crawl_url("https://mendable.ai", crawl_options)
        .await;

match crawl_result {
        Ok(data) => println!("Crawl Result (used {} credits):\n{:#?}", data.credits_used, data.data),
        Err(e) => eprintln!("Crawl failed: {}", e),
    }
}
rust Rust theme={null}
let options = ScrapeOptions {
    formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
    ..Default::default()
};

let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

match scrape_result {
    Ok(data) => println!("Scrape Result:\n{}", data.markdown.unwrap()),
    Err(e) => eprintln!("Map failed: {}", e),
}
rust Rust theme={null}
let json_schema = json!({
    "type": "object",
    "properties": {
        "top": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "points": {"type": "number"},
                    "by": {"type": "string"},
                    "commentsURL": {"type": "string"}
                },
                "required": ["title", "points", "by", "commentsURL"]
            },
            "minItems": 5,
            "maxItems": 5,
            "description": "Top 5 stories on Hacker News"
        }
    },
    "required": ["top"]
});

let llm_extraction_options = ScrapeOptions {
    formats: vec![ ScrapeFormats::Json ].into(),
    jsonOptions: ExtractOptions {
        schema: json_schema.into(),
        ..Default::default()
    }.into(),
    ..Default::default()
};

let llm_extraction_result = app
    .scrape_url("https://news.ycombinator.com", llm_extraction_options)
    .await;

match llm_extraction_result {
    Ok(data) => println!("LLM Extraction Result:\n{:#?}", data.extract.unwrap()),
    Err(e) => eprintln!("LLM Extraction failed: {}", e),
}
rust Rust theme={null}
let crawl_options = CrawlOptions {
    scrape_options: CrawlScrapeOptions {
        formats: vec![ CrawlScrapeFormats::Markdown, CrawlScrapeFormats::HTML ].into(),
        ..Default::default()
    }.into(),
    limit: 100.into(),
    ..Default::default()
};

let crawl_result = app
    .crawl_url("https://mendable.ai", crawl_options)
    .await;

match crawl_result {
    Ok(data) => println!("Crawl Result (used {} credits):\n{:#?}", data.credits_used, data.data),
    Err(e) => eprintln!("Crawl failed: {}", e),
}
rust Rust theme={null}
let crawl_id = app.crawl_url_async("https://mendable.ai", None).await?.id;

let status = app.check_crawl_status(crawl_id).await?;

if status.status == CrawlStatusTypes::Completed {
    println!("Crawl is done: {:#?}", status.data);
} else {
    // ... wait some more ...
}
rust Rust theme={null}
let map_result = app.map_url("https://firecrawl.dev", None).await;

match map_result {
    Ok(data) => println!("Mapped URLs: {:#?}", data),
    Err(e) => eprintln!("Map failed: {}", e),
}
```

The SDK handles errors returned by the Firecrawl API and by our dependencies, and combines them into the `FirecrawlError` enum, implementing `Error`, `Debug` and `Display`. All of our methods return a `Result<T, FirecrawlError>`.

**Examples:**

Example 1 (unknown):
```unknown
## Usage

First, you need to obtain an API key from [firecrawl.dev](https://firecrawl.dev). Then, you need to initialize the `FirecrawlApp`. From there, you can access functions like `FirecrawlApp::scrape_url`, which let you use our API.

Here's an example of how to use the SDK in Rust:
```

Example 2 (unknown):
```unknown
### Scraping a URL

To scrape a single URL, use the `scrape_url` method. It takes the URL as a parameter and returns the scraped data as a `Document`.
```

Example 3 (unknown):
```unknown
### Scraping with Extract

With Extract, you can easily extract structured data from any URL. You need to specify your schema in the JSON Schema format, using the `serde_json::json!` macro.
```

Example 4 (unknown):
```unknown
### Crawling a Website

To crawl a website, use the `crawl_url` method. This will wait for the crawl to complete, which may take a long time based on your starting URL and your options.
```

---

## Experimental: Use Ollama

**URL:** llms-txt#experimental:-use-ollama

---

## Firecrawl + n8n

**URL:** llms-txt#firecrawl-+-n8n

**Contents:**
- Introduction to Firecrawl and n8n
- Why Use Firecrawl with n8n?
- Step 1: Create Your Firecrawl Account
  - Sign Up for Firecrawl
  - Get Your API Key
- Step 2: Set Up n8n
  - Choose Your n8n Version
  - Option A: n8n Cloud (Recommended for Beginners)
  - Option B: Self-Hosted with Docker
  - Understanding the n8n Interface

Source: https://docs.firecrawl.dev/developer-guides/workflow-automation/n8n

Learn how to use Firecrawl with n8n for web scraping automation, a complete step-by-step guide.

## Introduction to Firecrawl and n8n

Web scraping automation has become essential for modern businesses. Whether you need to monitor competitor prices, aggregate content, generate leads, or power AI applications with real-time data, the combination of Firecrawl and n8n provides a powerful solution without requiring programming knowledge.

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=cb863000a893ef260cfe023e2455c88c" alt="Firecrawl and n8n integration" data-og-width="1536" width="1536" data-og-height="1024" height="1024" data-path="images/guides/n8n/firecrawl-n8n-integration-hero.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=f1f3cc979a390121e6683ac8ce626bb2 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=f3e7b4bf8a4d6582389a9fff0c36cda2 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=d556ffd5a96e792ee7a8432b4262bd74 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=a4ea6455383005074991026683bedef6 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=15402611e1a949138b65844df4be6b5f 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=226545dc94de7d3639b08f78c56c7d39 2500w" />

n8n is an open-source workflow automation platform that connects different tools and services together. Think of it as a visual programming environment where you drag and drop nodes onto a canvas, connect them, and create automated workflows. With over 400 integrations, n8n lets you build complex automations without writing code.

## Why Use Firecrawl with n8n?

Traditional web scraping presents several challenges. Custom scripts break when websites update their structure. Anti-bot systems block automated requests. JavaScript-heavy sites don't render properly. Infrastructure requires constant maintenance.

Firecrawl handles these technical complexities on the scraping side, while n8n provides the automation framework. Together, they let you build production-ready workflows that:

* Extract data from any website reliably
* Connect scraped data to other business tools
* Run on schedules or triggered by events
* Scale from simple tasks to complex pipelines

This guide will walk you through setting up both platforms and building your first scraping workflow from scratch.

## Step 1: Create Your Firecrawl Account

Firecrawl provides the web scraping capabilities for your workflows. Let's set up your account and get your API credentials.

### Sign Up for Firecrawl

1. Navigate to [firecrawl.dev](https://firecrawl.dev) in your web browser
2. Click the "Get Started" or "Sign Up" button
3. Create an account using your email address or GitHub login
4. Verify your email if prompted

After signing in, you need an API key to connect Firecrawl to n8n:

1. Go to your Firecrawl dashboard
2. Navigate to the [API Keys page](https://www.firecrawl.dev/app/api-keys)
3. Click "Create New API Key"
4. Give your key a descriptive name (e.g., "n8n Integration")
5. Copy the generated API key and save it somewhere secure

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-api-key-creation-dashboard.gif?s=2c04559b9027dfe825e3ba7d78af8527" alt="Firecrawl api key section" data-og-width="2092" width="2092" data-og-height="1080" height="1080" data-path="images/guides/n8n/firecrawl-api-key-creation-dashboard.gif" data-optimize="true" data-opv="3" />

<Note>
  Your API key is like a password. Keep it secure and never share it publicly. You'll need this key in the next section.
</Note>

Firecrawl provides free credits when you sign up, which is enough to test your workflows and complete this tutorial.

## Step 2: Set Up n8n

n8n offers two deployment options: cloud-hosted or self-hosted. For beginners, the cloud version is the fastest way to get started.

### Choose Your n8n Version

**n8n Cloud (Recommended for beginners):**

* No installation required
* Free tier available
* Managed infrastructure
* Automatic updates

* Complete data control
* Run on your own servers
* Requires Docker installation
* Good for advanced users with specific security requirements

Choose the option that fits your needs. Both paths will lead you to the same workflow editor interface.

### Option A: n8n Cloud (Recommended for Beginners)

1. Visit [n8n.cloud](https://n8n.cloud)
2. Click "Start Free" or "Sign Up"
3. Register using your email address or GitHub
4. Complete the verification process
5. You'll be directed to your n8n dashboard

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-cloud-signup-homepage.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7965f6fab8bd1d48b81db7c1dbed1e7f" alt="n8n Cloud homepage showing the signup options" data-og-width="938" width="938" data-og-height="534" height="534" data-path="images/guides/n8n/n8n-cloud-signup-homepage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-cloud-signup-homepage.png?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=3bbf22abf05c06de2404aacde9ceec14 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-cloud-signup-homepage.png?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=af8bebf5caf183382c2a82345cd45eb4 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-cloud-signup-homepage.png?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=e772095bc8395ea810ee93f567eaa177 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-cloud-signup-homepage.png?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=8088665e7a2402c1785536c73a3e4f92 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-cloud-signup-homepage.png?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=4234235fddb6fab5c91a9dd006a88a03 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-cloud-signup-homepage.png?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=aac25bf271e296ce946306741991c7f6 2500w" />

The free tier provides everything you need to build and test workflows. You can upgrade later if you need more execution time or advanced features.

### Option B: Self-Hosted with Docker

If you prefer to run n8n on your own infrastructure, you can set it up quickly using Docker.

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed on your computer
* Basic familiarity with command line/terminal

**Installation Steps:**

1. Open your terminal or command prompt
2. Create a Docker volume to persist your workflow data:

This volume stores your workflows, credentials, and execution history so they persist even if you restart the container.

3. Run the n8n Docker container:

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-docker-self-hosted-installation.gif?s=4968ecd0996ef3e76dc0abb886ae52ca" alt="Terminal showing the docker commands being executed with n8n starting up" data-og-width="1772" width="1772" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-docker-self-hosted-installation.gif" data-optimize="true" data-opv="3" />

4. Wait for n8n to start. You'll see output indicating the server is running
5. Open your web browser and navigate to `http://localhost:5678`
6. Create your n8n account by registering with an email

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=163949933d76425a68ec728639e767ea" alt="n8n self-hosted welcome screen at localhost:5678" data-og-width="1440" width="1440" data-og-height="1750" height="1750" data-path="images/guides/n8n/n8n-localhost-registration-form.gif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7117cdada65114430e0b2f3add817eb1 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=d5806bf16ad25fd0b6b20b932913b30d 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=bfaa828d9afa93df29b9d98dbe0febf5 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=0edfb7af89b630673ccee4caf414d151 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=e0f7afe2b5542837297f2fe132827f13 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=142ca42d7b819656bc8542b7ba141147 2500w" />

Your self-hosted n8n instance is now running locally. The interface is identical to n8n Cloud, so you can follow the rest of this guide regardless of which option you chose.

<Note>
  The `--rm` flag automatically removes the container when you stop it, but your data remains safe in the `n8n_data` volume. For production deployments, see the [n8n self-hosting documentation](https://docs.n8n.io/hosting/) for more advanced configuration options.
</Note>

### Understanding the n8n Interface

When you first log in to n8n, you'll see the main dashboard:

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=5d92092b94fd021c2cebf163c2ef4d01" alt="n8n dashboard showing the workflow list view with &#x22;Create new workflow&#x22; button" data-og-width="2488" width="2488" data-og-height="1582" height="1582" data-path="images/guides/n8n/n8n-dashboard-workflow-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=6b20e5dc04349c818a5cc167f5cc3ad5 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=197ca1ee4f6a43f7c5f9a1a72f3b10b8 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=8a9c1460cfa1bd0b8310923105fef65b 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=b11f57d89f97eb448a28f512a51d4151 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=5de359044829290c0857f4af7e507353 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=47441401d3a1950b07fb30367e0498de 2500w" />

Key interface elements:

* **Workflows**: Your saved automations appear here
* **Executions**: History of workflow runs
* **Credentials**: Stored API keys and authentication tokens
* **Settings**: Account and workspace configuration

Click "Create New Workflow" to open the workflow editor.

### The Workflow Canvas

The workflow editor is where you'll build your automations:

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7508078e88b57ccedc2a4d4a258fddf8" alt="Empty n8n workflow canvas with the &#x22;+&#x22; button visible in the center" data-og-width="2488" width="2488" data-og-height="1582" height="1582" data-path="images/guides/n8n/n8n-empty-workflow-canvas.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=e4f36a6dcf02ed2611204134db432a03 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=61688470374caaa12773c49b67ca9a80 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7db9b175cbc3d53ac55df860b666a262 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=20da1ab0dd67864fc8b13ba98589cff4 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=f5a78910ae2ce2ce3c71f2c7d1676b2a 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=cea1151777344d528779e3c8bf1c0195 2500w" />

* **Canvas**: The main area where you place and connect nodes
* **Add Node Button (+)**: Click this to add new nodes to your workflow
* **Node Panel**: Opens when you click "+" showing all available nodes
* **Execute Workflow**: Runs your workflow manually for testing
* **Save**: Saves your workflow configuration

Let's build your first workflow by adding the Firecrawl node.

## Step 3: Install and Configure the Firecrawl Node

n8n includes native support for Firecrawl. You'll install the node and connect it to your Firecrawl account using the API key you created earlier.

### Add the Firecrawl Node to Your Workflow

1. In your new workflow canvas, click the "**+**" button in the center
2. The node selection panel opens on the right side
3. In the search box at the top, type "**Firecrawl**"
4. You'll see the Firecrawl node appear in the search results

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-search-install-firecrawl-node.gif?s=6d81f8bf967429cfaf2bcf22c3976fbf" alt="Clicking the + button, typing &#x22;Firecrawl&#x22; in the search, and the Firecrawl node appearing" data-og-width="1692" width="1692" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-search-install-firecrawl-node.gif" data-optimize="true" data-opv="3" />

5. Click "**Install**" next to the Firecrawl node
6. Wait for the installation to complete (this takes a few seconds)
7. Once installed, click on the Firecrawl node to add it to your canvas

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-node-added-canvas.gif?s=d7480ebf8ef357fba9a0c5ee5123ffc8" alt="Firecrawl node now added to the canvas, showing as a box with the Firecrawl logo" data-og-width="1692" width="1692" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-firecrawl-node-added-canvas.gif" data-optimize="true" data-opv="3" />

The Firecrawl node will appear on your canvas as a box with the Firecrawl logo. This node represents a single Firecrawl operation in your workflow.

### Connect Your Firecrawl API Key

Before you can use the Firecrawl node, you need to authenticate it with your API key:

1. Click on the Firecrawl node box to open its configuration panel on the right
2. At the top, you'll see a "Credential to connect with" dropdown
3. Since this is your first time, click "**Create New Credential**"

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-api-credentials-setup.gif?s=547bda13daeb17dd963160a8ef4bbf48" alt="Firecrawl node configuration panel showing the credentials dropdown with &#x22;Create New Credential&#x22; option" data-og-width="1692" width="1692" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-firecrawl-api-credentials-setup.gif" data-optimize="true" data-opv="3" />

4. A credential configuration window opens
5. Enter a name for this credential (e.g., "My Firecrawl Account")
6. Paste your Firecrawl API key in the "API Key" field
7. Click "**Save**" at the bottom

The credential is now saved in n8n. You won't need to enter your API key again for future Firecrawl nodes.

### Test Your Connection

Let's verify that your Firecrawl node is properly connected:

1. With the Firecrawl node still selected, look at the configuration panel
2. In the "Resource" dropdown, select "**Scrape a url and get its content**"
3. In the "URL" field, enter: `https://firecrawl.dev`
4. Leave other settings at their defaults for now
5. Click the "**Test step**" button at the bottom right of the node

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-test-connection-scrape.gif?s=a5a832a971778744a6ceaf9d2ff0cdb1" alt="Selecting Scrape operation, entering example.com URL, and clicking Test step button" data-og-width="1260" width="1260" data-og-height="720" height="720" data-path="images/guides/n8n/n8n-firecrawl-test-connection-scrape.gif" data-optimize="true" data-opv="3" />

If everything is configured correctly, you'll see the scraped content from example.com appear in the output panel below the node.

Congratulations! Your Firecrawl node is now connected and working.

## Step 4: Create Your Telegram Bot

Before building your first workflow, you'll need a Telegram bot to receive notifications. Telegram bots are free and easy to create through Telegram's BotFather.

### Create a Bot with BotFather

1. Open Telegram on your phone or desktop
2. Search for "**@BotFather**" (the official bot from Telegram)
3. Start a conversation with BotFather by clicking "**Start**"
4. Send the command `/newbot` to create a new bot
5. BotFather will ask you to choose a name for your bot (this is the display name users will see)
6. Enter a name like "**My Firecrawl Bot**"
7. Next, choose a username for your bot. It must end with "bot" (e.g., "**my\_firecrawl\_updates\_bot**")
8. If the username is available, BotFather will create your bot and send you a message with your bot token

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=45ee39deae96fbc3eac5fdb2eeba2e0b" alt="Creating a bot with BotFather, showing the full conversation flow" data-og-width="1342" width="1342" data-og-height="1072" height="1072" data-path="images/guides/n8n/telegram-botfather-create-new-bot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=f0f0de8094553c112b63bdb9d8c8c295 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=b5388eda118f7b2bae054062a727eb58 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7bdb6a2e742e5988345cc43ed40e23c1 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=905a71c424bde6ddf252dea7a1350153 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=2465e5b372a42e11503748abdb6545cd 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=5ddd16e0f1c4787e37de492e1970fa4c 2500w" />

<Note>
  Save your bot token securely. This token is like a password that allows n8n to send messages as your bot. Never share it publicly.
</Note>

To send messages to yourself, you need your Telegram chat ID:

1. Open your web browser and visit this URL (replace `YOUR_BOT_TOKEN` with your actual bot token):
   
2. Keep this browser tab open
3. Now, search for your bot's username in Telegram (the one you just created)
4. Start a conversation with your bot by clicking "**Start**"
5. Send any message to your bot (e.g., "hello")
6. Go back to the browser tab and refresh the page
7. Look for the `"chat":{"id":` field in the JSON response
8. The number next to `"id":` is your chat ID (e.g., `123456789`)
9. Save this chat ID for later

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-api-get-chat-id-browser.gif?s=e074ecf1a659bdfa7284e86c923be06f" alt="Browser showing Telegram API getUpdates response with chat ID highlighted" data-og-width="1820" width="1820" data-og-height="1080" height="1080" data-path="images/guides/n8n/telegram-api-get-chat-id-browser.gif" data-optimize="true" data-opv="3" />

<Note>
  Your chat ID is the unique identifier for your conversation with the bot. You'll use this to tell n8n where to send messages.
</Note>

You now have everything needed to integrate Telegram with your n8n workflows.

## Step 5: Build Practical Workflows with Telegram

Now let's build three real-world workflows that send information directly to your Telegram. These examples demonstrate different Firecrawl operations and how to integrate them with Telegram notifications.

### Example 1: Daily Firecrawl Product Updates Summary

Get a daily summary of Firecrawl product updates delivered to your Telegram every morning.

**What you'll build:**

* Scrapes Firecrawl's product updates blog at 9 AM daily
* Uses AI to generate a summary of the content
* Sends the summary to your Telegram

1. Create a new workflow in n8n
2. Add a **Schedule Trigger** node:
   * Click the "**+**" button on canvas
   * Search for "**Schedule Trigger**"
   * Configure: Every day at 9:00 AM

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-schedule-trigger-daily-cron.gif?s=ae68cd74cdf14a1d012861df8319b245" alt="Schedule Trigger configured for daily 9 AM execution" data-og-width="2116" width="2116" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-schedule-trigger-daily-cron.gif" data-optimize="true" data-opv="3" />

3. Add the **Firecrawl** node:
   * Click "**+**" next to Schedule Trigger
   * Search for and add "**Firecrawl**"
   * Select your Firecrawl credential
   * Configure:
     * **Resource**: Scrape a url and get its content
     * **URL**: `https://www.firecrawl.dev/blog/category/product-updates`
     * **Formats**: Select "Summary"

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-scrape-blog-summary.gif?s=ad1684f165aacd7ab5d1530cdac73962" alt="Adding and configuring Firecrawl node with the blog URL and Summary format selected" data-og-width="2116" width="2116" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-firecrawl-scrape-blog-summary.gif" data-optimize="true" data-opv="3" />

4. Add the **Telegram** node:
   * Click "**+**" next to Firecrawl
   * Search for "**Telegram**"
   * Click "**Send a text message**" to add it to the canvas

5. Set up Telegram credentials:
   * Click on the Telegram node to open its configuration
   * In the "Credential to connect with" dropdown, click "**Create New Credential**"
   * Paste your bot token from BotFather
   * Click "**Save**"

<img src="https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-telegram-bot-token-credentials.gif" alt="Telegram credential configuration with bot token field" />

6. Configure the Telegram message:
   * **Operation**: Send Message

* **Chat ID**: Enter your chat ID

* **Text**: Leave this with a "hello" message for now

* Click **Execute step** to test sending a message while receiving the summary from Firecrawl.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-test-telegram-message-firecrawl.gif" alt="Configuring Telegram node and mapping the summary field to the message text" />

* Now with Firecrawl's summary structure, add the summary to the message text by dragging the `summary` field from Firecrawl node output.

7. Test the workflow:
   * Click "**Execute Workflow**"
   * Check your Telegram for the summary message

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=1c3eacbcb705c21c6265ae3ecbd59d59" alt="Complete workflow showing Schedule Trigger → Firecrawl → Telegram with all nodes connected" data-og-width="1538" width="1538" data-og-height="1046" height="1046" data-path="images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=d59acd307786d60f459c1d1f7fc9ed24 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=28da669238c05f0f840f51c9d9f4b35a 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7bb0f7e8bfbdd970bc5b5777501323b0 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=d2d407548ec49b2700e91eeb7dcca029 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=840a62d2cd26b7658b839ad1d0ab23a0 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=f9132a7d8e480ec8d64de845ddad6219 2500w" />

8. Activate the workflow by toggling the "**Active**" switch

Your Telegram bot will now send you a daily summary of Firecrawl product updates every morning at 9 AM.

### Example 2: AI News Search to Telegram

This workflow uses Firecrawl's Search operation to find AI news and send formatted results to Telegram.

**Key differences from Example 1:**

* Uses a **Manual Trigger** instead of Schedule (run on demand)
* Uses **Search** operation instead of Scrape
* Includes a **Code** node to format multiple results

**Build the workflow:**

1. Create a new workflow and add a **Manual Trigger** node

2. Add **Firecrawl** node with these settings:
   * **Resource**: Search and optionally scrape search results
   * **Query**: `ai news`
   * **Limit**: 5

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-search-ai-news-results.gif?s=23eb224783b0b3155d179a0342839621" alt="Firecrawl Search node configuration with &#x22;ai news&#x22; query" data-og-width="1776" width="1776" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-firecrawl-search-ai-news-results.gif" data-optimize="true" data-opv="3" />

3. Add a **Code** node to format the search results:
   * Select "Run Once for All Items"
   * Paste this code:

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-code-node-format-news-articles.gif?s=cafb96e0b7f2ef27a09ae2957390799b" alt="Adding Code node and pasting the formatting script" data-og-width="1768" width="1768" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-code-node-format-news-articles.gif" data-optimize="true" data-opv="3" />

4. Update **Telegram** node (using your saved credential):
   * **Text**: Drag the `message` field from Code node

<img src="https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-execute-workflow-telegram-delivery.gif" alt="Complete workflow execution with AI news sent to Telegram" />

<Tip>
  Replace the Manual Trigger with a Schedule Trigger to get automatic AI news updates at set intervals.
</Tip>

### Example 3: AI-Powered News Summary

This workflow adds AI to Example 2, using OpenAI to generate intelligent summaries of the latest AI news before sending to Telegram.

**Key changes from Example 2:**

* Add **OpenAI credentials** setup
* Add **AI Agent** node between Code and Telegram
* AI Agent analyzes and summarizes all the news articles intelligently
* Telegram receives the AI-generated summary instead of raw news list

**Modify the workflow:**

1. **Get your OpenAI API key**:
   * Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   * Sign in or create an account
   * Click "**Create new secret key**"
   * Give it a name (e.g., "n8n Integration")
   * Copy the API key immediately (you won't see it again)

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/openai-api-key-creation-dashboard.gif?s=8222a339a403f85272102256fa91fc27" alt="OpenAI dashboard showing API key creation" data-og-width="1780" width="1780" data-og-height="1080" height="1080" data-path="images/guides/n8n/openai-api-key-creation-dashboard.gif" data-optimize="true" data-opv="3" />

2. **Add and connect the AI Agent node**:
   * Click "**+**" after the Code node
   * Search for "**Basic LLM Chain**" or "**AI Agent**"
   * Drag the `message` field from the Code node to the AI Agent's input prompt field
   * Select **OpenAI** as the LLM provider

<img src="https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-ai-agent-openai-llm-setup.gif" alt="Adding AI Agent node, dragging input from Code node, and connecting OpenAI as LLM" />

3. **Add your OpenAI credentials**:
   * Click "**Create New Credential**" for OpenAI
   * Paste your OpenAI API key
   * Select model: **gpt-5-mini** (cost-effective) or **gpt-5** (more capable)
   * Click "**Save**"

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-openai-credentials-gpt-model.gif?s=c97249f572e8d530583918ebc3357d53" alt="Adding OpenAI credentials to the AI Agent node" data-og-width="1596" width="1596" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-openai-credentials-gpt-model.gif" data-optimize="true" data-opv="3" />

4. **Add the system prompt to the AI Agent**:
   * In the AI Agent node, add this system prompt:

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-ai-agent-system-prompt-configuration.gif?s=45c34c7010aa6319f8d4dde84c6e5ab9" alt="Adding the system prompt to the AI Agent node" data-og-width="1764" width="1764" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-ai-agent-system-prompt-configuration.gif" data-optimize="true" data-opv="3" />

5. **Update the Telegram node and test**:
   * Update the Telegram node:
     * **Text**: Drag the AI Agent's output (the generated summary)
     * Remove the old mapping to the Code node's message
   * Click "**Execute Workflow**" to test
   * The AI will analyze all news articles and create a summary
   * Check your Telegram for the AI-generated summary

<img src="https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-ai-summary-telegram-workflow-execution.gif" alt="Complete workflow execution with AI-generated summary sent to Telegram" />

<Note>
  The AI Agent receives all the formatted news articles and creates an intelligent summary, making it easier to understand trends and important developments at a glance.
</Note>

## Understanding Firecrawl Operations

Now that you've built some workflows, let's explore the different Firecrawl operations available in n8n. Each operation is designed for specific web scraping use cases.

### Scrape a url and get its content

Extracts content from a single web page and returns it in various formats.

* Scrapes a single URL
* Returns clean markdown, HTML, or AI-generated summaries
* Can capture screenshots and extract links

* Article extraction
* Product page monitoring
* Blog post scraping
* Generating page summaries

**Example use case:** Daily blog summaries (like Example 1 above)

### Search and optionally scrape search results

Performs web searches and returns results with optional content scraping.

* Searches the web, news, or images
* Returns titles, descriptions, and URLs
* Optionally scrapes the full content of results

* Research automation
* News monitoring
* Trend discovery
* Finding relevant content

**Example use case:** AI news aggregation (like Example 2 above)

Recursively discovers and scrapes multiple pages from a website.

* Follows links automatically
* Scrapes multiple pages in one operation
* Can filter URLs by patterns

* Full documentation extraction
* Site archiving
* Multi-page data collection

### Map a website and get urls

Returns all URLs found on a website without scraping content.

* Discovers all links on a site
* Returns clean URL list
* Fast and lightweight

* URL discovery
* Sitemap generation
* Planning larger crawls

Uses AI to extract structured information based on custom prompts or schemas.

* AI-powered data extraction
* Returns data in your specified format
* Works across multiple pages

* Custom data extraction
* Building databases
* Structured information gathering

Scrapes multiple URLs in parallel efficiently.

* Processes multiple URLs at once
* More efficient than loops
* Returns all results together

* Processing URL lists
* Bulk data collection
* Large-scale scraping projects

## Workflow Templates and Examples

Instead of building from scratch, you can start with pre-built templates. The n8n community has created numerous Firecrawl workflows you can copy and customize.

### Featured Templates

<CardGroup cols={2}>
  <Card title="Complete n8n Tutorial" icon="rocket" href="https://www.firecrawl.dev/blog/firecrawl-n8n-web-automation">
    Build an AI chatbot with web access using Firecrawl and n8n
  </Card>

<Card title="8 Production Workflows" icon="layer-group" href="https://www.firecrawl.dev/blog/n8n-web-scraping-workflow-templates">
    Ready-to-use templates for lead generation, price monitoring, and more
  </Card>

<Card title="n8n Community Workflows" icon="book" href="https://n8n.io/workflows?search=firecrawl">
    Browse hundreds of workflows using Firecrawl
  </Card>

<Card title="Official n8n Integration" icon="plug" href="https://n8n.io/integrations/firecrawl/">
    View official integration documentation
  </Card>
</CardGroup>

### How to Import Templates

To use a template from the n8n community:

1. Click on a workflow template link
2. Click "**Import template to localhost:5678 self-hosted instance**" button on the template page
3. The workflow opens in your n8n instance
4. Configure credentials for each node
5. Customize settings for your use case
6. Activate the workflow

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-import.gif?s=5bd77d25fa2dc525e0032a483803fd00" alt="Importing a template from n8n.io, showing the import button and workflow appearing in n8n" data-og-width="2088" width="2088" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-workflow-import.gif" data-optimize="true" data-opv="3" />

Follow these guidelines to build reliable, efficient workflows:

### Testing and Debugging

* Always test workflows manually before activating schedules
* Use the "**Execute Workflow**" button to test the entire flow
* Check output data at each node to verify correctness
* Use the "**Executions**" tab to review past runs and debug issues

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-debugging.gif?s=2962335b6f72ea39cf6cb68cb6ed83c3" alt="Executions tab showing workflow run history with timestamps and status" data-og-width="2080" width="2080" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-debugging.gif" data-optimize="true" data-opv="3" />

* Add Error Trigger nodes to catch and handle failures
* Set up notifications when workflows fail
* Use the "**Continue On Fail**" setting for non-critical nodes
* Monitor your workflow executions regularly

### Performance Optimization

* Use Batch Scrape for multiple URLs instead of loops
* Set appropriate rate limits to avoid overwhelming target sites
* Cache data when possible to reduce unnecessary requests
* Schedule intensive workflows during off-peak hours

* Never expose API keys in workflow configurations
* Use n8n's credential system to securely store authentication
* Be careful when sharing workflows publicly
* Follow target websites' terms of service and robots.txt

You now have the fundamentals to build web scraping automations with Firecrawl and n8n. Here's how to continue learning:

### Explore Advanced Features

* Study webhook configurations for real-time data processing
* Experiment with AI-powered extraction using prompts and schemas
* Build complex multi-step workflows with branching logic

### Join the Community

* [Firecrawl Discord](https://discord.gg/gSmWdAkdwd) - Get help with Firecrawl and discuss web scraping
* [n8n Community Forum](https://community.n8n.io/) - Ask questions about workflow automation
* Share your workflows and learn from others

### Recommended Learning Path

1. Complete the example workflows in this guide
2. Modify templates from the community library
3. Build a workflow to solve a real problem in your work
4. Explore advanced Firecrawl operations
5. Contribute your own templates to help others

<Note>
  **Need help?** If you're stuck or have questions, the Firecrawl and n8n communities are active and helpful. Don't hesitate to ask for guidance as you build your automations.
</Note>

## Additional Resources

* [Firecrawl API Documentation](/api-reference/v2-introduction)
* [n8n Documentation](https://docs.n8n.io/)
* [Web Scraping Best Practices](https://www.firecrawl.dev/blog)

**Examples:**

Example 1 (unknown):
```unknown
This volume stores your workflows, credentials, and execution history so they persist even if you restart the container.

3. Run the n8n Docker container:
```

Example 2 (unknown):
```unknown
<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-docker-self-hosted-installation.gif?s=4968ecd0996ef3e76dc0abb886ae52ca" alt="Terminal showing the docker commands being executed with n8n starting up" data-og-width="1772" width="1772" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-docker-self-hosted-installation.gif" data-optimize="true" data-opv="3" />

4. Wait for n8n to start. You'll see output indicating the server is running
5. Open your web browser and navigate to `http://localhost:5678`
6. Create your n8n account by registering with an email

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=163949933d76425a68ec728639e767ea" alt="n8n self-hosted welcome screen at localhost:5678" data-og-width="1440" width="1440" data-og-height="1750" height="1750" data-path="images/guides/n8n/n8n-localhost-registration-form.gif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7117cdada65114430e0b2f3add817eb1 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=d5806bf16ad25fd0b6b20b932913b30d 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=bfaa828d9afa93df29b9d98dbe0febf5 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=0edfb7af89b630673ccee4caf414d151 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=e0f7afe2b5542837297f2fe132827f13 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=142ca42d7b819656bc8542b7ba141147 2500w" />

Your self-hosted n8n instance is now running locally. The interface is identical to n8n Cloud, so you can follow the rest of this guide regardless of which option you chose.

<Note>
  The `--rm` flag automatically removes the container when you stop it, but your data remains safe in the `n8n_data` volume. For production deployments, see the [n8n self-hosting documentation](https://docs.n8n.io/hosting/) for more advanced configuration options.
</Note>

### Understanding the n8n Interface

When you first log in to n8n, you'll see the main dashboard:

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=5d92092b94fd021c2cebf163c2ef4d01" alt="n8n dashboard showing the workflow list view with &#x22;Create new workflow&#x22; button" data-og-width="2488" width="2488" data-og-height="1582" height="1582" data-path="images/guides/n8n/n8n-dashboard-workflow-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=6b20e5dc04349c818a5cc167f5cc3ad5 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=197ca1ee4f6a43f7c5f9a1a72f3b10b8 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=8a9c1460cfa1bd0b8310923105fef65b 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=b11f57d89f97eb448a28f512a51d4151 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=5de359044829290c0857f4af7e507353 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=47441401d3a1950b07fb30367e0498de 2500w" />

Key interface elements:

* **Workflows**: Your saved automations appear here
* **Executions**: History of workflow runs
* **Credentials**: Stored API keys and authentication tokens
* **Settings**: Account and workspace configuration

Click "Create New Workflow" to open the workflow editor.

### The Workflow Canvas

The workflow editor is where you'll build your automations:

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7508078e88b57ccedc2a4d4a258fddf8" alt="Empty n8n workflow canvas with the &#x22;+&#x22; button visible in the center" data-og-width="2488" width="2488" data-og-height="1582" height="1582" data-path="images/guides/n8n/n8n-empty-workflow-canvas.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=e4f36a6dcf02ed2611204134db432a03 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=61688470374caaa12773c49b67ca9a80 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7db9b175cbc3d53ac55df860b666a262 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=20da1ab0dd67864fc8b13ba98589cff4 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=f5a78910ae2ce2ce3c71f2c7d1676b2a 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=cea1151777344d528779e3c8bf1c0195 2500w" />

Important elements:

* **Canvas**: The main area where you place and connect nodes
* **Add Node Button (+)**: Click this to add new nodes to your workflow
* **Node Panel**: Opens when you click "+" showing all available nodes
* **Execute Workflow**: Runs your workflow manually for testing
* **Save**: Saves your workflow configuration

Let's build your first workflow by adding the Firecrawl node.

## Step 3: Install and Configure the Firecrawl Node

n8n includes native support for Firecrawl. You'll install the node and connect it to your Firecrawl account using the API key you created earlier.

### Add the Firecrawl Node to Your Workflow

1. In your new workflow canvas, click the "**+**" button in the center
2. The node selection panel opens on the right side
3. In the search box at the top, type "**Firecrawl**"
4. You'll see the Firecrawl node appear in the search results

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-search-install-firecrawl-node.gif?s=6d81f8bf967429cfaf2bcf22c3976fbf" alt="Clicking the + button, typing &#x22;Firecrawl&#x22; in the search, and the Firecrawl node appearing" data-og-width="1692" width="1692" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-search-install-firecrawl-node.gif" data-optimize="true" data-opv="3" />

5. Click "**Install**" next to the Firecrawl node
6. Wait for the installation to complete (this takes a few seconds)
7. Once installed, click on the Firecrawl node to add it to your canvas

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-node-added-canvas.gif?s=d7480ebf8ef357fba9a0c5ee5123ffc8" alt="Firecrawl node now added to the canvas, showing as a box with the Firecrawl logo" data-og-width="1692" width="1692" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-firecrawl-node-added-canvas.gif" data-optimize="true" data-opv="3" />

The Firecrawl node will appear on your canvas as a box with the Firecrawl logo. This node represents a single Firecrawl operation in your workflow.

### Connect Your Firecrawl API Key

Before you can use the Firecrawl node, you need to authenticate it with your API key:

1. Click on the Firecrawl node box to open its configuration panel on the right
2. At the top, you'll see a "Credential to connect with" dropdown
3. Since this is your first time, click "**Create New Credential**"

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-api-credentials-setup.gif?s=547bda13daeb17dd963160a8ef4bbf48" alt="Firecrawl node configuration panel showing the credentials dropdown with &#x22;Create New Credential&#x22; option" data-og-width="1692" width="1692" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-firecrawl-api-credentials-setup.gif" data-optimize="true" data-opv="3" />

4. A credential configuration window opens
5. Enter a name for this credential (e.g., "My Firecrawl Account")
6. Paste your Firecrawl API key in the "API Key" field
7. Click "**Save**" at the bottom

The credential is now saved in n8n. You won't need to enter your API key again for future Firecrawl nodes.

### Test Your Connection

Let's verify that your Firecrawl node is properly connected:

1. With the Firecrawl node still selected, look at the configuration panel
2. In the "Resource" dropdown, select "**Scrape a url and get its content**"
3. In the "URL" field, enter: `https://firecrawl.dev`
4. Leave other settings at their defaults for now
5. Click the "**Test step**" button at the bottom right of the node

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-test-connection-scrape.gif?s=a5a832a971778744a6ceaf9d2ff0cdb1" alt="Selecting Scrape operation, entering example.com URL, and clicking Test step button" data-og-width="1260" width="1260" data-og-height="720" height="720" data-path="images/guides/n8n/n8n-firecrawl-test-connection-scrape.gif" data-optimize="true" data-opv="3" />

If everything is configured correctly, you'll see the scraped content from example.com appear in the output panel below the node.

Congratulations! Your Firecrawl node is now connected and working.

## Step 4: Create Your Telegram Bot

Before building your first workflow, you'll need a Telegram bot to receive notifications. Telegram bots are free and easy to create through Telegram's BotFather.

### Create a Bot with BotFather

1. Open Telegram on your phone or desktop
2. Search for "**@BotFather**" (the official bot from Telegram)
3. Start a conversation with BotFather by clicking "**Start**"
4. Send the command `/newbot` to create a new bot
5. BotFather will ask you to choose a name for your bot (this is the display name users will see)
6. Enter a name like "**My Firecrawl Bot**"
7. Next, choose a username for your bot. It must end with "bot" (e.g., "**my\_firecrawl\_updates\_bot**")
8. If the username is available, BotFather will create your bot and send you a message with your bot token

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=45ee39deae96fbc3eac5fdb2eeba2e0b" alt="Creating a bot with BotFather, showing the full conversation flow" data-og-width="1342" width="1342" data-og-height="1072" height="1072" data-path="images/guides/n8n/telegram-botfather-create-new-bot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=f0f0de8094553c112b63bdb9d8c8c295 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=b5388eda118f7b2bae054062a727eb58 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7bdb6a2e742e5988345cc43ed40e23c1 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=905a71c424bde6ddf252dea7a1350153 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=2465e5b372a42e11503748abdb6545cd 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=5ddd16e0f1c4787e37de492e1970fa4c 2500w" />

<Note>
  Save your bot token securely. This token is like a password that allows n8n to send messages as your bot. Never share it publicly.
</Note>

### Get Your Chat ID

To send messages to yourself, you need your Telegram chat ID:

1. Open your web browser and visit this URL (replace `YOUR_BOT_TOKEN` with your actual bot token):
```

Example 3 (unknown):
```unknown
2. Keep this browser tab open
3. Now, search for your bot's username in Telegram (the one you just created)
4. Start a conversation with your bot by clicking "**Start**"
5. Send any message to your bot (e.g., "hello")
6. Go back to the browser tab and refresh the page
7. Look for the `"chat":{"id":` field in the JSON response
8. The number next to `"id":` is your chat ID (e.g., `123456789`)
9. Save this chat ID for later

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-api-get-chat-id-browser.gif?s=e074ecf1a659bdfa7284e86c923be06f" alt="Browser showing Telegram API getUpdates response with chat ID highlighted" data-og-width="1820" width="1820" data-og-height="1080" height="1080" data-path="images/guides/n8n/telegram-api-get-chat-id-browser.gif" data-optimize="true" data-opv="3" />

<Note>
  Your chat ID is the unique identifier for your conversation with the bot. You'll use this to tell n8n where to send messages.
</Note>

You now have everything needed to integrate Telegram with your n8n workflows.

## Step 5: Build Practical Workflows with Telegram

Now let's build three real-world workflows that send information directly to your Telegram. These examples demonstrate different Firecrawl operations and how to integrate them with Telegram notifications.

### Example 1: Daily Firecrawl Product Updates Summary

Get a daily summary of Firecrawl product updates delivered to your Telegram every morning.

**What you'll build:**

* Scrapes Firecrawl's product updates blog at 9 AM daily
* Uses AI to generate a summary of the content
* Sends the summary to your Telegram

**Step-by-step:**

1. Create a new workflow in n8n
2. Add a **Schedule Trigger** node:
   * Click the "**+**" button on canvas
   * Search for "**Schedule Trigger**"
   * Configure: Every day at 9:00 AM

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-schedule-trigger-daily-cron.gif?s=ae68cd74cdf14a1d012861df8319b245" alt="Schedule Trigger configured for daily 9 AM execution" data-og-width="2116" width="2116" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-schedule-trigger-daily-cron.gif" data-optimize="true" data-opv="3" />

3. Add the **Firecrawl** node:
   * Click "**+**" next to Schedule Trigger
   * Search for and add "**Firecrawl**"
   * Select your Firecrawl credential
   * Configure:
     * **Resource**: Scrape a url and get its content
     * **URL**: `https://www.firecrawl.dev/blog/category/product-updates`
     * **Formats**: Select "Summary"

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-scrape-blog-summary.gif?s=ad1684f165aacd7ab5d1530cdac73962" alt="Adding and configuring Firecrawl node with the blog URL and Summary format selected" data-og-width="2116" width="2116" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-firecrawl-scrape-blog-summary.gif" data-optimize="true" data-opv="3" />

4. Add the **Telegram** node:
   * Click "**+**" next to Firecrawl
   * Search for "**Telegram**"
   * Click "**Send a text message**" to add it to the canvas

5. Set up Telegram credentials:
   * Click on the Telegram node to open its configuration
   * In the "Credential to connect with" dropdown, click "**Create New Credential**"
   * Paste your bot token from BotFather
   * Click "**Save**"

<img src="https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-telegram-bot-token-credentials.gif" alt="Telegram credential configuration with bot token field" />

6. Configure the Telegram message:
   * **Operation**: Send Message

   * **Chat ID**: Enter your chat ID

   * **Text**: Leave this with a "hello" message for now

   * Click **Execute step** to test sending a message while receiving the summary from Firecrawl.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-test-telegram-message-firecrawl.gif" alt="Configuring Telegram node and mapping the summary field to the message text" />

* Now with Firecrawl's summary structure, add the summary to the message text by dragging the `summary` field from Firecrawl node output.

7. Test the workflow:
   * Click "**Execute Workflow**"
   * Check your Telegram for the summary message

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=1c3eacbcb705c21c6265ae3ecbd59d59" alt="Complete workflow showing Schedule Trigger → Firecrawl → Telegram with all nodes connected" data-og-width="1538" width="1538" data-og-height="1046" height="1046" data-path="images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=d59acd307786d60f459c1d1f7fc9ed24 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=28da669238c05f0f840f51c9d9f4b35a 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7bb0f7e8bfbdd970bc5b5777501323b0 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=d2d407548ec49b2700e91eeb7dcca029 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=840a62d2cd26b7658b839ad1d0ab23a0 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=f9132a7d8e480ec8d64de845ddad6219 2500w" />

8. Activate the workflow by toggling the "**Active**" switch

Your Telegram bot will now send you a daily summary of Firecrawl product updates every morning at 9 AM.

### Example 2: AI News Search to Telegram

This workflow uses Firecrawl's Search operation to find AI news and send formatted results to Telegram.

**Key differences from Example 1:**

* Uses a **Manual Trigger** instead of Schedule (run on demand)
* Uses **Search** operation instead of Scrape
* Includes a **Code** node to format multiple results

**Build the workflow:**

1. Create a new workflow and add a **Manual Trigger** node

2. Add **Firecrawl** node with these settings:
   * **Resource**: Search and optionally scrape search results
   * **Query**: `ai news`
   * **Limit**: 5

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-search-ai-news-results.gif?s=23eb224783b0b3155d179a0342839621" alt="Firecrawl Search node configuration with &#x22;ai news&#x22; query" data-og-width="1776" width="1776" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-firecrawl-search-ai-news-results.gif" data-optimize="true" data-opv="3" />

3. Add a **Code** node to format the search results:
   * Select "Run Once for All Items"
   * Paste this code:
```

Example 4 (unknown):
```unknown
<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-code-node-format-news-articles.gif?s=cafb96e0b7f2ef27a09ae2957390799b" alt="Adding Code node and pasting the formatting script" data-og-width="1768" width="1768" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-code-node-format-news-articles.gif" data-optimize="true" data-opv="3" />

4. Update **Telegram** node (using your saved credential):
   * **Text**: Drag the `message` field from Code node

<img src="https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-execute-workflow-telegram-delivery.gif" alt="Complete workflow execution with AI news sent to Telegram" />

<Tip>
  Replace the Manual Trigger with a Schedule Trigger to get automatic AI news updates at set intervals.
</Tip>

### Example 3: AI-Powered News Summary

This workflow adds AI to Example 2, using OpenAI to generate intelligent summaries of the latest AI news before sending to Telegram.

**Key changes from Example 2:**

* Add **OpenAI credentials** setup
* Add **AI Agent** node between Code and Telegram
* AI Agent analyzes and summarizes all the news articles intelligently
* Telegram receives the AI-generated summary instead of raw news list

**Modify the workflow:**

1. **Get your OpenAI API key**:
   * Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   * Sign in or create an account
   * Click "**Create new secret key**"
   * Give it a name (e.g., "n8n Integration")
   * Copy the API key immediately (you won't see it again)

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/openai-api-key-creation-dashboard.gif?s=8222a339a403f85272102256fa91fc27" alt="OpenAI dashboard showing API key creation" data-og-width="1780" width="1780" data-og-height="1080" height="1080" data-path="images/guides/n8n/openai-api-key-creation-dashboard.gif" data-optimize="true" data-opv="3" />

2. **Add and connect the AI Agent node**:
   * Click "**+**" after the Code node
   * Search for "**Basic LLM Chain**" or "**AI Agent**"
   * Drag the `message` field from the Code node to the AI Agent's input prompt field
   * Select **OpenAI** as the LLM provider

<img src="https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-ai-agent-openai-llm-setup.gif" alt="Adding AI Agent node, dragging input from Code node, and connecting OpenAI as LLM" />

3. **Add your OpenAI credentials**:
   * Click "**Create New Credential**" for OpenAI
   * Paste your OpenAI API key
   * Select model: **gpt-5-mini** (cost-effective) or **gpt-5** (more capable)
   * Click "**Save**"

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-openai-credentials-gpt-model.gif?s=c97249f572e8d530583918ebc3357d53" alt="Adding OpenAI credentials to the AI Agent node" data-og-width="1596" width="1596" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-openai-credentials-gpt-model.gif" data-optimize="true" data-opv="3" />

4. **Add the system prompt to the AI Agent**:
   * In the AI Agent node, add this system prompt:
```

---

## Deep Research

**URL:** llms-txt#deep-research

**Contents:**
- Start with a Template
- How It Works
- Why Researchers Choose Firecrawl
  - Accelerate Research from Weeks to Hours
  - Ensure Research Completeness
- Research Tool Capabilities
- FAQs
- Related Use Cases

Source: https://docs.firecrawl.dev/use-cases/deep-research

Build agentic research tools with deep web search capabilities

Academic researchers and analysts use Firecrawl's deep research mode to aggregate data from hundreds of sources automatically.

## Start with a Template

<CardGroup>
  <Card title="Fireplexity" icon="github" href="https://github.com/mendableai/fireplexity">
    Blazing-fast AI search with real-time citations
  </Card>

<Card title="Firesearch" icon="github" href="https://github.com/mendableai/firesearch">
    Deep research agent with LangGraph and answer validation
  </Card>

<Card title="Open Researcher" icon="github" href="https://github.com/mendableai/open-researcher">
    Visual AI research assistant for comprehensive analysis
  </Card>
</CardGroup>

<Note>
  **Choose from multiple research templates.** Clone, configure your API key, and start researching.
</Note>

Build powerful research tools that transform scattered web data into comprehensive insights. Use Firecrawl's APIs to iteratively explore topics, discover sources, and extract content with full citations for your research applications.

## Why Researchers Choose Firecrawl

### Accelerate Research from Weeks to Hours

Build automated research systems that discover, read, and synthesize information from across the web. Create tools that deliver comprehensive reports with full citations, eliminating manual searching through hundreds of sources.

### Ensure Research Completeness

Reduce the risk of missing critical information. Build systems that follow citation chains, discover related sources, and surface insights that traditional search methods miss.

## Research Tool Capabilities

* **Iterative Exploration**: Build tools that automatically discover related topics and sources
* **Multi-Source Synthesis**: Combine information from hundreds of websites
* **Citation Preservation**: Maintain full source attribution in your research outputs
* **Intelligent Summarization**: Extract key findings and insights for analysis
* **Trend Detection**: Identify patterns across multiple sources

<AccordionGroup>
  <Accordion title="How can I build research tools with Firecrawl?">
    Use Firecrawl's crawl and search APIs to build iterative research systems. Start with search results, extract content from relevant pages, follow citation links, and aggregate findings. Combine with LLMs to synthesize comprehensive research reports.
  </Accordion>

<Accordion title="Can Firecrawl handle academic and scientific websites?">
    Yes. Firecrawl can extract data from open-access research papers, academic websites, and publicly available scientific publications. It preserves formatting, citations, and technical content critical for research work.
  </Accordion>

<Accordion title="How do I ensure research data accuracy?">
    Firecrawl maintains source attribution and extracts content exactly as presented on websites. All data includes source URLs and timestamps, ensuring full traceability for research purposes.
  </Accordion>

<Accordion title="Can I use Firecrawl for longitudinal studies?">
    Yes. Set up scheduled crawls to track how information changes over time. This is perfect for monitoring trends, policy changes, or any research requiring temporal data analysis.
  </Accordion>

<Accordion title="How does Firecrawl handle large-scale research projects?">
    Our crawling infrastructure scales to handle thousands of sources simultaneously. Whether you're analyzing entire industries or tracking global trends, Firecrawl provides the data pipeline you need.
  </Accordion>
</AccordionGroup>

* [AI Platforms](/use-cases/ai-platforms) - Build AI research assistants
* [Content Generation](/use-cases/content-generation) - Research-based content
* [Competitive Intelligence](/use-cases/competitive-intelligence) - Market research

---

## MAX_CPU=0.8

**URL:** llms-txt#max_cpu=0.8

---

## https://abc123.trycloudflare.com

**URL:** llms-txt#https://abc123.trycloudflare.com

**Contents:**
- Debugging Common Issues
  - Webhooks Not Arriving
  - Signature Verification Failing

json  theme={null}
{
  "url": "https://abc123.trycloudflare.com/webhook"
}
javascript  theme={null}
// ❌ Wrong - using parsed body
const signature = crypto
  .createHmac('sha256', secret)
  .update(JSON.stringify(req.body))
  .digest('hex');

// ✅ Correct - using raw body
app.use('/webhook', express.raw({ type: 'application/json' }));
app.post('/webhook', (req, res) => {
  const signature = crypto
    .createHmac('sha256', secret)
    .update(req.body) // Raw buffer
    .digest('hex');
});
```

**Examples:**

Example 1 (unknown):
```unknown
Use the provided URL in your webhook configuration:
```

Example 2 (unknown):
```unknown
## Debugging Common Issues

### Webhooks Not Arriving

1. **Check URL accessibility** – Ensure your endpoint is publicly accessible
2. **Verify HTTPS** – Webhook URLs must use HTTPS
3. **Check firewall settings** – Allow incoming connections to your webhook port
4. **Review event filters** – Ensure you're subscribed to the correct event types

### Signature Verification Failing

1. **Check the secret key** – Ensure you're using the correct secret

2. **Verify raw body usage** – Make sure you're using the raw request body:
```

---

## Stealth Mode

**URL:** llms-txt#stealth-mode

**Contents:**
  - Proxy Types
  - Using Stealth Mode
- Using Stealth as a Retry Mechanism

Source: https://docs.firecrawl.dev/features/stealth-mode

Use stealth proxies for sites with advanced anti-bot solutions

Firecrawl provides different proxy types to help you scrape websites with varying levels of anti-bot protection. The proxy type can be specified using the `proxy` parameter.

Firecrawl supports three types of proxies:

* **basic**: Proxies for scraping sites with none to basic anti-bot solutions. Fast and usually works.
* **stealth**: Stealth proxies for scraping sites with advanced anti-bot solutions. Slower, but more reliable on certain sites.
* **auto**: Firecrawl will automatically retry scraping with stealth proxies if the basic proxy fails. If the retry with stealth is successful, 5 credits will be billed for the scrape. If the first attempt with basic is successful, only the regular cost will be billed.

If you do not specify a proxy, Firecrawl will default to auto.

### Using Stealth Mode

When scraping websites with advanced anti-bot protection, you can use the stealth proxy mode to improve your success rate.

**Note:** Stealth proxy requests cost 5 credits per request when used.

## Using Stealth as a Retry Mechanism

A common pattern is to first try scraping with the default proxy settings, and then retry with stealth mode if you encounter specific error status codes (401, 403, or 500) in the `metadata.statusCode` field of the response. These status codes can be indicative of the website blocking your request.

This approach allows you to optimize your credit usage by only using stealth mode when necessary.

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

**Note:** Stealth proxy requests cost 5 credits per request when used.

## Using Stealth as a Retry Mechanism

A common pattern is to first try scraping with the default proxy settings, and then retry with stealth mode if you encounter specific error status codes (401, 403, or 500) in the `metadata.statusCode` field of the response. These status codes can be indicative of the website blocking your request.

<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## MCP Web Search & Scrape in Claude Code

**URL:** llms-txt#mcp-web-search-&-scrape-in-claude-code

**Contents:**
- Quick Setup
  - 1. Get Your API Key
  - 2. Add Firecrawl MCP Server
- Quick Demo

Source: https://docs.firecrawl.dev/developer-guides/mcp-setup-guides/claude-code

Add web scraping and search to Claude Code in 2 minutes

Add web scraping and search capabilities to Claude Code with Firecrawl MCP.

### 1. Get Your API Key

Sign up at [firecrawl.dev/app](https://firecrawl.dev/app) and copy your API key.

### 2. Add Firecrawl MCP Server

Replace `your-api-key` with your actual Firecrawl API key.

Done! You can now search and scrape the web from Claude Code.

Try these in Claude Code:

**Get documentation:**

Claude will automatically use Firecrawl's search and scrape tools to get the information.

**Examples:**

Example 1 (unknown):
```unknown
Replace `your-api-key` with your actual Firecrawl API key.

Done! You can now search and scrape the web from Claude Code.

## Quick Demo

Try these in Claude Code:

**Search the web:**
```

Example 2 (unknown):
```unknown
**Scrape a page:**
```

Example 3 (unknown):
```unknown
**Get documentation:**
```

---

## Observability & Monitoring

**URL:** llms-txt#observability-&-monitoring

**Contents:**
- Start with a Template
- How It Works
- What You Can Monitor
- Monitoring Types
  - Synthetic Monitoring
  - Content Monitoring
- FAQs
- Related Use Cases

Source: https://docs.firecrawl.dev/use-cases/observability

Monitor websites, track uptime, and detect changes in real-time

DevOps and SRE teams use Firecrawl to monitor websites, track availability, and detect critical changes across their digital infrastructure.

## Start with a Template

<Card title="Firecrawl Observer" icon="github" href="https://github.com/mendableai/firecrawl-observer">
  Real-time website monitoring and intelligent change detection
</Card>

<Note>
  **Get started with the Firecrawl Observer template.** Monitor websites and track changes in real-time.
</Note>

Use Firecrawl's extraction capabilities to build observability systems for your websites. Extract page content, analyze changes over time, validate deployments, and create monitoring workflows that ensure your sites function correctly.

## What You Can Monitor

* **Availability**: Uptime, response times, error rates
* **Content**: Text changes, image updates, layout shifts
* **Performance**: Page load times, resource sizes, Core Web Vitals
* **Security**: SSL certificates, security headers, misconfigurations
* **SEO Health**: Meta tags, structured data, sitemap validity

### Synthetic Monitoring

* User journey validation
* Transaction monitoring
* Multi-step workflows
* Cross-browser testing

### Content Monitoring

* Text change detection
* Visual regression testing
* Dynamic content validation
* Internationalization checks

<AccordionGroup>
  <Accordion title="How does Firecrawl help with website monitoring?">
    Firecrawl extracts website content and structure on demand. Build monitoring systems that call Firecrawl's API to check pages, compare extracted data against baselines, and trigger your own alerts when changes occur.
  </Accordion>

<Accordion title="Can I monitor JavaScript-heavy applications?">
    Yes! Firecrawl fully renders JavaScript, making it perfect for monitoring modern SPAs, React apps, and dynamic content. We capture the page as users see it, not just the raw HTML.
  </Accordion>

<Accordion title="How quickly can I detect website issues?">
    Firecrawl extracts data in real-time when called. Build your monitoring system to check sites at whatever frequency you need - from minute-by-minute for critical pages to daily for routine checks.
  </Accordion>

<Accordion title="Can I validate specific page elements?">
    Yes. Use the extract API to pull specific elements like prices, inventory levels, or critical content. Build validation logic in your monitoring system to verify that important information is present and correct.
  </Accordion>

<Accordion title="How can I integrate Firecrawl with alerting systems?">
    Firecrawl provides webhooks that you can use to build integrations with your alerting tools. Send extracted data to PagerDuty, Slack, email, or any monitoring platform by building connectors that process Firecrawl's responses.
  </Accordion>
</AccordionGroup>

* [Competitive Intelligence](/use-cases/competitive-intelligence) - Monitor competitor changes
* [Product & E-commerce](/use-cases/product-ecommerce) - Track inventory and pricing
* [Data Migration](/use-cases/data-migration) - Validate migrations

---

## Map

**URL:** llms-txt#map

**Contents:**
- Introducing /map
- Mapping
  - /map endpoint
  - Installation
  - Usage
  - Response
- Location and Language
  - How it works
  - Usage
- Considerations

Source: https://docs.firecrawl.dev/features/map

Input a website and get all the urls on the website - extremely fast

The easiest way to go from a single url to a map of the entire website. This is extremely useful for:

* When you need to prompt the end-user to choose which links to scrape
* Need to quickly know the links on a website
* Need to scrape pages of a website that are related to a specific topic (use the `search` parameter)
* Only need to scrape specific pages of a website

Used to map a URL and get urls of the website. This returns most links present on the website.

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

<Warning>
  Title and description are not always present as it depends on the website.
</Warning>

Map with `search` param allows you to search for specific urls inside a website.

Response will be an ordered list from the most relevant to the least relevant.

## Location and Language

Specify country and preferred languages to get relevant content based on your target location and language preferences, similar to the scrape endpoint.

When you specify the location settings, Firecrawl will use an appropriate proxy if available and emulate the corresponding language and timezone settings. By default, the location is set to 'US' if not specified.

To use the location and language settings, include the `location` object in your request body with the following properties:

* `country`: ISO 3166-1 alpha-2 country code (e.g., 'US', 'AU', 'DE', 'JP'). Defaults to 'US'.
* `languages`: An array of preferred languages and locales for the request in order of priority. Defaults to the language of the specified location.

For more details about supported locations, refer to the [Proxies documentation](/features/proxies).

This endpoint prioritizes speed, so it may not capture all website links. We are working on improvements. Feedback and suggestions are very welcome.

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

### Usage

<CodeGroup>
```

Example 3 (unknown):
```unknown

```

Example 4 (unknown):
```unknown
</CodeGroup>

### Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.
```

---

## Investment & Finance

**URL:** llms-txt#investment-&-finance

**Contents:**
- Start with a Template
- How It Works
- What You Can Track
- Customer Stories
- FAQs
- Related Use Cases

Source: https://docs.firecrawl.dev/use-cases/investment-finance

Track companies and extract financial insights from web data

Hedge funds, VCs, and financial analysts use Firecrawl to monitor portfolio companies and gather market intelligence.

## Start with a Template

<Card title="Firecrawl Observer" icon="github" href="https://github.com/mendableai/firecrawl-observer">
  Monitor portfolio companies for material changes and trigger events
</Card>

<Note>
  **Get started with the Firecrawl Observer template.** Monitor portfolio companies and market changes.
</Note>

Extract financial signals from across the web. Monitor portfolio companies, track market movements, and support due diligence workflows with real-time web data extraction.

## What You Can Track

* **Company Metrics**: Growth indicators, team changes, product launches, funding rounds
* **Market Signals**: Industry trends, competitor moves, sentiment analysis, regulatory changes
* **Risk Indicators**: Leadership changes, legal issues, regulatory mentions, customer complaints
* **Financial Data**: Pricing updates, revenue signals, partnership announcements
* **Alternative Data**: Job postings, web traffic, social signals, news mentions

<CardGroup cols={2}>
  <Card href="https://www.firecrawl.dev/blog/how-athena-intelligence-empowers-analysts-with-firecrawl">
    **Athena Intelligence**

Discover how Athena Intelligence leverages Firecrawl to fuel its AI-native analytics platform for enterprise analysts.
  </Card>

<Card href="https://www.firecrawl.dev/blog/how-cargo-empowers-gtm-teams-with-firecrawl">
    **Cargo**

See how Cargo uses Firecrawl to analyze market data and power revenue intelligence workflows.
  </Card>
</CardGroup>

<AccordionGroup>
  <Accordion title="Can I track private companies?">
    Yes, you can monitor publicly available information about private companies from their websites, news mentions, job postings, and social media presence.
  </Accordion>

<Accordion title="How real-time is the data?">
    Firecrawl extracts data in real-time when called. Build your own monitoring system to fetch data at intervals that match your investment strategy - from minute-by-minute for critical events to daily for routine tracking.
  </Accordion>

<Accordion title="What alternative data sources can I monitor?">
    Public web sources such as company websites, news sites, job boards, review sites, forums, social media, government filings, and open-access industry data.
  </Accordion>

<Accordion title="How can I track ESG and sustainability signals?">
    Extract data from company ESG reports, sustainability pages, news mentions of environmental initiatives, and regulatory filings. Build tracking systems to identify changes in sustainability commitments or ESG-related developments.
  </Accordion>

<Accordion title="Can Firecrawl help with earnings call preparation?">
    Yes. Extract recent company updates, product launches, executive changes, and industry trends before earnings calls. Combine with competitor data to anticipate questions and identify key discussion points.
  </Accordion>
</AccordionGroup>

* [Competitive Intelligence](/use-cases/competitive-intelligence) - Track market competitors
* [Deep Research](/use-cases/deep-research) - Comprehensive market analysis
* [Lead Enrichment](/use-cases/lead-enrichment) - B2B investment opportunities

---

## PLAYWRIGHT_MICROSERVICE_URL=http://playwright-service:3000/scrape

**URL:** llms-txt#playwright_microservice_url=http://playwright-service:3000/scrape

---

## Migrating from v1 to v2

**URL:** llms-txt#migrating-from-v1-to-v2

**Contents:**
- Overview
  - Key Improvements
- Quick migration checklist
- SDK surface (v2)
  - JS/TS
  - Python (sync)
  - Python (async)
- Formats and scrape options
  - JSON format
  - Screenshot format

Source: https://docs.firecrawl.dev/migrate-to-v2

Key changes, mappings, and before/after snippets to upgrade your integration to v2.

* **Faster by default**: Requests are cached with `maxAge` defaulting to 2 days, and sensible defaults like `blockAds`, `skipTlsVerification`, and `removeBase64Images` are enabled.

* **New summary format**: You can now specify `"summary"` as a format to directly receive a concise summary of the page content.

* **Updated JSON extraction**: JSON extraction and change tracking now use an object format: `{ type: "json", prompt, schema }`. The old `"extract"` format has been renamed to `"json"`.

* **Enhanced screenshot options**: Use the object form: `{ type: "screenshot", fullPage, quality, viewport }`.

* **New search sources**: Search across `"news"` and `"images"` in addition to web results by setting the `sources` parameter.

* **Smart crawling with prompts**: Pass a natural-language `prompt` to crawl and the system derives paths/limits automatically. Use the new /crawl/params-preview endpoint to inspect the derived options before starting a job.

## Quick migration checklist

* Replace v1 client usage with v2 clients:
  * JS: `const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' })`
  * Python: `firecrawl = Firecrawl(api_key='fc-YOUR-API-KEY')`
  * API: use the new `https://api.firecrawl.dev/v2/` endpoints.
* Update formats:
  * Use `"summary"` where needed
  * JSON mode: Use `{ type: "json", prompt, schema }` for JSON extraction
  * Screenshot and Screenshot\@fullPage: Use screenshot object format when specifying options
* Adopt standardized async flows in the SDKs:
  * Crawls: `startCrawl` + `getCrawlStatus` (or `crawl` waiter)
  * Batch: `startBatchScrape` + `getBatchScrapeStatus` (or `batchScrape` waiter)
  * Extract: `startExtract` + `getExtractStatus` (or `extract` waiter)
* Crawl options mapping (see below)
* Check crawl `prompt` with `/crawl/params-preview`

#### Method name changes (v1 → v2)

**Scrape, Search, and Map**

| v1 (FirecrawlApp)     | v2 (Firecrawl)            |
| --------------------- | ------------------------- |
| `scrapeUrl(url, ...)` | `scrape(url, options?)`   |
| `search(query, ...)`  | `search(query, options?)` |
| `mapUrl(url, ...)`    | `map(url, options?)`      |

| v1                          | v2                              |
| --------------------------- | ------------------------------- |
| `crawlUrl(url, ...)`        | `crawl(url, options?)` (waiter) |
| `asyncCrawlUrl(url, ...)`   | `startCrawl(url, options?)`     |
| `checkCrawlStatus(id, ...)` | `getCrawlStatus(id)`            |
| `cancelCrawl(id)`           | `cancelCrawl(id)`               |
| `checkCrawlErrors(id)`      | `getCrawlErrors(id)`            |

| v1                                | v2                                  |
| --------------------------------- | ----------------------------------- |
| `batchScrapeUrls(urls, ...)`      | `batchScrape(urls, opts?)` (waiter) |
| `asyncBatchScrapeUrls(urls, ...)` | `startBatchScrape(urls, opts?)`     |
| `checkBatchScrapeStatus(id, ...)` | `getBatchScrapeStatus(id)`          |
| `checkBatchScrapeErrors(id)`      | `getBatchScrapeErrors(id)`          |

| v1                            | v2                     |
| ----------------------------- | ---------------------- |
| `extract(urls?, params?)`     | `extract(args)`        |
| `asyncExtract(urls, params?)` | `startExtract(args)`   |
| `getExtractStatus(id)`        | `getExtractStatus(id)` |

| v1                                | v2                    |
| --------------------------------- | --------------------- |
| `generateLLMsText(...)`           | (not in v2 SDK)       |
| `checkGenerateLLMsTextStatus(id)` | (not in v2 SDK)       |
| `crawlUrlAndWatch(...)`           | `watcher(jobId, ...)` |
| `batchScrapeUrlsAndWatch(...)`    | `watcher(jobId, ...)` |

#### Method name changes (v1 → v2)

**Scrape, Search, and Map**

| v1                | v2            |
| ----------------- | ------------- |
| `scrape_url(...)` | `scrape(...)` |
| `search(...)`     | `search(...)` |
| `map_url(...)`    | `map(...)`    |

| v1                        | v2                      |
| ------------------------- | ----------------------- |
| `crawl_url(...)`          | `crawl(...)` (waiter)   |
| `async_crawl_url(...)`    | `start_crawl(...)`      |
| `check_crawl_status(...)` | `get_crawl_status(...)` |
| `cancel_crawl(...)`       | `cancel_crawl(...)`     |

| v1                             | v2                             |
| ------------------------------ | ------------------------------ |
| `batch_scrape_urls(...)`       | `batch_scrape(...)` (waiter)   |
| `async_batch_scrape_urls(...)` | `start_batch_scrape(...)`      |
| `get_batch_scrape_status(...)` | `get_batch_scrape_status(...)` |
| `get_batch_scrape_errors(...)` | `get_batch_scrape_errors(...)` |

| v1                        | v2                        |
| ------------------------- | ------------------------- |
| `extract(...)`            | `extract(...)`            |
| `start_extract(...)`      | `start_extract(...)`      |
| `get_extract_status(...)` | `get_extract_status(...)` |

| v1                                   | v2                     |
| ------------------------------------ | ---------------------- |
| `generate_llms_text(...)`            | (not in v2 SDK)        |
| `get_generate_llms_text_status(...)` | (not in v2 SDK)        |
| `watch_crawl(...)`                   | `watcher(job_id, ...)` |

* `AsyncFirecrawl` mirrors the same methods (all awaitable).

## Formats and scrape options

* Use string formats for basics: `"markdown"`, `"html"`, `"rawHtml"`, `"links"`, `"summary"`, `"images"`.
* Instead of `parsePDF` use `parsers: [ { "type": "pdf" } | "pdf" ]`.
* Use object formats for JSON, change tracking, and screenshots:

### Screenshot format

## Crawl options mapping (v1 → v2)

| v1                      | v2                                                   |
| ----------------------- | ---------------------------------------------------- |
| `allowBackwardCrawling` | (removed) use `crawlEntireDomain`                    |
| `maxDepth`              | (removed) use `maxDiscoveryDepth`                    |
| `ignoreSitemap` (bool)  | `sitemap` (e.g., `"only"`, `"skip"`, or `"include"`) |
| (none)                  | `prompt`                                             |

## Crawl prompt + params preview

See crawl params preview examples:

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

### Screenshot format

<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## PROXY_SERVER=

**URL:** llms-txt#proxy_server=

---

## SUPABASE_URL=

**URL:** llms-txt#supabase_url=

---

## Security

**URL:** llms-txt#security

**Contents:**
- Why Webhook Security Matters
- How Firecrawl Signs Webhooks
- Finding Your Secret Key
- Signature Verification
  - How Signatures Work
  - Implementation Examples
  - Step-by-Step Verification
- Security Best Practices
  - Always Validate Signatures
  - Use Timing-Safe Comparisons

Source: https://docs.firecrawl.dev/webhooks/security

Verify webhook authenticity and implement security best practices

Webhook security is critical to ensure that requests to your endpoint are actually coming from Firecrawl and haven't been tampered with. This page covers how to verify webhook authenticity and implement security best practices.

## Why Webhook Security Matters

Without proper verification, attackers could:

* Send fake webhook requests to trigger unwanted actions
* Modify payload data to manipulate your application
* Overload your webhook endpoint with requests

## How Firecrawl Signs Webhooks

Firecrawl signs every webhook request using **HMAC-SHA256** encryption with your account's secret key. This creates a unique signature for each request that proves:

1. The request came from Firecrawl
2. The payload hasn't been modified

## Finding Your Secret Key

Your webhook secret is available under the [Advanced tab](https://www.firecrawl.dev/app/settings?tab=advanced) of your account settings. Each account has a unique secret that's used to sign all webhook requests.

<Warning>
  Keep your webhook secret secure and never expose it publicly. If you believe
  your secret has been compromised, regenerate it immediately from your account
  settings.
</Warning>

## Signature Verification

### How Signatures Work

Each webhook request includes an `X-Firecrawl-Signature` header with this format:

The signature is computed as follows:

1. Take the raw request body (JSON string)
2. Create HMAC-SHA256 hash using your secret key
3. Convert to hexadecimal string
4. Prefix with `sha256=`

### Implementation Examples

### Step-by-Step Verification

1. **Extract the signature** from the `X-Firecrawl-Signature` header
2. **Get the raw request body** as received (don't parse it first)
3. **Compute HMAC-SHA256** using your secret key and the raw body
4. **Compare signatures** using a timing-safe comparison function
5. **Only process** the webhook if signatures match

## Security Best Practices

### Always Validate Signatures

Never trust a webhook request without signature verification:

### Use Timing-Safe Comparisons

Standard string comparison can leak timing information. Use dedicated functions:

* **Node.js**: `crypto.timingSafeEqual()`
* **Python**: `hmac.compare_digest()`
* **Other languages**: Look for "constant-time" or "timing-safe" comparison functions

Always use HTTPS endpoints for webhooks:

**Examples:**

Example 1 (unknown):
```unknown
X-Firecrawl-Signature: sha256=abc123def456...
```

Example 2 (unknown):
```unknown

```

Example 3 (unknown):
```unknown
</CodeGroup>

### Step-by-Step Verification

1. **Extract the signature** from the `X-Firecrawl-Signature` header
2. **Get the raw request body** as received (don't parse it first)
3. **Compute HMAC-SHA256** using your secret key and the raw body
4. **Compare signatures** using a timing-safe comparison function
5. **Only process** the webhook if signatures match

## Security Best Practices

### Always Validate Signatures

Never trust a webhook request without signature verification:
```

Example 4 (unknown):
```unknown
### Use Timing-Safe Comparisons

Standard string comparison can leak timing information. Use dedicated functions:

* **Node.js**: `crypto.timingSafeEqual()`
* **Python**: `hmac.compare_digest()`
* **Other languages**: Look for "constant-time" or "timing-safe" comparison functions

### Require HTTPS

Always use HTTPS endpoints for webhooks:
```

---

## REDIS_RATE_LIMIT_URL=redis://redis:6379

**URL:** llms-txt#redis_rate_limit_url=redis://redis:6379

---

## ALLOW_LOCAL_WEBHOOKS=true

**URL:** llms-txt#allow_local_webhooks=true

**Contents:**
- Troubleshooting
  - Supabase client is not configured
  - You're bypassing authentication
  - Docker containers fail to start
  - Connection issues with Redis
  - API endpoint does not respond
- Install Firecrawl on a Kubernetes Cluster (Simple Version)

plaintext  theme={null}
         build: apps/playwright-service
     plaintext  theme={null}
         build: apps/playwright-service-ts
     plaintext  theme={null}
     PLAYWRIGHT_MICROSERVICE_URL=http://localhost:3000/scrape
     bash  theme={null}
   docker compose build
   docker compose up
   bash  theme={null}
curl -X POST http://localhost:3002/v2/crawl \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'
bash  theme={null}
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Attempted to access Supabase client when it's not configured.
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Error inserting scrape event: Error: Supabase client is not configured.
bash  theme={null}
[YYYY-MM-DDTHH:MM:SS.SSSz]WARN - You're bypassing authentication
bash  theme={null}
docker logs [container_name]
```

* Ensure all required environment variables are set correctly in the .env file.
* Verify that all Docker services defined in docker-compose.yml are correctly configured and the necessary images are available.

### Connection issues with Redis

**Symptom:**
Errors related to connecting to Redis, such as timeouts or "Connection refused".

* Ensure that the Redis service is up and running in your Docker environment.
* Verify that the REDIS\_URL and REDIS\_RATE\_LIMIT\_URL in your .env file point to the correct Redis instance.
* Check network settings and firewall rules that may block the connection to the Redis port.

### API endpoint does not respond

**Symptom:**
API requests to the Firecrawl instance timeout or return no response.

* Ensure that the Firecrawl service is running by checking the Docker container status.
* Verify that the PORT and HOST settings in your .env file are correct and that no other service is using the same port.
* Check the network configuration to ensure that the host is accessible from the client making the API request.

By addressing these common issues, you can ensure a smoother setup and operation of your self-hosted Firecrawl instance.

## Install Firecrawl on a Kubernetes Cluster (Simple Version)

Read the [examples/kubernetes-cluster-install/README.md](https://github.com/firecrawl/firecrawl/tree/main/examples/kubernetes/cluster-install#readme) for instructions on how to install Firecrawl on a Kubernetes Cluster.

**Examples:**

Example 1 (unknown):
```unknown
3. *(Optional) Running with TypeScript Playwright Service*

   * Update the `docker-compose.yml` file to change the Playwright service:
```

Example 2 (unknown):
```unknown
TO
```

Example 3 (unknown):
```unknown
* Set the `PLAYWRIGHT_MICROSERVICE_URL` in your `.env` file:
```

Example 4 (unknown):
```unknown
* Don't forget to set the proxy server in your `.env` file as needed.

4. Build and run the Docker containers:
```

---

## Expose your local server

**URL:** llms-txt#expose-your-local-server

cloudflared tunnel --url localhost:3000

---

## This key lets you access the queue admin panel. Change this if your deployment is publicly accessible.

**URL:** llms-txt#this-key-lets-you-access-the-queue-admin-panel.-change-this-if-your-deployment-is-publicly-accessible.

BULL_AUTH_KEY=CHANGEME

---

## Maximum RAM usage threshold (0.0-1.0). Worker will reject new jobs when memory usage exceeds this value.

**URL:** llms-txt#maximum-ram-usage-threshold-(0.0-1.0).-worker-will-reject-new-jobs-when-memory-usage-exceeds-this-value.

---

## Running locally

**URL:** llms-txt#running-locally

**Contents:**
- Running the project locally

Source: https://docs.firecrawl.dev/contributing/guide

Learn how to run Firecrawl locally to run on your own and/or contribute to the project.

Welcome to [Firecrawl](https://firecrawl.dev) 🔥! Here are some instructions on how to get the project locally, so you can run it on your own (and contribute)

If you're contributing, note that the process is similar to other open source repos i.e. (fork firecrawl, make changes, run tests, PR). If you have any questions, and would like help gettin on board, reach out to [help@firecrawl.com](mailto:help@firecrawl.com) for more or submit an issue!

## Running the project locally

First, start by installing dependencies:

1. node.js [instructions](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)
2. pnpm [instructions](https://pnpm.io/installation)
3. redis [instructions](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)
4. postgresql
5. Docker (optional) (for running postgres)

You need to set up the PostgreSQL database by running the SQL file at `apps/nuq-postgres/nuq.sql`. Easiest way is to use the docker image inside `apps/nuq-postgres`. With Docker running, build the image:

Set environment variables in a .env in the /apps/api/ directory you can copy over the template in .env.example.

To start, we wont set up authentication, or any optional sub services (pdf parsing, JS blocking support, AI features )

**Examples:**

Example 1 (unknown):
```unknown
and then run:
```

Example 2 (unknown):
```unknown
Set environment variables in a .env in the /apps/api/ directory you can copy over the template in .env.example.

To start, we wont set up authentication, or any optional sub services (pdf parsing, JS blocking support, AI features )

.env:
```

---

## MAX_RAM=0.8

**URL:** llms-txt#max_ram=0.8

---

## Download cloudflared from GitHub releases or use a package manager

**URL:** llms-txt#download-cloudflared-from-github-releases-or-use-a-package-manager

---

## Set if you have a llamaparse key you'd like to use to parse pdfs

**URL:** llms-txt#set-if-you-have-a-llamaparse-key-you'd-like-to-use-to-parse-pdfs

---

## SEARXNG_CATEGORIES=

**URL:** llms-txt#searxng_categories=

**Contents:**
- === Other ===

---

## Use Cases

**URL:** llms-txt#use-cases

Source: https://docs.firecrawl.dev/use-cases/overview

Transform web data into powerful features for your applications

Explore how different teams leverage Firecrawl to power their AI applications and data workflows.

<CardGroup cols={2}>
  <Card title="AI Platforms" href="/use-cases/ai-platforms">
    Add web knowledge to your RAG chatbots and AI assistants.
  </Card>

<Card title="Lead Enrichment" href="/use-cases/lead-enrichment">
    Extract and filter leads from websites to enrich your sales pipeline.
  </Card>

<Card title="SEO Platforms" href="/use-cases/seo-platforms">
    Monitor SERP rankings and optimize content strategy.
  </Card>

<Card title="Deep Research" href="/use-cases/deep-research">
    Build agentic research tools with deep web search capabilities.
  </Card>

<Card title="Product & E-commerce" href="/use-cases/product-ecommerce">
    Monitor pricing and track inventory across e-commerce sites.
  </Card>

<Card title="Content Generation" href="/use-cases/content-generation">
    Generate AI content based on website data and structure.
  </Card>

<Card title="Developers & MCP" href="/use-cases/developers-mcp">
    Build powerful integrations with Model Context Protocol support.
  </Card>

<Card title="Investment & Finance" href="/use-cases/investment-finance">
    Track companies and extract financial insights from web data.
  </Card>

<Card title="Competitive Intelligence" href="/use-cases/competitive-intelligence">
    Monitor competitor websites and track changes in real-time.
  </Card>

<Card title="Data Migration" href="/use-cases/data-migration">
    Transfer web data seamlessly between platforms and systems.
  </Card>

<Card title="Observability" href="/use-cases/observability">
    Monitor websites, track uptime, and detect changes in real-time.
  </Card>
</CardGroup>

---

## SLACK_WEBHOOK_URL=

**URL:** llms-txt#slack_webhook_url=

---

## MODEL_NAME=deepseek-r1:7b

**URL:** llms-txt#model_name=deepseek-r1:7b

---

## Set if you'd like to send server health status messages to Slack

**URL:** llms-txt#set-if-you'd-like-to-send-server-health-status-messages-to-slack

---

## REDIS_URL=redis://redis:6379

**URL:** llms-txt#redis_url=redis://redis:6379

---

## POSTHOG_HOST=

**URL:** llms-txt#posthog_host=

**Contents:**
- === System Resource Configuration ===

## === System Resource Configuration ===

---

## Do not uncomment PROXY_USERNAME and PROXY_PASSWORD if your proxy is unauthenticated

**URL:** llms-txt#do-not-uncomment-proxy_username-and-proxy_password-if-your-proxy-is-unauthenticated

---

## Lead Enrichment

**URL:** llms-txt#lead-enrichment

**Contents:**
- Start with a Template
- How It Works
- Why Sales Teams Choose Firecrawl
  - Transform Directories into Pipeline
  - Enrich CRM Data Automatically
- Customer Stories
- Lead Sources
  - Business Directories
  - Company Websites
- FAQs

Source: https://docs.firecrawl.dev/use-cases/lead-enrichment

Extract and filter leads from websites to power your sales pipeline

Sales ops and BizDev teams use Firecrawl to scrape directories for leads, enrich CRM data, and automate account research.

## Start with a Template

<Card title="Fire Enrich" icon="github" href="https://github.com/mendableai/fire-enrich">
  AI-powered lead enrichment and data extraction from websites
</Card>

<Note>
  **Get started with the Fire Enrich template.** Extract and enrich lead data from websites.
</Note>

Turn the web into your most powerful prospecting tool. Extract company information, find decision makers, and enrich your CRM with real-time data from company websites.

## Why Sales Teams Choose Firecrawl

### Transform Directories into Pipeline

Every industry directory is a goldmine of potential customers. Firecrawl extracts thousands of qualified leads from business directories, trade associations, and conference attendee lists-complete with company details and contact information.

### Enrich CRM Data Automatically

Stop paying for stale data from traditional providers. Firecrawl pulls real-time information directly from company websites, ensuring your sales team always has the latest company news, team changes, and growth signals.

<CardGroup cols={2}>
  <Card href="https://www.firecrawl.dev/blog/how-zapier-uses-firecrawl-to-power-chatbots">
    **Zapier**

Discover how Zapier uses Firecrawl to empower customers with custom knowledge in their chatbots.
  </Card>

<Card href="https://www.firecrawl.dev/blog/how-cargo-empowers-gtm-teams-with-firecrawl">
    **Cargo**

See how Cargo uses Firecrawl to instantly analyze webpage content and power Go-To-Market workflows.
  </Card>
</CardGroup>

### Business Directories

* Industry-specific directories
* Chamber of commerce listings
* Trade association members
* Conference attendee lists

* About pages and team sections
* Press releases and news
* Job postings for growth signals
* Customer case studies

<AccordionGroup>
  <Accordion title="How does Firecrawl enhance lead enrichment processes?">
    Firecrawl automatically extracts company information, contact details, product offerings, and recent news from prospect websites. This enriches your CRM with accurate, up-to-date information for better sales outreach.
  </Accordion>

<Accordion title="Can Firecrawl find contact information from websites?">
    Yes! Firecrawl extracts publicly available contact information including emails and phone numbers from company websites, team pages, and contact sections.
  </Accordion>

<Accordion title="How accurate is the lead data from Firecrawl?">
    Since Firecrawl extracts data directly from live websites, you get the most current information available. This is more accurate than static databases that quickly become outdated.
  </Accordion>

<Accordion title="Can I integrate Firecrawl with my CRM?">
    Yes. Use our API or Zapier integration to automatically enrich leads in Salesforce, HubSpot, Pipedrive, and other CRMs. Keep your lead data fresh without manual research.
  </Accordion>

<Accordion title="How does Firecrawl help with account-based marketing?">
    Extract detailed company information, recent updates, and trigger events from target account websites. This intelligence helps personalize outreach and identify the perfect timing for engagement.
  </Accordion>
</AccordionGroup>

* [AI Platforms](/use-cases/ai-platforms) - Build AI sales assistants
* [Competitive Intelligence](/use-cases/competitive-intelligence) - Track competitors
* [Investment & Finance](/use-cases/investment-finance) - Investment opportunities

---

## Content Generation

**URL:** llms-txt#content-generation

**Contents:**
- Start with a Template
- How It Works
- What You Can Create
- FAQs
- Related Use Cases

Source: https://docs.firecrawl.dev/use-cases/content-generation

Generate AI content based on website data, images, and news

Content teams use Firecrawl to generate personalized presentations, emails, marketing materials, and news-driven updates with real-time web data.

## Start with a Template

<Card title="Open Lovable" icon="github" href="https://github.com/mendableai/open-lovable">
  Clone and recreate any website as a modern React app
</Card>

<Note>
  **Get started with the Open Lovable template.** Transform websites into content and applications.
</Note>

Firecrawl extracts insights from websites in multiple formats — including structured HTML, Markdown, JSON, and screenshots. It can also capture images and surface relevant news stories as part of your request. This means your AI content is both factually grounded and visually enriched with the latest context.

## What You Can Create

* **Sales Decks**: Custom presentations with prospect data
* **Email Campaigns**: Personalized outreach at scale
* **Marketing Content**: Data-driven blog posts and reports
* **Social Media**: Trending topic and news-driven content generation
* **Documentation**: Auto-updated technical content
* **Newsletters**: Curated updates from industry and competitor news
* **Visual Content**: Posts and reports enriched with extracted images and screenshots

<AccordionGroup>
  <Accordion title="How does Firecrawl ensure data accuracy for content creation?">
    Firecrawl extracts data directly from source websites, preserving the original content structure and context. All extracted data includes source URLs and timestamps for verification.
  </Accordion>

<Accordion title="What data can Firecrawl provide for content generation?">
    Firecrawl provides clean markdown, structured JSON, HTML, images, and screenshots from websites. This extracted data serves as the factual foundation for your content generation workflows.
  </Accordion>

<Accordion title="Can Firecrawl handle images and news sources?">
    Yes. Firecrawl can extract images, capture screenshots, and pull content from news sites. This enables you to create visually rich content and stay current with industry developments.
  </Accordion>

<Accordion title="What types of websites can Firecrawl extract from?">
    Firecrawl excels at extracting from company websites, news sites, blogs, and documentation. Sites with structured HTML and clear content hierarchies yield the cleanest extraction results.
  </Accordion>

<Accordion title="How can I use Firecrawl for bulk data extraction?">
    Use Firecrawl's batch scraping and crawl APIs to extract data from multiple websites efficiently. Process hundreds of URLs in parallel to build comprehensive datasets for your content workflows.
  </Accordion>
</AccordionGroup>

* [AI Platforms](/use-cases/ai-platforms) - Build AI-powered content tools
* [Lead Enrichment](/use-cases/lead-enrichment) - Personalize with prospect data
* [SEO Platforms](/use-cases/seo-platforms) - Optimize generated content

---

## Crawl a website:

**URL:** llms-txt#crawl-a-website:

**Contents:**
  - Scraping a URL

crawl_status = firecrawl.crawl(
  'https://firecrawl.dev', 
  limit=100, 
  scrape_options={
    'formats': ['markdown', 'html']
  }
)
print(crawl_status)
python Python theme={null}

**Examples:**

Example 1 (unknown):
```unknown
### Scraping a URL

To scrape a single URL, use the `scrape` method. It takes the URL as a parameter and returns the scraped document.
```

---

## Go

**URL:** llms-txt#go

**Contents:**
- Installation
- Usage
  - Scraping a URL
  - Crawling a Website
  - Checking Crawl Status
  - Map a Website
- Error Handling

Source: https://docs.firecrawl.dev/sdks/go

Firecrawl Go SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.

<Warning>
  This SDK currently uses the **v1** version of the Firecrawl API, which is not the most recent (v2 is available). Some features and improvements may only be available in v2.
</Warning>

To install the Firecrawl Go SDK, you can use go get:

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the `API key` as a parameter to the `FirecrawlApp` struct.
3. Set the `API URL` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `https://api.firecrawl.dev`.
4. Set the `version` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `v1`.

Here's an example of how to use the SDK with error handling:

To scrape a single URL with error handling, use the `ScrapeURL` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

### Crawling a Website

To crawl a website, use the `CrawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

### Checking Crawl Status

To check the status of a crawl job, use the `CheckCrawlStatus` method. It takes the job ID as a parameter and returns the current status of the crawl job.

Use `MapUrl` to generate a list of URLs from a website. The `params` argument let you customize the mapping process, including options to exclude subdomains or to utilize the sitemap.

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.

**Examples:**

Example 1 (unknown):
```unknown
## Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the `API key` as a parameter to the `FirecrawlApp` struct.
3. Set the `API URL` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `https://api.firecrawl.dev`.
4. Set the `version` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `v1`.

Here's an example of how to use the SDK with error handling:
```

Example 2 (unknown):
```unknown
### Scraping a URL

To scrape a single URL with error handling, use the `ScrapeURL` method. It takes the URL as a parameter and returns the scraped data as a dictionary.
```

Example 3 (unknown):
```unknown
### Crawling a Website

To crawl a website, use the `CrawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.
```

Example 4 (unknown):
```unknown
### Checking Crawl Status

To check the status of a crawl job, use the `CheckCrawlStatus` method. It takes the job ID as a parameter and returns the current status of the crawl job.
```

---

## PROXY_SERVER can be a full URL (e.g. http://0.1.2.3:1234) or just an IP and port combo (e.g. 0.1.2.3:1234)

**URL:** llms-txt#proxy_server-can-be-a-full-url-(e.g.-http://0.1.2.3:1234)-or-just-an-ip-and-port-combo-(e.g.-0.1.2.3:1234)

---

## Product & E-commerce

**URL:** llms-txt#product-&-e-commerce

**Contents:**
- Start with a Template
- How It Works
- What You Can Extract
- Use Cases in Action
- FAQs
- Related Use Cases

Source: https://docs.firecrawl.dev/use-cases/product-ecommerce

Monitor pricing and track inventory across e-commerce sites

E-commerce teams use Firecrawl to monitor pricing, track inventory, and migrate product catalogs between platforms.

## Start with a Template

<Card title="Firecrawl Migrator" icon="github" href="https://github.com/mendableai/firecrawl-migrator">
  Migrate product catalogs and e-commerce data between platforms
</Card>

<Note>
  **Get started with the Firecrawl Migrator template.** Extract and migrate e-commerce data efficiently.
</Note>

Transform e-commerce websites into structured product data. Monitor competitor pricing in real-time, track inventory levels across suppliers, and seamlessly migrate product catalogs between platforms.

## What You Can Extract

* **Product Data**: Title, SKU, specs, descriptions, categories
* **Pricing**: Current price, discounts, shipping, tax
* **Inventory**: Stock levels, availability, lead times
* **Reviews**: Ratings, customer feedback, Q\&A sections

## Use Cases in Action

<CardGroup cols={2}>
  <Card>
    **Price Monitoring**

Track competitor pricing across multiple e-commerce sites, receive alerts on price changes, and optimize your pricing strategy based on real-time market data.
  </Card>

<Card>
    **Catalog Migration**

Seamlessly migrate thousands of products between e-commerce platforms, preserving all product data, variants, images, and metadata.
  </Card>
</CardGroup>

<AccordionGroup>
  <Accordion title="How can I track competitor pricing changes?">
    Build a monitoring system using Firecrawl's API to extract prices at regular intervals. Compare extracted data over time to identify pricing trends, promotions, and competitive positioning.
  </Accordion>

<Accordion title="Can I extract product variants (size, color, etc.)?">
    Yes, Firecrawl can extract all product variants including size, color, and other options. Structure the data with custom schemas to capture all variant information.
  </Accordion>

<Accordion title="How do I handle dynamic pricing or user-specific prices?">
    For dynamic pricing, you can use Firecrawl's JavaScript rendering to capture prices after they load. For user-specific pricing, configure authentication headers in your requests.
  </Accordion>

<Accordion title="Can I extract data from different e-commerce platforms?">
    Yes. Firecrawl can extract data from any publicly accessible e-commerce website. Users successfully extract from Shopify, WooCommerce, Magento, BigCommerce, and custom-built stores.
  </Accordion>

<Accordion title="Can Firecrawl handle pagination and infinite scroll?">
    Yes. Firecrawl can navigate through paginated product listings and handle infinite scroll mechanisms to extract complete product catalogs, ensuring no products are missed during extraction.
  </Accordion>
</AccordionGroup>

* [Lead Enrichment](/use-cases/lead-enrichment) - Enrich B2B e-commerce leads
* [Competitive Intelligence](/use-cases/competitive-intelligence) - Track competitor strategies
* [Data Migration](/use-cases/data-migration) - Migrate between platforms

---

## Competitive Intelligence

**URL:** llms-txt#competitive-intelligence

**Contents:**
- Start with a Template
- How It Works
- What You Can Track
- FAQs
- Related Use Cases

Source: https://docs.firecrawl.dev/use-cases/competitive-intelligence

Monitor competitor websites and track changes in real-time

Business intelligence teams use Firecrawl to monitor competitors and get alerts on strategic changes.

## Start with a Template

<CardGroup cols={2}>
  <Card title="Firecrawl Observer" icon="github" href="https://github.com/mendableai/firecrawl-observer">
    Real-time website monitoring with intelligent alerts
  </Card>

<Card title="Fireplexity" icon="github" href="https://github.com/mendableai/fireplexity">
    Research and analyze competitor strategies with AI
  </Card>
</CardGroup>

<Note>
  **Choose from monitoring and research templates.** Track competitors and analyze their strategies.
</Note>

Stay ahead of the competition with automated monitoring. Track product launches, pricing changes, marketing campaigns, and strategic moves across competitor websites and online properties.

## What You Can Track

* **Products**: New launches, features, specs, pricing, documentation
* **Marketing**: Messaging changes, campaigns, case studies, testimonials
* **Business**: Job postings, partnerships, funding, press releases
* **Strategy**: Positioning, target markets, pricing approaches, go-to-market
* **Technical**: API changes, integrations, technology stack updates

<AccordionGroup>
  <Accordion title="How quickly can I detect changes?">
    Firecrawl extracts current page content whenever called. Build your own monitoring system to check competitors at intervals that match your needs - from hourly for critical updates to daily for routine tracking.
  </Accordion>

<Accordion title="Can I monitor competitors in different regions?">
    Yes, Firecrawl can access region-specific content. You can monitor different versions of competitor sites across multiple countries and languages.
  </Accordion>

<Accordion title="How do I avoid false positive alerts?">
    When building your monitoring system, implement filters to ignore minor changes like timestamps or dynamic content. Compare extracted data over time and use your own logic to determine what constitutes a meaningful change.
  </Accordion>

<Accordion title="Can I track competitor social media and PR activity?">
    Yes. Extract data from competitor press releases, blog posts, and public social media pages. Build systems to analyze announcement patterns, messaging changes, and campaign launches over time.
  </Accordion>

<Accordion title="How do I organize intelligence across multiple competitors?">
    Extract data from multiple competitor sites using Firecrawl's APIs. Build your own system to organize and compare this data - many users create databases with competitor profiles and custom dashboards for analysis.
  </Accordion>
</AccordionGroup>

* [Product & E-commerce](/use-cases/product-ecommerce) - Track competitor products
* [Investment & Finance](/use-cases/investment-finance) - Market intelligence
* [SEO Platforms](/use-cases/seo-platforms) - SERP competitor tracking

---

## Open Source vs Cloud

**URL:** llms-txt#open-source-vs-cloud

Source: https://docs.firecrawl.dev/contributing/open-source-or-cloud

Understand the differences between Firecrawl's open-source and cloud offerings

Firecrawl is open source available under the [AGPL-3.0 license](https://github.com/mendableai/firecrawl/blob/main/LICENSE).

To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.

Firecrawl Cloud is available at [firecrawl.dev](https://firecrawl.dev) and offers a range of features that are not available in the open source version:

<img src="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=763a6e92c8605d06294ed7ed45df85d0" alt="Firecrawl Cloud vs Open Source" data-og-width="2808" width="2808" data-og-height="856" height="856" data-path="images/open-source-cloud.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=280&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2e9112d82aec51ca204ceee026b6bad3 280w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=560&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=9fabc257f1caa297b1b8ec68fb13eddc 560w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=840&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=e766290156ea4226df484ee815f5036f 840w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=1100&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=ed02646081bce28427156ba1d8bf4fa2 1100w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=1650&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=41d72e1c116d48ebc0cfa1a3499b3e9e 1650w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=2500&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=0f6f34e97633cabdc17cbc28d7af2bb9 2500w" />

---

## ===== Required ENVS ======

**URL:** llms-txt#=====-required-envs-======

PORT=3002
HOST=0.0.0.0

---

## AI Platforms

**URL:** llms-txt#ai-platforms

**Contents:**
- Start with a Template
- How It Works
- Why AI Platforms Choose Firecrawl
  - Reduce Hallucinations with Real-Time Data
- Customer Stories
- FAQs
- Related Use Cases

Source: https://docs.firecrawl.dev/use-cases/ai-platforms

Power AI assistants and let customers build AI apps

AI platform builders and teams use Firecrawl to power knowledge bases, chatbots, and enable customers to build AI applications with web data.

## Start with a Template

<Card title="Firestarter" icon="github" href="https://github.com/mendableai/firestarter">
  Instant AI chatbots for websites with web knowledge integration
</Card>

<Note>
  **Get started with templates and examples.** Build AI-powered applications with web data.
</Note>

Transform websites into AI-ready data. Power chatbots with real-time web knowledge, build RAG systems with up-to-date documentation, and enable your users to connect their AI applications to web sources.

## Why AI Platforms Choose Firecrawl

### Reduce Hallucinations with Real-Time Data

Your AI assistants need current information, not outdated training data. Whether it's domain-specific knowledge, technical documentation, or industry-specific content, Firecrawl ensures your knowledge bases stay synchronized with the latest updates-reducing hallucinations and improving response accuracy.

<CardGroup cols={2}>
  <Card href="https://www.firecrawl.dev/blog/how-replit-uses-firecrawl-to-power-ai-agents">
    **Replit**

Learn how Replit leverages Firecrawl to keep Replit Agent up-to-date with the latest API documentation and web content.
  </Card>

<Card href="https://www.firecrawl.dev/blog/how-stack-ai-uses-firecrawl-to-power-ai-agents">
    **Stack AI**

Discover how Stack AI uses Firecrawl to seamlessly feed agentic AI workflows with high-quality web data.
  </Card>
</CardGroup>

<AccordionGroup>
  <Accordion title="How does Firecrawl integrate with AI development platforms?">
    Firecrawl provides simple APIs and SDKs that integrate directly into AI platforms. Whether you're building with LangChain, using no-code tools like n8n, or custom frameworks, Firecrawl delivers clean, structured web data ready for AI consumption.
  </Accordion>

<Accordion title="Can Firecrawl handle the scale required for AI training?">
    Yes. Firecrawl is designed for enterprise-scale data extraction, processing millions of pages for AI training datasets. Our infrastructure scales automatically to meet your needs.
  </Accordion>

<Accordion title="What data formats does Firecrawl provide for AI platforms?">
    Firecrawl delivers data in AI-friendly formats including clean markdown, structured JSON, raw HTML, extracted images, screenshots, and news content. This flexibility ensures compatibility with any AI platform's data ingestion requirements.
  </Accordion>

<Accordion title="How do I handle authentication for gated content?">
    Firecrawl supports authentication headers and cookies for accessing protected content. Configure your API requests with the necessary credentials to extract data from login-protected documentation, knowledge bases, or member-only sites.
  </Accordion>

<Accordion title="Can I use Firecrawl for real-time AI applications?">
    Yes! Our API supports real-time data extraction, enabling AI applications to access fresh web data on-demand. This is perfect for AI agents that need current information to make decisions.
  </Accordion>
</AccordionGroup>

* [Deep Research](/use-cases/deep-research) - Advanced research capabilities
* [Content Generation](/use-cases/content-generation) - AI-powered content creation
* [Developers & MCP](/use-cases/developers-mcp) - Developer integrations

---

## ===== Optional ENVS ======

**URL:** llms-txt#=====-optional-envs-======

**Contents:**
- === AI features (JSON format on scrape, /extract API) ===

## === AI features (JSON format on scrape, /extract API) ===

---

## Build

**URL:** llms-txt#build

---

## Testing & Debugging

**URL:** llms-txt#testing-&-debugging

**Contents:**
- Local Development
  - Exposing Local Servers

Source: https://docs.firecrawl.dev/webhooks/testing

Tools and techniques for developing and debugging webhooks

This page covers tools and techniques for testing webhook integrations during development and debugging issues in production.

### Exposing Local Servers

Since webhooks need to reach your server from the internet, you'll need to expose your local development server publicly.

#### Using Cloudflare Tunnels

[Cloudflare Tunnels](https://github.com/cloudflare/cloudflared/releases) provide a free way to securely expose your local development server to the internet without requiring account registration or opening firewall ports:

```bash  theme={null}

---

## PROXY_USERNAME=

**URL:** llms-txt#proxy_username=

---

## This is now autoconfigured by the docker-compose.yaml. You shouldn't need to set it.

**URL:** llms-txt#this-is-now-autoconfigured-by-the-docker-compose.yaml.-you-shouldn't-need-to-set-it.

---

## Run tests

**URL:** llms-txt#run-tests

**Contents:**
  - Contributing
  - Thanks to contributors
- License

1. Fork the repository
2. Create your feature branch
3. Run tests: `npm test`
4. Submit a pull request

### Thanks to contributors

Thanks to [@vrknetha](https://github.com/vrknetha), [@cawstudios](https://caw.tech) for the initial implementation!

Thanks to MCP.so and Klavis AI for hosting and [@gstarwd](https://github.com/gstarwd), [@xiangkaiz](https://github.com/xiangkaiz) and [@zihaolin96](https://github.com/zihaolin96) for integrating our server.

MIT License - see LICENSE file for details

---

## Default: 0.8 (80%)

**URL:** llms-txt#default:-0.8-(80%)

---

## Maximum CPU usage threshold (0.0-1.0). Worker will reject new jobs when CPU usage exceeds this value.

**URL:** llms-txt#maximum-cpu-usage-threshold-(0.0-1.0).-worker-will-reject-new-jobs-when-cpu-usage-exceeds-this-value.

---

## Create a research agent

**URL:** llms-txt#create-a-research-agent

research_agent = Agent(
    model="gemini-2.5-pro",
    name="research_agent",
    description='An AI agent that researches topics by scraping and analyzing web content',
    instruction='''You are a research assistant. When given a topic or question:
    1. Use the search tool to find relevant websites
    2. Scrape the most relevant pages for detailed information
    3. Extract structured data when needed
    4. Provide comprehensive, well-sourced answers''',
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=f"https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp",
            ),
        )
    ],
)

---

## Optional credit monitoring

**URL:** llms-txt#optional-credit-monitoring

export FIRECRAWL_CREDIT_WARNING_THRESHOLD=2000    # Warning at 2000 credits
export FIRECRAWL_CREDIT_CRITICAL_THRESHOLD=500    # Critical at 500 credits
bash  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
For self-hosted instance:
```

---

## .env

**URL:** llms-txt#.env

---

## MODEL_EMBEDDING_NAME=nomic-embed-text

**URL:** llms-txt#model_embedding_name=nomic-embed-text

---

## Overview

**URL:** llms-txt#overview

**Contents:**
- Supported Operations
- Quick Setup
  - Configuration Options
- Basic Usage Examples
  - Crawl with Webhook
  - Batch Scrape with Webhook
- Handling Webhooks
  - Best Practices

Source: https://docs.firecrawl.dev/webhooks/overview

Real-time notifications for your Firecrawl operations

Webhooks allow you to receive real-time notifications about your Firecrawl operations as they progress. Instead of polling for status updates, Firecrawl will automatically send HTTP POST requests to your specified endpoint when events occur.

## Supported Operations

Webhooks are supported for most major Firecrawl operations:

* **Crawl** - Get notified as pages are crawled and when crawls complete
* **Batch scrape** - Receive updates for each URL scraped in a batch
* **Extract** - Receive updates when extract jobs start, complete, or fail

Configure webhooks by adding a `webhook` object to your request:

### Configuration Options

| Field      | Type   | Required | Description                                   |
| ---------- | ------ | -------- | --------------------------------------------- |
| `url`      | string | ✅        | Your webhook endpoint URL                     |
| `headers`  | object | ❌        | Custom headers to include in webhook requests |
| `metadata` | object | ❌        | Custom data included in all webhook payloads  |
| `events`   | array  | ❌        | Event types to receive (default: all events)  |

## Basic Usage Examples

### Crawl with Webhook

### Batch Scrape with Webhook

Here's a simple example of handling webhooks in your application:

1. **Respond quickly** – Always return a `2xx` status code within 30 seconds
2. **Process asynchronously** – For heavy processing, queue the work and respond immediately
3. **Validate authenticity** – Always verify the webhook signature (see [Security](/webhooks/security))

**Examples:**

Example 1 (unknown):
```unknown
### Configuration Options

| Field      | Type   | Required | Description                                   |
| ---------- | ------ | -------- | --------------------------------------------- |
| `url`      | string | ✅        | Your webhook endpoint URL                     |
| `headers`  | object | ❌        | Custom headers to include in webhook requests |
| `metadata` | object | ❌        | Custom data included in all webhook payloads  |
| `events`   | array  | ❌        | Event types to receive (default: all events)  |

## Basic Usage Examples

### Crawl with Webhook
```

Example 2 (unknown):
```unknown
### Batch Scrape with Webhook
```

Example 3 (unknown):
```unknown
## Handling Webhooks

Here's a simple example of handling webhooks in your application:

<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## Extract

**URL:** llms-txt#extract

**Contents:**
- Using `/extract`
  - Example Usage
  - Response (sdks)
- Job status and completion
  - Possible States
- Extracting without a Schema
- Improving Results with Web Search
  - Example Response with Web Search
- Extracting without URLs
- Known Limitations (Beta)

Source: https://docs.firecrawl.dev/features/extract

Extract structured data from pages using LLMs

The `/extract` endpoint simplifies collecting structured data from any number of URLs or entire domains. Provide a list of URLs, optionally with wildcards (e.g., `example.com/*`), and a prompt or schema describing the information you want. Firecrawl handles the details of crawling, parsing, and collating large or small datasets.

<Info>We've simplified billing so that Extract now uses credits, just like all of the other endpoints. Each credit is worth 15 tokens.</Info>

You can extract structured data from one or multiple URLs, including wildcards:

* **Single Page**\
  Example: `https://firecrawl.dev/some-page`
* **Multiple Pages / Full Domain**\
  Example: `https://firecrawl.dev/*`

When you use `/*`, Firecrawl will automatically crawl and parse all URLs it can discover in that domain, then extract the requested data. This feature is experimental; email [help@firecrawl.com](mailto:help@firecrawl.com) if you have issues.

* **urls**: An array of one or more URLs. Supports wildcards (`/*`) for broader crawling.
* **prompt** (Optional unless no schema): A natural language prompt describing the data you want or specifying how you want that data structured.
* **schema** (Optional unless no prompt): A more rigid structure if you already know the JSON layout.
* **enableWebSearch** (Optional): When `true`, extraction can follow links outside the specified domain.

See [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/extract) for more details.

## Job status and completion

When you submit an extraction job—either directly via the API or through the starter methods—you'll receive a Job ID. You can use this ID to:

* Get Job Status: Send a request to the /extract/{ID} endpoint to see if the job is still running or has finished.
* Wait for results: If you use the default `extract` method (Python/Node), the SDK waits and returns final results.
* Start then poll: If you use the start methods—`start_extract` (Python) or `startExtract` (Node)—the SDK returns a Job ID immediately. Use `get_extract_status` (Python) or `getExtractStatus` (Node) to check progress.

<Note>
  This endpoint only works for jobs in progress or recently completed (within 24
  hours).
</Note>

Below are code examples for checking an extraction job's status using Python, Node.js, and cURL:

* **completed**: The extraction finished successfully.
* **processing**: Firecrawl is still processing your request.
* **failed**: An error occurred; data was not fully extracted.
* **cancelled**: The job was cancelled by the user.

#### Completed Example

## Extracting without a Schema

If you prefer not to define a strict structure, you can simply provide a `prompt`. The underlying model will choose a structure for you, which can be useful for more exploratory or flexible requests.

## Improving Results with Web Search

Setting `enableWebSearch = true` in your request will expand the crawl beyond the provided URL set. This can capture supporting or related information from linked pages.

Here's an example that extracts information about dash cams, enriching the results with data from related pages:

### Example Response with Web Search

The response includes additional context gathered from related pages, providing more comprehensive and accurate information.

## Extracting without URLs

The `/extract` endpoint now supports extracting structured data using a prompt without needing specific URLs. This is useful for research or when exact URLs are unknown. Currently in Alpha.

## Known Limitations (Beta)

1. **Large-Scale Site Coverage**\
   Full coverage of massive sites (e.g., "all products on Amazon") in a single request is not yet supported.

2. **Complex Logical Queries**\
   Requests like "find every post from 2025" may not reliably return all expected data. More advanced query capabilities are in progress.

3. **Occasional Inconsistencies**\
   Results might differ across runs, particularly for very large or dynamic sites. Usually it captures core details, but some variation is possible.

4. **Beta State**\
   Since `/extract` is still in Beta, features and performance will continue to evolve. We welcome bug reports and feedback to help us improve.

FIRE-1 is an AI agent that enhances Firecrawl's scraping capabilities. It can controls browser actions and navigates complex website structures to enable comprehensive data extraction beyond traditional scraping methods.

You can leverage the FIRE-1 agent with the `/extract` endpoint for complex extraction tasks that require navigation across multiple pages or interaction with elements.

> FIRE-1 is already live and available under preview.

## Billing and Usage Tracking

We've simplified billing so that Extract now uses credits, just like all of the other endpoints. Each credit is worth 15 tokens.

You can monitor Extract usage via the [dashboard](https://www.firecrawl.dev/app/extract).

Have feedback or need help? Email [help@firecrawl.com](mailto:help@firecrawl.com).

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

**Key Parameters:**

* **urls**: An array of one or more URLs. Supports wildcards (`/*`) for broader crawling.
* **prompt** (Optional unless no schema): A natural language prompt describing the data you want or specifying how you want that data structured.
* **schema** (Optional unless no prompt): A more rigid structure if you already know the JSON layout.
* **enableWebSearch** (Optional): When `true`, extraction can follow links outside the specified domain.

See [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/extract) for more details.

### Response (sdks)
```

Example 4 (unknown):
```unknown
## Job status and completion

When you submit an extraction job—either directly via the API or through the starter methods—you'll receive a Job ID. You can use this ID to:

* Get Job Status: Send a request to the /extract/{ID} endpoint to see if the job is still running or has finished.
* Wait for results: If you use the default `extract` method (Python/Node), the SDK waits and returns final results.
* Start then poll: If you use the start methods—`start_extract` (Python) or `startExtract` (Node)—the SDK returns a Job ID immediately. Use `get_extract_status` (Python) or `getExtractStatus` (Node) to check progress.

<Note>
  This endpoint only works for jobs in progress or recently completed (within 24
  hours).
</Note>

Below are code examples for checking an extraction job's status using Python, Node.js, and cURL:

<CodeGroup>
```

---

## SUPABASE_SERVICE_TOKEN=

**URL:** llms-txt#supabase_service_token=

---
