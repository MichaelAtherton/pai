# Advanced Scraping Guide
Source: https://docs.firecrawl.dev/advanced-scraping-guide

Learn how to improve your Firecrawl scraping with advanced options.

This guide will walk you through the different endpoints of Firecrawl and how to use them fully with all its parameters.

## Basic scraping with Firecrawl

To scrape a single page and get clean markdown content, you can use the `/scrape` endpoint.

<CodeGroup>
  ```python Python theme={null}
  # pip install firecrawl-py

  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  doc = firecrawl.scrape("https://firecrawl.dev")

  print(doc.markdown)
  ```

  ```JavaScript JavaScript theme={null}
  // npm install @mendable/firecrawl-js

  import { Firecrawl } from 'firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

  const doc = await firecrawl.scrape('https://firecrawl.dev');

  console.log(doc.markdown);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer fc-YOUR-API-KEY' \
      -d '{
        "url": "https://docs.firecrawl.dev"
      }'
  ```
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
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key='fc-YOUR-API-KEY')

  doc = firecrawl.scrape('https://example.com', {
    actions: [
      { type: 'wait', milliseconds: 1000 },
      { type: 'click', selector: '#accept' },
      { type: 'scroll', direction: 'down' },
      { type: 'write', selector: '#q', text: 'firecrawl' },
      { type: 'press', key: 'Enter' }
    ],
    formats: ['markdown']
  })

  print(doc.markdown)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

  const doc = await firecrawl.scrape('https://example.com', {
    actions: [
      { type: 'wait', milliseconds: 1000 },
      { type: 'click', selector: '#accept' },
      { type: 'scroll', direction: 'down' },
      { type: 'write', selector: '#q', text: 'firecrawl' },
      { type: 'press', key: 'Enter' }
    ],
    formats: ['markdown']
  });

  console.log(doc.markdown);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://example.com",
      "actions": [
        { "type": "wait", "milliseconds": 1000 },
        { "type": "click", "selector": "#accept" },
        { "type": "scroll", "direction": "down" },
        { "type": "write", "selector": "#q", "text": "firecrawl" },
        { "type": "press", "key": "Enter" }
      ],
      "formats": ["markdown"]
    }'
  ```
</CodeGroup>

### Example Usage

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/scrape \
    -H '
    Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "formats": [
        "markdown",
        "links",
        "html",
        "rawHtml",
        { "type": "screenshot", "fullPage": true, "quality": 80 }
      ],
      "includeTags": ["h1", "p", "a", ".main-content"],
      "excludeTags": ["#ad", "#footer"],
      "onlyMainContent": false,
      "waitFor": 1000,
      "timeout": 15000,
      "parsers": ["pdf"]
    }'
```

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

```bash  theme={null}
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://firecrawl.dev",
    "formats": [{
      "type": "json",
      "prompt": "Extract the features of the product",
      "schema": {"type": "object", "properties": {"features": {"type": "object"}}, "required": ["features"]}
    }]
  }'
```

## Extract endpoint

Use the dedicated extract job API when you want asynchronous extraction with status polling.

<CodeGroup>
  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

  // Start extract job
  const started = await firecrawl.startExtract({
    urls: ['https://docs.firecrawl.dev'],
    prompt: 'Extract title',
    schema: { type: 'object', properties: { title: { type: 'string' } }, required: ['title'] }
  });

  // Poll status
  const status = await firecrawl.getExtractStatus(started.id);
  console.log(status.status, status.data);
  ```

  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key='fc-YOUR-API-KEY')

  started = firecrawl.start_extract(
      urls=["https://docs.firecrawl.dev"],
      prompt="Extract title",
      schema={"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"]}
  )
  status = firecrawl.get_extract_status(started.id)
  print(status.get("status"), status.get("data"))
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/extract \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "urls": ["https://docs.firecrawl.dev"],
      "prompt": "Extract title",
      "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"]}
    }'
  ```
</CodeGroup>

## Crawling multiple pages

To crawl multiple pages, use the `/v2/crawl` endpoint.

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'
```

Returns an id

```json  theme={null}
{ "id": "1234-5678-9101" }
```

### Check Crawl Job

Used to check the status of a crawl job and get its result.

```bash cURL theme={null}
curl -X GET https://api.firecrawl.dev/v2/crawl/1234-5678-9101 \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY'
```

#### Pagination/Next URL

If the content is larger than 10MB or if the crawl job is still running, the response may include a `next` parameter, a URL to the next page of results.

### Crawl prompt and params preview

You can provide a natural-language `prompt` to let Firecrawl derive crawl settings. Preview them first:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/crawl/params-preview \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://docs.firecrawl.dev",
    "prompt": "Extract docs and blog"
  }'
```

### Crawler options

When using the `/v2/crawl` endpoint, you can customize the crawling behavior with:

#### includePaths

* **Type**: `array`
* **Description**: Regex patterns to include.
* **Example**: `["^/blog/.*$", "^/docs/.*$"]`

#### excludePaths

* **Type**: `array`
* **Description**: Regex patterns to exclude.
* **Example**: `["^/admin/.*$", "^/private/.*$"]`

#### maxDiscoveryDepth

* **Type**: `integer`
* **Description**: Max discovery depth for finding new URLs.

#### limit

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

#### allowSubdomains

* **Type**: `boolean`
* **Description**: Follow subdomains of the main domain.
* **Default**: `false`

#### delay

* **Type**: `number`
* **Description**: Delay in seconds between scrapes.
* **Default**: `undefined`

#### scrapeOptions

* **Type**: `object`
* **Description**: Options for the scraper (see Formats above).
* **Example**: `{ "formats": ["markdown", "links", {"type": "screenshot", "fullPage": true}], "includeTags": ["h1", "p", "a", ".main-content"], "excludeTags": ["#ad", "#footer"], "onlyMainContent": false, "waitFor": 1000, "timeout": 15000}`
* **Defaults**: `formats: ["markdown"]`, caching enabled by default (maxAge \~ 2 days)

### Example Usage

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "includePaths": ["^/blog/.*$", "^/docs/.*$"],
      "excludePaths": ["^/admin/.*$", "^/private/.*$"],
      "maxDiscoveryDepth": 2,
      "limit": 1000
    }'
```

## Mapping website links

The `/v2/map` endpoint identifies URLs related to a given website.

### Usage

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/map \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'
```

### Map Options

#### search

* **Type**: `string`
* **Description**: Filter links containing text.

#### limit

* **Type**: `integer`
* **Description**: Maximum number of links to return.
* **Default**: `100`

#### sitemap

* **Type**: `"only" | "include" | "skip"`
* **Description**: Control sitemap usage during mapping.
* **Default**: `"include"`

#### includeSubdomains

* **Type**: `boolean`
* **Description**: Include subdomains of the website.
* **Default**: `true`

Here is the API Reference for it: [Map Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/map)

Thanks for reading!


# Batch Scrape
Source: https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape

v2-openapi POST /batch/scrape



# Cancel Batch Scrape
Source: https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-delete

v2-openapi DELETE /batch/scrape/{id}



# Get Batch Scrape Status
Source: https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get

v2-openapi GET /batch/scrape/{id}



# Get Batch Scrape Errors
Source: https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-get-errors

v2-openapi GET /batch/scrape/{id}/errors



# Get Active Crawls
Source: https://docs.firecrawl.dev/api-reference/endpoint/crawl-active

v2-openapi GET /crawl/active



# Cancel Crawl
Source: https://docs.firecrawl.dev/api-reference/endpoint/crawl-delete

v2-openapi DELETE /crawl/{id}



# Get Crawl Status
Source: https://docs.firecrawl.dev/api-reference/endpoint/crawl-get

v2-openapi GET /crawl/{id}



# Get Crawl Errors
Source: https://docs.firecrawl.dev/api-reference/endpoint/crawl-get-errors

v2-openapi GET /crawl/{id}/errors



# Crawl Params Preview
Source: https://docs.firecrawl.dev/api-reference/endpoint/crawl-params-preview

v2-openapi POST /crawl/params-preview

## What's New in v2

### Crawl Params Preview

```json  theme={null}
{
  "url": "https://example.com",
  "prompt": "Crawl the entire website but exclude /admin and /api"
}   
```

### Response

```json  theme={null}
{
  "url": "https://example.com",
  "prompt": "Crawl the entire website",
  "crawlEntireDomain": true,
  "excludePaths": ["/admin/.*", "/api/.*"],
  "sitemap": "include"
}
```


# Crawl
Source: https://docs.firecrawl.dev/api-reference/endpoint/crawl-post

v2-openapi POST /crawl

## What's New in v2

### Tell crawl what you want

Describe what to crawl in plain English:

```json  theme={null}
{
  "url": "https://example.com",
  "prompt": "Only crawl blog posts and docs, skip marketing pages"
}
```

This will map the prompt to a set of crawler settings to perform the crawl.

### Improved Sitemap Control

In v1, sitemap usage was a boolean. In v2, the `sitemap` option lets you choose:

* `"include"` (default): Use the sitemap and also discover other pages.
* `"skip"`: Ignore the sitemap entirely.

### New Crawling Options

* `crawlEntireDomain` - Crawl whole domain, not just child pages
* `maxDiscoveryDepth` - Control crawl depth (replaces `maxDepth`)

```json  theme={null}
{
  "url": "https://example.com/features",
  "crawlEntireDomain": true,
  "maxDiscoveryDepth": 2,
  "sitemap": "include"
}
```


# Credit Usage
Source: https://docs.firecrawl.dev/api-reference/endpoint/credit-usage

v2-openapi GET /team/credit-usage



# Historical Credit Usage
Source: https://docs.firecrawl.dev/api-reference/endpoint/credit-usage-historical

v2-openapi GET /team/credit-usage/historical

Returns historical credit usage on a month-by-month basis. The endpoint can also breaks usage down by API key optionally.


# Extract
Source: https://docs.firecrawl.dev/api-reference/endpoint/extract

v2-openapi POST /extract



# Get Extract Status
Source: https://docs.firecrawl.dev/api-reference/endpoint/extract-get

v2-openapi GET /extract/{id}



# Map
Source: https://docs.firecrawl.dev/api-reference/endpoint/map

v2-openapi POST /map

## What's New in v2

### Better Sitemap Control

Three ways to handle sitemaps:

* `"include"` - Use sitemap + find other pages (default)
* `"skip"` - Ignore sitemap completely
* `"only"` - Only return sitemap URLs

```json  theme={null}
{
  "url": "https://example.com",
  "sitemap": "only"
}
```

### Response format changed

We now return the links in the `links` array of objects with enhanced metadata.

```json  theme={null}
{
  "url": "https://example.com",
  "links": [
    {
      "url": "https://example.com/page1",
      "title": "Page 1",
      "description": "Page 1 description"
    }
  ]
}
```


# Queue Status
Source: https://docs.firecrawl.dev/api-reference/endpoint/queue-status

v2-openapi GET /team/queue-status

Metrics about your team's scrape queue.


# Scrape
Source: https://docs.firecrawl.dev/api-reference/endpoint/scrape

v2-openapi POST /scrape

## What's New in v2

### New Formats

* `"summary"` - Get a concise summary of the page content
* JSON extraction now uses object format: `{ type: "json", prompt, schema }`
* Screenshot format now uses object format: `{ type: "screenshot", fullPage, quality, viewport }`
* `"images"` - Extract all image URLs from the page
* `"branding"` - Extract brand identity including colors, fonts, typography, spacing, and UI components

### Key Improvements

* **Faster by default**: Requests are cached with `maxAge` defaulting to 2 days
* **Sensible defaults**: `blockAds`, `skipTlsVerification`, and `removeBase64Images` are enabled by default
* **Enhanced screenshot options**: Full control over screenshot parameters using object format


# Search
Source: https://docs.firecrawl.dev/api-reference/endpoint/search

v2-openapi POST /search

## What's New in v2

### Search Multiple Sources

Search web, images, and news at once:

```json  theme={null}
{
  "query": "firecrawl web scraping",
  "sources": [ "web", "images", "news" ]
}
```

### Response Format Changed

v1: flat list of results. v2: organized by source type:

```json  theme={null}
{
  "success": true,
  "data": {
    "web": [/* web results */],
    "images": [/* image results */],
    "news": [/* news results */]
  }
}
```

### New Features

* Filter by time ranges ("past week", "past month")
* Target specific countries/regions
* Category Filtering: Search within GitHub repositories or research websites
* Results capped at 500 during alpha

The search endpoint combines web search (SERP) with Firecrawl's scraping capabilities to return full page content for any query.

Include `scrapeOptions` with `formats: [{"type": "markdown"}]` to get complete markdown content for each search result otherwise you will default to getting the SERP results (url, title, description). You can also use other formats like `{"type": "summary"}` for condensed content.

## Supported query operators

We support a variety of query operators that allow you to filter your searches better.

| Operator      | Functionality                                                             | Examples                          |
| ------------- | ------------------------------------------------------------------------- | --------------------------------- |
| `""`          | Non-fuzzy matches a string of text                                        | `"Firecrawl"`                     |
| `-`           | Excludes certain keywords or negates other operators                      | `-bad`, `-site:firecrawl.dev`     |
| `site:`       | Only returns results from a specified website                             | `site:firecrawl.dev`              |
| `inurl:`      | Only returns results that include a word in the URL                       | `inurl:firecrawl`                 |
| `allinurl:`   | Only returns results that include multiple words in the URL               | `allinurl:git firecrawl`          |
| `intitle:`    | Only returns results that include a word in the title of the page         | `intitle:Firecrawl`               |
| `allintitle:` | Only returns results that include multiple words in the title of the page | `allintitle:firecrawl playground` |
| `related:`    | Only returns results that are related to a specific domain                | `related:firecrawl.dev`           |
| `imagesize:`  | Only returns images with exact dimensions                                 | `imagesize:1920x1080`             |
| `larger:`     | Only returns images larger than specified dimensions                      | `larger:1920x1080`                |

## Location Parameter

Use the `location` parameter to get geo-targeted search results. Format: `"string"`. Examples: `"Germany"`, `"San Francisco,California,United States"`.

See the [complete list of supported locations](https://firecrawl.dev/search_locations.json) for all available countries and languages.

## Country Parameter

Use the `country` parameter to specify the country for search results using ISO country codes. Default: `"US"`.

Examples: `"US"`, `"DE"`, `"FR"`, `"JP"`, `"UK"`, `"CA"`.

```json  theme={null}
{
  "query": "restaurants",
  "country": "DE"
}
```

## Categories Parameter

Filter search results by specific categories using the `categories` parameter:

* **`github`**: Search within GitHub repositories, code, issues, and documentation
* **`research`**: Search academic and research websites (arXiv, Nature, IEEE, PubMed, etc.)
* **`pdf`**: Search for PDFs

### Example Usage

```json  theme={null}
{
  "query": "machine learning",
  "categories": ["github", "research"],
  "limit": 10
}
```

### Category Response

Each result includes a `category` field indicating its source:

```json  theme={null}
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/ml-project",
        "title": "Machine Learning Project",
        "description": "Implementation of ML algorithms",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "ML Research Paper",
        "description": "Latest advances in machine learning",
        "category": "research"
      }
    ]
  }
}
```

## Time-Based Search

Use the `tbs` parameter to filter results by time periods, including custom date ranges. See the [Search Feature documentation](https://docs.firecrawl.dev/features/search#time-based-search) for detailed examples and supported formats.


# Token Usage
Source: https://docs.firecrawl.dev/api-reference/endpoint/token-usage

v2-openapi GET /team/token-usage

<Info>We've simplified billing so that Extract now uses credits, just like all of the other endpoints. Each credit is worth 15 tokens. Reported token usage now includes usage from all endpoints.</Info>


# Historical Token Usage
Source: https://docs.firecrawl.dev/api-reference/endpoint/token-usage-historical

v2-openapi GET /team/token-usage/historical

Returns historical token usage on a month-by-month basis. The endpoint can also breaks usage down by API key optionally.

<Info>We've simplified billing so that Extract now uses credits, just like all of the other endpoints. Each credit is worth 15 tokens. Reported token usage now includes usage from all endpoints.</Info>


# Introduction
Source: https://docs.firecrawl.dev/api-reference/v2-introduction

Firecrawl API Reference (v2)

## Features

<CardGroup cols={3}>
  <Card title="Scrape" icon="markdown" href="/api-reference/endpoint/scrape" color="FF713C">
    Extract content from any webpage in markdown or json format.
  </Card>

  <Card title="Crawl" icon="spider" href="/api-reference/endpoint/crawl-post" color="FF713C">
    Crawl entire websites, extract their content and metadata.
  </Card>

  <Card title="Map" icon="map" href="/api-reference/endpoint/map" color="FF713C">
    Get a complete list of URLs from any website quickly and reliably.
  </Card>

  <Card title="Search" icon="magnifying-glass" href="/api-reference/endpoint/search" color="FF713C">
    Search the web and get full page content in any format.
  </Card>
</CardGroup>

## Agentic Features

<CardGroup cols={3}>
  <Card title="Extract" icon="barcode-read" href="/api-reference/endpoint/extract" color="FF713C">
    Extract structured data from entire webpages using natural language.
  </Card>
</CardGroup>

## Base URL

All requests contain the following base URL:

```bash  theme={null}
https://api.firecrawl.dev 
```

## Authentication

For authentication, it's required to include an Authorization header. The header should contain `Bearer fc-123456789`, where `fc-123456789` represents your API Key.

```bash  theme={null}
Authorization: Bearer fc-123456789
```

​

## Response codes

Firecrawl employs conventional HTTP status codes to signify the outcome of your requests.

Typically, 2xx HTTP status codes denote success, 4xx codes represent failures related to the user, and 5xx codes signal infrastructure problems.

| Status | Description                                  |
| ------ | -------------------------------------------- |
| 200    | Request was successful.                      |
| 400    | Verify the correctness of the parameters.    |
| 401    | The API key was not provided.                |
| 402    | Payment required                             |
| 404    | The requested resource could not be located. |
| 429    | The rate limit has been surpassed.           |
| 5xx    | Signifies a server error with Firecrawl.     |

Refer to the Error Codes section for a detailed explanation of all potential API errors.

​

## Rate limit

The Firecrawl API has a rate limit to ensure the stability and reliability of the service. The rate limit is applied to all endpoints and is based on the number of requests made within a specific time frame.

When you exceed the rate limit, you will receive a 429 response code.


# Running locally
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

```bash  theme={null}
docker build -t nuq-postgres .
```

and then run:

```bash  theme={null}
docker run --name nuqdb \          
  -e POSTGRES_PASSWORD=postgres \
  -p 5433:5432 \
  -v nuq-data:/var/lib/postgresql/data \
  -d nuq-postgres
```

Set environment variables in a .env in the /apps/api/ directory you can copy over the template in .env.example.

To start, we wont set up authentication, or any optional sub services (pdf parsing, JS blocking support, AI features )

.env:

```
# ===== Required ENVS ======
NUM_WORKERS_PER_QUEUE=8
PORT=3002
HOST=0.0.0.0
REDIS_URL=redis://localhost:6379
REDIS_RATE_LIMIT_URL=redis://localhost:6379

## To turn on DB authentication, you need to set up supabase.
USE_DB_AUTHENTICATION=false

## Using the PostgreSQL for queuing -- change if credentials, host, or DB is different
NUQ_DATABASE_URL=postgres://postgres:postgres@localhost:5433/postgres

# ===== Optional ENVS ======

# Supabase Setup (used to support DB authentication, advanced logging, etc.)
SUPABASE_ANON_TOKEN=
SUPABASE_URL=
SUPABASE_SERVICE_TOKEN=

# Other Optionals
TEST_API_KEY= # use if you've set up authentication and want to test with a real API key
OPENAI_API_KEY= # add for LLM dependednt features (image alt generation, etc.)
BULL_AUTH_KEY= @
PLAYWRIGHT_MICROSERVICE_URL=  # set if you'd like to run a playwright fallback
LLAMAPARSE_API_KEY= #Set if you have a llamaparse key you'd like to use to parse pdfs
SLACK_WEBHOOK_URL= # set if you'd like to send slack server health status messages
POSTHOG_API_KEY= # set if you'd like to send posthog events like job logs
POSTHOG_HOST= # set if you'd like to send posthog events like job logs


```

### Installing dependencies

First, install the dependencies using pnpm.

```bash  theme={null}
# cd apps/api # to make sure you're in the right folder
pnpm install # make sure you have pnpm version 9+!
```

### Running the project

You're going to need to open 3 terminals.

### Terminal 1 - setting up redis

Run the command anywhere within your project

```bash  theme={null}
redis-server
```

### Terminal 2 - setting up the service

Now, navigate to the apps/api/ directory and run:

```bash  theme={null}
pnpm start
# if you are going to use the [llm-extract feature](https://github.com/firecrawl/firecrawl/pull/586/), you should also export OPENAI_API_KEY=sk-______
```

This will start the workers who are responsible for processing crawl jobs.

### Terminal 3 - sending our first request.

Alright: now let’s send our first request.

```curl  theme={null}
curl -X GET http://localhost:3002/test
```

This should return the response Hello, world!

If you’d like to test the crawl endpoint, you can run this

```curl  theme={null}
curl -X POST http://localhost:3002/v1/crawl \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://mendable.ai"
    }'
```

### Alternative: Using Docker Compose

For a simpler setup, you can use Docker Compose to run all services:

1. Prerequisites: Make sure you have Docker and Docker Compose installed
2. Copy the `.env.example` file to `.env` in the `/apps/api/` directory and configure as needed
3. From the root directory, run:

```bash  theme={null}
docker compose up
```

This will start Redis, the API server, and workers automatically in the correct configuration.

## Tests:

The best way to do this is run the test with `npm run test:snips`.


# Open Source vs Cloud
Source: https://docs.firecrawl.dev/contributing/open-source-or-cloud

Understand the differences between Firecrawl's open-source and cloud offerings

Firecrawl is open source available under the [AGPL-3.0 license](https://github.com/mendableai/firecrawl/blob/main/LICENSE).

To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.

Firecrawl Cloud is available at [firecrawl.dev](https://firecrawl.dev) and offers a range of features that are not available in the open source version:

<img src="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=763a6e92c8605d06294ed7ed45df85d0" alt="Firecrawl Cloud vs Open Source" data-og-width="2808" width="2808" data-og-height="856" height="856" data-path="images/open-source-cloud.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=280&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2e9112d82aec51ca204ceee026b6bad3 280w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=560&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=9fabc257f1caa297b1b8ec68fb13eddc 560w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=840&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=e766290156ea4226df484ee815f5036f 840w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=1100&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=ed02646081bce28427156ba1d8bf4fa2 1100w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=1650&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=41d72e1c116d48ebc0cfa1a3499b3e9e 1650w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=2500&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=0f6f34e97633cabdc17cbc28d7af2bb9 2500w" />


# Self-hosting
Source: https://docs.firecrawl.dev/contributing/self-host

Learn how to self-host Firecrawl to run on your own and contribute to the project.

#### Contributor?

Welcome to [Firecrawl](https://firecrawl.dev) 🔥! Here are some instructions on how to get the project locally so you can run it on your own and contribute.

If you're contributing, note that the process is similar to other open-source repos, i.e., fork Firecrawl, make changes, run tests, PR.

If you have any questions or would like help getting on board, join our Discord community [here](https://discord.gg/gSmWdAkdwd) for more information or submit an issue on Github [here](https://github.com/mendableai/firecrawl/issues/new/choose)!

## Self-hosting Firecrawl

Refer to [SELF\_HOST.md](https://github.com/mendableai/firecrawl/blob/main/SELF_HOST.md) for instructions on how to run it locally.

## Why?

Self-hosting Firecrawl is particularly beneficial for organizations with stringent security policies that require data to remain within controlled environments. Here are some key reasons to consider self-hosting:

* **Enhanced Security and Compliance:** By self-hosting, you ensure that all data handling and processing complies with internal and external regulations, keeping sensitive information within your secure infrastructure. Note that Firecrawl is a Mendable product and relies on SOC2 Type2 certification, which means that the platform adheres to high industry standards for managing data security.
* **Customizable Services:** Self-hosting allows you to tailor the services, such as the Playwright service, to meet specific needs or handle particular use cases that may not be supported by the standard cloud offering.
* **Learning and Community Contribution:** By setting up and maintaining your own instance, you gain a deeper understanding of how Firecrawl works, which can also lead to more meaningful contributions to the project.

### Considerations

However, there are some limitations and additional responsibilities to be aware of:

1. **Limited Access to Fire-engine:** Currently, self-hosted instances of Firecrawl do not have access to Fire-engine, which includes advanced features for handling IP blocks, robot detection mechanisms, and more. This means that while you can manage basic scraping tasks, more complex scenarios might require additional configuration or might not be supported.
2. **Manual Configuration Required:** If you need to use scraping methods beyond the basic fetch and Playwright options, you will need to manually configure these in the `.env` file. This requires a deeper understanding of the technologies and might involve more setup time.

Self-hosting Firecrawl is ideal for those who need full control over their scraping and data processing environments but comes with the trade-off of additional maintenance and configuration efforts.

## Steps

1. First, start by installing the dependencies

* Docker [instructions](https://docs.docker.com/get-docker/)

2. Set environment variables

Create an `.env` in the root directory you can copy over the template in `apps/api/.env.example`

To start, we wont set up authentication, or any optional sub services (pdf parsing, JS blocking support, AI features)

```
# .env

# ===== Required ENVS ======
PORT=3002
HOST=0.0.0.0

# Note: PORT is used by both the main API server and worker liveness check endpoint

# To turn on DB authentication, you need to set up Supabase.
USE_DB_AUTHENTICATION=false

# ===== Optional ENVS ======

## === AI features (JSON format on scrape, /extract API) ===
# Provide your OpenAI API key here to enable AI features
# OPENAI_API_KEY=

# Experimental: Use Ollama
# OLLAMA_BASE_URL=http://localhost:11434/api
# MODEL_NAME=deepseek-r1:7b
# MODEL_EMBEDDING_NAME=nomic-embed-text

# Experimental: Use any OpenAI-compatible API
# OPENAI_BASE_URL=https://example.com/v1
# OPENAI_API_KEY=

## === Proxy ===
# PROXY_SERVER can be a full URL (e.g. http://0.1.2.3:1234) or just an IP and port combo (e.g. 0.1.2.3:1234)
# Do not uncomment PROXY_USERNAME and PROXY_PASSWORD if your proxy is unauthenticated
# PROXY_SERVER=
# PROXY_USERNAME=
# PROXY_PASSWORD=

## === /search API ===
# By default, the /search API will use Google search.

# You can specify a SearXNG server with the JSON format enabled, if you'd like to use that instead of direct Google.
# You can also customize the engines and categories parameters, but the defaults should also work just fine.
# SEARXNG_ENDPOINT=http://your.searxng.server
# SEARXNG_ENGINES=
# SEARXNG_CATEGORIES=

## === Other ===

# Supabase Setup (used to support DB authentication, advanced logging, etc.)
# SUPABASE_ANON_TOKEN=
# SUPABASE_URL=
# SUPABASE_SERVICE_TOKEN=

# Use if you've set up authentication and want to test with a real API key
# TEST_API_KEY=

# This key lets you access the queue admin panel. Change this if your deployment is publicly accessible.
BULL_AUTH_KEY=CHANGEME

# This is now autoconfigured by the docker-compose.yaml. You shouldn't need to set it.
# PLAYWRIGHT_MICROSERVICE_URL=http://playwright-service:3000/scrape
# REDIS_URL=redis://redis:6379
# REDIS_RATE_LIMIT_URL=redis://redis:6379

# Set if you have a llamaparse key you'd like to use to parse pdfs
# LLAMAPARSE_API_KEY=

# Set if you'd like to send server health status messages to Slack
# SLACK_WEBHOOK_URL=

# Set if you'd like to send posthog events like job logs
# POSTHOG_API_KEY=
# POSTHOG_HOST=

## === System Resource Configuration ===
# Maximum CPU usage threshold (0.0-1.0). Worker will reject new jobs when CPU usage exceeds this value.
# Default: 0.8 (80%)
# MAX_CPU=0.8

# Maximum RAM usage threshold (0.0-1.0). Worker will reject new jobs when memory usage exceeds this value.
# Default: 0.8 (80%)
# MAX_RAM=0.8

# Set if you'd like to allow local webhooks to be sent to your self-hosted instance
# ALLOW_LOCAL_WEBHOOKS=true
```

3. *(Optional) Running with TypeScript Playwright Service*

   * Update the `docker-compose.yml` file to change the Playwright service:

     ```plaintext  theme={null}
         build: apps/playwright-service
     ```

     TO

     ```plaintext  theme={null}
         build: apps/playwright-service-ts
     ```

   * Set the `PLAYWRIGHT_MICROSERVICE_URL` in your `.env` file:

     ```plaintext  theme={null}
     PLAYWRIGHT_MICROSERVICE_URL=http://localhost:3000/scrape
     ```

   * Don't forget to set the proxy server in your `.env` file as needed.

4. Build and run the Docker containers:

   ```bash  theme={null}
   docker compose build
   docker compose up
   ```

This will run a local instance of Firecrawl which can be accessed at `http://localhost:3002`.

You should be able to see the Bull Queue Manager UI on `http://localhost:3002/admin/@/queues`.

5. *(Optional)* Test the API

If you’d like to test the crawl endpoint, you can run this:

```bash  theme={null}
curl -X POST http://localhost:3002/v2/crawl \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'
```

## Troubleshooting

This section provides solutions to common issues you might encounter while setting up or running your self-hosted instance of Firecrawl.

### Supabase client is not configured

**Symptom:**

```bash  theme={null}
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Attempted to access Supabase client when it's not configured.
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Error inserting scrape event: Error: Supabase client is not configured.
```

**Explanation:**
This error occurs because the Supabase client setup is not completed. You should be able to scrape and crawl with no problems. Right now it's not possible to configure Supabase in self-hosted instances.

### You're bypassing authentication

**Symptom:**

```bash  theme={null}
[YYYY-MM-DDTHH:MM:SS.SSSz]WARN - You're bypassing authentication
```

**Explanation:**
This error occurs because the Supabase client setup is not completed. You should be able to scrape and crawl with no problems. Right now it's not possible to configure Supabase in self-hosted instances.

### Docker containers fail to start

**Symptom:**
Docker containers exit unexpectedly or fail to start.

**Solution:**
Check the Docker logs for any error messages using the command:

```bash  theme={null}
docker logs [container_name]
```

* Ensure all required environment variables are set correctly in the .env file.
* Verify that all Docker services defined in docker-compose.yml are correctly configured and the necessary images are available.

### Connection issues with Redis

**Symptom:**
Errors related to connecting to Redis, such as timeouts or "Connection refused".

**Solution:**

* Ensure that the Redis service is up and running in your Docker environment.
* Verify that the REDIS\_URL and REDIS\_RATE\_LIMIT\_URL in your .env file point to the correct Redis instance.
* Check network settings and firewall rules that may block the connection to the Redis port.

### API endpoint does not respond

**Symptom:**
API requests to the Firecrawl instance timeout or return no response.

**Solution:**

* Ensure that the Firecrawl service is running by checking the Docker container status.
* Verify that the PORT and HOST settings in your .env file are correct and that no other service is using the same port.
* Check the network configuration to ensure that the host is accessible from the client making the API request.

By addressing these common issues, you can ensure a smoother setup and operation of your self-hosted Firecrawl instance.

## Install Firecrawl on a Kubernetes Cluster (Simple Version)

Read the [examples/kubernetes-cluster-install/README.md](https://github.com/firecrawl/firecrawl/tree/main/examples/kubernetes/cluster-install#readme) for instructions on how to install Firecrawl on a Kubernetes Cluster.


# Authenticated Scraping
Source: https://docs.firecrawl.dev/developer-guides/advanced-guides/authenticated-scraping

Learn how to scrape content behind authentication using cookies

<Warning>
  **Important:** Only use authenticated scraping on systems where you have explicit permission from both parties (yourself and the platform owner), such as internal, self-hosted tools or resources you fully control. Do not use authentication on platforms unless you are certain it abides by the site's Terms and Conditions and get written permission when in doubt. Using session cookies improperly can violate terms of service or laws; always confirm you are authorized to access protected content in this way.
</Warning>

## Overview

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

***

## Setup

<Steps>
  <Step title="Get API Key">
    Get your Firecrawl API key from [firecrawl.dev/app](https://firecrawl.dev/app)
  </Step>

  <Step title="Install Dependencies">
    ```bash npm theme={null}
    npm install @mendable/firecrawl-js
    ```

    <Note>
      **Node.js \< v20**: If you're using Node.js version 19 or earlier, you'll also need to install `dotenv`:

      ```bash  theme={null}
      npm install dotenv
      ```

      And import it with `import 'dotenv/config'` at the top of your file.
    </Note>
  </Step>

  <Step title="Configure Environment">
    Create a `.env` file:

    ```bash .env theme={null}
    FIRECRAWL_API_KEY=your_firecrawl_api_key
    ```
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
auth-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJleGFtcGxlLXVzZXItaWQiLCJlbWFpbCI6InRlc3RAZXhhbXBsZS5jb20ifQ.example-signature-hash
```

<Warning>
  **Important:** Cookies are sensitive credentials. Never share them publicly or commit them to version control. Treat them like passwords.
</Warning>

### Step 2: Use Cookies with Firecrawl

```typescript  theme={null}
import FirecrawlApp from "@mendable/firecrawl-js";

const app = new FirecrawlApp({
  apiKey: process.env.FIRECRAWL_API_KEY
});

const result = await app.scrape("https://firecrawl-auth.vercel.app/dashboard", {
  formats: ["markdown", "screenshot"],
  headers: {
    Cookie: 'auth-token=COOKIE_GOES_HERE'
  },
  waitFor: 3000 // Wait 3 seconds for the page to load
});

console.log("=== Markdown ===\n" + result.markdown + "\n\n=== Screenshot URL ===\n" + result.screenshot);
```

## Best Practices

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

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="Getting 401 Unauthorized Errors" icon="ban">
    **Possible causes:**

    * Cookie has expired
    * Cookie was copied incorrectly
    * Application requires additional headers
    * Session was invalidated on the server

    **Solutions:**

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


# Scraping Amazon
Source: https://docs.firecrawl.dev/developer-guides/common-sites/amazon

Extract product data, prices, and reviews from Amazon using Firecrawl

<Info>
  Amazon is one of the most scraped e-commerce sites. This guide shows you how to effectively extract product data, pricing, reviews, and search results using Firecrawl's powerful features.
</Info>

## Setup

```bash  theme={null}
npm install @mendable/firecrawl-js zod
```

## Overview

When scraping Amazon, you'll typically want to:

* Extract product information (title, price, availability)
* Get customer reviews and ratings
* Monitor price changes
* Search for products programmatically
* Track competitor listings

## Scrape with JSON Mode

Extract structured product data using Zod schemas.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

// Define Zod schema
const ProductSchema = z.object({
    title: z.string(),
    price: z.string(),
    rating: z.number(),
    availability: z.string(),
    features: z.array(z.string())
});

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.amazon.com/dp/B0DZZWMB2L', {
    formats: [{
        type: 'json',
        schema: z.toJSONSchema(ProductSchema)
    }],
});

// Parse and validate with Zod
const jsonData = typeof result.json === 'string' ? JSON.parse(result.json) : result.json;
const validated = ProductSchema.parse(jsonData);

console.log('✅ Validated product data:');
console.log(validated);
```

## Search

Find products on Amazon.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('gaming laptop site:amazon.com', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }, { type: 'images' }
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## Scrape

Scrape a single Amazon product page.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0DZZWMB2L', {
    formats: ['markdown'], // i.e. html, links, etc.
    onlyMainContent: true
});

console.log(result);
```

## Map

Discover all available URLs on Amazon product or category pages. Note: Map returns URLs only, without content.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics');

console.log(mapResult.links);
// Returns array of URLs without content
```

## Crawl

Crawl multiple pages from Amazon category or search results.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const crawlResult = await firecrawl.crawl('https://www.amazon.com/s?k=mechanical+keyboards', {
    limit: 10,
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(crawlResult.data);
```

## Batch Scrape

Scrape multiple Amazon product URLs simultaneously.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Wait for completion
const job = await firecrawl.batchScrape([
    'https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0DZZWMB2L',
    'https://www.amazon.com/Razer-Blade-Gaming-Laptop-Lightweight/dp/B0FP47DNFQ',
    'https://www.amazon.com/HP-2025-Omen-Gaming-Laptop/dp/B0FL4RMGSH'],
    {
        options: {
            formats: ['markdown']
        },
        pollInterval: 2,
        timeout: 120
    }
);


console.log(job.status, job.completed, job.total);

console.log(job);
```


# Scraping Etsy
Source: https://docs.firecrawl.dev/developer-guides/common-sites/etsy

Extract handmade products, shop data, and pricing from Etsy marketplace

<Info>
  Etsy is a global marketplace for unique and creative goods. This guide shows you how to extract product listings, shop information, reviews, and trending items using Firecrawl.
</Info>

## Setup

```bash  theme={null}
npm install @mendable/firecrawl-js zod
```

## Overview

When scraping Etsy, you'll typically want to:

* Extract product listings and variations
* Get shop information and ratings
* Monitor trending items and categories
* Track pricing and sales data
* Extract customer reviews

## Scrape with JSON Mode

Extract structured listing data using Zod schemas.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

// Define Zod schema
const ListingSchema = z.object({
    title: z.string(),
    price: z.string(),
    shopName: z.string(),
    rating: z.number()
});

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.etsy.com/listing/1844315896/handmade-925-sterling-silver-jewelry-set', {
    formats: [{
        type: 'json',
        schema: z.toJSONSchema(ListingSchema)
    }],
});

// Parse and validate with Zod
const jsonData = typeof result.json === 'string' ? JSON.parse(result.json) : result.json;
const validated = ListingSchema.parse(jsonData);

console.log('✅ Validated listing data:');
console.log(validated);
```

## Search

Find products on Etsy marketplace.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('handmade jewelry site:etsy.com', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }, { type: 'images' }
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## Scrape

Scrape a single Etsy product listing.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.etsy.com/listing/1844315896/handmade-925-sterling-silver-jewelry-set', {
    formats: ['markdown'], // i.e. html, links, etc.
    onlyMainContent: true
});

console.log(result);
```

## Map

Discover all available URLs in an Etsy shop or category. Note: Map returns URLs only, without content.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://www.etsy.com/shop/YourShopName');

console.log(mapResult.links);
// Returns array of URLs without content
```

## Crawl

Crawl multiple pages from Etsy shop or category.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const crawlResult = await firecrawl.crawl('https://www.etsy.com/c/jewelry', {
    limit: 10,
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(crawlResult.data);
```

## Batch Scrape

Scrape multiple Etsy listing URLs simultaneously.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Wait for completion
const job = await firecrawl.batchScrape([
    'https://www.etsy.com/listing/1844315896/handmade-925-sterling-silver-jewelry-set',
    'https://www.etsy.com/market/handmade_jewelry',
    'https://www.etsy.com/market/jewelry_handmade'],
    {
        options: {
            formats: ['markdown']
        },
        pollInterval: 2,
        timeout: 120
    }
);


console.log(job.status, job.completed, job.total);

console.log(job);
```


# Scraping GitHub
Source: https://docs.firecrawl.dev/developer-guides/common-sites/github

Learn how to scrape GitHub using Firecrawl's core features

Learn how to use Firecrawl's core features to scrape GitHub repositories, issues, and documentation.

## Setup

```bash  theme={null}
npm install @mendable/firecrawl-js zod
```

## Scrape with JSON Mode

Extract structured data from repositories using Zod schemas.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://github.com/firecrawl/firecrawl', {
    formats: [{
        type: 'json',
        schema: z.object({
            name: z.string(),
            description: z.string(),
            stars: z.number(),
            forks: z.number(),
            language: z.string(),
            topics: z.array(z.string())
        })
    }]
});

console.log(result.json);
```

## Search

Find repositories, issues, or documentation on GitHub.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('machine learning site:github.com', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }, { type: 'images' }
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## Scrape

Scrape a single GitHub page - repository, issue, or file.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://github.com/mendableai/firecrawl', {
    formats: ['markdown'] // i.e. html, links, etc.
});

console.log(result);
```

## Map

Discover all available URLs in a repository or documentation site. Note: Map returns URLs only, without content.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://github.com/vercel/next.js/tree/canary/docs');

console.log(mapResult.links);
// Returns array of URLs without content
```

## Crawl

Crawl multiple pages from a repository or documentation.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const crawlResult = await firecrawl.crawl('https://github.com/facebook/react/wiki', {
    limit: 10,
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(crawlResult.data);
```

## Batch Scrape

Scrape multiple GitHub URLs simultaneously.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Wait for completion
const job = await firecrawl.batchScrape([
    'https://github.com/vercel/next.js',
    'https://github.com/facebook/react',
    'https://github.com/microsoft/typescript'],
    {
        options: {
            formats: ['markdown']
        },
        pollInterval: 2,
        timeout: 120
    }
);


console.log(job.status, job.completed, job.total);

console.log(job);
```

## Batch Scrape with JSON Mode

Extract structured data from multiple repositories at once.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Wait for completion
const job = await firecrawl.batchScrape([
    'https://github.com/vercel/next.js',
    'https://github.com/facebook/react'],
    {
        options: {
            formats: [{
                type: 'json',
                schema: z.object({
                    name: z.string(),
                    description: z.string(),
                    stars: z.number(),
                    language: z.string()
                })
            }]
        },
        pollInterval: 2,
        timeout: 120
    }
);


console.log(job.status, job.completed, job.total);

console.log(job);
```


# Scraping Wikipedia
Source: https://docs.firecrawl.dev/developer-guides/common-sites/wikipedia

Extract articles, infoboxes, and build knowledge graphs from Wikipedia

Learn how to effectively scrape Wikipedia for research, knowledge extraction, and building AI applications.

## Setup

```bash  theme={null}
npm install @mendable/firecrawl-js zod
```

## Use Cases

* Research automation and fact-checking
* Building knowledge graphs
* Multi-language content extraction
* Educational content aggregation
* Entity information extraction

## Scrape with JSON Mode

Extract structured data from Wikipedia articles using Zod schemas.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://en.wikipedia.org/wiki/JavaScript', {
    formats: [{
        type: 'json',
        schema: z.object({
            name: z.string(),
            creator: z.string(),
            firstAppeared: z.string(),
            typingDiscipline: z.string(),
            website: z.string()
        })
    }]
});

console.log(result.json);
```

## Search

Find articles on Wikipedia.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('quantum computing site:en.wikipedia.org', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }, { type: 'images' }
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## Scrape

Scrape a single Wikipedia article.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://en.wikipedia.org/wiki/Artificial_intelligence', {
    formats: ['markdown'], // i.e. html, links, etc.
    onlyMainContent: true
});

console.log(result);
```

## Map

Discover all available URLs in a Wikipedia portal or category. Note: Map returns URLs only, without content.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://en.wikipedia.org/wiki/Portal:Computer_science');

console.log(mapResult.links);
// Returns array of URLs without content
```

## Crawl

Crawl multiple pages from Wikipedia documentation or categories.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const crawlResult = await firecrawl.crawl('https://en.wikipedia.org/wiki/Portal:Artificial_intelligence', {
    limit: 10,
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(crawlResult.data);
```

## Batch Scrape

Scrape multiple Wikipedia URLs simultaneously.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Wait for completion
const job = await firecrawl.batchScrape([
    'https://en.wikipedia.org/wiki/Machine_learning',
    'https://en.wikipedia.org/wiki/Artificial_intelligence',
    'https://en.wikipedia.org/wiki/Deep_learning'],
    {
        options: {
            formats: ['markdown']
        },
        pollInterval: 2,
        timeout: 120
    }
);


console.log(job.status, job.completed, job.total);

console.log(job);
```


# Building an AI Research Assistant with Firecrawl and AI SDK
Source: https://docs.firecrawl.dev/developer-guides/cookbooks/ai-research-assistant-cookbook

Build a complete AI-powered research assistant with web scraping and search capabilities

Build a complete AI-powered research assistant that can scrape websites and search the web to answer questions. The assistant automatically decides when to use web scraping or search tools to gather information, then provides comprehensive answers based on collected data.

<img src="https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif?s=cfcbad69aa3f087a474414c0763a260b" alt="AI research assistant chatbot interface showing real-time web scraping with Firecrawl and conversational responses powered by OpenAI" data-og-width="1044" width="1044" data-og-height="716" height="716" data-path="images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif" data-optimize="true" data-opv="3" />

## What You'll Build

An AI chat interface where users can ask questions about any topic. The AI assistant automatically decides when to use web scraping or search tools to gather information, then provides comprehensive answers based on the data it collects.

## Prerequisites

* Node.js 18 or later installed
* An OpenAI API key from [platform.openai.com](https://platform.openai.com)
* A Firecrawl API key from [firecrawl.dev](https://firecrawl.dev)
* Basic knowledge of React and Next.js

<Steps>
  <Step title="Create a New Next.js Project">
    Start by creating a fresh Next.js application and navigating into the project directory:

    ```bash  theme={null}
    npx create-next-app@latest ai-sdk-firecrawl && cd ai-sdk-firecrawl
    ```

    When prompted, select the following options:

    * TypeScript: Yes
    * ESLint: Yes
    * Tailwind CSS: Yes
    * App Router: Yes
    * Use `src/` directory: No
    * Import alias: Yes (@/\*)
  </Step>

  <Step title="Install Dependencies">
    ### Install AI SDK Packages

    The AI SDK is a TypeScript toolkit that provides a unified API for working with different LLM providers:

    ```bash  theme={null}
    npm i ai @ai-sdk/react zod
    ```

    These packages provide:

    * `ai`: Core SDK with streaming, tool calling, and response handling
    * `@ai-sdk/react`: React hooks like `useChat` for building chat interfaces
    * `zod`: Schema validation for tool inputs

    Learn more at [ai-sdk.dev/docs](https://ai-sdk.dev/docs).

    ### Install AI Elements

    AI Elements provides pre-built UI components for AI applications. Run the following command to scaffold all the necessary components:

    ```bash  theme={null}
    npx ai-elements@latest
    ```

    This sets up AI Elements in your project, including conversation components, message displays, prompt inputs, and tool call visualizations.

    Documentation: [ai-sdk.dev/elements/overview](https://ai-sdk.dev/elements/overview).

    ### Install OpenAI Provider

    Install the OpenAI provider to connect with OpenAI's models:

    ```bash  theme={null}
    npm install @ai-sdk/openai
    ```
  </Step>

  <Step title="Build the Frontend Chat Interface">
    Create the main page at `app/page.tsx` and copy the code from the Code tab below. This will be the chat interface where users interact with the AI assistant.

    <Tabs>
      <Tab title="Preview">
                <img src="https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif?s=cfcbad69aa3f087a474414c0763a260b" alt="AI research assistant chatbot interface showing real-time web scraping with Firecrawl and conversational responses powered by OpenAI" data-og-width="1044" width="1044" data-og-height="716" height="716" data-path="images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif" data-optimize="true" data-opv="3" />
      </Tab>

      <Tab title="Code">
        ```typescript app/page.tsx theme={null}
        "use client";

        import {
          Conversation,
          ConversationContent,
          ConversationScrollButton,
        } from "@/components/ai-elements/conversation";
        import {
          PromptInput,
          PromptInputActionAddAttachments,
          PromptInputActionMenu,
          PromptInputActionMenuContent,
          PromptInputActionMenuTrigger,
          PromptInputAttachment,
          PromptInputAttachments,
          PromptInputBody,
          PromptInputButton,
          PromptInputHeader,
          type PromptInputMessage,
          PromptInputSelect,
          PromptInputSelectContent,
          PromptInputSelectItem,
          PromptInputSelectTrigger,
          PromptInputSelectValue,
          PromptInputSubmit,
          PromptInputTextarea,
          PromptInputFooter,
          PromptInputTools,
        } from "@/components/ai-elements/prompt-input";
        import {
          MessageResponse,
          Message,
          MessageContent,
          MessageActions,
          MessageAction,
        } from "@/components/ai-elements/message";

        import { Fragment, useState } from "react";
        import { useChat } from "@ai-sdk/react";
        import type { ToolUIPart } from "ai";
        import {
          Tool,
          ToolContent,
          ToolHeader,
          ToolInput,
          ToolOutput,
        } from "@/components/ai-elements/tool";

        import { CopyIcon, GlobeIcon, RefreshCcwIcon } from "lucide-react";
        import {
          Source,
          Sources,
          SourcesContent,
          SourcesTrigger,
        } from "@/components/ai-elements/sources";
        import {
          Reasoning,
          ReasoningContent,
          ReasoningTrigger,
        } from "@/components/ai-elements/reasoning";
        import { Loader } from "@/components/ai-elements/loader";

        const models = [
          {
            name: "GPT 5 Mini (Thinking)",
            value: "gpt-5-mini",
          },
          {
            name: "GPT 4o Mini",
            value: "gpt-4o-mini",
          },
        ];

        const ChatBotDemo = () => {
          const [input, setInput] = useState("");
          const [model, setModel] = useState<string>(models[0].value);
          const [webSearch, setWebSearch] = useState(false);
          const { messages, sendMessage, status, regenerate } = useChat();

          const handleSubmit = (message: PromptInputMessage) => {
            const hasText = Boolean(message.text);
            const hasAttachments = Boolean(message.files?.length);

            if (!(hasText || hasAttachments)) {
              return;
            }

            sendMessage(
              {
                text: message.text || "Sent with attachments",
                files: message.files,
              },
              {
                body: {
                  model: model,
                  webSearch: webSearch,
                },
              }
            );
            setInput("");
          };

          return (
            <div className="max-w-4xl mx-auto p-6 relative size-full h-screen">
              <div className="flex flex-col h-full">
                <Conversation className="h-full">
                  <ConversationContent>
                    {messages.map((message) => (
                      <div key={message.id}>
                        {message.role === "assistant" &&
                          message.parts.filter((part) => part.type === "source-url")
                            .length > 0 && (
                            <Sources>
                              <SourcesTrigger
                                count={
                                  message.parts.filter(
                                    (part) => part.type === "source-url"
                                  ).length
                                }
                              />
                              {message.parts
                                .filter((part) => part.type === "source-url")
                                .map((part, i) => (
                                  <SourcesContent key={`${message.id}-${i}`}>
                                    <Source
                                      key={`${message.id}-${i}`}
                                      href={part.url}
                                      title={part.url}
                                    />
                                  </SourcesContent>
                                ))}
                            </Sources>
                          )}
                        {message.parts.map((part, i) => {
                          switch (part.type) {
                            case "text":
                              return (
                                <Fragment key={`${message.id}-${i}`}>
                                  <Message from={message.role}>
                                    <MessageContent>
                                      <MessageResponse>{part.text}</MessageResponse>
                                    </MessageContent>
                                  </Message>
                                  {message.role === "assistant" &&
                                    i === messages.length - 1 && (
                                      <MessageActions className="mt-2">
                                        <MessageAction
                                          onClick={() => regenerate()}
                                          label="Retry"
                                        >
                                          <RefreshCcwIcon className="size-3" />
                                        </MessageAction>
                                        <MessageAction
                                          onClick={() =>
                                            navigator.clipboard.writeText(part.text)
                                          }
                                          label="Copy"
                                        >
                                          <CopyIcon className="size-3" />
                                        </MessageAction>
                                      </MessageActions>
                                    )}
                                </Fragment>
                              );
                            case "reasoning":
                              return (
                                <Reasoning
                                  key={`${message.id}-${i}`}
                                  className="w-full"
                                  isStreaming={
                                    status === "streaming" &&
                                    i === message.parts.length - 1 &&
                                    message.id === messages.at(-1)?.id
                                  }
                                >
                                  <ReasoningTrigger />
                                  <ReasoningContent>{part.text}</ReasoningContent>
                                </Reasoning>
                              );
                            default: {
                              if (part.type.startsWith("tool-")) {
                                const toolPart = part as ToolUIPart;
                                return (
                                  <Tool
                                    key={`${message.id}-${i}`}
                                    defaultOpen={toolPart.state === "output-available"}
                                  >
                                    <ToolHeader
                                      type={toolPart.type}
                                      state={toolPart.state}
                                    />
                                    <ToolContent>
                                      <ToolInput input={toolPart.input} />
                                      <ToolOutput
                                        output={toolPart.output}
                                        errorText={toolPart.errorText}
                                      />
                                    </ToolContent>
                                  </Tool>
                                );
                              }
                              return null;
                            }
                          }
                        })}
                      </div>
                    ))}
                    {status === "submitted" && <Loader />}
                  </ConversationContent>
                  <ConversationScrollButton />
                </Conversation>

                <PromptInput
                  onSubmit={handleSubmit}
                  className="mt-4"
                  globalDrop
                  multiple
                >
                  <PromptInputHeader>
                    <PromptInputAttachments>
                      {(attachment) => <PromptInputAttachment data={attachment} />}
                    </PromptInputAttachments>
                  </PromptInputHeader>
                  <PromptInputBody>
                    <PromptInputTextarea
                      onChange={(e) => setInput(e.target.value)}
                      value={input}
                    />
                  </PromptInputBody>
                  <PromptInputFooter>
                    <PromptInputTools>
                      <PromptInputActionMenu>
                        <PromptInputActionMenuTrigger />
                        <PromptInputActionMenuContent>
                          <PromptInputActionAddAttachments />
                        </PromptInputActionMenuContent>
                      </PromptInputActionMenu>
                      <PromptInputButton
                        variant={webSearch ? "default" : "ghost"}
                        onClick={() => setWebSearch(!webSearch)}
                      >
                        <GlobeIcon size={16} />
                        <span>Search</span>
                      </PromptInputButton>
                      <PromptInputSelect
                        onValueChange={(value) => {
                          setModel(value);
                        }}
                        value={model}
                      >
                        <PromptInputSelectTrigger>
                          <PromptInputSelectValue />
                        </PromptInputSelectTrigger>
                        <PromptInputSelectContent>
                          {models.map((model) => (
                            <PromptInputSelectItem
                              key={model.value}
                              value={model.value}
                            >
                              {model.name}
                            </PromptInputSelectItem>
                          ))}
                        </PromptInputSelectContent>
                      </PromptInputSelect>
                    </PromptInputTools>
                    <PromptInputSubmit disabled={!input && !status} status={status} />
                  </PromptInputFooter>
                </PromptInput>
              </div>
            </div>
          );
        };

        export default ChatBotDemo;
        ```
      </Tab>
    </Tabs>

    ### Understanding the Frontend

    The frontend uses AI Elements components to provide a complete chat interface:

    **Key Features:**

    * **Conversation Display**: The `Conversation` component automatically handles message scrolling and display
    * **Message Rendering**: Each message part is rendered based on its type (text, reasoning, tool calls)
    * **Tool Visualization**: Tool calls are displayed with collapsible sections showing inputs and outputs
    * **Interactive Controls**: Users can toggle web search, select models, and attach files
    * **Message Actions**: Copy and retry actions for assistant messages
  </Step>

  <Step title="Add Markdown Rendering Support">
    To ensure the markdown from the LLM is correctly rendered, add the following import to your `app/globals.css` file:

    ```css  theme={null}
    @source "../node_modules/streamdown/dist/index.js";
    ```

    This imports the necessary styles for rendering markdown content in the message responses.
  </Step>

  <Step title="Build the Basic API Route">
    Create the chat API endpoint at `app/api/chat/route.ts`. This route will handle incoming messages and stream responses from the AI.

    ```typescript  theme={null}
    import { streamText, UIMessage, convertToModelMessages } from "ai";
    import { createOpenAI } from "@ai-sdk/openai";

    const openai = createOpenAI({
      apiKey: process.env.OPENAI_API_KEY!,
    });

    // Allow streaming responses up to 5 minutes
    export const maxDuration = 300;

    export async function POST(req: Request) {
      const {
        messages,
        model,
        webSearch,
      }: {
        messages: UIMessage[];
        model: string;
        webSearch: boolean;
      } = await req.json();

      const result = streamText({
        model: openai(model),
        messages: convertToModelMessages(messages),
        system:
          "You are a helpful assistant that can answer questions and help with tasks.",
      });

      // send sources and reasoning back to the client
      return result.toUIMessageStreamResponse({
        sendSources: true,
        sendReasoning: true,
      });
    }
    ```

    This basic route:

    * Receives messages from the frontend
    * Uses the OpenAI model selected by the user
    * Streams responses back to the client
    * Doesn't include tools yet - we'll add those next
  </Step>

  <Step title="Configure Environment Variables">
    Create a `.env.local` file in your project root:

    ```bash  theme={null}
    touch .env.local
    ```

    Add your OpenAI API key:

    ```env  theme={null}
    OPENAI_API_KEY=sk-your-openai-api-key
    ```

    The `OPENAI_API_KEY` is required for the AI model to function.
  </Step>

  <Step title="Test the Basic Chat">
    Now you can test the AI SDK chatbot without Firecrawl integration. Start the development server:

    ```bash  theme={null}
    npm run dev
    ```

    Open [localhost:3000](http://localhost:3000) in your browser and test the basic chat functionality. The assistant should respond to messages, but won't have web scraping or search capabilities yet.

        <img src="https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/simple-ai-sdk-chatbot.gif?s=dd40938ec93fd0ad13568d2825d7552d" alt="Basic AI chatbot without web scraping capabilities" data-og-width="1192" width="1192" data-og-height="720" height="720" data-path="images/guides/cookbooks/ai-sdk-cookbook/simple-ai-sdk-chatbot.gif" data-optimize="true" data-opv="3" />
  </Step>

  <Step title="Add Firecrawl Tools">
    Now let's enhance the assistant with web scraping and search capabilities using Firecrawl.

    ### Install Firecrawl SDK

    Firecrawl converts websites into LLM-ready formats with scraping and search capabilities:

    ```bash  theme={null}
    npm i @mendable/firecrawl-js
    ```

    ### Create the Tools File

    Create a `lib` folder and add a `tools.ts` file inside it:

    ```bash  theme={null}
    mkdir lib && touch lib/tools.ts
    ```

    Add the following code to define the web scraping and search tools:

    ```typescript lib/tools.ts theme={null}
    import FirecrawlApp from "@mendable/firecrawl-js";
    import { tool } from "ai";
    import { z } from "zod";

    const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

    export const scrapeWebsiteTool = tool({
      description: 'Scrape content from any website URL',
      inputSchema: z.object({
        url: z.string().url().describe('The URL to scrape')
      }),
      execute: async ({ url }) => {
        console.log('Scraping:', url);
        const result = await firecrawl.scrape(url, {
          formats: ['markdown'],
          onlyMainContent: true,
          timeout: 30000
        });
        console.log('Scraped content preview:', result.markdown?.slice(0, 200) + '...');
        return { content: result.markdown };
      }
    });

    export const searchWebTool = tool({
      description: 'Search the web using Firecrawl',
      inputSchema: z.object({
        query: z.string().describe('The search query'),
        limit: z.number().optional().describe('Number of results'),
        location: z.string().optional().describe('Location for localized results'),
        tbs: z.string().optional().describe('Time filter (qdr:h, qdr:d, qdr:w, qdr:m, qdr:y)'),
        sources: z.array(z.enum(['web', 'news', 'images'])).optional().describe('Result types'),
        categories: z.array(z.enum(['github', 'research', 'pdf'])).optional().describe('Filter categories'),
      }),
      execute: async ({ query, limit, location, tbs, sources, categories }) => {
        console.log('Searching:', query);
        const response = await firecrawl.search(query, {
          ...(limit && { limit }),
          ...(location && { location }),
          ...(tbs && { tbs }),
          ...(sources && { sources }),
          ...(categories && { categories }),
        }) as { web?: Array<{ title?: string; url?: string; description?: string }> };

        const results = (response.web || []).map((item) => ({
          title: item.title || item.url || 'Untitled',
          url: item.url || '',
          description: item.description || '',
        }));

        console.log('Search results:', results.length);
        return { results };
      },
    });
    ```

    ### Understanding the Tools

    **Scrape Website Tool:**

    * Accepts a URL as input (validated by Zod schema)
    * Uses Firecrawl's `scrape` method to fetch the page as markdown
    * Extracts only the main content to reduce token usage
    * Returns the scraped content for the AI to analyze

    **Search Web Tool:**

    * Accepts a search query with optional filters
    * Uses Firecrawl's `search` method to find relevant web pages
    * Supports advanced filters like location, time range, and content categories
    * Returns structured results with titles, URLs, and descriptions

    Learn more about tools: [ai-sdk.dev/docs/foundations/tools](https://ai-sdk.dev/docs/foundations/tools).
  </Step>

  <Step title="Update the API Route with Firecrawl Tools">
    Now update your `app/api/chat/route.ts` to include the Firecrawl tools we just created.

    <Accordion title="View complete app/api/chat/route.ts code">
      ```typescript  theme={null}
      import { streamText, UIMessage, stepCountIs, convertToModelMessages } from "ai";
      import { createOpenAI } from "@ai-sdk/openai";
      import { scrapeWebsiteTool, searchWebTool } from "@/lib/tools";

      const openai = createOpenAI({
        apiKey: process.env.OPENAI_API_KEY!,
      });

      export const maxDuration = 300;

      export async function POST(req: Request) {
        const {
          messages,
          model,
          webSearch,
        }: {
          messages: UIMessage[];
          model: string;
          webSearch: boolean;
        } = await req.json();

        const result = streamText({
          model: openai(model),
          messages: convertToModelMessages(messages),
          system:
            "You are a helpful assistant that can answer questions and help with tasks.",
          // Add the Firecrawl tools here
          tools: {
            scrapeWebsite: scrapeWebsiteTool,
            searchWeb: searchWebTool,
          },
          stopWhen: stepCountIs(5),
          toolChoice: webSearch ? "auto" : "none",
        });

        return result.toUIMessageStreamResponse({
          sendSources: true,
          sendReasoning: true,
        });
      }
      ```
    </Accordion>

    The key changes from the basic route:

    * Import `stepCountIs` from the AI SDK
    * Import the Firecrawl tools from `@/lib/tools`
    * Add the `tools` object with both `scrapeWebsite` and `searchWeb` tools
    * Add `stopWhen: stepCountIs(5)` to limit execution steps
    * Set `toolChoice` to "auto" when web search is enabled, "none" otherwise

    Learn more about `streamText`: [ai-sdk.dev/docs/reference/ai-sdk-core/stream-text](https://ai-sdk.dev/docs/reference/ai-sdk-core/stream-text).
  </Step>

  <Step title="Add Your Firecrawl API Key">
    Update your `.env.local` file to include your Firecrawl API key:

    ```env  theme={null}
    OPENAI_API_KEY=sk-your-openai-api-key
    FIRECRAWL_API_KEY=fc-your-firecrawl-api-key
    ```

    Get your Firecrawl API key from [firecrawl.dev](https://firecrawl.dev).
  </Step>

  <Step title="Test the Complete Application">
    Restart your development server:

    ```bash  theme={null}
    npm run dev
    ```

        <img src="https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/active-firecrawl-tools-ai-sdk.gif?s=015de571c2352a0cf6eb70ddb2eaec64" alt="AI chatbot with active Firecrawl tools" data-og-width="1084" width="1084" data-og-height="720" height="720" data-path="images/guides/cookbooks/ai-sdk-cookbook/active-firecrawl-tools-ai-sdk.gif" data-optimize="true" data-opv="3" />

    Open [localhost:3000](http://localhost:3000) and test the enhanced assistant:

    1. Toggle the "Search" button to enable web search
    2. Ask: "What are the latest features from firecrawl.dev?"
    3. Watch as the AI calls the `searchWeb` or `scrapeWebsite` tool
    4. See the tool execution in the UI with inputs and outputs
    5. Read the AI's analysis based on the scraped data
  </Step>
</Steps>

## How It Works

### Message Flow

1. **User sends a message**: The user types a question and clicks submit
2. **Frontend sends request**: `useChat` sends the message to `/api/chat` with the selected model and web search setting
3. **Backend processes message**: The API route receives the message and calls `streamText`
4. **AI decides on tools**: The model analyzes the question and decides whether to use `scrapeWebsite` or `searchWeb` (only if web search is enabled)
5. **Tools execute**: If tools are called, Firecrawl scrapes or searches the web
6. **AI generates response**: The model analyzes tool results and generates a natural language response
7. **Frontend displays results**: The UI shows tool calls and the final response in real-time

### Tool Calling Process

The AI SDK's tool calling system ([ai-sdk.dev/docs/foundations/tools](https://ai-sdk.dev/docs/foundations/tools)) works as follows:

1. The model receives the user's message and available tool descriptions
2. If the model determines a tool is needed, it generates a tool call with parameters
3. The SDK executes the tool function with those parameters
4. The tool result is sent back to the model
5. The model uses the result to generate its final response

This all happens automatically within a single `streamText` call, with results streaming to the frontend in real-time.

## Key Features

### Model Selection

The application supports multiple OpenAI models:

* **GPT-5 Mini (Thinking)**: Recent OpenAI model with advanced reasoning capabilities
* **GPT-4o Mini**: Fast and cost-effective model

Users can switch between models using the dropdown selector.

### Web Search Toggle

The Search button controls whether the AI can use Firecrawl tools:

* **Enabled**: AI can call `scrapeWebsite` and `searchWeb` tools as needed
* **Disabled**: AI responds only with its training knowledge

This gives users control over when to use web data versus the model's built-in knowledge.

## Customization Ideas

### Add More Tools

Extend the assistant with additional tools:

* Database lookups for internal company data
* CRM integration to fetch customer information
* Email sending capabilities
* Document generation

Each tool follows the same pattern: define a schema with Zod, implement the execute function, and register it in the `tools` object.

### Change the AI Model

Swap OpenAI for another provider:

```typescript  theme={null}
import { anthropic } from "@ai-sdk/anthropic";

const result = streamText({
  model: anthropic("claude-4.5-sonnet"),
  // ... rest of config
});
```

The AI SDK supports 20+ providers with the same API. Learn more: [ai-sdk.dev/docs/foundations/providers-and-models](https://ai-sdk.dev/docs/foundations/providers-and-models).

### Customize the UI

AI Elements components are built on shadcn/ui, so you can:

* Modify component styles in the component files
* Add new variants to existing components
* Create custom components that match the design system

## Best Practices

1. **Use appropriate tools**: Choose `searchWeb` to find relevant pages first, `scrapeWebsite` for single pages, or let the AI decide

2. **Monitor API usage**: Track your Firecrawl and OpenAI API usage to avoid unexpected costs

3. **Handle errors gracefully**: The tools include error handling, but consider adding user-facing error messages

4. **Optimize performance**: Use streaming to provide immediate feedback and consider caching frequently accessed content

5. **Set reasonable limits**: The `stopWhen: stepCountIs(5)` prevents excessive tool calls and runaway costs

***

## Related Resources

<CardGroup cols={2}>
  <Card title="AI SDK Documentation" href="https://ai-sdk.dev/docs">
    Explore the AI SDK for building AI-powered applications with streaming, tool
    calling, and multi-provider support.
  </Card>

  <Card title="AI Elements Components" href="https://ai-sdk.dev/elements/overview">
    Pre-built UI components for AI applications built on shadcn/ui.
  </Card>
</CardGroup>


# Full-Stack Templates
Source: https://docs.firecrawl.dev/developer-guides/examples

Explore real-world examples and tutorials for Firecrawl

## Official Examples

<CardGroup cols={2}>
  <Card title="Open Lovable" href="https://github.com/firecrawl/open-lovable">
    <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExODAwZGJzcDVmZGYxc3MyNDUycTliYnAwem1qbzhtNHh0c2JrNDdmZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LMYzMkNmOecj3yFw81/giphy.gif" alt="Open Lovable" width="100%" />

    **Use Case**: Build a RAG-powered chatbot with live web data

    * [GitHub Repo](https://github.com/firecrawl/open-lovable)
  </Card>

  <Card title="Open Agent Builder" href="https://github.com/firecrawl/open-agent-builder">
    <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGNoY25xY2ptZTZtcDN6czBmdXJ2dnpkdWVjcXlqNXNhdjgyZXpkaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tWtopK29eXAbvaDpi5/giphy.gif" alt="Demo" width="100%" />

    **Use Case**: Build and deploy AI agents with web scraping capabilities

    * [GitHub Repo](https://github.com/firecrawl/open-agent-builder)
  </Card>

  <Card title="Fireplexity" href="https://github.com/firecrawl/fireplexity">
    <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjBxbmFxamZycWRrMmVhMGFibmZuc3NuZjMxc3lpNHpuamR4OWlwcXF4NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QbfaTCB1OmkRmIQwzJ/giphy.gif" alt="Fireplexity" width="100%" />

    **Use Case**: AI search engine with real-time citations, streaming responses, and live data

    * [GitHub Repo](https://github.com/firecrawl/fireplexity)
  </Card>

  <Card title="FireGEO" href="https://github.com/firecrawl/firegeo">
    <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjh4N3VwdGw2YXg2ZXpvMHBlNDFlejd1MjBpZXBxNHZ5YXJxOGk5OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/x2sTqbCW5m7z0qaNJM/giphy.gif" alt="FireGEO Demo" width="100%" />

    **Use Case**: SaaS starter with brand monitoring, authentication, and billing

    * [GitHub Repo](https://github.com/firecrawl/firegeo)
  </Card>

  <Card title="Fire Enrich" href="https://github.com/firecrawl/fire-enrich">
    <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjJwMnF2cW5zbXBhbGV6NXBpb3lkZmVhMWEwY3hmdmt3d3ZtbWc5YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QhpbWI09KyFZ0rwD72/giphy.gif" alt="Fire Enrich" width="100%" />

    **Use Case**: AI-powered data enrichment tool that transforms emails into rich datasets

    * [GitHub Repo](https://github.com/firecrawl/fire-enrich)
  </Card>

  <Card title="Firesearch" href="https://github.com/firecrawl/firesearch">
    <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2F2YWo4amdieGVnOXR3aGM5ZnBlcDZvbnRjNW1vNmtpeWNhc3VtbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Jw7Q08ll8Vh0BoApI8/giphy.gif" alt="Firesearch" width="100%" />

    **Use Case**: AI-powered deep research tool with validated answers and citations

    * [GitHub Repo](https://github.com/firecrawl/firesearch)
  </Card>

  <Card title="Firestarter" href="https://github.com/firecrawl/firestarter">
    <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGVhOTdxaDhxZGJ6bnAwaDB3bWp3bXpnYzN1NDBrazJ1MGpvOG51aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZAOM1psWWVQYeAaS38/giphy.gif" alt="Firestarter" width="100%" />

    **Use Case**: Instantly create AI chatbots for any website with RAG-powered search

    * [GitHub Repo](https://github.com/firecrawl/firestarter)
  </Card>

  <Card title="AI Ready Website" href="https://github.com/firecrawl/ai-ready-website">
    <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzZyaXVlOXoyaGJmMGV5YzBlbXNod2U5emRrZ2lqZTM1eGI1aHlzZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/irNt0XtSKmenMRqMre/giphy.gif" alt="AI Ready Website" width="100%" />

    **Use Case**: Transform any website into AI-ready structured data

    * [GitHub Repo](https://github.com/firecrawl/ai-ready-website)
  </Card>

  <Card title="Open Researcher" href="https://github.com/firecrawl/open-researcher">
    <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGJncnpmamlzc3RnMzNpeXNwcGk1Z3kwemd6c2w1ZDdxcGZwdWJwdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hhNLykzY76wu7oGFU0/giphy.gif" alt="Open Researcher" width="100%" />

    **Use Case**: AI-powered research assistant that gathers and analyzes web data

    * [GitHub Repo](https://github.com/firecrawl/open-researcher)
  </Card>
</CardGroup>


# Anthropic
Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/anthropic

Use Firecrawl with Claude for web scraping + AI workflows

Integrate Firecrawl with Claude to build AI applications powered by web data.

## Setup

```bash  theme={null}
npm install @mendable/firecrawl-js @anthropic-ai/sdk zod zod-to-json-schema
```

Create `.env` file:

```bash  theme={null}
FIRECRAWL_API_KEY=your_firecrawl_key
ANTHROPIC_API_KEY=your_anthropic_key
```

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Summarize

This example demonstrates a simple workflow: scrape a website and summarize the content using Claude.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import Anthropic from '@anthropic-ai/sdk';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const message = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    messages: [
        { role: 'user', content: `Summarize in 100 words: ${scrapeResult.markdown}` }
    ]
});

console.log('Response:', message);
```

## Tool Use

This example shows how to use Claude's tool use feature to let the model decide when to scrape websites based on user requests.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { Anthropic } from '@anthropic-ai/sdk';
import { z } from 'zod';
import { zodToJsonSchema } from 'zod-to-json-schema';

const firecrawl = new FirecrawlApp({
    apiKey: process.env.FIRECRAWL_API_KEY
});

const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY
});

const ScrapeArgsSchema = z.object({
    url: z.string()
});

console.log("Sending user message to Claude and requesting tool use if necessary...");
const response = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    tools: [{
        name: 'scrape_website',
        description: 'Scrape and extract markdown content from a website URL',
        input_schema: zodToJsonSchema(ScrapeArgsSchema, 'ScrapeArgsSchema') as any
    }],
    messages: [{
        role: 'user',
        content: 'What is Firecrawl? Check firecrawl.dev'
    }]
});

const toolUse = response.content.find(block => block.type === 'tool_use');

if (toolUse && toolUse.type === 'tool_use') {
    const input = toolUse.input as { url: string };
    console.log(`Calling tool: ${toolUse.name} | URL: ${input.url}`);

    const result = await firecrawl.scrape(input.url, {
        formats: ['markdown']
    });

    console.log(`Scraped content preview: ${result.markdown?.substring(0, 300)}...`);
    // Continue with the conversation or process the scraped content as needed
}
```

## Structured Extraction

This example demonstrates how to use Claude to extract structured data from scraped website content.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import Anthropic from '@anthropic-ai/sdk';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const CompanyInfoSchema = z.object({
    name: z.string(),
    industry: z.string().optional(),
    description: z.string().optional()
});

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown'],
    onlyMainContent: true
});

const prompt = `Extract company information from this website content.

Output ONLY valid JSON in this exact format (no markdown, no explanation):

{
  "name": "Company Name",
  "industry": "Industry",
  "description": "One sentence description"
}

Website content:
${scrapeResult.markdown}`;

const message = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    messages: [
        { role: 'user', content: prompt },
        { role: 'assistant', content: '{' }
    ]
});

const textBlock = message.content.find(block => block.type === 'text');

if (textBlock && textBlock.type === 'text') {
    const jsonText = '{' + textBlock.text;
    const companyInfo = CompanyInfoSchema.parse(JSON.parse(jsonText));
  
    console.log(companyInfo);
}
```

For more examples, check the [Claude documentation](https://docs.anthropic.com/claude/docs).


# Gemini
Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/gemini

Use Firecrawl with Google's Gemini AI for web scraping + AI workflows

Integrate Firecrawl with Google's Gemini for AI applications powered by web data.

## Setup

```bash  theme={null}
npm install @mendable/firecrawl-js @google/genai
```

Create `.env` file:

```bash  theme={null}
FIRECRAWL_API_KEY=your_firecrawl_key
GEMINI_API_KEY=your_gemini_key
```

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Summarize

This example demonstrates a simple workflow: scrape a website and summarize the content using Gemini.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { GoogleGenAI } from '@google/genai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: `Summarize: ${scrapeResult.markdown}`,
});

console.log('Summary:', response.text);
```

## Content Analysis

This example shows how to analyze website content using Gemini's multi-turn conversation capabilities.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { GoogleGenAI } from '@google/genai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://news.ycombinator.com/', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const chat = ai.chats.create({
    model: 'gemini-2.5-flash'
});

// Ask for the top 3 stories on Hacker News
const result1 = await chat.sendMessage({
    message: `Based on this website content from Hacker News, what are the top 3 stories right now?\n\n${scrapeResult.markdown}`
});
console.log('Top 3 Stories:', result1.text);

// Ask for the 4th and 5th stories on Hacker News
const result2 = await chat.sendMessage({
    message: `Now, what are the 4th and 5th top stories on Hacker News from the same content?`
});
console.log('4th and 5th Stories:', result2.text);
```

## Structured Extraction

This example demonstrates how to extract structured data using Gemini's JSON mode from scraped website content.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { GoogleGenAI, Type } from '@google/genai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: `Extract company information: ${scrapeResult.markdown}`,
    config: {
        responseMimeType: 'application/json',
        responseSchema: {
            type: Type.OBJECT,
            properties: {
                name: { type: Type.STRING },
                industry: { type: Type.STRING },
                description: { type: Type.STRING },
                products: {
                    type: Type.ARRAY,
                    items: { type: Type.STRING }
                }
            },
            propertyOrdering: ['name', 'industry', 'description', 'products']
        }
    }
});

console.log('Extracted company info:', response?.text);
```

For more examples, check the [Gemini documentation](https://ai.google.dev/docs).


# Agent Development Kit (ADK)
Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/google-adk

Integrate Firecrawl with Google's ADK using MCP for advanced agent workflows

Integrate Firecrawl with Google's Agent Development Kit (ADK) to build powerful AI agents with web scraping capabilities through the Model Context Protocol (MCP).

## Overview

Firecrawl provides an MCP server that seamlessly integrates with Google's ADK, enabling your agents to efficiently scrape, crawl, and extract structured data from any website. The integration supports both cloud-based and self-hosted Firecrawl instances with streamable HTTP for optimal performance.

## Features

* Efficient web scraping, crawling, and content discovery from any website
* Advanced search capabilities and intelligent content extraction
* Deep research and high-volume batch scraping
* Flexible deployment (cloud-based or self-hosted)
* Optimized for modern web environments with streamable HTTP support

## Prerequisites

* Obtain an API key for Firecrawl from [firecrawl.dev](https://firecrawl.dev)
* Install Google ADK

## Setup

<CodeGroup>
  ```python Remote MCP Server theme={null}
  from google.adk.agents.llm_agent import Agent
  from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
  from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

  FIRECRAWL_API_KEY = "YOUR-API-KEY"

  root_agent = Agent(
      model="gemini-2.5-pro",
      name="firecrawl_agent",
      description='A helpful assistant for scraping websites with Firecrawl',
      instruction='Help the user search for website content',
      tools=[
          MCPToolset(
              connection_params=StreamableHTTPServerParams(
                  url=f"https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp",
              ),
          )
      ],
  )
  ```

  ```python Local MCP Server theme={null}
  from google.adk.agents.llm_agent import Agent
  from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
  from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
  from mcp import StdioServerParameters

  root_agent = Agent(
      model='gemini-2.5-pro',
      name='firecrawl_agent',
      description='A helpful assistant for scraping websites with Firecrawl',
      instruction='Help the user search for website content',
      tools=[
          MCPToolset(
              connection_params=StdioConnectionParams(
                  server_params = StdioServerParameters(
                      command='npx',
                      args=[
                          "-y",
                          "firecrawl-mcp",
                      ],
                      env={
                          "FIRECRAWL_API_KEY": "YOUR-API-KEY",
                      }
                  ),
                  timeout=30,
              ),
          )
      ],
  )
  ```
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

```python  theme={null}
from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

FIRECRAWL_API_KEY = "YOUR-API-KEY"

# Create a research agent
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

# Use the agent
response = research_agent.run("What are the latest features in Python 3.13?")
print(response)
```

## Best Practices

1. **Use the right tool for the job**:
   * `firecrawl_search` when you need to find relevant pages first
   * `firecrawl_scrape` for single pages
   * `firecrawl_batch_scrape` for multiple known URLs
   * `firecrawl_crawl` for discovering and scraping entire sites

2. **Monitor your usage**: Configure credit thresholds to avoid unexpected usage

3. **Handle errors gracefully**: Configure retry settings based on your use case

4. **Optimize performance**: Use batch operations when scraping multiple URLs

***

## Related Resources

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


# LangChain
Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/langchain

Use Firecrawl with LangChain for web scraping + AI workflows

Integrate Firecrawl with LangChain to build AI applications powered by web data.

## Setup

```bash  theme={null}
npm install @langchain/openai @mendable/firecrawl-js 
```

Create `.env` file:

```bash  theme={null}
FIRECRAWL_API_KEY=your_firecrawl_key
OPENAI_API_KEY=your_openai_key
```

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Chat

This example demonstrates a simple workflow: scrape a website and process the content using LangChain.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { HumanMessage } from '@langchain/core/messages';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const chat = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
});

const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const response = await chat.invoke([
    new HumanMessage(`Summarize: ${scrapeResult.markdown}`)
]);

console.log('Summary:', response.content);
```

## Chains

This example shows how to build a LangChain chain to process and analyze scraped content.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { ChatPromptTemplate } from '@langchain/core/prompts';
import { StringOutputParser } from '@langchain/core/output_parsers';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const model = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
});

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

// Create processing chain
const prompt = ChatPromptTemplate.fromMessages([
    ['system', 'You are an expert at analyzing company websites.'],
    ['user', 'Extract the company name and main products from: {content}']
]);

const chain = prompt.pipe(model).pipe(new StringOutputParser());

// Execute the chain
const result = await chain.invoke({
    content: scrapeResult.markdown
});

console.log('Chain result:', result);
```

## Tool Calling

This example demonstrates how to use LangChain's tool calling feature to let the model decide when to scrape websites.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { DynamicStructuredTool } from '@langchain/core/tools';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Create the scraping tool
const scrapeWebsiteTool = new DynamicStructuredTool({
    name: 'scrape_website',
    description: 'Scrape content from any website URL',
    schema: z.object({
        url: z.string().url().describe('The URL to scrape')
    }),
    func: async ({ url }) => {
        console.log('Scraping:', url);
        const result = await firecrawl.scrape(url, {
            formats: ['markdown']
        });
        console.log('Scraped content preview:', result.markdown?.substring(0, 200) + '...');
        return result.markdown || 'No content scraped';
    }
});

const model = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
}).bindTools([scrapeWebsiteTool]);

const response = await model.invoke('What is Firecrawl? Visit firecrawl.dev and tell me about it.');

console.log('Response:', response.content);
console.log('Tool calls:', response.tool_calls);
```

## Structured Data Extraction

This example shows how to extract structured data using LangChain's structured output feature.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const CompanyInfoSchema = z.object({
    name: z.string(),
    industry: z.string(),
    description: z.string(),
    products: z.array(z.string())
});

const model = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
}).withStructuredOutput(CompanyInfoSchema);

const companyInfo = await model.invoke([
    {
        role: 'system',
        content: 'Extract company information from website content.'
    },
    {
        role: 'user',
        content: `Extract data: ${scrapeResult.markdown}`
    }
]);

console.log('Extracted company info:', companyInfo);
```

For more examples, check the [LangChain documentation](https://js.langchain.com/docs).


# LangGraph
Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/langgraph

Integrate Firecrawl with LangGraph for building agent workflows

This guide shows how to integrate Firecrawl with LangGraph to build AI agent workflows that can scrape and process web content.

## Setup

```bash  theme={null}
npm install @langchain/langgraph @langchain/openai @mendable/firecrawl-js
```

Create `.env` file:

```bash  theme={null}
FIRECRAWL_API_KEY=your_firecrawl_key
OPENAI_API_KEY=your_openai_key
```

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Basic Workflow

This example demonstrates a basic LangGraph workflow that scrapes a website and analyzes the content.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { StateGraph, MessagesAnnotation, START, END } from '@langchain/langgraph';

// Initialize Firecrawl
const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Initialize LLM
const llm = new ChatOpenAI({
    model: "gpt-5-nano",
    apiKey: process.env.OPENAI_API_KEY
});

// Define the scrape node
async function scrapeNode(state: typeof MessagesAnnotation.State) {
    console.log('Scraping...');
    const result = await firecrawl.scrape('https://firecrawl.dev', { formats: ['markdown'] });
    return {
        messages: [{
            role: "system",
            content: `Scraped content: ${result.markdown}`
        }]
    };
}

// Define the analyze node
async function analyzeNode(state: typeof MessagesAnnotation.State) {
    console.log('Analyzing...');
    const response = await llm.invoke(state.messages);
    return { messages: [response] };
}

// Build the graph
const graph = new StateGraph(MessagesAnnotation)
    .addNode("scrape", scrapeNode)
    .addNode("analyze", analyzeNode)
    .addEdge(START, "scrape")
    .addEdge("scrape", "analyze")
    .addEdge("analyze", END);

// Compile the graph
const app = graph.compile();

// Run the workflow
const result = await app.invoke({
    messages: [{ role: "user", content: "Summarize the website" }]
});

console.log(JSON.stringify(result, null, 2));
```

## Multi-Step Workflow

This example demonstrates a more complex workflow that scrapes multiple URLs and processes them.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { StateGraph, Annotation, START, END } from '@langchain/langgraph';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const llm = new ChatOpenAI({ model: "gpt-5-nano", apiKey: process.env.OPENAI_API_KEY });

// Define custom state
const WorkflowState = Annotation.Root({
    urls: Annotation<string[]>(),
    scrapedData: Annotation<Array<{ url: string; content: string }>>(),
    summary: Annotation<string>()
});

// Scrape multiple URLs
async function scrapeMultiple(state: typeof WorkflowState.State) {
    const scrapedData = [];
    for (const url of state.urls) {
        const result = await firecrawl.scrape(url, { formats: ['markdown'] });
        scrapedData.push({ url, content: result.markdown || '' });
    }
    return { scrapedData };
}

// Summarize all scraped content
async function summarizeAll(state: typeof WorkflowState.State) {
    const combinedContent = state.scrapedData
        .map(item => `Content from ${item.url}:\n${item.content}`)
        .join('\n\n');

    const response = await llm.invoke([
        { role: "user", content: `Summarize these websites:\n${combinedContent}` }
    ]);

    return { summary: response.content as string };
}

// Build the workflow graph
const workflow = new StateGraph(WorkflowState)
    .addNode("scrape", scrapeMultiple)
    .addNode("summarize", summarizeAll)
    .addEdge(START, "scrape")
    .addEdge("scrape", "summarize")
    .addEdge("summarize", END);

const app = workflow.compile();

// Execute workflow
const result = await app.invoke({
    urls: ["https://firecrawl.dev", "https://firecrawl.dev/pricing"]
});

console.log(result.summary);
```

For more examples, check the [LangGraph documentation](https://langchain-ai.github.io/langgraphjs/).


# LlamaIndex
Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/llamaindex

Use Firecrawl with LlamaIndex for RAG applications

Integrate Firecrawl with LlamaIndex to build AI applications with vector search and embeddings powered by web content.

## Setup

```bash  theme={null}
npm install llamaindex @llamaindex/openai @mendable/firecrawl-js
```

Create `.env` file:

```bash  theme={null}
FIRECRAWL_API_KEY=your_firecrawl_key
OPENAI_API_KEY=your_openai_key
```

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## RAG with Vector Search

This example demonstrates how to use LlamaIndex with Firecrawl to crawl a website, create embeddings, and query the content using RAG.

```typescript  theme={null}
import Firecrawl from '@mendable/firecrawl-js';
import { Document, VectorStoreIndex, Settings } from 'llamaindex';
import { OpenAI, OpenAIEmbedding } from '@llamaindex/openai';

Settings.llm = new OpenAI({ model: "gpt-4o" });
Settings.embedModel = new OpenAIEmbedding({ model: "text-embedding-3-small" });

const firecrawl = new Firecrawl({ apiKey: process.env.FIRECRAWL_API_KEY });
const crawlResult = await firecrawl.crawl('https://firecrawl.dev', {
  limit: 10,
  scrapeOptions: { formats: ['markdown'] }
});
console.log(`Crawled ${crawlResult.data.length } pages`);

const documents = crawlResult.data.map((page: any, i: number) =>
  new Document({
    text: page.markdown,
    id_: `page-${i}`,
    metadata: { url: page.metadata?.sourceURL }
  })
);

const index = await VectorStoreIndex.fromDocuments(documents);
console.log('Vector index created with embeddings');

const queryEngine = index.asQueryEngine();
const response = await queryEngine.query({ query: 'What is Firecrawl and how does it work?' });

console.log('\nAnswer:', response.toString());
```

For more examples, check the [LlamaIndex documentation](https://ts.llamaindex.ai/).


# Mastra
Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/mastra

Use Firecrawl with Mastra for building AI workflows

Integrate Firecrawl with Mastra, the TypeScript framework for building AI agents and workflows.

## Setup

```bash  theme={null}
npm install @mastra/core @mendable/firecrawl-js zod
```

Create `.env` file:

```bash  theme={null}
FIRECRAWL_API_KEY=your_firecrawl_key
OPENAI_API_KEY=your_openai_key
```

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Multi-Step Workflow

This example demonstrates a complete workflow that searches, scrapes, and summarizes documentation using Firecrawl and Mastra.

```typescript  theme={null}
import { createWorkflow, createStep } from "@mastra/core/workflows";
import { z } from "zod";
import Firecrawl from "@mendable/firecrawl-js";
import { Agent } from "@mastra/core/agent";

const firecrawl = new Firecrawl({
  apiKey: process.env.FIRECRAWL_API_KEY || "fc-YOUR_API_KEY"
});

const agent = new Agent({
  name: "summarizer",
  instructions: "You are a helpful assistant that creates concise summaries of documentation.",
  model: "openai/gpt-5-nano",
});

// Step 1: Search with Firecrawl SDK
const searchStep = createStep({
  id: "search",
  inputSchema: z.object({
    query: z.string(),
  }),
  outputSchema: z.object({
    url: z.string(),
    title: z.string(),
  }),
  execute: async ({ inputData }: { inputData: { query: string } }) => {
    console.log(`Searching: ${inputData.query}`);
    const searchResults = await firecrawl.search(inputData.query, { limit: 1 });
    const webResults = (searchResults as any)?.web;

    if (!webResults || !Array.isArray(webResults) || webResults.length === 0) {
      throw new Error("No search results found");
    }

    const firstResult = webResults[0];
    console.log(`Found: ${firstResult.title}`);
    return {
      url: firstResult.url,
      title: firstResult.title,
    };
  },
});

// Step 2: Scrape the URL with Firecrawl SDK
const scrapeStep = createStep({
  id: "scrape",
  inputSchema: z.object({
    url: z.string(),
    title: z.string(),
  }),
  outputSchema: z.object({
    markdown: z.string(),
    title: z.string(),
  }),
  execute: async ({ inputData }: { inputData: { url: string; title: string } }) => {
    console.log(`Scraping: ${inputData.url}`);
    const scrapeResult = await firecrawl.scrape(inputData.url, {
      formats: ["markdown"],
    });

    console.log(`Scraped: ${scrapeResult.markdown?.length || 0} characters`);
    return {
      markdown: scrapeResult.markdown || "",
      title: inputData.title,
    };
  },
});

// Step 3: Summarize with Claude
const summarizeStep = createStep({
  id: "summarize",
  inputSchema: z.object({
    markdown: z.string(),
    title: z.string(),
  }),
  outputSchema: z.object({
    summary: z.string(),
  }),
  execute: async ({ inputData }: { inputData: { markdown: string; title: string } }) => {
    console.log(`Summarizing: ${inputData.title}`);

    const prompt = `Summarize the following documentation in 2-3 sentences:\n\nTitle: ${inputData.title}\n\n${inputData.markdown}`;
    const result = await agent.generate(prompt);

    console.log(`Summary generated`);
    return { summary: result.text };
  },
});

// Create workflow
export const workflow = createWorkflow({
  id: "firecrawl-workflow",
  inputSchema: z.object({
    query: z.string(),
  }),
  outputSchema: z.object({
    summary: z.string(),
  }),
  steps: [searchStep, scrapeStep, summarizeStep],
})
  .then(searchStep)
  .then(scrapeStep)
  .then(summarizeStep)
  .commit();

async function testWorkflow() {
  const run = await workflow.createRunAsync();
  const result = await run.start({
    inputData: { query: "Firecrawl documentation" }
  });

  if (result.status === "success") {
    const { summarize } = result.steps;

    if (summarize.status === "success") {
      console.log(`\n${summarize.output.summary}`);
    }
  } else {
    console.error("Workflow failed:", result.status);
  }
}

testWorkflow().catch(console.error);
```

For more examples, check the [Mastra documentation](https://mastra.ai/docs).


# OpenAI
Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/openai

Use Firecrawl with OpenAI for web scraping + AI workflows

Integrate Firecrawl with OpenAI to build AI applications powered by web data.

## Setup

```bash  theme={null}
npm install @mendable/firecrawl-js openai zod
```

Create `.env` file:

```bash  theme={null}
FIRECRAWL_API_KEY=your_firecrawl_key
OPENAI_API_KEY=your_openai_key
```

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Summarize

This example demonstrates a simple workflow: scrape a website and summarize the content using an OpenAI model.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import OpenAI from 'openai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// Scrape the website content
const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

// Summarize with OpenAI model
const completion = await openai.chat.completions.create({
    model: 'gpt-5-nano',
    messages: [
        { role: 'user', content: `Summarize: ${scrapeResult.markdown}` }
    ]
});

console.log('Summary:', completion.choices[0]?.message.content);
```

## Function Calling

This example shows how to use OpenAI's function calling feature to let the model decide when to scrape websites based on user requests.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import OpenAI from 'openai';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const ScrapeArgsSchema = z.object({
    url: z.string().describe('The URL of the website to scrape')
});

const tools = [{
    type: 'function' as const,
    function: {
        name: 'scrape_website',
        description: 'Scrape content from any website URL',
        parameters: z.toJSONSchema(ScrapeArgsSchema)
    }
}];

const response = await openai.chat.completions.create({
    model: 'gpt-5-nano',
    messages: [{
        role: 'user',
        content: 'What is Firecrawl? Visit firecrawl.dev and tell me about it.'
    }],
    tools
});

const message = response.choices[0]?.message;

if (message?.tool_calls && message.tool_calls.length > 0) {
    for (const toolCall of message.tool_calls) {
        if (toolCall.type === 'function') {
            console.log('Tool called:', toolCall.function.name);

            const args = ScrapeArgsSchema.parse(JSON.parse(toolCall.function.arguments));
            const result = await firecrawl.scrape(args.url, {
                formats: ['markdown'] // Other formats: html, links, etc.
            });
            console.log('Scraped content:', result.markdown?.substring(0, 200) + '...');

            // Send the scraped content back to the model for final response
            const finalResponse = await openai.chat.completions.create({
                model: 'gpt-5-nano',
                messages: [
                    {
                        role: 'user',
                        content: 'What is Firecrawl? Visit firecrawl.dev and tell me about it.'
                    },
                    message,
                    {
                        role: 'tool',
                        tool_call_id: toolCall.id,
                        content: result.markdown || 'No content scraped'
                    }
                ],
                tools
            });

            console.log('Final response:', finalResponse.choices[0]?.message?.content);
        }
    }
} else {
    console.log('Direct response:', message?.content);
}
```

## Structured Data Extraction

This example demonstrates how to use OpenAI models with structured outputs to extract specific data from scraped content.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import OpenAI from 'openai';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const CompanyInfoSchema = z.object({
    name: z.string(),
    industry: z.string(),
    description: z.string(),
    products: z.array(z.string())
});

const response = await openai.chat.completions.create({
    model: 'gpt-5-nano',
    messages: [
        {
            role: 'system',
            content: 'Extract company information from website content.'
        },
        {
            role: 'user',
            content: `Extract data: ${scrapeResult.markdown}`
        }
    ],
    response_format: {
        type: 'json_schema',
        json_schema: {
            name: 'company_info',
            schema: z.toJSONSchema(CompanyInfoSchema),
            strict: true
        }
    }
});

const content = response.choices[0]?.message?.content;
const companyInfo = content ? CompanyInfoSchema.parse(JSON.parse(content)) : null;
console.log('Validated company info:', companyInfo);
```

## Search + Analyze

This example combines Firecrawl's search capabilities with OpenAI model analysis to find and summarize information from multiple sources.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import OpenAI from 'openai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// Search for relevant information
const searchResult = await firecrawl.search('Next.js 16 new features', {
    limit: 3,
    sources: [{ type: 'web' }], // Other sources: { type: 'news' }, { type: 'images' }
    scrapeOptions: { formats: ['markdown'] }
});

console.log('Search results:', searchResult.web?.length, 'pages found');

// Analyze and summarize the key features
const analysis = await openai.chat.completions.create({
    model: 'gpt-5-nano',
    messages: [{
        role: 'user',
        content: `Summarize the key features: ${JSON.stringify(searchResult)}`
    }]
});

console.log('Analysis:', analysis.choices[0]?.message?.content);
```

## Responses API with MCP

This example shows how to use OpenAI's Responses API with Firecrawl configured as an MCP (Model Context Protocol) server.

```typescript  theme={null}
import OpenAI from 'openai';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const response = await openai.responses.create({
    model: 'gpt-5-nano',
    tools: [
        {
            type: 'mcp',
            server_label: 'firecrawl',
            server_description: 'A web search and scraping MCP server to scrape and extract content from websites.',
            server_url: `https://mcp.firecrawl.dev/${process.env.FIRECRAWL_API_KEY}/v2/mcp`,
            require_approval: 'never'
        }
    ],
    input: 'Find out what the top stories on Hacker News are and the latest blog post on OpenAI and summarize them in a bullet point format'
});

console.log('Response:', JSON.stringify(response.output, null, 2));
```

For more examples, check the [OpenAI documentation](https://platform.openai.com/docs).


# Vercel AI SDK
Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk

Use Firecrawl with Vercel AI SDK for web scraping + AI workflows

Integrate Firecrawl with Vercel AI SDK to build AI applications powered by web data.

## Setup

```bash  theme={null}
npm install ai @ai-sdk/openai @mendable/firecrawl-js 
```

Create `.env` file:

```bash  theme={null}
FIRECRAWL_API_KEY=your_firecrawl_key
OPENAI_API_KEY=your_openai_key
```

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Generate Text

This example demonstrates a simple workflow: scrape a website and generate text using the Vercel AI SDK.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { openai } from '@ai-sdk/openai';
import { generateText } from 'ai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const { text } = await generateText({
    model: openai('gpt-5-nano'),
    prompt: `Summarize: ${scrapeResult.markdown}`
});

console.log('Summary:', text);
```

## Scrape + Stream Text

This example shows how to stream AI responses for better user experience.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { openai } from '@ai-sdk/openai';
import { streamText } from 'ai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const { textStream } = await streamText({
    model: openai('gpt-5-nano'),
    prompt: `Analyze this company and list key products: ${scrapeResult.markdown}`
});

for await (const chunk of textStream) {
    process.stdout.write(chunk);
}
```

## Tool Calling

This example demonstrates how to use Vercel AI SDK's tool calling feature to let the model decide when to scrape websites.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { openai } from '@ai-sdk/openai';
import { generateText, tool } from 'ai';
import { z } from 'zod';

console.log('Initializing Firecrawl...');
const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const scrapeWebsiteTool = tool({
    description: 'Scrape content from any website URL',
    inputSchema: z.object({
        url: z.string().url().describe('The URL to scrape')
    }),
    execute: async ({ url }) => {
        console.log('Scraping:', url);
        const result = await firecrawl.scrape(url, {
            formats: ['markdown']
        });
        console.log('Scraped content preview:', result.markdown?.slice(0, 200) + '...');
        return { content: result.markdown };
    }
});

console.log('Generating text with AI...');

const { text, toolCalls } = await generateText({
    model: openai('gpt-5-nano'),
    prompt: 'What is Firecrawl? Visit firecrawl.dev and tell me about it.',
    tools: {
        scrapeWebsite: scrapeWebsiteTool
    },
});

console.log('Tool calls:', toolCalls);
// Continue the conversation OR use the text for something else
```

## Structured Data Extraction

This example shows how to extract structured data using Vercel AI SDK's structured output feature.

```typescript  theme={null}
import FirecrawlApp from '@mendable/firecrawl-js';
import { openai } from '@ai-sdk/openai';
import { generateObject } from 'ai';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const CompanyInfoSchema = z.object({
    name: z.string(),
    industry: z.string(),
    description: z.string(),
    products: z.array(z.string())
});

const { object } = await generateObject({
    model: openai('gpt-5-nano'),
    schema: CompanyInfoSchema,
    prompt: `Extract company information from this website content: ${scrapeResult.markdown}`
});

console.log('Extracted company info:', object);
```

For more examples, check the [Vercel AI SDK documentation](https://sdk.vercel.ai/docs).


# MCP Web Search & Scrape in Claude Code
Source: https://docs.firecrawl.dev/developer-guides/mcp-setup-guides/claude-code

Add web scraping and search to Claude Code in 2 minutes

Add web scraping and search capabilities to Claude Code with Firecrawl MCP.

## Quick Setup

### 1. Get Your API Key

Sign up at [firecrawl.dev/app](https://firecrawl.dev/app) and copy your API key.

### 2. Add Firecrawl MCP Server

```bash  theme={null}
claude mcp add firecrawl -e FIRECRAWL_API_KEY=your-api-key -- npx -y firecrawl-mcp
```

Replace `your-api-key` with your actual Firecrawl API key.

Done! You can now search and scrape the web from Claude Code.

## Quick Demo

Try these in Claude Code:

**Search the web:**

```
Search for the latest Next.js 15 features
```

**Scrape a page:**

```
Scrape firecrawl.dev and tell me what it does
```

**Get documentation:**

```
Find and scrape the Stripe API docs for payment intents
```

Claude will automatically use Firecrawl's search and scrape tools to get the information.


# MCP Web Search & Scrape in Cursor
Source: https://docs.firecrawl.dev/developer-guides/mcp-setup-guides/cursor

Add web scraping and search to Cursor in 2 minutes

Add web scraping and search capabilities to Cursor with Firecrawl MCP.

## Quick Setup

### 1. Get Your API Key

Sign up at [firecrawl.dev/app](https://firecrawl.dev/app) and copy your API key.

### 2. Add to Cursor

Open Settings (`Cmd+,`), search for "MCP", and add:

```json  theme={null}
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

Replace `your_api_key_here` with your actual Firecrawl API key.

### 3. Restart Cursor

Done! You can now search and scrape the web from Cursor.

## Quick Demo

Try these in Cursor Chat (`Cmd+K`):

**Search:**

```
Search for TypeScript best practices 2025
```

**Scrape:**

```
Scrape firecrawl.dev and tell me what it does
```

**Get docs:**

```
Scrape the React hooks documentation and explain useEffect
```

Cursor will automatically use Firecrawl tools.


# MCP Web Search & Scrape in Factory AI
Source: https://docs.firecrawl.dev/developer-guides/mcp-setup-guides/factory-ai

Add web scraping and search to Factory AI in 2 minutes

Add web scraping and search capabilities to Factory AI with Firecrawl MCP.

## Quick Setup

### 1. Get Your API Key

Sign up at [firecrawl.dev/app](https://firecrawl.dev/app) and copy your API key.

### 2. Install Factory AI CLI

Install the [Factory AI CLI](https://docs.factory.ai/cli/getting-started/quickstart) if you haven't already:

**macOS/Linux:**

```bash  theme={null}
curl -fsSL https://app.factory.ai/cli | sh
```

**Windows:**

```powershell  theme={null}
iwr https://app.factory.ai/cli/install.ps1 -useb | iex
```

### 3. Add Firecrawl MCP Server

In the Factory droid CLI, add Firecrawl using the `/mcp add` command:

```bash  theme={null}
/mcp add firecrawl "npx -y firecrawl-mcp" -e FIRECRAWL_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with your actual Firecrawl API key.

### 4. Done!

The Firecrawl tools are now available in your Factory AI session!

## Quick Demo

Try these in Factory AI:

**Search the web:**

```
Search for the latest Next.js 15 features
```

**Scrape a page:**

```
Scrape firecrawl.dev and tell me what it does
```

**Get documentation:**

```
Find and scrape the Stripe API docs for payment intents
```

Factory will automatically use Firecrawl's search and scrape tools to get the information.


# MCP Web Search & Scrape in Windsurf
Source: https://docs.firecrawl.dev/developer-guides/mcp-setup-guides/windsurf

Add web scraping and search to Windsurf in 2 minutes

Add web scraping and search capabilities to Windsurf with Firecrawl MCP.

## Quick Setup

### 1. Get Your API Key

Sign up at [firecrawl.dev/app](https://firecrawl.dev/app) and copy your API key.

### 2. Add to Windsurf

Add this to your `./codeium/windsurf/model_config.json`:

```json  theme={null}
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

Replace `YOUR_API_KEY` with your actual Firecrawl API key.

### 3. Restart Windsurf

Done! Windsurf can now search and scrape the web.

## Quick Demo

Try these in Windsurf:

**Search:**

```
Search for the latest Tailwind CSS features
```

**Scrape:**

```
Scrape firecrawl.dev and explain what it does
```

**Get docs:**

```
Find and scrape the Supabase authentication documentation
```

Windsurf's AI agents will automatically use Firecrawl tools.


# Firecrawl + Dify
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

## Getting Started

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

## Usage Patterns

<Tabs>
  <Tab title="Chatflow Apps">
    **Visual Pipeline Integration**

    1. Add Firecrawl node to your pipeline
    2. Select action (Map, Crawl, Scrape)
    3. Define input variables
    4. Execute pipeline sequentially

    **Example Flow:**

    ```
    User Input → Firecrawl (Scrape) → LLM Processing → Response
    ```
  </Tab>

  <Tab title="Workflow Apps">
    **Automated Data Processing**

    Build multi-step workflows with:

    * Scheduled scraping
    * Data transformation
    * Database storage
    * Notifications

    **Example Flow:**

    ```
    Schedule Trigger → Firecrawl (Crawl) → Data Processing → Storage
    ```
  </Tab>

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

## Common Use Cases

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

## Firecrawl Actions

| Tool          | Description                    | Best For                |
| ------------- | ------------------------------ | ----------------------- |
| **Scrape**    | Single-page data extraction    | Quick content capture   |
| **Crawl**     | Multi-page recursive crawling  | Full site extraction    |
| **Map**       | URL discovery and site mapping | SEO analysis, URL lists |
| **Crawl Job** | Async job management           | Long-running operations |

## Best Practices

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


# Firecrawl + Make
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

    ***

    ### Extract a Website

    Extract structured data from pages using LLMs

    ***

    ### Scrape a Website

    Scrape a URL and get its content from a single page

    ***

    ### Map a Website

    Map multiple URLs based on options

    ***

    ### Search a Website

    Web search (SERP) with Firecrawl's scraping capabilities

    ***

    ### Get Crawl Status

    Get the status of a given crawl event ID

    ***

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

## Getting Started

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

## Best Practices

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


# Firecrawl + n8n
Source: https://docs.firecrawl.dev/developer-guides/workflow-automation/n8n

Learn how to use Firecrawl with n8n for web scraping automation, a complete step-by-step guide.

## Introduction to Firecrawl and n8n

Web scraping automation has become essential for modern businesses. Whether you need to monitor competitor prices, aggregate content, generate leads, or power AI applications with real-time data, the combination of Firecrawl and n8n provides a powerful solution without requiring programming knowledge.

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=cb863000a893ef260cfe023e2455c88c" alt="Firecrawl and n8n integration" data-og-width="1536" width="1536" data-og-height="1024" height="1024" data-path="images/guides/n8n/firecrawl-n8n-integration-hero.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?w=280&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=f1f3cc979a390121e6683ac8ce626bb2 280w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?w=560&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=f3e7b4bf8a4d6582389a9fff0c36cda2 560w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?w=840&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=d556ffd5a96e792ee7a8432b4262bd74 840w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?w=1100&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=a4ea6455383005074991026683bedef6 1100w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?w=1650&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=15402611e1a949138b65844df4be6b5f 1650w, https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?w=2500&fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=226545dc94de7d3639b08f78c56c7d39 2500w" />

**What is n8n?**

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

### Get Your API Key

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

**Self-Hosted:**

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

**Prerequisites:**

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed on your computer
* Basic familiarity with command line/terminal

**Installation Steps:**

1. Open your terminal or command prompt
2. Create a Docker volume to persist your workflow data:

```bash  theme={null}
docker volume create n8n_data
```

This volume stores your workflows, credentials, and execution history so they persist even if you restart the container.

3. Run the n8n Docker container:

```bash  theme={null}
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

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
   https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
   ```
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

```javascript  theme={null}
const results = $input.all();
let message = "Latest AI News:\n\n";

results.forEach((item) => {
  const webData = item.json.data.web;
  webData.forEach((article, index) => {
    message += `${index + 1}. ${article.title}\n`;
    message += `${article.description}\n`;
    message += `${article.url}\n\n`;
  });
});

return [{ json: { message } }];
```

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
You are an AI news analyst. Analyze the provided AI news articles and create a concise,
insightful summary highlighting the most important developments and trends.
Group related topics together and provide context about why these developments matter.
Keep the summary conversational and engaging, around 3-4 paragraphs.
```

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

**What it does:**

* Scrapes a single URL
* Returns clean markdown, HTML, or AI-generated summaries
* Can capture screenshots and extract links

**Best for:**

* Article extraction
* Product page monitoring
* Blog post scraping
* Generating page summaries

**Example use case:** Daily blog summaries (like Example 1 above)

### Search and optionally scrape search results

Performs web searches and returns results with optional content scraping.

**What it does:**

* Searches the web, news, or images
* Returns titles, descriptions, and URLs
* Optionally scrapes the full content of results

**Best for:**

* Research automation
* News monitoring
* Trend discovery
* Finding relevant content

**Example use case:** AI news aggregation (like Example 2 above)

### Crawl a website

Recursively discovers and scrapes multiple pages from a website.

**What it does:**

* Follows links automatically
* Scrapes multiple pages in one operation
* Can filter URLs by patterns

**Best for:**

* Full documentation extraction
* Site archiving
* Multi-page data collection

### Map a website and get urls

Returns all URLs found on a website without scraping content.

**What it does:**

* Discovers all links on a site
* Returns clean URL list
* Fast and lightweight

**Best for:**

* URL discovery
* Sitemap generation
* Planning larger crawls

### Extract Data

Uses AI to extract structured information based on custom prompts or schemas.

**What it does:**

* AI-powered data extraction
* Returns data in your specified format
* Works across multiple pages

**Best for:**

* Custom data extraction
* Building databases
* Structured information gathering

### Batch Scrape

Scrapes multiple URLs in parallel efficiently.

**What it does:**

* Processes multiple URLs at once
* More efficient than loops
* Returns all results together

**Best for:**

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

## Best Practices

Follow these guidelines to build reliable, efficient workflows:

### Testing and Debugging

* Always test workflows manually before activating schedules
* Use the "**Execute Workflow**" button to test the entire flow
* Check output data at each node to verify correctness
* Use the "**Executions**" tab to review past runs and debug issues

<img src="https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-debugging.gif?s=2962335b6f72ea39cf6cb68cb6ed83c3" alt="Executions tab showing workflow run history with timestamps and status" data-og-width="2080" width="2080" data-og-height="1080" height="1080" data-path="images/guides/n8n/n8n-debugging.gif" data-optimize="true" data-opv="3" />

### Error Handling

* Add Error Trigger nodes to catch and handle failures
* Set up notifications when workflows fail
* Use the "**Continue On Fail**" setting for non-critical nodes
* Monitor your workflow executions regularly

### Performance Optimization

* Use Batch Scrape for multiple URLs instead of loops
* Set appropriate rate limits to avoid overwhelming target sites
* Cache data when possible to reduce unnecessary requests
* Schedule intensive workflows during off-peak hours

### Security

* Never expose API keys in workflow configurations
* Use n8n's credential system to securely store authentication
* Be careful when sharing workflows publicly
* Follow target websites' terms of service and robots.txt

## Next Steps

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


# Firecrawl + Zapier
Source: https://docs.firecrawl.dev/developer-guides/workflow-automation/zapier

Official tutorials and Zapier integration templates for Firecrawl + Zapier automation

<Note>
  **Official Zapier Integration:** [zapier.com/apps/firecrawl/integrations](https://zapier.com/apps/firecrawl/integrations)

  Connect with 8,000+ apps • No-code automation • Pre-built Zap templates • Cloud-based
</Note>

## Official Blog Post

<Card title="How Zapier uses Firecrawl" icon="rocket" href="https://www.firecrawl.dev/blog/how-zapier-uses-firecrawl-to-power-chatbots">
  Real-world case study: How Zapier integrated Firecrawl into Zapier Chatbots in a single afternoon.
</Card>

## Popular Integrations

<AccordionGroup>
  <Accordion title="Data Storage & Databases" icon="database">
    ### Google Sheets

    → [View Integration](https://zapier.com/apps/google-sheets/integrations/firecrawl)

    Track competitor data, centralize marketing insights, and automate data collection.

    **Best For:** Business owners, marketing teams

    ***

    ### Airtable

    → [View Integration](https://zapier.com/apps/airtable/integrations/firecrawl)

    Build lead generation databases and content aggregation systems with structured storage.

    **Best For:** Sales teams, project managers

    ***

    ### Zapier Tables

    → [View Integration](https://zapier.com/apps/zapier-tables/integrations/firecrawl)

    No-code database automation for employee onboarding and centralized lead management.

    **Best For:** HR teams, operations
  </Accordion>

  <Accordion title="Communication & Notifications" icon="bell">
    ### Slack

    → [View Integration](https://zapier.com/apps/slack/integrations/firecrawl)

    Get website change notifications, competitor monitoring alerts, and market intelligence updates.

    **Best For:** Marketing teams, product managers

    ***

    ### Telegram

    → [View Integration](https://zapier.com/apps/telegram/integrations/firecrawl)

    Instant price alerts, breaking news notifications, and real-time monitoring.

    **Best For:** Traders, news enthusiasts
  </Accordion>

  <Accordion title="CRM & Sales" icon="briefcase">
    ### HubSpot

    → [View Integration](https://zapier.com/apps/hubspot/integrations/firecrawl)

    Contact enrichment, lead scoring with web data, and marketing automation.

    **Best For:** Marketing ops, sales ops

    ***

    ### Pipedrive

    → [View Integration](https://zapier.com/apps/pipedrive/integrations/firecrawl)

    Lead enrichment from websites and competitor intelligence tracking.

    **Best For:** Sales teams, account executives

    ***

    ### Attio

    → [View Integration](https://zapier.com/apps/attio/integrations/firecrawl)

    Modern CRM data enrichment and relationship intelligence.

    **Best For:** Modern sales teams
  </Accordion>

  <Accordion title="Productivity & Documentation" icon="file-lines">
    ### Google Docs

    → [View Integration](https://zapier.com/apps/google-docs/integrations/firecrawl)

    Automated report generation, research documentation, and content aggregation.

    **Best For:** Researchers, content creators

    ***

    ### Notion

    → [View Integration](https://zapier.com/apps/notion/integrations/firecrawl)

    Knowledge base updates, research library building, and content curation.

    **Best For:** Product teams, researchers
  </Accordion>

  <Accordion title="Zapier Native Tools" icon="zap">
    ### Schedule by Zapier

    → [View Integration](https://zapier.com/apps/schedule/integrations/firecrawl)

    Run hourly, daily, weekly, or monthly scraping automatically.

    ***

    ### Zapier Interfaces

    → [View Integration](https://zapier.com/apps/interfaces/integrations/firecrawl)

    Build custom internal tools with form-based scraping and team dashboards.

    **Best For:** Operations teams

    ***

    ### Zapier Chatbots

    → [View Integration](https://zapier.com/apps/zapier-chatbots/integrations/firecrawl)

    AI chatbots with live web knowledge for customer support and lead generation.

    <Info>Official Zapier product uses Firecrawl internally</Info>
  </Accordion>
</AccordionGroup>

## Firecrawl Actions

| Action                      | Use Case                                  |
| --------------------------- | ----------------------------------------- |
| **Scrape URL**              | Quick single-page data capture            |
| **Crawl Website**           | Full site scraping with multiple pages    |
| **Extract Structured Data** | AI-powered extraction with custom schemas |
| **Search Web**              | Research automation with search + scrape  |
| **Map Website**             | SEO analysis and site structure mapping   |

## Quick Reference

<CardGroup cols={2}>
  <Card title="Getting Started" icon="play">
    1. Sign up at [firecrawl.dev](https://firecrawl.dev)
    2. Get your API key
    3. Create a Zap in Zapier
    4. Connect Firecrawl with your API key
    5. Choose your workflow and activate
  </Card>

  <Card title="Best Practices" icon="lightbulb">
    * Use `/Scrape URL` for single pages (faster)
    * Schedule strategically (hourly/daily/weekly)
    * Test in Firecrawl playground first
    * Add error handling for failed scrapes
    * Use filters to prevent unnecessary runs
  </Card>
</CardGroup>

## Industry Use Cases

<AccordionGroup>
  <Accordion title="E-commerce" icon="cart-shopping">
    * Price monitoring across competitors
    * Product availability tracking
    * Review aggregation
  </Accordion>

  <Accordion title="Real Estate" icon="house">
    * Listing aggregation
    * Market trend analysis
    * Property data collection
  </Accordion>

  <Accordion title="Marketing" icon="bullhorn">
    * Competitor content tracking
    * SEO monitoring
    * Backlink analysis
  </Accordion>

  <Accordion title="Finance" icon="chart-line">
    * Market data collection
    * News aggregation
    * Regulatory filing monitoring
  </Accordion>

  <Accordion title="Recruitment" icon="user-tie">
    * Job posting aggregation
    * Company research automation
    * Candidate information enrichment
  </Accordion>
</AccordionGroup>

## Zapier vs n8n

| Feature          | Zapier                                | n8n                      |
| ---------------- | ------------------------------------- | ------------------------ |
| **Setup**        | No-code, cloud-based                  | Self-hosted or cloud     |
| **Pricing**      | Per-task pricing                      | Flat monthly             |
| **Integrations** | 8,000+ apps                           | 400+ integrations        |
| **Best For**     | Quick automation, non-technical users | Custom logic, developers |

<Tip>
  **Pro Tip:** Start with Zapier's pre-built templates and customize as needed. Perfect for quick, no-code automation!
</Tip>


# Batch Scrape
Source: https://docs.firecrawl.dev/features/batch-scrape

Batch scrape multiple URLs

## Batch scraping multiple URLs

You can now batch scrape multiple URLs at the same time. It takes the starting URLs and optional parameters as arguments. The params argument allows you to specify additional options for the batch scrape job, such as the output formats.

### How it works

It is very similar to how the `/crawl` endpoint works. You can either start the batch and wait for completion, or start it and handle completion yourself.

* `batchScrape` (JS) / `batch_scrape` (Python): starts a batch job and waits for it to complete, returning the results.
* `startBatchScrape` (JS) / `start_batch_scrape` (Python): starts a batch job and returns the job ID so you can poll or use webhooks.

### Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  start = firecrawl.start_batch_scrape([
      "https://firecrawl.dev",
      "https://docs.firecrawl.dev",
  ], formats=["markdown"])  # returns id

  job = firecrawl.batch_scrape([
      "https://firecrawl.dev",
      "https://docs.firecrawl.dev",
  ], formats=["markdown"], poll_interval=2, wait_timeout=120)

  print(job.status, job.completed, job.total)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  // Start a batch scrape job
  const { id } = await firecrawl.startBatchScrape([
    'https://firecrawl.dev',
    'https://docs.firecrawl.dev'
  ], {
    options: { formats: ['markdown'] },
  });

  // Wait for completion
  const job = await firecrawl.batchScrape([
    'https://firecrawl.dev',
    'https://docs.firecrawl.dev'
  ], { options: { formats: ['markdown'] }, pollInterval: 2, timeout: 120 });

  console.log(job.status, job.completed, job.total);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/batch/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "urls": ["https://firecrawl.dev", "https://docs.firecrawl.dev"],
      "formats": ["markdown"]
    }'
  ```
</CodeGroup>

### Response

Calling `batchScrape`/`batch_scrape` returns the full results when the batch completes.

```json Completed theme={null}
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "markdown": "[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
      "metadata": {
        "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
        "language": "en",
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
        "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",
        "ogLocaleAlternate": [],
        "statusCode": 200
      }
    },
    ...
  ]
}
```

Calling `startBatchScrape`/`start_batch_scrape` returns
a job ID you can track via `getBatchScrapeStatus`/`get_batch_scrape_status`, using
the API endpoint `/batch/scrape/{id}`, or webhooks. This endpoint is intended for
in-progress checks or immediately after completion, **as batch jobs expire after
24 hours**.

```json  theme={null}
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Batch scrape with structured extraction

You can also use the batch scrape endpoint to extract structured data from the pages. This is useful if you want to get the same structured data from a list of URLs.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Scrape multiple websites:
  batch_scrape_result = firecrawl.batch_scrape(
      ['https://docs.firecrawl.dev', 'https://docs.firecrawl.dev/sdks/overview'], 
      formats=[{
          'type': 'json',
          'prompt': 'Extract the title and description from the page.',
          'schema': {
              'type': 'object',
              'properties': {
                  'title': {'type': 'string'},
                  'description': {'type': 'string'}
              },
              'required': ['title', 'description']
          }
      }]
  )
  print(batch_scrape_result)

  # Or, you can use the start method:
  batch_scrape_job = firecrawl.start_batch_scrape(
      ['https://docs.firecrawl.dev', 'https://docs.firecrawl.dev/sdks/overview'], 
      formats=[{
          'type': 'json',
          'prompt': 'Extract the title and description from the page.',
          'schema': {
              'type': 'object',
              'properties': {
                  'title': {'type': 'string'},
                  'description': {'type': 'string'}
              },
              'required': ['title', 'description']
          }
      }]
  )
  print(batch_scrape_job)

  # You can then use the job ID to check the status of the batch scrape:
  batch_scrape_status = firecrawl.get_batch_scrape_status(batch_scrape_job.id)
  print(batch_scrape_status)
  ```

  ```js Node theme={null}
  import Firecrawl, { ScrapeResponse } from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

  // Define schema to extract contents into
  const schema = {
    type: "object",
    properties: {
      title: { type: "string" },
      description: { type: "string" }
    },
    required: ["title", "description"]
  };

  // Scrape multiple websites (synchronous):
  const batchScrapeResult = await firecrawl.batchScrape(['https://docs.firecrawl.dev', 'https://docs.firecrawl.dev/sdks/overview'], { 
    formats: [
      {
        type: "json",
        prompt: "Extract the title and description from the page.",
        schema: schema
      }
    ]
  });

  // Output all the results of the batch scrape:
  console.log(batchScrapeResult)

  // Or, you can use the start method:
  const batchScrapeJob = await firecrawl.startBatchScrape(['https://docs.firecrawl.dev', 'https://docs.firecrawl.dev/sdks/overview'], { 
    formats: [
      {
        type: "json",
        prompt: "Extract the title and description from the page.",
        schema: schema
      }
    ]
  });
  console.log(batchScrapeJob)

  // You can then use the job ID to check the status of the batch scrape:
  const batchScrapeStatus = await firecrawl.getBatchScrapeStatus(batchScrapeJob.id);
  console.log(batchScrapeStatus)
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/batch/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "urls": ["https://docs.firecrawl.dev", "https://docs.firecrawl.dev/sdks/overview"],
        "formats" : [{
          "type": "json",
          "prompt": "Extract the title and description from the page.",
          "schema": {
            "type": "object",
            "properties": {
              "title": {
                "type": "string"
              },
              "description": {
                "type": "string"
              }
            },
            "required": [
              "title",
              "description"
            ]
          }
        }]
      }'
  ```
</CodeGroup>

### Response

`batchScrape`/`batch_scrape` returns full results:

```json Completed theme={null}
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "json": {
        "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
        "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot."
      }
    },
    ...
  ]
}
```

`startBatchScrape`/`start_batch_scrape` returns a job ID:

```json  theme={null}
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Batch scrape with webhooks

You can configure webhooks to receive real-time notifications as each URL in your batch is scraped. This allows you to process results immediately instead of waiting for the entire batch to complete.

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/batch/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
      ],
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }' 
```

For comprehensive webhook documentation including event types, payload structure, and implementation examples, see the [Webhooks documentation](/webhooks/overview).

### Quick Reference

**Event Types:**

* `batch_scrape.started` - When the batch scrape begins
* `batch_scrape.page` - For each URL successfully scraped
* `batch_scrape.completed` - When all URLs are processed
* `batch_scrape.failed` - If the batch scrape encounters an error

**Basic Payload:**

```json  theme={null}
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "batch-job-id",
  "data": [...], // Page data for 'page' events
  "metadata": {}, // Your custom metadata
  "error": null
}
```

<Note>
  For detailed webhook configuration, security best practices, and
  troubleshooting, visit the [Webhooks documentation](/webhooks/overview).
</Note>


# Change Tracking
Source: https://docs.firecrawl.dev/features/change-tracking

Firecrawl can track changes between the current page and a previous version, and tell you if it updated or not

<img src="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=cc56c24d15e1b2ed4806ddb66d0f5c3f" alt="Change Tracking" data-og-width="2400" width="2400" data-og-height="1350" height="1350" data-path="images/launch-week/lw3d12.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?w=280&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2f46113bc318badaeaf0fb32e7645df8 280w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?w=560&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2fd31b621bcb393815715ce8fe1e5abd 560w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?w=840&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2423ca2755bdb28f4d3e64e1abffebf6 840w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?w=1100&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=cc14d2752f8888824b84ea121fcbbb7d 1100w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?w=1650&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2e8a59b9d8f69c378551f4c5ff20e13d 1650w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?w=2500&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=830c7f2a9465d9f6f3733a5289a5e9fe 2500w" />

Change tracking allows you to monitor and detect changes in web content over time. This feature is available in both the JavaScript and Python SDKs.

## Overview

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

## SDKs

### Basic Usage

To use change tracking, include `'changeTracking'` in the formats when scraping a URL:

<CodeGroup>
  ```js Node theme={null}
  const firecrawl = new Firecrawl({ apiKey: 'your-api-key' });
  const result = await firecrawl.scrape('https://example.com', {
    formats: ['markdown', 'changeTracking']
  });

  // Access change tracking data
  console.log(result.changeTracking)
  ```

  ```python Python theme={null}
  from firecrawl import Firecrawl
  from pydantic import BaseModel

  firecrawl = Firecrawl(api_key='your-api-key')
  result = firecrawl.scrape('https://example.com',
      formats=['markdown', 'change_tracking']
  )

  # Access change tracking data
  print("Change Tracking:", result.change_tracking)
  ```
</CodeGroup>

Example Response:

```json  theme={null}
{
  "url": "https://firecrawl.dev",
  "markdown": "# AI Agents for great customer experiences\n\nChatbots that delight your users...",
  "changeTracking": {
    "previousScrapeAt": "2025-04-10T12:00:00Z",
    "changeStatus": "changed",
    "visibility": "visible"
  }
}
```

### Advanced Options

You can configure change tracking by passing an object in the `formats` array:

<CodeGroup>
  ```js Node theme={null}
  const result = await firecrawl.scrape('https://example.com', {
    formats: [
      'markdown',
      {
        type: 'changeTracking',
        modes: ['git-diff', 'json'], // Enable specific change tracking modes
        schema: {
          type: 'object',
          properties: {
            title: { type: 'string' },
            content: { type: 'string' }
          }
        }, // Schema for structured JSON comparison
        prompt: 'Custom prompt for extraction', // Optional custom prompt
        tag: 'production' // Optional tag for separate change tracking histories
      }
    ]
  });

  // Access git-diff format changes
  if (result.changeTracking.diff) {
    console.log(result.changeTracking.diff.text); // Git-style diff text
    console.log(result.changeTracking.diff.json); // Structured diff data
  }

  // Access JSON comparison changes
  if (result.changeTracking.json) {
    console.log(result.changeTracking.json.title.previous); // Previous title
    console.log(result.changeTracking.json.title.current); // Current title
  }
  ```

  ```python Python theme={null}
  result = firecrawl.scrape('https://example.com',
      formats=[
          'markdown',
          {
              'type': 'change_tracking',
              'modes': ['git-diff', 'json'],  # Enable specific change tracking modes
              'schema': {
                  'type': 'object',
                  'properties': {
                      'title': {'type': 'string'},
                      'content': {'type': 'string'}
                  }
              },  # Schema for structured JSON comparison
              'prompt': 'Custom prompt for extraction',  # Optional custom prompt
              'tag': 'production'  # Optional tag for separate change tracking histories
          }
      ]
  )

  # Access git-diff format changes
  if 'diff' in result.change_tracking:
      print(result.change_tracking.diff.text)  # Git-style diff text
      print(result.change_tracking.diff.json)  # Structured diff data

  # Access JSON comparison changes
  if 'json' in result.change_tracking:
      print(result.change_tracking.json.title.previous)  # Previous title
      print(result.change_tracking.json.title.current)  # Current title
  ```
</CodeGroup>

### Git-Diff Results Example:

```
 **April, 13 2025**
 
-**05:55:05 PM**
+**05:58:57 PM**

...
```

### JSON Comparison Results Example:

```json  theme={null}
{
  "time": { 
    "previous": "2025-04-13T17:54:32Z", 
    "current": "2025-04-13T17:55:05Z" 
  }
}
```

### Data Models

The change tracking feature includes the following data models:

<CodeGroup>
  ```js Node theme={null}
  interface FirecrawlDocument {
    // ... other properties
    changeTracking?: {
      previousScrapeAt: string | null;
      changeStatus: "new" | "same" | "changed" | "removed";
      visibility: "visible" | "hidden";
      diff?: {
        text: string;
        json: {
          files: Array<{
            from: string | null;
            to: string | null;
            chunks: Array<{
              content: string;
              changes: Array<{
                type: string;
                normal?: boolean;
                ln?: number;
                ln1?: number;
                ln2?: number;
                content: string;
              }>;
            }>;
          }>;
        };
      };
      json?: any;
    };
  }

  interface ChangeTrackingFormat {
    type: 'changeTracking';
    prompt?: string;
    schema?: any;
    modes?: ("json" | "git-diff")[];
    tag?: string | null;
  }

  interface ScrapeParams {
    // ... other properties
    formats?: Array<'markdown' | 'html' | ChangeTrackingFormat>;
  }
  ```

  ```python Python theme={null}
  class ChangeTrackingData(BaseModel):
      """
      Data for the change tracking format.
      """
      previous_scrape_at: Optional[str] = None
      change_status: str  # "new" | "same" | "changed" | "removed"
      visibility: str  # "visible" | "hidden"
      diff: Optional[Dict[str, Any]] = None
      json: Optional[Dict[str, Any]] = None
  ```
</CodeGroup>

## Change Tracking Modes

The change tracking feature supports two modes:

### Git-Diff Mode

The `git-diff` mode provides a traditional diff format similar to Git's output. It shows line-by-line changes with additions and deletions marked.

Example output:

```
@@ -1,1 +1,1 @@
-old content
+new content
```

The structured JSON representation of the diff includes:

* `files`: Array of changed files (in web context, typically just one)
* `chunks`: Sections of changes within a file
* `changes`: Individual line changes with type (add, delete, normal)

### JSON Mode

The `json` mode provides a structured comparison of specific fields extracted from the content. This is useful for tracking changes in specific data points rather than the entire content.

Example output:

```json  theme={null}
{
  "title": {
    "previous": "Old Title",
    "current": "New Title"
  },
  "price": {
    "previous": "$19.99",
    "current": "$24.99"
  }
}
```

To use JSON mode, you need to provide a schema that defines the fields to extract and compare.

## Important Facts

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

## Examples

### Basic Scrape Example

```json  theme={null}
// Request
{
    "url": "https://firecrawl.dev",
    "formats": ["markdown", "changeTracking"]
}

// Response
{
  "success": true,
  "data": {
    "markdown": "...",
    "metadata": {...},
    "changeTracking": {
      "previousScrapeAt": "2025-03-30T15:07:17.543071+00:00",
      "changeStatus": "same",
      "visibility": "visible"
    }
  }
}
```

### Crawl Example

```json  theme={null}
// Request
{
    "url": "https://firecrawl.dev",
    "scrapeOptions": {
        "formats": ["markdown", "changeTracking"]
    }
}
```

### Tracking Product Price Changes

<CodeGroup>
  ```js Node theme={null}
  const result = await firecrawl.scrape('https://example.com/product', {
    formats: [
      'markdown',
      {
        type: 'changeTracking',
        modes: ['json'],
        schema: {
          type: 'object',
          properties: {
            price: { type: 'string' },
            availability: { type: 'string' }
          }
        }
      }
    ]
  });

  if (result.changeTracking.changeStatus === 'changed') {
    console.log(`Price changed from ${result.changeTracking.json.price.previous} to ${result.changeTracking.json.price.current}`);
  }
  ```

  ```python Python theme={null}
  result = firecrawl.scrape('https://example.com/product',
      formats=[
          'markdown',
          {
              'type': 'change_tracking',
              'modes': ['json'],
              'schema': {
                  'type': 'object',
                  'properties': {
                      'price': {'type': 'string'},
                      'availability': {'type': 'string'}
                  }
              }
          }
      ]
  )

  if result.change_tracking.change_status == 'changed':
      print(f"Price changed from {result.change_tracking.json.price.previous} to {result.change_tracking.json.price.current}")
  ```
</CodeGroup>

### Monitoring Content Changes with Git-Diff

<CodeGroup>
  ```js Node theme={null}
  const result = await firecrawl.scrape('https://example.com/blog', {
    formats: [
      'markdown',
      { type: 'changeTracking', modes: ['git-diff'] }
    ]
  });

  if (result.changeTracking.changeStatus === 'changed') {
    console.log('Content changes:');
    console.log(result.changeTracking.diff.text);
  }
  ```

  ```python Python theme={null}
  result = firecrawl.scrape('https://example.com/blog',
      formats=[
          'markdown',
          { 'type': 'change_tracking', 'modes': ['git-diff'] }
      ]
  )

  if result.change_tracking.change_status == 'changed':
      print('Content changes:')
      print(result.change_tracking.diff.text)
  ```
</CodeGroup>

## Billing

The change tracking feature is currently in beta. Using the basic change tracking functionality and `git-diff` mode has no additional cost. However, if you use the `json` mode for structured data comparison, the page scrape will cost 5 credits per page.


# Crawl
Source: https://docs.firecrawl.dev/features/crawl

Firecrawl can recursively search through a urls subdomains, and gather the content

Firecrawl efficiently crawls websites to extract comprehensive data while bypassing blockers. The process:

1. **URL Analysis:** Scans sitemap and crawls website to identify links
2. **Traversal:** Recursively follows links to find all subpages
3. **Scraping:** Extracts content from each page, handling JS and rate limits
4. **Output:** Converts data to clean markdown or structured format

This ensures thorough data collection from any starting URL.

## Crawling

### /crawl endpoint

Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.

<Warning>
  By default - Crawl will ignore sublinks of a page if they aren't children of
  the url you provide. So, the website.com/other-parent/blog-1 wouldn't be
  returned if you crawled website.com/blogs/. If you want
  website.com/other-parent/blog-1, use the `crawlEntireDomain` parameter. To
  crawl subdomains like blog.website.com when crawling website.com, use the
  `allowSubdomains` parameter.
</Warning>

### Installation

<CodeGroup>
  ```python Python theme={null}
  # pip install firecrawl-py

  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
  ```

  ```js Node theme={null}
  # npm install @mendable/firecrawl-js

  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
  ```
</CodeGroup>

### Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  docs = firecrawl.crawl(url="https://docs.firecrawl.dev", limit=10)
  print(docs)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const docs = await firecrawl.crawl('https://docs.firecrawl.dev', { limit: 10 });
  console.log(docs);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/crawl" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 10
    }'
  ```
</CodeGroup>

### Scrape options in crawl

All options from the Scrape endpoint are available in Crawl via `scrapeOptions` (JS) / `scrape_options` (Python). These apply to every page the crawler scrapes: formats, proxy, caching, actions, location, tags, etc. See the full list in the [Scrape API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

<CodeGroup>
  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR_API_KEY' });

  // Crawl with scrape options
  const crawlResponse = await firecrawl.crawl('https://example.com', {
    limit: 100,
    scrapeOptions: {
      formats: [
        'markdown',
        {
          type: 'json',
          schema: { type: 'object', properties: { title: { type: 'string' } } },
        },
      ],
      proxy: 'auto',
      maxAge: 600000,
      onlyMainContent: true,
    },
  });
  ```

  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

  # Crawl with scrape options
  response = firecrawl.crawl('https://example.com',
      limit=100,
      scrape_options={
          'formats': [
              'markdown',
              { 'type': 'json', 'schema': { 'type': 'object', 'properties': { 'title': { 'type': 'string' } } } }
          ],
          'proxy': 'auto',
          'maxAge': 600000,
          'onlyMainContent': True
      }
  )
  ```
</CodeGroup>

### API Response

If you're using cURL or the starter method, this will return an `ID` to check the status of the crawl.

<Note>
  If you're using the SDK, see methods below for waiter vs starter behavior.
</Note>

```json  theme={null}
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
}
```

### Check Crawl Job

Used to check the status of a crawl job and get its result.

<Note>
  This endpoint only works for crawls that are in progress or crawls that have
  completed recently.{' '}
</Note>

<CodeGroup>
  ```python Python theme={null}
  status = firecrawl.get_crawl_status("<crawl-id>")
  print(status)
  ```

  ```js Node theme={null}
  const status = await firecrawl.getCrawlStatus("<crawl-id>");
  console.log(status);
  ```

  ```bash cURL theme={null}
  # After starting a crawl, poll status by jobId
  curl -s -X GET "https://api.firecrawl.dev/v2/crawl/<jobId>" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY"
  ```
</CodeGroup>

#### Response Handling

The response varies based on the crawl's status.

For not completed or large responses exceeding 10MB, a `next` URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the `next` parameter is absent, it indicates the end of the crawl data.

The skip parameter sets the maximum number of results returned for each chunk of results returned.

<Info>
  The skip and next parameter are only relavent when hitting the api directly.
  If you're using the SDK, we handle this for you and will return all the
  results at once.
</Info>

<CodeGroup>
  ```json Scraping theme={null}
  {
    "status": "scraping",
    "total": 36,
    "completed": 10,
    "creditsUsed": 10,
    "expiresAt": "2024-00-00T00:00:00.000Z",
    "next": "https://api.firecrawl.dev/v2/crawl/123-456-789?skip=10",
    "data": [
      {
        "markdown": "[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
        "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
        "metadata": {
          "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
          "language": "en",
          "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
          "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",
          "ogLocaleAlternate": [],
          "statusCode": 200
        }
      },
      ...
    ]
  }
  ```

  ```json Completed theme={null}
  {
    "status": "completed",
    "total": 36,
    "completed": 36,
    "creditsUsed": 36,
    "expiresAt": "2024-00-00T00:00:00.000Z",
    "next": "https://api.firecrawl.dev/v2/crawl/123-456-789?skip=26",
    "data": [
      {
        "markdown": "[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
        "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
        "metadata": {
          "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
          "language": "en",
          "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
          "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",
          "ogLocaleAlternate": [],
          "statusCode": 200
        }
      },
      ...
    ]
  }
  ```
</CodeGroup>

### SDK methods

There are two ways to use the SDK:

1. **Crawl then wait** (`crawl`):
   * Waits for the crawl to complete and returns the full response
   * Handles pagination automatically
   * Recommended for most use cases

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl
  from firecrawl.types import ScrapeOptions

  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Crawl a website:
  crawl_status = firecrawl.crawl(
    'https://firecrawl.dev', 
    limit=100, 
    scrape_options=ScrapeOptions(formats=['markdown', 'html']),
    poll_interval=30
  )
  print(crawl_status)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

  const crawlResponse = await firecrawl.crawl('https://firecrawl.dev', {
    limit: 100,
    scrapeOptions: {
      formats: ['markdown', 'html'],
    }
  })

  console.log(crawlResponse)
  ```
</CodeGroup>

The response includes the crawl status and all scraped data:

<CodeGroup>
  ```bash Python theme={null}
  success=True
  status='completed'
  completed=100
  total=100
  creditsUsed=100
  expiresAt=datetime.datetime(2025, 4, 23, 19, 21, 17, tzinfo=TzInfo(UTC))
  next=None
  data=[
    Document(
      markdown='[Day 7 - Launch Week III.Integrations DayApril 14th to 20th](...',
      metadata={
        'title': '15 Python Web Scraping Projects: From Beginner to Advanced',
        ...
        'scrapeId': '97dcf796-c09b-43c9-b4f7-868a7a5af722',
        'sourceURL': 'https://www.firecrawl.dev/blog/python-web-scraping-projects',
        'url': 'https://www.firecrawl.dev/blog/python-web-scraping-projects',
        'statusCode': 200
      }
    ),
    ...
  ]
  ```

  ```json Node theme={null}
  {
    success: true,
    status: "completed",
    completed: 100,
    total: 100,
    creditsUsed: 100,
    expiresAt: "2025-04-23T19:28:45.000Z",
    data: [
      {
        markdown: "[Day 7 - Launch Week III.Integrations DayApril ...",
        html: `<!DOCTYPE html><html lang="en" class="light" style="color...`,
        metadata: [Object],
      },
      ...
    ]
  }
  ```
</CodeGroup>

2. **Start then check status** (`startCrawl`/`start_crawl`):
   * Returns immediately with a crawl ID
   * Allows manual status checking
   * Useful for long-running crawls or custom polling logic

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  job = firecrawl.start_crawl(url="https://docs.firecrawl.dev", limit=10)
  print(job)

  # Check the status of the crawl
  status = firecrawl.get_crawl_status(job.id)
  print(status)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const { id } = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 10 });
  console.log(id);

  // Check the status of the crawl
  const status = await firecrawl.getCrawlStatus(id);
  console.log(status);

  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/crawl" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 10
    }'
  ```
</CodeGroup>

## Crawl WebSocket

Firecrawl's WebSocket-based method, `Crawl URL and Watch`, enables real-time data extraction and monitoring. Start a crawl with a URL and customize it with options like page limits, allowed domains, and output formats, ideal for immediate data processing needs.

<CodeGroup>
  ```python Python theme={null}
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
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

  // Start a crawl and then watch it
  const { id } = await firecrawl.startCrawl('https://mendable.ai', {
    excludePaths: ['blog/*'],
    limit: 5,
  });

  const watcher = firecrawl.watcher(id, { kind: 'crawl', pollInterval: 2, timeout: 120 });

  watcher.on('document', (doc) => {
    console.log('DOC', doc);
  });

  watcher.on('error', (err) => {
    console.error('ERR', err?.error || err);
  });

  watcher.on('done', (state) => {
    console.log('DONE', state.status);
  });

  // Begin watching (WS with HTTP fallback)
  await watcher.start();
  ```
</CodeGroup>

## Crawl Webhook

You can configure webhooks to receive real-time notifications as your crawl progresses. This allows you to process pages as they're scraped instead of waiting for the entire crawl to complete.

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

For comprehensive webhook documentation including event types, payload structure, and implementation examples, see the [Webhooks documentation](/webhooks/overview).

### Quick Reference

**Event Types:**

* `crawl.started` - When the crawl begins
* `crawl.page` - For each page successfully scraped
* `crawl.completed` - When the crawl finishes
* `crawl.failed` - If the crawl encounters an error

**Basic Payload:**

```json  theme={null}
{
  "success": true,
  "type": "crawl.page",
  "id": "crawl-job-id",
  "data": [...], // Page data for 'page' events
  "metadata": {}, // Your custom metadata
  "error": null
}
```

<Note>
  For detailed webhook configuration, security best practices, and
  troubleshooting, visit the [Webhooks documentation](/webhooks/overview).
</Note>


# Document Parsing
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

```js Node theme={null}
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const doc = await firecrawl.scrape('https://example.com/data.xlsx');

console.log(doc.markdown);
```

### Example: Scraping a Word Document

```js Node theme={null}
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const doc = await firecrawl.scrape('https://example.com/data.docx');

console.log(doc.markdown);
```

## Output Format

All supported document types are converted to clean, structured markdown. For example, an Excel file with multiple sheets might be converted to:

```markdown  theme={null}
## Sheet1

| Name  | Value |
|-------|-------|
| Item 1 | 100   |
| Item 2 | 200   |

## Sheet2

| Date       | Description  |
|------------|--------------|
| 2023-01-01 | First quarter|
```


# Extract
Source: https://docs.firecrawl.dev/features/extract

Extract structured data from pages using LLMs

The `/extract` endpoint simplifies collecting structured data from any number of URLs or entire domains. Provide a list of URLs, optionally with wildcards (e.g., `example.com/*`), and a prompt or schema describing the information you want. Firecrawl handles the details of crawling, parsing, and collating large or small datasets.

<Info>We've simplified billing so that Extract now uses credits, just like all of the other endpoints. Each credit is worth 15 tokens.</Info>

## Using `/extract`

You can extract structured data from one or multiple URLs, including wildcards:

* **Single Page**\
  Example: `https://firecrawl.dev/some-page`
* **Multiple Pages / Full Domain**\
  Example: `https://firecrawl.dev/*`

When you use `/*`, Firecrawl will automatically crawl and parse all URLs it can discover in that domain, then extract the requested data. This feature is experimental; email [help@firecrawl.com](mailto:help@firecrawl.com) if you have issues.

### Example Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  schema = {
      "type": "object",
      "properties": {"description": {"type": "string"}},
      "required": ["description"],
  }

  res = firecrawl.extract(
      urls=["https://docs.firecrawl.dev"],
      prompt="Extract the page description",
      schema=schema,
  )

  print(res.data["description"])
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const schema = {
    type: 'object',
    properties: {
      title: { type: 'string' }
    },
    required: ['title']
  };

  const res = await firecrawl.extract({
    urls: ['https://docs.firecrawl.dev'],
    prompt: 'Extract the page title',
    schema,
    scrapeOptions: { formats: [{ type: 'json', prompt: 'Extract', schema }] }
  });

  console.log(res.status || res.success, res.data);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/extract" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "urls": ["https://docs.firecrawl.dev"],
      "prompt": "Extract the page title",
      "schema": {
        "type": "object",
        "properties": {"title": {"type": "string"}},
        "required": ["title"]
      },
      "scrapeOptions": {
        "formats": [{"type": "json", "prompt": "Extract", "schema": {"type": "object"}}]
      }
    }'
  ```
</CodeGroup>

**Key Parameters:**

* **urls**: An array of one or more URLs. Supports wildcards (`/*`) for broader crawling.
* **prompt** (Optional unless no schema): A natural language prompt describing the data you want or specifying how you want that data structured.
* **schema** (Optional unless no prompt): A more rigid structure if you already know the JSON layout.
* **enableWebSearch** (Optional): When `true`, extraction can follow links outside the specified domain.

See [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/extract) for more details.

### Response (sdks)

```json JSON theme={null}
{
  "success": true,
  "data": {
    "company_mission": "Firecrawl is the easiest way to extract data from the web. Developers use us to reliably convert URLs into LLM-ready markdown or structured data with a single API call.",
    "supports_sso": false,
    "is_open_source": true,
    "is_in_yc": true
  }
}
```

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
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
      api_key="fc-YOUR_API_KEY"
  )

  # Start an extraction job first
  extract_job = firecrawl.start_extract([
      'https://docs.firecrawl.dev/*', 
      'https://firecrawl.dev/'
  ], prompt="Extract the company mission and features from these pages.")

  # Get the status of the extraction job
  job_status = firecrawl.get_extract_status(extract_job.id)

  print(job_status)
  # Example output:
  # id=None
  # status='completed'
  # expires_at=datetime.datetime(...)
  # success=True
  # data=[{ ... }]
  # error=None
  # warning=None
  # sources=None
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const started = await firecrawl.startExtract({
    urls: ['https://docs.firecrawl.dev'],
    prompt: 'Extract title',
    schema: { type: 'object', properties: { title: { type: 'string' } }, required: ['title'] },
  });

  if (started.id) {
    const done = await firecrawl.getExtractStatus(started.id);
    console.log(done.status, done.data);
  }
  ```

  ```bash cURL theme={null}
  curl -s -X GET "https://api.firecrawl.dev/v2/extract/<jobId>" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY"
  ```
</CodeGroup>

### Possible States

* **completed**: The extraction finished successfully.
* **processing**: Firecrawl is still processing your request.
* **failed**: An error occurred; data was not fully extracted.
* **cancelled**: The job was cancelled by the user.

#### Pending Example

```json JSON theme={null}
{
  "success": true,
  "data": [],
  "status": "processing",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

#### Completed Example

```json JSON theme={null}
{
  "success": true,
  "data": {
      "company_mission": "Firecrawl is the easiest way to extract data from the web. Developers use us to reliably convert URLs into LLM-ready markdown or structured data with a single API call.",
      "supports_sso": false,
      "is_open_source": true,
      "is_in_yc": true
    },
  "status": "completed",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

## Extracting without a Schema

If you prefer not to define a strict structure, you can simply provide a `prompt`. The underlying model will choose a structure for you, which can be useful for more exploratory or flexible requests.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  # Initialize the FirecrawlApp with your API key
  firecrawl = Firecrawl(api_key='your_api_key')

  data = firecrawl.extract([
    'https://docs.firecrawl.dev/',
    'https://firecrawl.dev/'
  ], prompt="Extract Firecrawl's mission from the page.")
  print(data)
  ```

  ```js Node theme={null}
  import Firecrawl from "@mendable/firecrawl-js";

  const firecrawl = new Firecrawl({
  apiKey: "fc-YOUR_API_KEY"
  });

  const scrapeResult = await firecrawl.extract([
  'https://docs.firecrawl.dev/',
  'https://firecrawl.dev/'
  ], {
  prompt: "Extract Firecrawl's mission from the page."
  });

  console.log(scrapeResult);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/extract \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "urls": [
          "https://docs.firecrawl.dev/",
          "https://firecrawl.dev/"
        ],
        "prompt": "Extract Firecrawl'\''s mission from the page."
      }'
  ```
</CodeGroup>

```json JSON theme={null}
{
  "success": true,
  "data": {
    "company_mission": "Turn websites into LLM-ready data. Power your AI apps with clean data crawled from any website."
  }
}
```

## Improving Results with Web Search

Setting `enableWebSearch = true` in your request will expand the crawl beyond the provided URL set. This can capture supporting or related information from linked pages.

Here's an example that extracts information about dash cams, enriching the results with data from related pages:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  # Initialize the FirecrawlApp with your API key

  firecrawl = Firecrawl(api_key='your_api_key')

  data = firecrawl.extract([
  'https://nextbase.com/dash-cams/622gw-dash-cam'
  ], prompt="Extract details about the best dash cams including prices, features, pros/cons and reviews.", enable_web_search=True)
  print(data)
  ```

  ```js Node theme={null}
  import Firecrawl from "@mendable/firecrawl-js";

  const firecrawl = new Firecrawl({
  apiKey: "fc-YOUR_API_KEY"
  });

  const scrapeResult = await firecrawl.extract([
  'https://nextbase.com/dash-cams/622gw-dash-cam'
  ], {
  prompt: "Extract details about the best dash cams including prices, features, pros/cons and reviews.",
  enableWebSearch: true // Enable web search for better context
  });

  console.log(scrapeResult);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/extract \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "urls": ["https://nextbase.com/dash-cams/622gw-dash-cam"],
        "prompt": "Extract details about the best dash cams including prices, features, pros/cons, and reviews.",
        "enableWebSearch": true
      }'
  ```
</CodeGroup>

### Example Response with Web Search

```json JSON theme={null}
{
  "success": true,
  "data": {
    "dash_cams": [
      {
        "name": "Nextbase 622GW",
        "price": "$399.99",
        "features": [
          "4K video recording",
          "Image stabilization",
          "Alexa built-in",
          "What3Words integration"
        ],
        /* Information below enriched with other websites like 
        https://www.techradar.com/best/best-dash-cam found 
        via enableWebSearch parameter */
        "pros": [
          "Excellent video quality",
          "Great night vision",
          "Built-in GPS"
        ],
        "cons": ["Premium price point", "App can be finicky"]
      }
    ],
  }

```

The response includes additional context gathered from related pages, providing more comprehensive and accurate information.

## Extracting without URLs

The `/extract` endpoint now supports extracting structured data using a prompt without needing specific URLs. This is useful for research or when exact URLs are unknown. Currently in Alpha.

<CodeGroup>
  ```python Python theme={null}
  from pydantic import BaseModel

  class ExtractSchema(BaseModel):
      company_mission: str


  # Define the prompt for extraction
  prompt = 'Extract the company mission from Firecrawl\'s website.'

  # Perform the extraction
  scrape_result = firecrawl.extract(prompt=prompt, schema=ExtractSchema)

  print(scrape_result)
  ```

  ```js Node theme={null}
  import { z } from "zod";

  // Define schema to extract contents into
  const schema = z.object({
    company_mission: z.string(),
  });

  const scrapeResult = await firecrawl.extract([], {
    prompt: "Extract the company mission from Firecrawl's website.",
    schema: schema
  });

  console.log(scrapeResult);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/extract \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "urls": [],
        "prompt": "Extract the company mission from the Firecrawl's website.",
        "schema": {
          "type": "object",
          "properties": {
            "company_mission": {
              "type": "string"
            }
          },
          "required": ["company_mission"]
        }
      }'
  ```
</CodeGroup>

## Known Limitations (Beta)

1. **Large-Scale Site Coverage**\
   Full coverage of massive sites (e.g., "all products on Amazon") in a single request is not yet supported.

2. **Complex Logical Queries**\
   Requests like "find every post from 2025" may not reliably return all expected data. More advanced query capabilities are in progress.

3. **Occasional Inconsistencies**\
   Results might differ across runs, particularly for very large or dynamic sites. Usually it captures core details, but some variation is possible.

4. **Beta State**\
   Since `/extract` is still in Beta, features and performance will continue to evolve. We welcome bug reports and feedback to help us improve.

## Using FIRE-1

FIRE-1 is an AI agent that enhances Firecrawl's scraping capabilities. It can controls browser actions and navigates complex website structures to enable comprehensive data extraction beyond traditional scraping methods.

You can leverage the FIRE-1 agent with the `/extract` endpoint for complex extraction tasks that require navigation across multiple pages or interaction with elements.

**Example (cURL):**

```bash  theme={null}
curl -X POST https://api.firecrawl.dev/v2/extract \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": ["https://example-forum.com/topic/123"],
      "prompt": "Extract all user comments from this forum thread.",
      "schema": {
        "type": "object",
        "properties": {
          "comments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "author": {"type": "string"},
                "comment_text": {"type": "string"}
              },
              "required": ["author", "comment_text"]
            }
          }
        },
        "required": ["comments"]
      },
      "agent": {
        "model": "FIRE-1"
      }
    }'
```

> FIRE-1 is already live and available under preview.

## Billing and Usage Tracking

We've simplified billing so that Extract now uses credits, just like all of the other endpoints. Each credit is worth 15 tokens.

You can monitor Extract usage via the [dashboard](https://www.firecrawl.dev/app/extract).

Have feedback or need help? Email [help@firecrawl.com](mailto:help@firecrawl.com).


# Faster Scraping
Source: https://docs.firecrawl.dev/features/fast-scraping

Speed up your scrapes by 500% with the maxAge parameter

## How It Works

Firecrawl caches previously scraped pages and, by default, returns a recent copy when available.

* **Default freshness**: `maxAge = 172800000` ms (2 days). If the cached copy is newer than this, it’s returned instantly; otherwise, Firecrawl scrapes fresh and updates the cache.
* **Force fresh**: Set `maxAge: 0` to always scrape.
* **Skip caching**: Set `storeInCache: false` if you don’t want to store results for a request.

Get your results **up to 500% faster** when you don’t need the absolute freshest data. Control freshness via `maxAge`:

1. **Return instantly** if we have a recent version of the page
2. **Scrape fresh** only if our version is older than your specified age
3. **Save you time** - results come back in milliseconds instead of seconds

## When to Use This

**Great for:**

* Documentation, articles, product pages
* Bulk processing jobs
* Development and testing
* Building knowledge bases

**Skip for:**

* Real-time data (stock prices, live scores, breaking news)
* Frequently updated content
* Time-sensitive applications

## Usage

Add `maxAge` to your scrape request. Values are in milliseconds (e.g., `3600000` = 1 hour).

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Use cached data if it's less than 1 hour old (3600000 ms)
  # This can be 500% faster than a fresh scrape!
  scrape_result = firecrawl.scrape(
      'https://firecrawl.dev', 
      formats=['markdown'],
      maxAge=3600000  # 1 hour in milliseconds
  )

  print(scrape_result['markdown'])
  ```

  ```javascript JavaScript theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR_API_KEY" });

  // Use cached data if it's less than 1 hour old (3600000 ms)
  // This can be 500% faster than a fresh scrape!
  const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown'],
    maxAge: 3600000 // 1 hour in milliseconds
  });

  console.log(scrapeResult.markdown);
  ```
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
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Crawl with cached scraping - 500% faster for pages we've seen recently
  crawl_result = firecrawl.crawl(
      'https://firecrawl.dev', 
      limit=100,
      scrape_options={
          formats=['markdown'],
          maxAge=3600000  # Use cached data if less than 1 hour old
      }
  )

  for page in crawl_result['data']:
      print(f"URL: {page['metadata']['sourceURL']}")
      print(f"Content: {page['markdown'][:200]}...")
  ```

  ```javascript JavaScript theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR_API_KEY" });

  // Crawl with cached scraping - 500% faster for pages we've seen recently
  const crawlResult = await firecrawl.crawl('https://firecrawl.dev', {
    limit: 100,
    scrapeOptions: {
      formats: ['markdown'],
      maxAge: 3600000 // Use cached data if less than 1 hour old
    }
  });

  crawlResult.data.forEach(page => {
    console.log(`URL: ${page.metadata.sourceURL}`);
    console.log(`Content: ${page.markdown.substring(0, 200)}...`);
  });
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR_API_KEY' \
    -d '{
      "url": "https://firecrawl.dev",
      "limit": 100,
      "scrapeOptions": {
        "formats": ["markdown"],
        "maxAge": 3600000
      }
    }'
  ```
</CodeGroup>

When crawling with `maxAge`, each page in your crawl will benefit from the 500% speed improvement if we have recent cached data for that page.

Start using `maxAge` today for dramatically faster scrapes and crawls!


# JSON mode - Structured result
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

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl
  from pydantic import BaseModel

  app = Firecrawl(api_key="fc-YOUR-API-KEY")

  class CompanyInfo(BaseModel):
      company_mission: str
      supports_sso: bool
      is_open_source: bool
      is_in_yc: bool

  result = app.scrape(
      'https://firecrawl.dev',
      formats=[{
        "type": "json",
        "schema": CompanyInfo.model_json_schema()
      }],
      only_main_content=False,
      timeout=120000
  )

  print(result)
  ```

  ```js Node theme={null}
  import FirecrawlApp from "@mendable/firecrawl-js";
  import { z } from "zod";

  const app = new FirecrawlApp({
    apiKey: "fc-YOUR_API_KEY"
  });

  // Define schema to extract contents into
  const schema = z.object({
    company_mission: z.string(),
    supports_sso: z.boolean(),
    is_open_source: z.boolean(),
    is_in_yc: z.boolean()
  });

  const result = await app.scrape("https://firecrawl.dev", {
    formats: [{
      type: "json",
      schema: schema
    }],
  });

  console.log(result);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://firecrawl.dev",
        "formats": [ {
          "type": "json",
          "schema": {
            "type": "object",
            "properties": {
              "company_mission": {
                        "type": "string"
              },
              "supports_sso": {
                        "type": "boolean"
              },
              "is_open_source": {
                        "type": "boolean"
              },
              "is_in_yc": {
                        "type": "boolean"
              }
            },
            "required": [
              "company_mission",
              "supports_sso",
              "is_open_source",
              "is_in_yc"
            ]
          }
        } ]
      }'
  ```
</CodeGroup>

Output:

```json JSON theme={null}
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI-powered web scraping and data extraction",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI-powered web scraping and data extraction",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI-powered web scraping and data extraction",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### Structured data without schema

You can also extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  app = Firecrawl(api_key="fc-YOUR-API-KEY")

  result = app.scrape(
      'https://firecrawl.dev',
      formats=[{
        "type": "json",
        "prompt": "Extract the company mission from the page."
      }],
      only_main_content=False,
      timeout=120000
  )

  print(result)
  ```

  ```js Node theme={null}
  import FirecrawlApp from "@mendable/firecrawl-js";

  const app = new FirecrawlApp({
    apiKey: "fc-YOUR_API_KEY"
  });

  const result = await app.scrape("https://firecrawl.dev", {
    formats: [{
      type: "json",
      prompt: "Extract the company mission from the page."
    }]
  });

  console.log(result);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://firecrawl.dev",
        "formats": [{
          "type": "json",
          "prompt": "Extract the company mission from the page."
        }]
      }'
  ```
</CodeGroup>

Output:

```json JSON theme={null}
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI-powered web scraping and data extraction",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI-powered web scraping and data extraction",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI-powered web scraping and data extraction",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### Real-world example: Extracting company information

Here's a comprehensive example extracting structured company information from a website:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl
  from pydantic import BaseModel

  app = Firecrawl(api_key="fc-YOUR-API-KEY")

  class CompanyInfo(BaseModel):
      company_mission: str
      supports_sso: bool
      is_open_source: bool
      is_in_yc: bool

  result = app.scrape(
      'https://firecrawl.dev/',
      formats=[{
          "type": "json",
          "schema": CompanyInfo.model_json_schema()
      }]
  )

  print(result)
  ```

  ```js Node theme={null}
  import FirecrawlApp from "@mendable/firecrawl-js";
  import { z } from "zod";

  const app = new FirecrawlApp({
    apiKey: "fc-YOUR_API_KEY"
  });

  const companyInfoSchema = z.object({
    company_mission: z.string(),
    supports_sso: z.boolean(),
    is_open_source: z.boolean(),
    is_in_yc: z.boolean()
  });

  const result = await app.scrape("https://firecrawl.dev/", {
    formats: [{
      type: "json",
      schema: companyInfoSchema
    }]
  });

  console.log(result);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://firecrawl.dev/",
        "formats": [{
          "type": "json",
          "schema": {
            "type": "object",
            "properties": {
              "company_mission": {
                "type": "string"
              },
              "supports_sso": {
                "type": "boolean"
              },
              "is_open_source": {
                "type": "boolean"
              },
              "is_in_yc": {
                "type": "boolean"
              }
            },
            "required": [
              "company_mission",
              "supports_sso",
              "is_open_source",
              "is_in_yc"
            ]
          }
        }]
      }'
  ```
</CodeGroup>

Output:

```json Output theme={null}
{
  "success": true,
  "data": {
    "json": {
      "company_mission": "Turn websites into LLM-ready data",
      "supports_sso": true,
      "is_open_source": true,
      "is_in_yc": true
    }
  }
}
```

### JSON format options

When using JSON mode in v2, include an object in `formats` with the schema embedded directly:

`formats: [{ type: 'json', schema: { ... }, prompt: '...' }]`

Parameters:

* `schema`: JSON Schema describing the structured output you want (required for schema-based extraction).
* `prompt`: Optional prompt to guide extraction (also used for no-schema extraction).

**Important:** Unlike v1, there is no separate `jsonOptions` parameter in v2. The schema must be included directly inside the format object in the `formats` array.


# Map
Source: https://docs.firecrawl.dev/features/map

Input a website and get all the urls on the website - extremely fast

## Introducing /map

The easiest way to go from a single url to a map of the entire website. This is extremely useful for:

* When you need to prompt the end-user to choose which links to scrape
* Need to quickly know the links on a website
* Need to scrape pages of a website that are related to a specific topic (use the `search` parameter)
* Only need to scrape specific pages of a website

## Mapping

### /map endpoint

Used to map a URL and get urls of the website. This returns most links present on the website.

### Installation

<CodeGroup>
  ```python Python theme={null}
  # pip install firecrawl-py

  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
  ```

  ```js Node theme={null}
  # npm install @mendable/firecrawl-js

  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
  ```
</CodeGroup>

### Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
  res = firecrawl.map(url="https://firecrawl.dev", limit=50, sitemap="include")
  print(res)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const res = await firecrawl.map('https://firecrawl.dev', { limit: 50, sitemap: 'include' });
  console.log(res);
  ```
</CodeGroup>

### Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```json  theme={null}
{
  "success": true,
  "links": [
    {
      "url": "https://docs.firecrawl.dev/features/scrape",
      "title": "Scrape | Firecrawl",
      "description": "Turn any url into clean data"
    },
    {
      "url": "https://www.firecrawl.dev/blog/5_easy_ways_to_access_glm_4_5",
      "title": "5 Easy Ways to Access GLM-4.5",
      "description": "Discover how to access GLM-4.5 models locally, through chat applications, via the official API, and using the LLM marketplaces API for seamless integration i..."
    },
    {
      "url": "https://www.firecrawl.dev/playground",
      "title": "Playground - Firecrawl",
      "description": "Preview the API response and get the code snippets for the API"
    },
    {
      "url": "https://www.firecrawl.dev/?testId=2a7e0542-077b-4eff-bec7-0130395570d6",
      "title": "Firecrawl - The Web Data API for AI",
      "description": "The web crawling, scraping, and search API for AI. Built for scale. Firecrawl delivers the entire internet to AI agents and builders. Clean, structured, and ..."
    },
    {
      "url": "https://www.firecrawl.dev/?testId=af391f07-ca0e-40d3-8ff2-b1ecf2e3fcde",
      "title": "Firecrawl - The Web Data API for AI",
      "description": "The web crawling, scraping, and search API for AI. Built for scale. Firecrawl delivers the entire internet to AI agents and builders. Clean, structured, and ..."
    },
    ...
  ]
}
```

<Warning>
  Title and description are not always present as it depends on the website.
</Warning>

#### Map with search

Map with `search` param allows you to search for specific urls inside a website.

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/map \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "url": "https://firecrawl.dev",
    "search": "docs"
  }'
```

Response will be an ordered list from the most relevant to the least relevant.

```json  theme={null}
{
  "status": "success",
  "links": [
    {
      "url": "https://docs.firecrawl.dev",
      "title": "Firecrawl Docs",
      "description": "Firecrawl documentation"
    },
    {
      "url": "https://docs.firecrawl.dev/sdks/python",
      "title": "Firecrawl Python SDK",
      "description": "Firecrawl Python SDK documentation"
    },
    ...
  ]
}
```

## Location and Language

Specify country and preferred languages to get relevant content based on your target location and language preferences, similar to the scrape endpoint.

### How it works

When you specify the location settings, Firecrawl will use an appropriate proxy if available and emulate the corresponding language and timezone settings. By default, the location is set to 'US' if not specified.

### Usage

To use the location and language settings, include the `location` object in your request body with the following properties:

* `country`: ISO 3166-1 alpha-2 country code (e.g., 'US', 'AU', 'DE', 'JP'). Defaults to 'US'.
* `languages`: An array of preferred languages and locales for the request in order of priority. Defaults to the language of the specified location.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  res = firecrawl.map('https://example.com',
      location={
          'country': 'US',
          'languages': ['en']
      }
  )

  print(res)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const res = await firecrawl.map('https://example.com', {
    location: { country: 'US', languages: ['en'] },
  });

  console.log(res.metadata);
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.firecrawl.dev/v2/map" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://example.com",
      "location": { "country": "US", "languages": ["en"] }
    }'
  ```
</CodeGroup>

For more details about supported locations, refer to the [Proxies documentation](/features/proxies).

## Considerations

This endpoint prioritizes speed, so it may not capture all website links. We are working on improvements. Feedback and suggestions are very welcome.


# Proxies
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

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  doc = firecrawl.scrape('https://example.com',
      formats=['markdown'],
      location={
          'country': 'US',
          'languages': ['en']
      }
  )

  print(doc)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const doc = await firecrawl.scrape('https://example.com', {
    formats: ['markdown'],
    location: { country: 'US', languages: ['en'] },
  });

  console.log(doc.metadata);
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://example.com",
      "formats": ["markdown"],
      "location": { "country": "US", "languages": ["en"] }
    }'
  ```
</CodeGroup>

<Info>If you request a country where a proxy is not available, Firecrawl will use the closest available region (EU or US) and set the browser location to your requested country.</Info>

## Proxy Types

Firecrawl supports three types of proxies:

* **basic**: Proxies for scraping sites with none to basic anti-bot solutions. Fast and usually works.
* **stealth**: Stealth proxies for scraping sites with advanced anti-bot solutions, or for sites that block regular proxies. Slower, but more reliable on certain sites. [Learn more about Stealth Mode →](/features/stealth-mode)
* **auto**: Firecrawl will automatically retry scraping with stealth proxies if the basic proxy fails. If the retry with stealth is successful, 5 credits will be billed for the scrape. If the first attempt with basic is successful, only the regular cost will be billed.

***

> **Note:** For detailed information on using stealth proxies, including credit costs and retry strategies, see the [Stealth Mode documentation](/features/stealth-mode).


# Scrape
Source: https://docs.firecrawl.dev/features/scrape

Turn any url into clean data

Firecrawl converts web pages into markdown, ideal for LLM applications.

* It manages complexities: proxies, caching, rate limits, js-blocked content
* Handles dynamic content: dynamic websites, js-rendered sites, PDFs, images
* Outputs clean markdown, structured data, screenshots or html.

For details, see the [Scrape Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## Scraping a URL with Firecrawl

### /scrape endpoint

Used to scrape a URL and get its content.

### Installation

<CodeGroup>
  ```python Python theme={null}
  # pip install firecrawl-py

  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
  ```

  ```js Node theme={null}
  # npm install @mendable/firecrawl-js

  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
  ```
</CodeGroup>

### Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  # Scrape a website:
  doc = firecrawl.scrape("https://firecrawl.dev", formats=["markdown", "html"])
  print(doc)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  // Scrape a website:
  const doc = await firecrawl.scrape('https://firecrawl.dev', { formats: ['markdown', 'html'] });
  console.log(doc);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": ["markdown", "html"]
    }'
  ```
</CodeGroup>

For more details about the parameters, refer to the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

### Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```json  theme={null}
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

## Scrape Formats

You can now choose what formats you want your output in. You can specify multiple output formats. Supported formats are:

* Markdown (`markdown`)
* Summary (`summary`)
* HTML (`html`)
* Raw HTML (`rawHtml`) (with no modifications)
* Screenshot (`screenshot`, with options like `fullPage`, `quality`, `viewport`)
* Links (`links`)
* JSON (`json`) - structured output
* Images (`images`) - extract all image URLs from the page
* Branding (`branding`) - extract brand identity and design system

Output keys will match the format you choose.

## Extract brand identity

### /scrape (with branding) endpoint

The branding format extracts comprehensive brand identity information from a webpage, including colors, fonts, typography, spacing, UI components, and more. This is useful for design system analysis, brand monitoring, or building tools that need to understand a website's visual identity.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

  result = firecrawl.scrape(
      url='https://firecrawl.dev',
      formats=['branding']
  )

  print(result['branding'])
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const result = await firecrawl.scrape('https://firecrawl.dev', {
      formats: ['branding']
  });

  console.log(result.branding);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": ["branding"]
    }'
  ```
</CodeGroup>

### Response

The branding format returns a comprehensive `BrandingProfile` object with the following structure:

```json Output theme={null}
{
  "success": true,
  "data": {
    "branding": {
      "colorScheme": "dark",
      "logo": "https://firecrawl.dev/logo.svg",
      "colors": {
        "primary": "#FF6B35",
        "secondary": "#004E89",
        "accent": "#F77F00",
        "background": "#1A1A1A",
        "textPrimary": "#FFFFFF",
        "textSecondary": "#B0B0B0"
      },
      "fonts": [
        {
          "family": "Inter"
        },
        {
          "family": "Roboto Mono"
        }
      ],
      "typography": {
        "fontFamilies": {
          "primary": "Inter",
          "heading": "Inter",
          "code": "Roboto Mono"
        },
        "fontSizes": {
          "h1": "48px",
          "h2": "36px",
          "h3": "24px",
          "body": "16px"
        },
        "fontWeights": {
          "regular": 400,
          "medium": 500,
          "bold": 700
        }
      },
      "spacing": {
        "baseUnit": 8,
        "borderRadius": "8px"
      },
      "components": {
        "buttonPrimary": {
          "background": "#FF6B35",
          "textColor": "#FFFFFF",
          "borderRadius": "8px"
        },
        "buttonSecondary": {
          "background": "transparent",
          "textColor": "#FF6B35",
          "borderColor": "#FF6B35",
          "borderRadius": "8px"
        }
      },
      "images": {
        "logo": "https://firecrawl.dev/logo.svg",
        "favicon": "https://firecrawl.dev/favicon.ico",
        "ogImage": "https://firecrawl.dev/og-image.png"
      }
    }
  }
}
```

### Branding Profile Structure

The `branding` object contains the following properties:

* `colorScheme`: The detected color scheme (`"light"` or `"dark"`)
* `logo`: URL of the primary logo
* `colors`: Object containing brand colors:
  * `primary`, `secondary`, `accent`: Main brand colors
  * `background`, `textPrimary`, `textSecondary`: UI colors
  * `link`, `success`, `warning`, `error`: Semantic colors
* `fonts`: Array of font families used on the page
* `typography`: Detailed typography information:
  * `fontFamilies`: Primary, heading, and code font families
  * `fontSizes`: Size definitions for headings and body text
  * `fontWeights`: Weight definitions (light, regular, medium, bold)
  * `lineHeights`: Line height values for different text types
* `spacing`: Spacing and layout information:
  * `baseUnit`: Base spacing unit in pixels
  * `borderRadius`: Default border radius
  * `padding`, `margins`: Spacing values
* `components`: UI component styles:
  * `buttonPrimary`, `buttonSecondary`: Button styles
  * `input`: Input field styles
* `icons`: Icon style information
* `images`: Brand images (logo, favicon, og:image)
* `animations`: Animation and transition settings
* `layout`: Layout configuration (grid, header/footer heights)
* `personality`: Brand personality traits (tone, energy, target audience)

### Combining with other formats

You can combine the branding format with other formats to get comprehensive page data:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

  result = firecrawl.scrape(
      url='https://firecrawl.dev',
      formats=['markdown', 'branding', 'screenshot']
  )

  print(result['markdown'])
  print(result['branding'])
  print(result['screenshot'])
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const result = await firecrawl.scrape('https://firecrawl.dev', {
      formats: ['markdown', 'branding', 'screenshot']
  });

  console.log(result.markdown);
  console.log(result.branding);
  console.log(result.screenshot);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": ["markdown", "branding", "screenshot"]
    }'
  ```
</CodeGroup>

## Extract structured data

### /scrape (with json) endpoint

Used to extract structured data from scraped pages.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl
  from pydantic import BaseModel

  app = Firecrawl(api_key="fc-YOUR-API-KEY")

  class CompanyInfo(BaseModel):
      company_mission: str
      supports_sso: bool
      is_open_source: bool
      is_in_yc: bool

  result = app.scrape(
      'https://firecrawl.dev',
      formats=[{
        "type": "json",
        "schema": CompanyInfo.model_json_schema()
      }],
      only_main_content=False,
      timeout=120000
  )

  print(result)
  ```

  ```js Node theme={null}
  import FirecrawlApp from "@mendable/firecrawl-js";
  import { z } from "zod";

  const app = new FirecrawlApp({
    apiKey: "fc-YOUR_API_KEY"
  });

  // Define schema to extract contents into
  const schema = z.object({
    company_mission: z.string(),
    supports_sso: z.boolean(),
    is_open_source: z.boolean(),
    is_in_yc: z.boolean()
  });

  const result = await app.scrape("https://firecrawl.dev", {
    formats: [{
      type: "json",
      schema: schema
    }],
  });

  console.log(result);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://firecrawl.dev",
        "formats": [ {
          "type": "json",
          "schema": {
            "type": "object",
            "properties": {
              "company_mission": {
                        "type": "string"
              },
              "supports_sso": {
                        "type": "boolean"
              },
              "is_open_source": {
                        "type": "boolean"
              },
              "is_in_yc": {
                        "type": "boolean"
              }
            },
            "required": [
              "company_mission",
              "supports_sso",
              "is_open_source",
              "is_in_yc"
            ]
          }
        } ]
      }'
  ```
</CodeGroup>

Output:

```json JSON theme={null}
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI-powered web scraping and data extraction",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI-powered web scraping and data extraction",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI-powered web scraping and data extraction",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### Extracting without schema

You can now extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  app = Firecrawl(api_key="fc-YOUR-API-KEY")

  result = app.scrape(
      'https://firecrawl.dev',
      formats=[{
        "type": "json",
        "prompt": "Extract the company mission from the page."
      }],
      only_main_content=False,
      timeout=120000
  )

  print(result)
  ```

  ```js Node theme={null}
  import FirecrawlApp from "@mendable/firecrawl-js";

  const app = new FirecrawlApp({
    apiKey: "fc-YOUR_API_KEY"
  });

  const result = await app.scrape("https://firecrawl.dev", {
    formats: [{
      type: "json",
      prompt: "Extract the company mission from the page."
    }]
  });

  console.log(result);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://firecrawl.dev",
        "formats": [{
          "type": "json",
          "prompt": "Extract the company mission from the page."
        }]
      }'
  ```
</CodeGroup>

Output:

```json JSON theme={null}
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI-powered web scraping and data extraction",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI-powered web scraping and data extraction",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI-powered web scraping and data extraction",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### JSON format options

When using the `json` format, pass an object inside `formats` with the following parameters:

* `schema`: JSON Schema for the structured output.
* `prompt`: Optional prompt to help guide extraction when a schema is present or when you prefer light guidance.

## Interacting with the page with Actions

Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.

Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.

It is important to almost always use the `wait` action before/after executing other actions to give enough time for the page to load.

### Example

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  doc = firecrawl.scrape(
      url="https://example.com/login",
      formats=["markdown"],
      actions=[
          {"type": "write", "text": "john@example.com"},
          {"type": "press", "key": "Tab"},
          {"type": "write", "text": "secret"},
          {"type": "click", "selector": 'button[type="submit"]'},
          {"type": "wait", "milliseconds": 1500},
          {"type": "screenshot", "fullPage": True},
      ],
  )

  print(doc.markdown, doc.screenshot)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const doc = await firecrawl.scrape('https://example.com/login', {
    formats: ['markdown'],
    actions: [
      { type: 'write', text: 'john@example.com' },
      { type: 'press', key: 'Tab' },
      { type: 'write', text: 'secret' },
      { type: 'click', selector: 'button[type="submit"]' },
      { type: 'wait', milliseconds: 1500 },
      { type: 'screenshot', fullPage: true },
    ],
  });

  console.log(doc.markdown, doc.screenshot);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://example.com/login",
        "formats": ["markdown"],
        "actions": [
          { "type": "write", "text": "john@example.com" },
          { "type": "press", "key": "Tab" },
          { "type": "write", "text": "secret" },
          { "type": "click", "selector": "button[type=\"submit\"]" },
          { "type": "wait", "milliseconds": 1500 },
          { "type": "screenshot", "fullPage": true },
        ],
    }'
  ```
</CodeGroup>

### Output

<CodeGroup>
  ```json JSON theme={null}
  {
    "success": true,
    "data": {
      "markdown": "Our first Launch Week is over! [See the recap 🚀](blog/firecrawl-launch-week-1-recap)...",
      "actions": {
        "screenshots": [
          "https://alttmdsdujxrfnakrkyi.supabase.co/storage/v1/object/public/media/screenshot-75ef2d87-31e0-4349-a478-fb432a29e241.png"
        ],
        "scrapes": [
          {
            "url": "https://www.firecrawl.dev/",
            "html": "<html><body><h1>Firecrawl</h1></body></html>"
          }
        ]
      },
      "metadata": {
        "title": "Home - Firecrawl",
        "description": "Firecrawl crawls and converts any website into clean markdown.",
        "language": "en",
        "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "Turn any website into LLM-ready data.",
        "ogUrl": "https://www.firecrawl.dev/",
        "ogImage": "https://www.firecrawl.dev/og.png?123",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "http://google.com",
        "statusCode": 200
      }
    }
  }
  ```
</CodeGroup>

For more details about the actions parameters, refer to the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## Location and Language

Specify country and preferred languages to get relevant content based on your target location and language preferences.

### How it works

When you specify the location settings, Firecrawl will use an appropriate proxy if available and emulate the corresponding language and timezone settings. By default, the location is set to 'US' if not specified.

### Usage

To use the location and language settings, include the `location` object in your request body with the following properties:

* `country`: ISO 3166-1 alpha-2 country code (e.g., 'US', 'AU', 'DE', 'JP'). Defaults to 'US'.
* `languages`: An array of preferred languages and locales for the request in order of priority. Defaults to the language of the specified location.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  doc = firecrawl.scrape('https://example.com',
      formats=['markdown'],
      location={
          'country': 'US',
          'languages': ['en']
      }
  )

  print(doc)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const doc = await firecrawl.scrape('https://example.com', {
    formats: ['markdown'],
    location: { country: 'US', languages: ['en'] },
  });

  console.log(doc.metadata);
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://example.com",
      "formats": ["markdown"],
      "location": { "country": "US", "languages": ["en"] }
    }'
  ```
</CodeGroup>

For more details about supported locations, refer to the [Proxies documentation](/features/proxies).

## Caching and maxAge

To make requests faster, Firecrawl serves results from cache by default when a recent copy is available.

* **Default freshness window**: `maxAge = 172800000` ms (2 days). If a cached page is newer than this, it’s returned instantly; otherwise, the page is scraped and then cached.
* **Performance**: This can speed up scrapes by up to 5x when data doesn’t need to be ultra-fresh.
* **Always fetch fresh**: Set `maxAge` to `0`.
* **Avoid storing**: Set `storeInCache` to `false` if you don’t want Firecrawl to cache/store results for this request.

Example (force fresh content):

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl
  firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

  doc = firecrawl.scrape(url='https://example.com', maxAge=0, formats=['markdown'])
  print(doc)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const doc = await firecrawl.scrape('https://example.com', { maxAge: 0, formats: ['markdown'] });
  console.log(doc);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://example.com",
      "maxAge": 0,
      "formats": ["markdown"]
    }'
  ```
</CodeGroup>

Example (use a 10-minute cache window):

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl
  firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

  doc = firecrawl.scrape(url='https://example.com', maxAge=600000, formats=['markdown', 'html'])
  print(doc)
  ```

  ```js Node theme={null}

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const doc = await firecrawl.scrape('https://example.com', { maxAge: 600000, formats: ['markdown', 'html'] });
  console.log(doc);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://example.com",
      "maxAge": 600000,
      "formats": ["markdown", "html"]
    }'
  ```
</CodeGroup>

## Batch scraping multiple URLs

You can now batch scrape multiple URLs at the same time. It takes the starting URLs and optional parameters as arguments. The params argument allows you to specify additional options for the batch scrape job, such as the output formats.

### How it works

It is very similar to how the `/crawl` endpoint works. It submits a batch scrape job and returns a job ID to check the status of the batch scrape.

The sdk provides 2 methods, synchronous and asynchronous. The synchronous method will return the results of the batch scrape job, while the asynchronous method will return a job ID that you can use to check the status of the batch scrape.

### Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  job = firecrawl.batch_scrape([
      "https://firecrawl.dev",
      "https://docs.firecrawl.dev",
  ], formats=["markdown"], poll_interval=2, wait_timeout=120)

  print(job)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const job = await firecrawl.batchScrape([
    'https://firecrawl.dev',
    'https://docs.firecrawl.dev',
  ], { options: { formats: ['markdown'] }, pollInterval: 2, timeout: 120 });

  console.log(job);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/batch/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "urls": ["https://firecrawl.dev", "https://docs.firecrawl.dev"],
      "formats": ["markdown"]
    }'
  ```
</CodeGroup>

### Response

If you’re using the sync methods from the SDKs, it will return the results of the batch scrape job. Otherwise, it will return a job ID that you can use to check the status of the batch scrape.

#### Synchronous

```json Completed theme={null}
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "markdown": "[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
      "metadata": {
        "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
        "language": "en",
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
        "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",
        "ogLocaleAlternate": [],
        "statusCode": 200
      }
    },
    ...
  ]
}
```

#### Asynchronous

You can then use the job ID to check the status of the batch scrape by calling the `/batch/scrape/{id}` endpoint. This endpoint is meant to be used while the job is still running or right after it has completed **as batch scrape jobs expire after 24 hours**.

```json  theme={null}
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Stealth Mode

For websites with advanced anti-bot protection, Firecrawl offers a stealth proxy mode that provides better success rates at scraping challenging sites.

Learn more about [Stealth Mode](/features/stealth-mode).


# Search
Source: https://docs.firecrawl.dev/features/search

Search the web and get full content from results

Firecrawl's search API allows you to perform web searches and optionally scrape the search results in one operation.

* Choose specific output formats (markdown, HTML, links, screenshots)
* Search the web with customizable parameters (location, etc.)
* Optionally retrieve content from search results in various formats
* Control the number of results and set timeouts

For details, see the [Search Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/search).

## Performing a Search with Firecrawl

### /search endpoint

Used to perform web searches and optionally retrieve content from the results.

### Installation

<CodeGroup>
  ```python Python theme={null}
  # pip install firecrawl-py

  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
  ```

  ```js Node theme={null}
  # npm install @mendable/firecrawl-js

  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
  ```
</CodeGroup>

### Basic Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  results = firecrawl.search(
      query="firecrawl",
      limit=3,
  )
  print(results)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const results = await firecrawl.search('firecrawl', {
    limit: 3,
    scrapeOptions: { formats: ['markdown'] }
  });
  console.log(results);
  ```

  ```bash  theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/search" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "query": "firecrawl",
      "limit": 3
    }'
  ```
</CodeGroup>

### Response

SDKs will return the data object directly. cURL will return the complete payload.

```json JSON theme={null}
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://www.firecrawl.dev/",
        "title": "Firecrawl - The Web Data API for AI",
        "description": "The web crawling, scraping, and search API for AI. Built for scale. Firecrawl delivers the entire internet to AI agents and builders.",
        "position": 1
      },
      {
        "url": "https://github.com/mendableai/firecrawl",
        "title": "mendableai/firecrawl: Turn entire websites into LLM-ready ... - GitHub",
        "description": "Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data.",
        "position": 2
      },
      ...
    ],
    "images": [
      {
        "title": "Quickstart | Firecrawl",
        "imageUrl": "https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png",
        "imageWidth": 5814,
        "imageHeight": 1200,
        "url": "https://docs.firecrawl.dev/",
        "position": 1
      },
      ...
    ],
    "news": [
      {
        "title": "Y Combinator startup Firecrawl is ready to pay $1M to hire three AI agents as employees",
        "url": "https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/",
        "snippet": "It's now placed three new ads on YC's job board for “AI agents only” and has set aside a $1 million budget total to make it happen.",
        "date": "3 months ago",
        "position": 1
      },
      ...
    ]
  }
}
```

## Search result types

In addition to regular web results, Search supports specialized result types via the `sources` parameter:

* `web`: standard web results (default)
* `news`: news-focused results
* `images`: image search results

## Search Categories

Filter search results by specific categories using the `categories` parameter:

* `github`: Search within GitHub repositories, code, issues, and documentation
* `research`: Search academic and research websites (arXiv, Nature, IEEE, PubMed, etc.)
* `pdf`: Search for PDFs

### GitHub Category Search

Search specifically within GitHub repositories:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "web scraping python",
    "categories": ["github"],
    "limit": 10
  }'
```

### Research Category Search

Search academic and research websites:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "machine learning transformers",
    "categories": ["research"],
    "limit": 10
  }'
```

### Mixed Category Search

Combine multiple categories in one search:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "neural networks",
    "categories": ["github", "research"],
    "limit": 15
  }'
```

### Category Response Format

Each search result includes a `category` field indicating its source:

```json  theme={null}
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/neural-network",
        "title": "Neural Network Implementation",
        "description": "A PyTorch implementation of neural networks",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "Advances in Neural Network Architecture",
        "description": "Research paper on neural network improvements",
        "category": "research"
      }
    ]
  }
}
```

Examples:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "openai",
    "sources": ["news"],
    "limit": 5
  }'
```

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "jupiter",
    "sources": ["images"],
    "limit": 8
  }'
```

### HD Image Search with Size Filtering

Use Google Images operators to find high-resolution images:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sunset imagesize:1920x1080",
    "sources": ["images"],
    "limit": 5
  }'
```

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "mountain wallpaper larger:2560x1440",
    "sources": ["images"],
    "limit": 8
  }'
```

**Common HD resolutions:**

* `imagesize:1920x1080` - Full HD (1080p)
* `imagesize:2560x1440` - QHD (1440p)
* `imagesize:3840x2160` - 4K UHD
* `larger:1920x1080` - HD and above
* `larger:2560x1440` - QHD and above

## Search with Content Scraping

Search and retrieve content from the search results in one operation.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Search and scrape content
  results = firecrawl.search(
      "firecrawl web scraping",
      limit=3,
      scrape_options={
          "formats": ["markdown", "links"]
      }
  )
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const results = await firecrawl.search('firecrawl', {
    limit: 3,
    scrapeOptions: { formats: ['markdown'] }
  });
  console.log(results);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer fc-YOUR_API_KEY" \
    -d '{
      "query": "firecrawl web scraping",
      "limit": 3,
      "scrapeOptions": {
        "formats": ["markdown", "links"]
      }
    }'
  ```
</CodeGroup>

Every option in scrape endpoint is supported by this search endpoint through the `scrapeOptions` parameter.

### Response with Scraped Content

```json  theme={null}
{
  "success": true,
  "data": [
    {
      "title": "Firecrawl - The Ultimate Web Scraping API",
      "description": "Firecrawl is a powerful web scraping API that turns any website into clean, structured data for AI and analysis.",
      "url": "https://firecrawl.dev/",
      "markdown": "# Firecrawl\n\nThe Ultimate Web Scraping API\n\n## Turn any website into clean, structured data\n\nFirecrawl makes it easy to extract data from websites for AI applications, market research, content aggregation, and more...",
      "links": [
        "https://firecrawl.dev/pricing",
        "https://firecrawl.dev/docs",
        "https://firecrawl.dev/guides"
      ],
      "metadata": {
        "title": "Firecrawl - The Ultimate Web Scraping API",
        "description": "Firecrawl is a powerful web scraping API that turns any website into clean, structured data for AI and analysis.",
        "sourceURL": "https://firecrawl.dev/",
        "statusCode": 200
      }
    }
  ]
}
```

## Advanced Search Options

Firecrawl's search API supports various parameters to customize your search:

### Location Customization

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Search with location settings (Germany)
  search_result = firecrawl.search(
      "web scraping tools",
      limit=5,
      location="Germany"
  )

  # Process the results
  for result in search_result.data:
      print(f"Title: {result['title']}")
      print(f"URL: {result['url']}")
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  // Search with location settings (Germany)
  const results = await firecrawl.search('web scraping tools', {
    limit: 5,
    location: "Germany"
  });

  // Process the results
  console.log(results);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer fc-YOUR_API_KEY" \
    -d '{
      "query": "web scraping tools",
      "limit": 5,
      "location": "Germany"
    }'
  ```
</CodeGroup>

### Time-Based Search

Use the `tbs` parameter to filter results by time:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  results = firecrawl.search(
      query="firecrawl",
      limit=5,
      tbs="qdr:d",
  )
  print(len(results.get('web', [])))
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const results = await firecrawl.search('firecrawl', {
    limit: 5,
    tbs: 'qdr:d', // past day
  });

  console.log(results.web);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer fc-YOUR_API_KEY" \
    -d '{
      "query": "latest web scraping techniques",
      "limit": 5,
      "tbs": "qdr:w"
    }'
  ```
</CodeGroup>

Common `tbs` values:

* `qdr:h` - Past hour
* `qdr:d` - Past 24 hours
* `qdr:w` - Past week
* `qdr:m` - Past month
* `qdr:y` - Past year

For more precise time filtering, you can specify exact date ranges using the custom date range format:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  # Initialize the client with your API key
  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Search for results from December 2024
  search_result = firecrawl.search(
      "firecrawl updates",
      limit=10,
      tbs="cdr:1,cd_min:12/1/2024,cd_max:12/31/2024"
  )
  ```

  ```js JavaScript theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  // Initialize the client with your API key
  const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

  // Search for results from December 2024
  firecrawl.search("firecrawl updates", {
    limit: 10,
    tbs: "cdr:1,cd_min:12/1/2024,cd_max:12/31/2024"
  })
  .then(searchResult => {
    console.log(searchResult.data);
  });
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer fc-YOUR_API_KEY" \
    -d '{
      "query": "firecrawl updates",
      "limit": 10,
      "tbs": "cdr:1,cd_min:12/1/2024,cd_max:12/31/2024"
    }'
  ```
</CodeGroup>

### Custom Timeout

Set a custom timeout for search operations:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import FirecrawlApp

  # Initialize the client with your API key
  app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

  # Set a 30-second timeout
  search_result = app.search(
      "complex search query",
      limit=10,
      timeout=30000  # 30 seconds in milliseconds
  )
  ```

  ```js JavaScript theme={null}
  import FirecrawlApp from '@mendable/firecrawl-js';

  // Initialize the client with your API key
  const app = new FirecrawlApp({apiKey: "fc-YOUR_API_KEY"});

  // Set a 30-second timeout
  app.search("complex search query", {
    limit: 10,
    timeout: 30000  // 30 seconds in milliseconds
  })
  .then(searchResult => {
    // Process results
    console.log(searchResult.data);
  });
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer fc-YOUR_API_KEY" \
    -d '{
      "query": "complex search query",
      "limit": 10,
      "timeout": 30000
    }'
  ```
</CodeGroup>

## Cost Implications

When search results are not scraped (no scrape options specified), the cost is 2 credits per 10 search results. When scraping is enabled, there is no additional charge for basic scrapes of each search result beyond the standard scraping costs.

However, be aware of these cost factors:

* **PDF parsing**: 1 credit per PDF page (can significantly increase costs for multi-page PDFs)
* **Stealth proxy mode**: +4 additional credits per search result
* ***JSON mode***: +4 additional credits per search result

To control costs:

* Set `parsers: []` if you don't need PDF content
* Use `proxy: "basic"` instead of `"stealth"` when possible
* Limit the number of search results with the `limit` parameter

## Advanced Scraping Options

For more details about the scraping options, refer to the [Scrape Feature documentation](https://docs.firecrawl.dev/features/scrape). Everything except for the FIRE-1 Agent and Change-Tracking features are supported by this Search endpoint.


# Stealth Mode
Source: https://docs.firecrawl.dev/features/stealth-mode

Use stealth proxies for sites with advanced anti-bot solutions

Firecrawl provides different proxy types to help you scrape websites with varying levels of anti-bot protection. The proxy type can be specified using the `proxy` parameter.

### Proxy Types

Firecrawl supports three types of proxies:

* **basic**: Proxies for scraping sites with none to basic anti-bot solutions. Fast and usually works.
* **stealth**: Stealth proxies for scraping sites with advanced anti-bot solutions. Slower, but more reliable on certain sites.
* **auto**: Firecrawl will automatically retry scraping with stealth proxies if the basic proxy fails. If the retry with stealth is successful, 5 credits will be billed for the scrape. If the first attempt with basic is successful, only the regular cost will be billed.

If you do not specify a proxy, Firecrawl will default to auto.

### Using Stealth Mode

When scraping websites with advanced anti-bot protection, you can use the stealth proxy mode to improve your success rate.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key='fc-YOUR-API-KEY')

  # Choose proxy strategy: 'basic' | 'stealth' | 'auto'
  doc = firecrawl.scrape('https://example.com', formats=['markdown'], proxy='auto')

  print(doc.warning or 'ok')
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  // Choose proxy strategy: 'basic' | 'stealth' | 'auto'
  const doc = await firecrawl.scrape('https://example.com', {
    formats: ['markdown'],
    proxy: 'auto'
  });

  console.log(doc.warning || 'ok');
  ```

  ```bash cURL theme={null}

  // Choose proxy strategy: 'basic' | 'stealth' | 'auto'
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer fc-YOUR-API-KEY' \
      -d '{
        "url": "https://example.com",
        "proxy": "auto"
      }'

  ```
</CodeGroup>

**Note:** Stealth proxy requests cost 5 credits per request when used.

## Using Stealth as a Retry Mechanism

A common pattern is to first try scraping with the default proxy settings, and then retry with stealth mode if you encounter specific error status codes (401, 403, or 500) in the `metadata.statusCode` field of the response. These status codes can be indicative of the website blocking your request.

<CodeGroup>
  ```python Python theme={null}
  # pip install firecrawl-py

  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="YOUR_API_KEY")

  # First try with basic proxy
  try:
      content = firecrawl.scrape("https://example.com")
      
      # Check if we got an error status code
      status_code = content.get("metadata", {}).get("statusCode")
      if status_code in [401, 403, 500]:
          print(f"Got status code {status_code}, retrying with stealth proxy")
          # Retry with stealth proxy
          content = firecrawl.scrape("https://example.com", proxy="stealth")
      
      print(content["markdown"])
  except Exception as e:
      print(f"Error: {e}")
      # Retry with stealth proxy on exception
      try:
          content = firecrawl.scrape("https://example.com", proxy="stealth")
          print(content["markdown"])
      except Exception as e:
          print(f"Stealth proxy also failed: {e}")
  ```

  ```js Node theme={null}
  // npm install @mendable/firecrawl-js

  import { Firecrawl } from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: 'YOUR_API_KEY' });

  // Function to scrape with retry logic
  async function scrapeWithRetry(url) {
    try {
      // First try with default proxy
      const content = await firecrawl.scrape(url);
      
      // Check if we got an error status code
      const statusCode = content?.metadata?.statusCode;
      if ([401, 403, 500].includes(statusCode)) {
        console.log(`Got status code ${statusCode}, retrying with stealth proxy`);
        // Retry with stealth proxy
        return await firecrawl.scrape(url, {
          proxy: 'stealth'
        });
      }
      
      return content;
    } catch (error) {
      console.error(`Error: ${error.message}`);
      // Retry with stealth proxy on exception
      try {
        return await firecrawl.scrape(url, {
          proxy: 'stealth'
        });
      } catch (retryError) {
        console.error(`Stealth proxy also failed: ${retryError.message}`);
        throw retryError;
      }
    }
  }

  // Usage
  const content = await scrapeWithRetry('https://example.com');
  console.log(content.markdown);
  ```

  ```bash cURL theme={null}
  # First try with default proxy
  RESPONSE=$(curl -s -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://example.com"
      }')

  # Extract status code from response
  STATUS_CODE=$(echo $RESPONSE | jq -r '.data.metadata.statusCode')

  # Check if status code indicates we should retry with stealth
  if [[ "$STATUS_CODE" == "401" || "$STATUS_CODE" == "403" || "$STATUS_CODE" == "500" ]]; then
      echo "Got status code $STATUS_CODE, retrying with stealth proxy"
      
      # Retry with stealth proxy
      curl -X POST https://api.firecrawl.dev/v2/scrape \
          -H 'Content-Type: application/json' \
          -H 'Authorization: Bearer YOUR_API_KEY' \
          -d '{
            "url": "https://example.com",
            "proxy": "stealth"
          }'
  else
      # Output the original response
      echo $RESPONSE
  fi
  ```
</CodeGroup>

This approach allows you to optimize your credit usage by only using stealth mode when necessary.


# Quickstart
Source: https://docs.firecrawl.dev/introduction

Firecrawl allows you to turn entire websites into LLM-ready markdown

<img className="block" src="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=4e7b593752a4ff638c1d1dbfddb54a9a" alt="Hero Light" data-og-width="1200" width="1200" data-og-height="675" height="675" data-path="images/turn-websites-into-llm-ready-data--firecrawl.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?w=280&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=e80d7c4a694a930342577283249d461a 280w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?w=560&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=1344a5340ddad90ee50ccf66b088b430 560w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?w=840&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=060bf67f6a5b76002c4b416b165d0dce 840w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?w=1100&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=f89c070acdb98f7e2b91f58209f7a628 1100w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?w=1650&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=0486baeea836b83b6c84e28635b20604 1650w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?w=2500&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=1fe62bc4843cf736d0462e93ae0610c8 2500w" />

## Welcome to Firecrawl

[Firecrawl](https://firecrawl.dev?ref=github) is an API service that takes a URL, crawls it, and converts it into clean markdown. We crawl all accessible subpages and give you clean markdown for each. No sitemap required.

## How to use it?

We provide an easy to use API with our hosted version. You can find the playground and documentation [here](https://firecrawl.dev/playground). You can also self host the backend if you'd like.

Check out the following resources to get started:

* **API**: [Documentation](https://docs.firecrawl.dev/api-reference/introduction)
* **SDKs**: [Python](https://docs.firecrawl.dev/sdks/python), [Node](https://docs.firecrawl.dev/sdks/node)
* **LLM Frameworks**: [Langchain (python)](https://python.langchain.com/docs/integrations/document_loaders/firecrawl/), [Langchain (js)](https://js.langchain.com/docs/integrations/document_loaders/web_loaders/firecrawl), [Llama Index](https://docs.llamaindex.ai/en/latest/examples/data_connectors/WebPageDemo/#using-firecrawl-reader), [Crew.ai](https://docs.crewai.com/), [Composio](https://composio.dev/tools/firecrawl/all), [PraisonAI](https://docs.praison.ai/firecrawl/), [Superinterface](https://superinterface.ai/docs/assistants/functions/firecrawl), [Vectorize](https://docs.vectorize.io/integrations/source-connectors/firecrawl)
* **Low-code Frameworks**: [Dify](https://dify.ai/blog/dify-ai-blog-integrated-with-firecrawl), [Langflow](https://docs.langflow.org/), [Flowise AI](https://docs.flowiseai.com/integrations/langchain/document-loaders/firecrawl), [Cargo](https://docs.getcargo.io/integration/firecrawl), [Pipedream](https://pipedream.com/apps/firecrawl/)
* **Community SDKs**: [Go](https://docs.firecrawl.dev/sdks/go), [Rust](https://docs.firecrawl.dev/sdks/rust) (v1)
* **Others**: [Zapier](https://zapier.com/apps/firecrawl/integrations), [Pabbly Connect](https://www.pabbly.com/connect/integrations/firecrawl/)
* **Self-host:** To self-host refer to guide [here](/contributing/self-host).

Want an SDK or Integration? Let us know by opening an [issue](https://github.com/firecrawl/firecrawl/issues).

### API Key

To use the API, you need to sign up on [Firecrawl](https://firecrawl.dev) and get an API key.

### Features

* [**Scrape**](#scraping): scrapes a URL and get its content in LLM-ready format (markdown, summary, structured data via [json mode](#json-mode), screenshot, html)
* [**Crawl**](#crawling): scrapes all the URLs of a web page and return content in LLM-ready format
* [**Map**](/features/map): input a website and get all the website urls - extremely fast
* [**Search**](/features/search): search the web and get full content from results
* [**Extract**](/features/extract): get structured data from single page, multiple pages or entire websites with AI.

### Powerful Capabilities

* **LLM-ready formats**: markdown, summary, structured data, screenshot, HTML, links, metadata, images
* **The hard stuff**: proxies, anti-bot mechanisms, dynamic content (js-rendered), output parsing, orchestration
* **Lightning fast**: Get results in seconds—built for speed and high-throughput use cases.
* **Customizability**: exclude tags, crawl behind auth walls with custom headers, max crawl depth, etc...
* **Media parsing**: pdfs, docx, images.
* **Reliability first**: designed to get the data you need - no matter how hard it is.
* **Actions**: click, scroll, input, wait and more before extracting data

You can find all of Firecrawl's capabilities and how to use them in our [documentation](https://docs.firecrawl.dev/api-reference/v2-introduction)

## Installing Firecrawl

<CodeGroup>
  ```python Python theme={null}
  # pip install firecrawl-py

  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
  ```

  ```js Node theme={null}
  # npm install @mendable/firecrawl-js

  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
  ```
</CodeGroup>

## Scraping

To scrape a single URL, use the `scrape` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  # Scrape a website:
  doc = firecrawl.scrape("https://firecrawl.dev", formats=["markdown", "html"])
  print(doc)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  // Scrape a website:
  const doc = await firecrawl.scrape('https://firecrawl.dev', { formats: ['markdown', 'html'] });
  console.log(doc);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": ["markdown", "html"]
    }'
  ```
</CodeGroup>

### Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```json  theme={null}
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

## Crawling

The crawl feature allows you to automatically discover and extract content from a URL and all of its accessible subpages. With our SDKs, simply call the crawl method—this will submit a crawl job, wait for it to finish, and return the complete results for the entire site.

### Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  docs = firecrawl.crawl(url="https://docs.firecrawl.dev", limit=10)
  print(docs)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const docs = await firecrawl.crawl('https://docs.firecrawl.dev', { limit: 10 });
  console.log(docs);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/crawl" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 10
    }'
  ```
</CodeGroup>

If you're using our API directly, cURL or `start crawl` functions on SDKs, this will return an `ID` where you can use to check the status of the crawl.

```json  theme={null}
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
}
```

### Get Crawl Status

Used to check the status of a crawl job and get its result.

<CodeGroup>
  ```python Python theme={null}
  status = firecrawl.get_crawl_status("<crawl-id>")
  print(status)
  ```

  ```js Node theme={null}
  const status = await firecrawl.getCrawlStatus("<crawl-id>");
  console.log(status);
  ```

  ```bash cURL theme={null}
  # After starting a crawl, poll status by jobId
  curl -s -X GET "https://api.firecrawl.dev/v2/crawl/<jobId>" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY"
  ```
</CodeGroup>

#### Response

The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a `next` URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the `next` parameter is absent, it indicates the end of the crawl data.

<CodeGroup>
  ```json Scraping theme={null}
  {
    "status": "scraping",
    "total": 36,
    "completed": 10,
    "creditsUsed": 10,
    "expiresAt": "2024-00-00T00:00:00.000Z",
    "next": "https://api.firecrawl.dev/v2/crawl/123-456-789?skip=10",
    "data": [
      {
        "markdown": "[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
        "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
        "metadata": {
          "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
          "language": "en",
          "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
          "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",
          "ogLocaleAlternate": [],
          "statusCode": 200
        }
      },
      ...
    ]
  }
  ```

  ```json Completed theme={null}
  {
    "status": "completed",
    "total": 36,
    "completed": 36,
    "creditsUsed": 36,
    "expiresAt": "2024-00-00T00:00:00.000Z",
    "next": "https://api.firecrawl.dev/v2/crawl/123-456-789?skip=26",
    "data": [
      {
        "markdown": "[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
        "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
        "metadata": {
          "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
          "language": "en",
          "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
          "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",
          "ogLocaleAlternate": [],
          "statusCode": 200
        }
      },
      ...
    ]
  }
  ```
</CodeGroup>

## JSON mode

With JSON mode, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl
  from pydantic import BaseModel

  app = Firecrawl(api_key="fc-YOUR-API-KEY")

  class CompanyInfo(BaseModel):
      company_mission: str
      supports_sso: bool
      is_open_source: bool
      is_in_yc: bool

  result = app.scrape(
      'https://firecrawl.dev',
      formats=[{
        "type": "json",
        "schema": CompanyInfo.model_json_schema()
      }],
      only_main_content=False,
      timeout=120000
  )

  print(result)
  ```

  ```js Node theme={null}
  import FirecrawlApp from "@mendable/firecrawl-js";
  import { z } from "zod";

  const app = new FirecrawlApp({
    apiKey: "fc-YOUR_API_KEY"
  });

  // Define schema to extract contents into
  const schema = z.object({
    company_mission: z.string(),
    supports_sso: z.boolean(),
    is_open_source: z.boolean(),
    is_in_yc: z.boolean()
  });

  const result = await app.scrape("https://firecrawl.dev", {
    formats: [{
      type: "json",
      schema: schema
    }],
  });

  console.log(result);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://firecrawl.dev",
        "formats": [ {
          "type": "json",
          "schema": {
            "type": "object",
            "properties": {
              "company_mission": {
                        "type": "string"
              },
              "supports_sso": {
                        "type": "boolean"
              },
              "is_open_source": {
                        "type": "boolean"
              },
              "is_in_yc": {
                        "type": "boolean"
              }
            },
            "required": [
              "company_mission",
              "supports_sso",
              "is_open_source",
              "is_in_yc"
            ]
          }
        } ]
      }'
  ```
</CodeGroup>

Output:

```json JSON theme={null}
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI-powered web scraping and data extraction",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI-powered web scraping and data extraction",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI-powered web scraping and data extraction",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

## Search

Firecrawl's search API allows you to perform web searches and optionally scrape the search results in one operation.

* Choose specific output formats (markdown, HTML, links, screenshots)
* Choose specific sources (web, news, images)
* Search the web with customizable parameters (location, etc.)

For details, see the [Search Endpoint API Reference](/api-reference/endpoint/search).

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  results = firecrawl.search(
      query="firecrawl",
      limit=3,
  )
  print(results)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const results = await firecrawl.search('firecrawl', {
    limit: 3,
    scrapeOptions: { formats: ['markdown'] }
  });
  console.log(results);
  ```

  ```bash  theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/search" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "query": "firecrawl",
      "limit": 3
    }'
  ```
</CodeGroup>

### Response

SDKs will return the data object directly. cURL will return the complete payload.

```json JSON theme={null}
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://www.firecrawl.dev/",
        "title": "Firecrawl - The Web Data API for AI",
        "description": "The web crawling, scraping, and search API for AI. Built for scale. Firecrawl delivers the entire internet to AI agents and builders.",
        "position": 1
      },
      {
        "url": "https://github.com/mendableai/firecrawl",
        "title": "mendableai/firecrawl: Turn entire websites into LLM-ready ... - GitHub",
        "description": "Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data.",
        "position": 2
      },
      ...
    ],
    "images": [
      {
        "title": "Quickstart | Firecrawl",
        "imageUrl": "https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png",
        "imageWidth": 5814,
        "imageHeight": 1200,
        "url": "https://docs.firecrawl.dev/",
        "position": 1
      },
      ...
    ],
    "news": [
      {
        "title": "Y Combinator startup Firecrawl is ready to pay $1M to hire three AI agents as employees",
        "url": "https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/",
        "snippet": "It's now placed three new ads on YC's job board for “AI agents only” and has set aside a $1 million budget total to make it happen.",
        "date": "3 months ago",
        "position": 1
      },
      ...
    ]
  }
}
```

### Extracting without schema

You can now extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  app = Firecrawl(api_key="fc-YOUR-API-KEY")

  result = app.scrape(
      'https://firecrawl.dev',
      formats=[{
        "type": "json",
        "prompt": "Extract the company mission from the page."
      }],
      only_main_content=False,
      timeout=120000
  )

  print(result)
  ```

  ```js Node theme={null}
  import FirecrawlApp from "@mendable/firecrawl-js";

  const app = new FirecrawlApp({
    apiKey: "fc-YOUR_API_KEY"
  });

  const result = await app.scrape("https://firecrawl.dev", {
    formats: [{
      type: "json",
      prompt: "Extract the company mission from the page."
    }]
  });

  console.log(result);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://firecrawl.dev",
        "formats": [{
          "type": "json",
          "prompt": "Extract the company mission from the page."
        }]
      }'
  ```
</CodeGroup>

Output:

```json JSON theme={null}
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI-powered web scraping and data extraction",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI-powered web scraping and data extraction",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI-powered web scraping and data extraction",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

## Interacting with the page with Actions

Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.

Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.

It is important to almost always use the `wait` action before/after executing other actions to give enough time for the page to load.

### Example

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  doc = firecrawl.scrape(
      url="https://example.com/login",
      formats=["markdown"],
      actions=[
          {"type": "write", "text": "john@example.com"},
          {"type": "press", "key": "Tab"},
          {"type": "write", "text": "secret"},
          {"type": "click", "selector": 'button[type="submit"]'},
          {"type": "wait", "milliseconds": 1500},
          {"type": "screenshot", "fullPage": True},
      ],
  )

  print(doc.markdown, doc.screenshot)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const doc = await firecrawl.scrape('https://example.com/login', {
    formats: ['markdown'],
    actions: [
      { type: 'write', text: 'john@example.com' },
      { type: 'press', key: 'Tab' },
      { type: 'write', text: 'secret' },
      { type: 'click', selector: 'button[type="submit"]' },
      { type: 'wait', milliseconds: 1500 },
      { type: 'screenshot', fullPage: true },
    ],
  });

  console.log(doc.markdown, doc.screenshot);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://example.com/login",
        "formats": ["markdown"],
        "actions": [
          { "type": "write", "text": "john@example.com" },
          { "type": "press", "key": "Tab" },
          { "type": "write", "text": "secret" },
          { "type": "click", "selector": "button[type=\"submit\"]" },
          { "type": "wait", "milliseconds": 1500 },
          { "type": "screenshot", "fullPage": true },
        ],
    }'
  ```
</CodeGroup>

### Output

<CodeGroup>
  ```json JSON theme={null}
  {
    "success": true,
    "data": {
      "markdown": "Our first Launch Week is over! [See the recap 🚀](blog/firecrawl-launch-week-1-recap)...",
      "actions": {
        "screenshots": [
          "https://alttmdsdujxrfnakrkyi.supabase.co/storage/v1/object/public/media/screenshot-75ef2d87-31e0-4349-a478-fb432a29e241.png"
        ],
        "scrapes": [
          {
            "url": "https://www.firecrawl.dev/",
            "html": "<html><body><h1>Firecrawl</h1></body></html>"
          }
        ]
      },
      "metadata": {
        "title": "Home - Firecrawl",
        "description": "Firecrawl crawls and converts any website into clean markdown.",
        "language": "en",
        "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "Turn any website into LLM-ready data.",
        "ogUrl": "https://www.firecrawl.dev/",
        "ogImage": "https://www.firecrawl.dev/og.png?123",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "http://google.com",
        "statusCode": 200
      }
    }
  }
  ```
</CodeGroup>

## Open Source vs Cloud

Firecrawl is open source available under the [AGPL-3.0 license](https://github.com/mendableai/firecrawl/blob/main/LICENSE).

To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.

Firecrawl Cloud is available at [firecrawl.dev](https://firecrawl.dev) and offers a range of features that are not available in the open source version:

<img src="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=763a6e92c8605d06294ed7ed45df85d0" alt="Firecrawl Cloud vs Open Source" data-og-width="2808" width="2808" data-og-height="856" height="856" data-path="images/open-source-cloud.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=280&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2e9112d82aec51ca204ceee026b6bad3 280w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=560&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=9fabc257f1caa297b1b8ec68fb13eddc 560w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=840&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=e766290156ea4226df484ee815f5036f 840w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=1100&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=ed02646081bce28427156ba1d8bf4fa2 1100w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=1650&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=41d72e1c116d48ebc0cfa1a3499b3e9e 1650w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=2500&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=0f6f34e97633cabdc17cbc28d7af2bb9 2500w" />

## Contributing

We love contributions! Please read our [contributing guide](https://github.com/mendableai/firecrawl/blob/main/CONTRIBUTING.md) before submitting a pull request.


# Firecrawl MCP Server
Source: https://docs.firecrawl.dev/mcp-server

Use Firecrawl's API through the Model Context Protocol

A Model Context Protocol (MCP) server implementation that integrates [Firecrawl](https://github.com/mendableai/firecrawl) for web scraping capabilities. Our MCP server is open-source and available on [GitHub](https://github.com/mendableai/firecrawl-mcp-server).

## Features

* Web scraping, crawling, and discovery
* Search and content extraction
* Deep research and batch scraping
* Cloud and self-hosted support
* Streamable HTTP support

## Installation

You can either use our remote hosted URL or run the server locally. Get your API key from [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)

### Remote hosted URL

```bash  theme={null}
https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp
```

### Running with npx

```bash  theme={null}
env FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

### Manual Installation

```bash  theme={null}
npm install -g firecrawl-mcp
```

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
   ```json  theme={null}
   {
     "mcpServers": {
       "firecrawl-mcp": {
         "command": "npx",
         "args": ["-y", "firecrawl-mcp"],
         "env": {
           "FIRECRAWL_API_KEY": "YOUR-API-KEY"
         }
       }
     }
   }
   ```

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

```json  theme={null}
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

### Running with Streamable HTTP Mode

To run the server using streamable HTTP transport locally instead of the default stdio transport:

```bash  theme={null}
env HTTP_STREAMABLE_SERVER=true FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

Use the url: [http://localhost:3000/v2/mcp](http://localhost:3000/v2/mcp) or [https://mcp.firecrawl.dev/\{FIRECRAWL\_API\_KEY}/v2/mcp](https://mcp.firecrawl.dev/\{FIRECRAWL_API_KEY}/v2/mcp)

### Installing via Smithery (Legacy)

To install Firecrawl for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@mendableai/mcp-server-firecrawl):

```bash  theme={null}
npx -y @smithery/cli install @mendableai/mcp-server-firecrawl --client claude
```

### Running on VS Code

For one-click installation, click one of the install buttons below\...

[![Install with NPX in VS Code](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl\&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D\&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D) [![Install with NPX in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-NPM-24bfa5?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl\&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D\&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D\&quality=insiders)

For manual installation, add the following JSON block to your User Settings (JSON) file in VS Code. You can do this by pressing `Ctrl + Shift + P` and typing `Preferences: Open User Settings (JSON)`.

```json  theme={null}
{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "apiKey",
        "description": "Firecrawl API Key",
        "password": true
      }
    ],
    "servers": {
      "firecrawl": {
        "command": "npx",
        "args": ["-y", "firecrawl-mcp"],
        "env": {
          "FIRECRAWL_API_KEY": "${input:apiKey}"
        }
      }
    }
  }
}
```

Optionally, you can add it to a file called `.vscode/mcp.json` in your workspace. This will allow you to share the configuration with others:

```json  theme={null}
{
  "inputs": [
    {
      "type": "promptString",
      "id": "apiKey",
      "description": "Firecrawl API Key",
      "password": true
    }
  ],
  "servers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "${input:apiKey}"
      }
    }
  }
}
```

**Note:** Some users have reported issues when adding the MCP server to VS Code due to how it validates JSON with an outdated schema format ([microsoft/vscode#155379](https://github.com/microsoft/vscode/issues/155379)).
This affects several MCP tools, including Firecrawl.

**Workaround:** Disable JSON validation in VS Code to allow the MCP server to load properly.\
See reference: [directus/directus#25906 (comment)](https://github.com/directus/directus/issues/25906#issuecomment-3369169513).

The MCP server still works fine when invoked via other extensions, but the issue occurs specifically when registering it directly in the MCP server list. We plan to add guidance once VS Code updates their schema validation.

### Running on Claude Desktop

Add this to the Claude config file:

```json  theme={null}
{
  "mcpServers": {
    "firecrawl": {
      "url": "https://mcp.firecrawl.dev/v2/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

### Running on Claude Code

Add the Firecrawl MCP server using the Claude Code CLI:

```bash  theme={null}
claude mcp add firecrawl -e FIRECRAWL_API_KEY=your-api-key -- npx -y firecrawl-mcp
```

### Running on n8n

To connect the Firecrawl MCP server in n8n:

1. Get your Firecrawl API key from [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)
2. In your n8n workflow, add an **AI Agent** node
3. In the AI Agent configuration, add a new **Tool**
4. Select **MCP Client Tool** as the tool type
5. Enter the MCP server Endpoint (replace `{YOUR_FIRECRAWL_API_KEY}` with your actual API key):

```
https://mcp.firecrawl.dev/{YOUR_FIRECRAWL_API_KEY}/v2/mcp
```

6. Set **Server Transport** to **HTTP Streamable**
7. Set **Authentication** to **None**
8. For **Tools to include**, you can select **All**, **Selected**, or **All Except** - this will expose the Firecrawl tools (scrape, crawl, map, search, extract, etc.)

For self-hosted deployments, run the MCP server with npx and enable HTTP transport mode:

```bash  theme={null}
env HTTP_STREAMABLE_SERVER=true \
    FIRECRAWL_API_KEY=fc-YOUR_API_KEY \
    FIRECRAWL_API_URL=YOUR_FIRECRAWL_INSTANCE \
    npx -y firecrawl-mcp
```

This will start the server on `http://localhost:3000/v2/mcp` which you can use in your n8n workflow as Endpoint. The `HTTP_STREAMABLE_SERVER=true` environment variable is required since n8n needs HTTP transport.

## Configuration

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
# Required for cloud API
export FIRECRAWL_API_KEY=your-api-key

# Optional retry configuration
export FIRECRAWL_RETRY_MAX_ATTEMPTS=5        # Increase max retry attempts
export FIRECRAWL_RETRY_INITIAL_DELAY=2000    # Start with 2s delay
export FIRECRAWL_RETRY_MAX_DELAY=30000       # Maximum 30s delay
export FIRECRAWL_RETRY_BACKOFF_FACTOR=3      # More aggressive backoff

# Optional credit monitoring
export FIRECRAWL_CREDIT_WARNING_THRESHOLD=2000    # Warning at 2000 credits
export FIRECRAWL_CREDIT_CRITICAL_THRESHOLD=500    # Critical at 500 credits
```

For self-hosted instance:

```bash  theme={null}
# Required for self-hosted
export FIRECRAWL_API_URL=https://firecrawl.your-domain.com

# Optional authentication for self-hosted
export FIRECRAWL_API_KEY=your-api-key  # If your instance requires auth

# Custom retry configuration
export FIRECRAWL_RETRY_MAX_ATTEMPTS=10
export FIRECRAWL_RETRY_INITIAL_DELAY=500     # Start with faster retries
```

### Custom configuration with Claude Desktop

Add this to your `claude_desktop_config.json`:

```json  theme={null}
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY_HERE",

        "FIRECRAWL_RETRY_MAX_ATTEMPTS": "5",
        "FIRECRAWL_RETRY_INITIAL_DELAY": "2000",
        "FIRECRAWL_RETRY_MAX_DELAY": "30000",
        "FIRECRAWL_RETRY_BACKOFF_FACTOR": "3",

        "FIRECRAWL_CREDIT_WARNING_THRESHOLD": "2000",
        "FIRECRAWL_CREDIT_CRITICAL_THRESHOLD": "500"
      }
    }
  }
}
```

### System Configuration

The server includes several configurable parameters that can be set via environment variables. Here are the default values if not configured:

```typescript  theme={null}
const CONFIG = {
  retry: {
    maxAttempts: 3, // Number of retry attempts for rate-limited requests
    initialDelay: 1000, // Initial delay before first retry (in milliseconds)
    maxDelay: 10000, // Maximum delay between retries (in milliseconds)
    backoffFactor: 2, // Multiplier for exponential backoff
  },
  credit: {
    warningThreshold: 1000, // Warn when credit usage reaches this level
    criticalThreshold: 100, // Critical alert when credit usage reaches this level
  },
};
```

These configurations control:

1. **Retry Behavior**

   * Automatically retries failed requests due to rate limits
   * Uses exponential backoff to avoid overwhelming the API
   * Example: With default settings, retries will be attempted at:
     * 1st retry: 1 second delay
     * 2nd retry: 2 seconds delay
     * 3rd retry: 4 seconds delay (capped at maxDelay)

2. **Credit Usage Monitoring**
   * Tracks API credit consumption for cloud API usage
   * Provides warnings at specified thresholds
   * Helps prevent unexpected service interruption
   * Example: With default settings:
     * Warning at 1000 credits remaining
     * Critical alert at 100 credits remaining

### Rate Limiting and Batch Processing

The server utilizes Firecrawl's built-in rate limiting and batch processing capabilities:

* Automatic rate limit handling with exponential backoff
* Efficient parallel processing for batch operations
* Smart request queuing and throttling
* Automatic retries for transient errors

## Available Tools

### 1. Scrape Tool (`firecrawl_scrape`)

Scrape content from a single URL with advanced options.

```json  theme={null}
{
  "name": "firecrawl_scrape",
  "arguments": {
    "url": "https://example.com",
    "formats": ["markdown"],
    "onlyMainContent": true,
    "waitFor": 1000,
    "timeout": 30000,
    "mobile": false,
    "includeTags": ["article", "main"],
    "excludeTags": ["nav", "footer"],
    "skipTlsVerification": false
  }
}
```

### 2. Batch Scrape Tool (`firecrawl_batch_scrape`)

Scrape multiple URLs efficiently with built-in rate limiting and parallel processing.

```json  theme={null}
{
  "name": "firecrawl_batch_scrape",
  "arguments": {
    "urls": ["https://example1.com", "https://example2.com"],
    "options": {
      "formats": ["markdown"],
      "onlyMainContent": true
    }
  }
}
```

Response includes operation ID for status checking:

```json  theme={null}
{
  "content": [
    {
      "type": "text",
      "text": "Batch operation queued with ID: batch_1. Use firecrawl_check_batch_status to check progress."
    }
  ],
  "isError": false
}
```

### 3. Check Batch Status (`firecrawl_check_batch_status`)

Check the status of a batch operation.

```json  theme={null}
{
  "name": "firecrawl_check_batch_status",
  "arguments": {
    "id": "batch_1"
  }
}
```

### 4. Map Tool (`firecrawl_map`)

Map a website to discover all indexed URLs on the site.

```json  theme={null}
{
  "name": "firecrawl_map",
  "arguments": {
    "url": "https://example.com",
    "search": "blog",
    "sitemap": "include",
    "includeSubdomains": false,
    "limit": 100,
    "ignoreQueryParameters": true
  }
}
```

#### Map Tool Options:

* `url`: The base URL of the website to map
* `search`: Optional search term to filter URLs
* `sitemap`: Control sitemap usage - "include", "skip", or "only"
* `includeSubdomains`: Whether to include subdomains in the mapping
* `limit`: Maximum number of URLs to return
* `ignoreQueryParameters`: Whether to ignore query parameters when mapping

**Best for:** Discovering URLs on a website before deciding what to scrape; finding specific sections of a website.
**Returns:** Array of URLs found on the site.

### 5. Search Tool (`firecrawl_search`)

Search the web and optionally extract content from search results.

```json  theme={null}
{
  "name": "firecrawl_search",
  "arguments": {
    "query": "your search query",
    "limit": 5,
    "lang": "en",
    "country": "us",
    "scrapeOptions": {
      "formats": ["markdown"],
      "onlyMainContent": true
    }
  }
}
```

### 6. Crawl Tool (`firecrawl_crawl`)

Start an asynchronous crawl with advanced options.

```json  theme={null}
{
  "name": "firecrawl_crawl",
  "arguments": {
    "url": "https://example.com",
    "maxDepth": 2,
    "limit": 100,
    "allowExternalLinks": false,
    "deduplicateSimilarURLs": true
  }
}
```

### 7. Check Crawl Status (`firecrawl_check_crawl_status`)

Check the status of a crawl job.

```json  theme={null}
{
  "name": "firecrawl_check_crawl_status",
  "arguments": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

**Returns:** Status and progress of the crawl job, including results if available.

### 8. Extract Tool (`firecrawl_extract`)

Extract structured information from web pages using LLM capabilities. Supports both cloud AI and self-hosted LLM extraction.

```json  theme={null}
{
  "name": "firecrawl_extract",
  "arguments": {
    "urls": ["https://example.com/page1", "https://example.com/page2"],
    "prompt": "Extract product information including name, price, and description",
    "systemPrompt": "You are a helpful assistant that extracts product information",
    "schema": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "price": { "type": "number" },
        "description": { "type": "string" }
      },
      "required": ["name", "price"]
    },
    "allowExternalLinks": false,
    "enableWebSearch": false,
    "includeSubdomains": false
  }
}
```

Example response:

```json  theme={null}
{
  "content": [
    {
      "type": "text",
      "text": {
        "name": "Example Product",
        "price": 99.99,
        "description": "This is an example product description"
      }
    }
  ],
  "isError": false
}
```

#### Extract Tool Options:

* `urls`: Array of URLs to extract information from
* `prompt`: Custom prompt for the LLM extraction
* `systemPrompt`: System prompt to guide the LLM
* `schema`: JSON schema for structured data extraction
* `allowExternalLinks`: Allow extraction from external links
* `enableWebSearch`: Enable web search for additional context
* `includeSubdomains`: Include subdomains in extraction

When using a self-hosted instance, the extraction will use your configured LLM. For cloud API, it uses Firecrawl's managed LLM service.

## Logging System

The server includes comprehensive logging:

* Operation status and progress
* Performance metrics
* Credit usage monitoring
* Rate limit tracking
* Error conditions

Example log messages:

```
[INFO] Firecrawl MCP Server initialized successfully
[INFO] Starting scrape for URL: https://example.com
[INFO] Batch operation queued with ID: batch_1
[WARNING] Credit usage has reached warning threshold
[ERROR] Rate limit exceeded, retrying in 2s...
```

## Error Handling

The server provides robust error handling:

* Automatic retries for transient errors
* Rate limit handling with backoff
* Detailed error messages
* Credit usage warnings
* Network resilience

Example error response:

```json  theme={null}
{
  "content": [
    {
      "type": "text",
      "text": "Error: Rate limit exceeded. Retrying in 2 seconds..."
    }
  ],
  "isError": true
}
```

## Development

```bash  theme={null}
# Install dependencies
npm install

# Build
npm run build

# Run tests
npm test
```

### Contributing

1. Fork the repository
2. Create your feature branch
3. Run tests: `npm test`
4. Submit a pull request

### Thanks to contributors

Thanks to [@vrknetha](https://github.com/vrknetha), [@cawstudios](https://caw.tech) for the initial implementation!

Thanks to MCP.so and Klavis AI for hosting and [@gstarwd](https://github.com/gstarwd), [@xiangkaiz](https://github.com/xiangkaiz) and [@zihaolin96](https://github.com/zihaolin96) for integrating our server.

## License

MIT License - see LICENSE file for details


# Migrating from v1 to v2
Source: https://docs.firecrawl.dev/migrate-to-v2

Key changes, mappings, and before/after snippets to upgrade your integration to v2.

## Overview

### Key Improvements

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

## SDK surface (v2)

### JS/TS

#### Method name changes (v1 → v2)

**Scrape, Search, and Map**

| v1 (FirecrawlApp)     | v2 (Firecrawl)            |
| --------------------- | ------------------------- |
| `scrapeUrl(url, ...)` | `scrape(url, options?)`   |
| `search(query, ...)`  | `search(query, options?)` |
| `mapUrl(url, ...)`    | `map(url, options?)`      |

**Crawling**

| v1                          | v2                              |
| --------------------------- | ------------------------------- |
| `crawlUrl(url, ...)`        | `crawl(url, options?)` (waiter) |
| `asyncCrawlUrl(url, ...)`   | `startCrawl(url, options?)`     |
| `checkCrawlStatus(id, ...)` | `getCrawlStatus(id)`            |
| `cancelCrawl(id)`           | `cancelCrawl(id)`               |
| `checkCrawlErrors(id)`      | `getCrawlErrors(id)`            |

**Batch Scraping**

| v1                                | v2                                  |
| --------------------------------- | ----------------------------------- |
| `batchScrapeUrls(urls, ...)`      | `batchScrape(urls, opts?)` (waiter) |
| `asyncBatchScrapeUrls(urls, ...)` | `startBatchScrape(urls, opts?)`     |
| `checkBatchScrapeStatus(id, ...)` | `getBatchScrapeStatus(id)`          |
| `checkBatchScrapeErrors(id)`      | `getBatchScrapeErrors(id)`          |

**Extraction**

| v1                            | v2                     |
| ----------------------------- | ---------------------- |
| `extract(urls?, params?)`     | `extract(args)`        |
| `asyncExtract(urls, params?)` | `startExtract(args)`   |
| `getExtractStatus(id)`        | `getExtractStatus(id)` |

**Other / Removed**

| v1                                | v2                    |
| --------------------------------- | --------------------- |
| `generateLLMsText(...)`           | (not in v2 SDK)       |
| `checkGenerateLLMsTextStatus(id)` | (not in v2 SDK)       |
| `crawlUrlAndWatch(...)`           | `watcher(jobId, ...)` |
| `batchScrapeUrlsAndWatch(...)`    | `watcher(jobId, ...)` |

***

### Python (sync)

#### Method name changes (v1 → v2)

**Scrape, Search, and Map**

| v1                | v2            |
| ----------------- | ------------- |
| `scrape_url(...)` | `scrape(...)` |
| `search(...)`     | `search(...)` |
| `map_url(...)`    | `map(...)`    |

**Crawling**

| v1                        | v2                      |
| ------------------------- | ----------------------- |
| `crawl_url(...)`          | `crawl(...)` (waiter)   |
| `async_crawl_url(...)`    | `start_crawl(...)`      |
| `check_crawl_status(...)` | `get_crawl_status(...)` |
| `cancel_crawl(...)`       | `cancel_crawl(...)`     |

**Batch Scraping**

| v1                             | v2                             |
| ------------------------------ | ------------------------------ |
| `batch_scrape_urls(...)`       | `batch_scrape(...)` (waiter)   |
| `async_batch_scrape_urls(...)` | `start_batch_scrape(...)`      |
| `get_batch_scrape_status(...)` | `get_batch_scrape_status(...)` |
| `get_batch_scrape_errors(...)` | `get_batch_scrape_errors(...)` |

**Extraction**

| v1                        | v2                        |
| ------------------------- | ------------------------- |
| `extract(...)`            | `extract(...)`            |
| `start_extract(...)`      | `start_extract(...)`      |
| `get_extract_status(...)` | `get_extract_status(...)` |

**Other / Removed**

| v1                                   | v2                     |
| ------------------------------------ | ---------------------- |
| `generate_llms_text(...)`            | (not in v2 SDK)        |
| `get_generate_llms_text_status(...)` | (not in v2 SDK)        |
| `watch_crawl(...)`                   | `watcher(job_id, ...)` |

***

### Python (async)

* `AsyncFirecrawl` mirrors the same methods (all awaitable).

## Formats and scrape options

* Use string formats for basics: `"markdown"`, `"html"`, `"rawHtml"`, `"links"`, `"summary"`, `"images"`.
* Instead of `parsePDF` use `parsers: [ { "type": "pdf" } | "pdf" ]`.
* Use object formats for JSON, change tracking, and screenshots:

### JSON format

<CodeGroup>
  ```js Node theme={null}
  const formats = [ {
    "type": "json",
    "prompt": "Extract the company mission from the page."
  }];

  doc = firecrawl.scrape(url, { formats });
  ```

  ```python Python theme={null}
  formats = [ { "type": "json", "prompt": "Extract the company mission from the page." } ];

  doc = firecrawl.scrape(url, formats=formats);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://docs.firecrawl.dev/",
        "formats": [{
          "type": "json",
          "prompt": "Extract the company mission from the page."
        }]
      }'
  ```
</CodeGroup>

### Screenshot format

<CodeGroup>
  ```js Node theme={null}
  // Screenshot format (JS)
  const formats = [ { "type": "screenshot", "fullPage": true, "quality": 80, "viewport": { "width": 1280, "height": 800 } } ];

  doc = firecrawl.scrape(url, { formats });
  ```

  ```python Python theme={null}
  formats = [ { "type": "screenshot", "fullPage": true, "quality": 80, "viewport": { "width": 1280, "height": 800 } } ];
  doc = firecrawl.scrape(url, formats=formats);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://docs.firecrawl.dev/",
        "formats": [{
          "type": "screenshot",
          "fullPage": true,
          "quality": 80,
          "viewport": { "width": 1280, "height": 800 }
        }]
      }'
  ```
</CodeGroup>

## Crawl options mapping (v1 → v2)

| v1                      | v2                                                   |
| ----------------------- | ---------------------------------------------------- |
| `allowBackwardCrawling` | (removed) use `crawlEntireDomain`                    |
| `maxDepth`              | (removed) use `maxDiscoveryDepth`                    |
| `ignoreSitemap` (bool)  | `sitemap` (e.g., `"only"`, `"skip"`, or `"include"`) |
| (none)                  | `prompt`                                             |

## Crawl prompt + params preview

See crawl params preview examples:

<CodeGroup>
  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const params = await firecrawl.crawlParamsPreview('https://docs.firecrawl.dev', 'Extract docs and blog');
  console.log(params);
  ```

  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key='fc-YOUR-API-KEY')
  preview = firecrawl.crawl_params_preview(url='https://docs.firecrawl.dev', prompt='Extract docs and blog')
  print(preview)
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/crawl/params-preview \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://docs.firecrawl.dev",
        "prompt": "Extract docs and blog"
      }'
  ```
</CodeGroup>


# Rate Limits
Source: https://docs.firecrawl.dev/rate-limits

Rate limits for different pricing plans and API requests

## Concurrent Browser Limits

Concurrent browsers represent how many web pages Firecrawl can process for you at the same time.
Your plan determines how many of these jobs can run simultaneously - if you exceed this limit,
additional jobs will wait in a queue until resources become available.

### Standard Plans (most API endpoints)

| Plan     | Concurrent Browsers |
| -------- | ------------------- |
| Free     | 2                   |
| Hobby    | 5                   |
| Standard | 50                  |
| Growth   | 100                 |

### Extract plans (/extract API)

| Plan     | Concurrent Browsers |
| -------- | ------------------- |
| Free     | 2                   |
| Starter  | 50                  |
| Explorer | 100                 |
| Pro      | 200                 |

## Standard API

The following rate limits apply to standard API requests and are primarily in place to prevent abuse:

| Plan     | /scrape (requests/min) | /map (requests/min) | /crawl (requests/min) | /search (requests/min) |
| -------- | ---------------------- | ------------------- | --------------------- | ---------------------- |
| Free     | 10                     | 10                  | 1                     | 5                      |
| Hobby    | 100                    | 100                 | 15                    | 50                     |
| Standard | 500                    | 500                 | 50                    | 250                    |
| Growth   | 5000                   | 5000                | 250                   | 2500                   |

|         | /crawl/status (requests/min) |
| ------- | ---------------------------- |
| Default | 1500                         |

These rate limits are enforced to ensure fair usage and availability of the API for all users. If you require higher limits, please contact us at [help@firecrawl.com](mailto:help@firecrawl.com) to discuss custom plans.

### Batch Endpoints

Batch endpoints follow the /crawl rate limit.

## Extract API

| Plan       | /extract (requests/min) |
| ---------- | ----------------------- |
| Free       | 10                      |
| Starter    | 100                     |
| Explorer   | 500                     |
| Pro        | 1000                    |
| Enterprise | Custom                  |

|      | /extract/status (requests/min) |
| ---- | ------------------------------ |
| Free | 500                            |

## FIRE-1 Agent

Requests involving the FIRE-1 agent requests have separate rate limits that are counted independently for each endpoint:

| Endpoint   | Rate Limit (requests/min) |
| ---------- | ------------------------- |
| `/scrape`  | 10                        |
| `/extract` | 10                        |

## Legacy Plans

| Plan            | /scrape (requests/min) | /crawl (concurrent req) | /search (requests/min) |
| --------------- | ---------------------- | ----------------------- | ---------------------- |
| Starter         | 100                    | 15                      | 100                    |
| Standard Legacy | 200                    | 200                     | 200                    |
| Scaled Legacy   | 250                    | 100                     | 250                    |

If you require higher limits, please contact us at [help@firecrawl.com](mailto:help@firecrawl.com) to discuss custom plans.


# Go
Source: https://docs.firecrawl.dev/sdks/go

Firecrawl Go SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.

<Warning>
  This SDK currently uses the **v1** version of the Firecrawl API, which is not the most recent (v2 is available). Some features and improvements may only be available in v2.
</Warning>

## Installation

To install the Firecrawl Go SDK, you can use go get:

```bash Go theme={null}
go get github.com/mendableai/firecrawl-go
```

## Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the `API key` as a parameter to the `FirecrawlApp` struct.
3. Set the `API URL` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `https://api.firecrawl.dev`.
4. Set the `version` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `v1`.

Here's an example of how to use the SDK with error handling:

```go Go theme={null}
import (
	"fmt"
	"log"
	"github.com/google/uuid"
	"github.com/mendableai/firecrawl-go"
)

func ptr[T any](v T) *T {
	return &v
}

func main() {
	// Initialize the FirecrawlApp with your API key
	apiKey := "fc-YOUR_API_KEY"
	apiUrl := "https://api.firecrawl.dev"
	version := "v1"

	app, err := firecrawl.NewFirecrawlApp(apiKey, apiUrl, version)
	if err != nil {
		log.Fatalf("Failed to initialize FirecrawlApp: %v", err)
	}

  // Scrape a website
  scrapeStatus, err := app.ScrapeUrl("https://firecrawl.dev", firecrawl.ScrapeParams{
    Formats: []string{"markdown", "html"},
  })
  if err != nil {
    log.Fatalf("Failed to send scrape request: %v", err)
  }

  fmt.Println(scrapeStatus)

	// Crawl a website
  idempotencyKey := uuid.New().String() // optional idempotency key
  crawlParams := &firecrawl.CrawlParams{
		ExcludePaths: []string{"blog/*"},
		MaxDepth:     ptr(2),
	}

	crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", crawlParams, &idempotencyKey)
	if err != nil {
		log.Fatalf("Failed to send crawl request: %v", err)
	}

	fmt.Println(crawlStatus) 
}
```

### Scraping a URL

To scrape a single URL with error handling, use the `ScrapeURL` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```go Go theme={null}
// Scrape a website
scrapeResult, err := app.ScrapeUrl("https://firecrawl.dev", map[string]any{
  "formats": []string{"markdown", "html"},
})
if err != nil {
  log.Fatalf("Failed to scrape URL: %v", err)
}

fmt.Println(scrapeResult)
```

### Crawling a Website

To crawl a website, use the `CrawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

```go Go theme={null}
crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", map[string]any{
  "limit": 100,
  "scrapeOptions": map[string]any{
    "formats": []string{"markdown", "html"},
  },
})
if err != nil {
  log.Fatalf("Failed to send crawl request: %v", err)
}

fmt.Println(crawlStatus) 
```

### Checking Crawl Status

To check the status of a crawl job, use the `CheckCrawlStatus` method. It takes the job ID as a parameter and returns the current status of the crawl job.

```go Go theme={null}
// Get crawl status
crawlStatus, err := app.CheckCrawlStatus("<crawl_id>")

if err != nil {
  log.Fatalf("Failed to get crawl status: %v", err)
}

fmt.Println(crawlStatus)
```

### Map a Website

Use `MapUrl` to generate a list of URLs from a website. The `params` argument let you customize the mapping process, including options to exclude subdomains or to utilize the sitemap.

```go Go theme={null}
// Map a website
mapResult, err := app.MapUrl("https://firecrawl.dev", nil)
if err != nil {
  log.Fatalf("Failed to map URL: %v", err)
}

fmt.Println(mapResult)
```

## Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.


# Node
Source: https://docs.firecrawl.dev/sdks/node

Firecrawl Node SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.

## Installation

To install the Firecrawl Node SDK, you can use npm:

```js Node theme={null}
# npm install @mendable/firecrawl-js

import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
```

## Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `FirecrawlApp` class.

Here's an example of how to use the SDK with error handling:

```js Node theme={null}
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

// Scrape a website
const scrapeResponse = await firecrawl.scrape('https://firecrawl.dev', {
  formats: ['markdown', 'html'],
});

console.log(scrapeResponse)

// Crawl a website
const crawlResponse = await firecrawl.crawl('https://firecrawl.dev', {
  limit: 100,
  scrapeOptions: {
    formats: ['markdown', 'html'],
  }
});

console.log(crawlResponse)
```

### Scraping a URL

To scrape a single URL with error handling, use the `scrapeUrl` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```js Node theme={null}
// Scrape a website:
const scrapeResult = await firecrawl.scrape('firecrawl.dev', { formats: ['markdown', 'html'] });

console.log(scrapeResult)
```

### Crawling a Website

To crawl a website with error handling, use the `crawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format. See [Pagination](#pagination) for auto/ manual pagination and limiting.

```js Node theme={null}
const job = await firecrawl.crawl('https://docs.firecrawl.dev', { limit: 5, pollInterval: 1, timeout: 120 });
console.log(job.status);
```

### Start a Crawl

Start a job without waiting using `startCrawl`. It returns a job `ID` you can use to check status. Use `crawl` when you want a waiter that blocks until completion. See [Pagination](#pagination) for paging behavior and limits.

```js Node theme={null}
const { id } = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 10 });
console.log(id);
```

### Checking Crawl Status

To check the status of a crawl job with error handling, use the `checkCrawlStatus` method. It takes the `ID` as a parameter and returns the current status of the crawl job.

```js Node theme={null}
const status = await firecrawl.getCrawlStatus("<crawl-id>");
console.log(status);
```

### Cancelling a Crawl

To cancel an crawl job, use the `cancelCrawl` method. It takes the job ID of the `startCrawl` as a parameter and returns the cancellation status.

```js Node theme={null}
const ok = await firecrawl.cancelCrawl("<crawl-id>");
console.log("Cancelled:", ok);
```

### Mapping a Website

To map a website with error handling, use the `mapUrl` method. It takes the starting URL as a parameter and returns the mapped data as a dictionary.

```js Node theme={null}
const res = await firecrawl.map('https://firecrawl.dev', { limit: 10 });
console.log(res.links);
```

### Crawling a Website with WebSockets

To crawl a website with WebSockets, use the `crawlUrlAndWatch` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

```js Node theme={null}
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

// Start a crawl and then watch it
const { id } = await firecrawl.startCrawl('https://mendable.ai', {
  excludePaths: ['blog/*'],
  limit: 5,
});

const watcher = firecrawl.watcher(id, { kind: 'crawl', pollInterval: 2, timeout: 120 });

watcher.on('document', (doc) => {
  console.log('DOC', doc);
});

watcher.on('error', (err) => {
  console.error('ERR', err?.error || err);
});

watcher.on('done', (state) => {
  console.log('DONE', state.status);
});

// Begin watching (WS with HTTP fallback)
await watcher.start();
```

### Pagination

Firecrawl endpoints for crawl and batch return a `next` URL when more data is available. The Node SDK auto-paginates by default and aggregates all documents; in that case `next` will be `null`. You can disable auto-pagination or set limits.

#### Crawl

Use the waiter method `crawl` for the simplest experience, or start a job and page manually.

##### Simple crawl (auto-pagination, default)

* See the default flow in [Crawling a Website](#crawling-a-website).

##### Manual crawl with pagination control (single page)

* Start a job, then fetch one page at a time with `autoPaginate: false`.

```js Node theme={null}
const crawlStart = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 5 });
const crawlJobId = crawlStart.id;

const crawlSingle = await firecrawl.getCrawlStatus(crawlJobId, { autoPaginate: false });
console.log('crawl single page:', crawlSingle.status, 'docs:', crawlSingle.data.length, 'next:', crawlSingle.next);
```

##### Manual crawl with limits (auto-pagination + early stop)

* Keep auto-pagination on but stop early with `maxPages`, `maxResults`, or `maxWaitTime`.

```js Node theme={null}
const crawlLimited = await firecrawl.getCrawlStatus(crawlJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 50,
  maxWaitTime: 15,
});
console.log('crawl limited:', crawlLimited.status, 'docs:', crawlLimited.data.length, 'next:', crawlLimited.next);
```

#### Batch Scrape

Use the waiter method `batchScrape`, or start a job and page manually.

##### Simple batch scrape (auto-pagination, default)

* See the default flow in [Batch Scrape](/features/batch-scrape).

##### Manual batch scrape with pagination control (single page)

* Start a job, then fetch one page at a time with `autoPaginate: false`.

```js Node theme={null}
const batchStart = await firecrawl.startBatchScrape([
  'https://docs.firecrawl.dev',
  'https://firecrawl.dev',
], { options: { formats: ['markdown'] } });
const batchJobId = batchStart.id;

const batchSingle = await firecrawl.getBatchScrapeStatus(batchJobId, { autoPaginate: false });
console.log('batch single page:', batchSingle.status, 'docs:', batchSingle.data.length, 'next:', batchSingle.next);
```

##### Manual batch scrape with limits (auto-pagination + early stop)

* Keep auto-pagination on but stop early with `maxPages`, `maxResults`, or `maxWaitTime`.

```js Node theme={null}
const batchLimited = await firecrawl.getBatchScrapeStatus(batchJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 100,
  maxWaitTime: 20,
});
console.log('batch limited:', batchLimited.status, 'docs:', batchLimited.data.length, 'next:', batchLimited.next);
```

## Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message. The examples above demonstrate how to handle these errors using `try/catch` blocks.


# Overview
Source: https://docs.firecrawl.dev/sdks/overview

Firecrawl SDKs are wrappers around the Firecrawl API to help you easily extract data from websites.

## Official SDKs

<CardGroup cols={2}>
  <Card title="Python SDK" icon="python" href="python">
    Explore the Python SDK for Firecrawl.
  </Card>

  <Card title="Node SDK" icon="node" href="node">
    Explore the Node SDK for Firecrawl.
  </Card>
</CardGroup>

## Community SDKs (v1 only)

<CardGroup cols={2}>
  <Card title="Go SDK" icon="golang" href="go">
    Explore the Go SDK for Firecrawl.
  </Card>

  <Card title="Rust SDK" icon="rust" href="rust">
    Explore the Rust SDK for Firecrawl.
  </Card>
</CardGroup>


# Python
Source: https://docs.firecrawl.dev/sdks/python

Firecrawl Python SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.

## Installation

To install the Firecrawl Python SDK, you can use pip:

```python Python theme={null}
# pip install firecrawl-py

from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
```

## Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `Firecrawl` class.

Here's an example of how to use the SDK:

```python Python theme={null}
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

# Scrape a website:
scrape_status = firecrawl.scrape(
  'https://firecrawl.dev', 
  formats=['markdown', 'html']
)
print(scrape_status)

# Crawl a website:
crawl_status = firecrawl.crawl(
  'https://firecrawl.dev', 
  limit=100, 
  scrape_options={
    'formats': ['markdown', 'html']
  }
)
print(crawl_status)
```

### Scraping a URL

To scrape a single URL, use the `scrape` method. It takes the URL as a parameter and returns the scraped document.

```python Python theme={null}
# Scrape a website:
scrape_result = firecrawl.scrape('firecrawl.dev', formats=['markdown', 'html'])
print(scrape_result)
```

### Crawl a Website

To crawl a website, use the `crawl` method. It takes the starting URL and optional options as arguments. The options allow you to specify additional settings for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format. See [Pagination](#pagination) for auto/manual pagination and limiting.

```python Python theme={null}
job = firecrawl.crawl(url="https://docs.firecrawl.dev", limit=5, poll_interval=1, timeout=120)
print(job)
```

### Start a Crawl

<Tip>Prefer non-blocking? Check out the [Async Class](#async-class) section below.</Tip>

Start a job without waiting using `start_crawl`. It returns a job `ID` you can use to check status. Use `crawl` when you want a waiter that blocks until completion. See [Pagination](#pagination) for paging behavior and limits.

```python Python theme={null}
job = firecrawl.start_crawl(url="https://docs.firecrawl.dev", limit=10)
print(job)
```

### Checking Crawl Status

To check the status of a crawl job, use the `get_crawl_status` method. It takes the job ID as a parameter and returns the current status of the crawl job.

```python Python theme={null}
status = firecrawl.get_crawl_status("<crawl-id>")
print(status)
```

### Cancelling a Crawl

To cancel an crawl job, use the `cancel_crawl` method. It takes the job ID of the `start_crawl` as a parameter and returns the cancellation status.

```python Python theme={null}
ok = firecrawl.cancel_crawl("<crawl-id>")
print("Cancelled:", ok)
```

### Map a Website

Use `map` to generate a list of URLs from a website. The options let you customize the mapping process, including excluding subdomains or utilizing the sitemap.

```python Python theme={null}
res = firecrawl.map(url="https://firecrawl.dev", limit=10)
print(res)
```

### Crawling a Website with WebSockets

To crawl a website with WebSockets, start the job with `start_crawl` and subscribe using the `watcher` helper. Create a watcher with the job ID and attach handlers (e.g., for page, completed, failed) before calling `start()`.

```python Python theme={null}
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
```

### Pagination

Firecrawl endpoints for crawl and batch return a `next` URL when more data is available. The Python SDK auto-paginates by default and aggregates all documents; in that case `next` will be `None`. You can disable auto-pagination or set limits.

#### Crawl

Use the waiter method `crawl` for the simplest experience, or start a job and page manually.

##### Simple crawl (auto-pagination, default)

* See the default flow in [Crawl a Website](#crawl-a-website).

##### Manual crawl with pagination control (single page)

* Start a job, then fetch one page at a time with `auto_paginate=False`.

```python Python theme={null}
crawl_job = client.start_crawl("https://example.com", limit=100)

status = client.get_crawl_status(crawl_job.id, pagination_config=PaginationConfig(auto_paginate=False))
print("crawl single page:", status.status, "docs:", len(status.data), "next:", status.next)
```

##### Manual crawl with limits (auto-pagination + early stop)

* Keep auto-pagination on but stop early with `max_pages`, `max_results`, or `max_wait_time`.

```python Python theme={null}
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=50, max_wait_time=15),
)
print("crawl limited:", status.status, "docs:", len(status.data), "next:", status.next)
```

#### Batch Scrape

Use the waiter method `batch_scrape`, or start a job and page manually.

##### Simple batch scrape (auto-pagination, default)

* See the default flow in [Batch Scrape](/features/batch-scrape).

##### Manual batch scrape with pagination control (single page)

* Start a job, then fetch one page at a time with `auto_paginate=False`.

```python Python theme={null}
batch_job = client.start_batch_scrape(urls)
status = client.get_batch_scrape_status(batch_job.id, pagination_config=PaginationConfig(auto_paginate=False))
print("batch single page:", status.status, "docs:", len(status.data), "next:", status.next)
```

##### Manual batch scrape with limits (auto-pagination + early stop)

* Keep auto-pagination on but stop early with `max_pages`, `max_results`, or `max_wait_time`.

```python Python theme={null}
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=100, max_wait_time=20),
)
print("batch limited:", status.status, "docs:", len(status.data), "next:", status.next)
```

## Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.

## Async Class

For async operations, use the `AsyncFirecrawl` class. Its methods mirror `Firecrawl`, but they don't block the main thread.

```python Python theme={null}
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


# Rust
Source: https://docs.firecrawl.dev/sdks/rust

Firecrawl Rust SDK is a library to help you easily scrape and crawl websites, and output the data in a format ready for use with language models (LLMs).

<Warning>
  This SDK currently uses the **v1** version of the Firecrawl API, which is not the most recent (v2 is available). Some features and improvements may only be available in v2.
</Warning>

## Installation

To install the Firecrawl Rust SDK, add the following to your `Cargo.toml`:

```yaml Rust theme={null}
# Add this to your Cargo.toml
[dependencies]
firecrawl = "^1.0"
tokio = { version = "^1", features = ["full"] }
```

## Usage

First, you need to obtain an API key from [firecrawl.dev](https://firecrawl.dev). Then, you need to initialize the `FirecrawlApp`. From there, you can access functions like `FirecrawlApp::scrape_url`, which let you use our API.

Here's an example of how to use the SDK in Rust:

```rust Rust theme={null}
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
```

### Scraping a URL

To scrape a single URL, use the `scrape_url` method. It takes the URL as a parameter and returns the scraped data as a `Document`.

```rust Rust theme={null}
let options = ScrapeOptions {
    formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
    ..Default::default()
};

let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

match scrape_result {
    Ok(data) => println!("Scrape Result:\n{}", data.markdown.unwrap()),
    Err(e) => eprintln!("Map failed: {}", e),
}
```

### Scraping with Extract

With Extract, you can easily extract structured data from any URL. You need to specify your schema in the JSON Schema format, using the `serde_json::json!` macro.

```rust Rust theme={null}
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
```

### Crawling a Website

To crawl a website, use the `crawl_url` method. This will wait for the crawl to complete, which may take a long time based on your starting URL and your options.

```rust Rust theme={null}
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
```

#### Crawling asynchronously

To crawl without waiting for the result, use the `crawl_url_async` method. It takes the same parameters, but it returns a `CrawlAsyncRespone` struct, containing the crawl's ID. You can use that ID with the `check_crawl_status` method to check the status at any time. Do note that completed crawls are deleted after 24 hours.

```rust Rust theme={null}
let crawl_id = app.crawl_url_async("https://mendable.ai", None).await?.id;

// ... later ...

let status = app.check_crawl_status(crawl_id).await?;

if status.status == CrawlStatusTypes::Completed {
    println!("Crawl is done: {:#?}", status.data);
} else {
    // ... wait some more ...
}
```

### Map a URL

Map all associated links from a starting URL.

```rust Rust theme={null}
let map_result = app.map_url("https://firecrawl.dev", None).await;

match map_result {
    Ok(data) => println!("Mapped URLs: {:#?}", data),
    Err(e) => eprintln!("Map failed: {}", e),
}
```

## Error Handling

The SDK handles errors returned by the Firecrawl API and by our dependencies, and combines them into the `FirecrawlError` enum, implementing `Error`, `Debug` and `Display`. All of our methods return a `Result<T, FirecrawlError>`.


# AI Platforms
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

## How It Works

Transform websites into AI-ready data. Power chatbots with real-time web knowledge, build RAG systems with up-to-date documentation, and enable your users to connect their AI applications to web sources.

## Why AI Platforms Choose Firecrawl

### Reduce Hallucinations with Real-Time Data

Your AI assistants need current information, not outdated training data. Whether it's domain-specific knowledge, technical documentation, or industry-specific content, Firecrawl ensures your knowledge bases stay synchronized with the latest updates-reducing hallucinations and improving response accuracy.

## Customer Stories

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

## FAQs

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

## Related Use Cases

* [Deep Research](/use-cases/deep-research) - Advanced research capabilities
* [Content Generation](/use-cases/content-generation) - AI-powered content creation
* [Developers & MCP](/use-cases/developers-mcp) - Developer integrations


# Competitive Intelligence
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

## How It Works

Stay ahead of the competition with automated monitoring. Track product launches, pricing changes, marketing campaigns, and strategic moves across competitor websites and online properties.

## What You Can Track

* **Products**: New launches, features, specs, pricing, documentation
* **Marketing**: Messaging changes, campaigns, case studies, testimonials
* **Business**: Job postings, partnerships, funding, press releases
* **Strategy**: Positioning, target markets, pricing approaches, go-to-market
* **Technical**: API changes, integrations, technology stack updates

## FAQs

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

## Related Use Cases

* [Product & E-commerce](/use-cases/product-ecommerce) - Track competitor products
* [Investment & Finance](/use-cases/investment-finance) - Market intelligence
* [SEO Platforms](/use-cases/seo-platforms) - SERP competitor tracking


# Content Generation
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

## How It Works

Firecrawl extracts insights from websites in multiple formats — including structured HTML, Markdown, JSON, and screenshots. It can also capture images and surface relevant news stories as part of your request. This means your AI content is both factually grounded and visually enriched with the latest context.

## What You Can Create

* **Sales Decks**: Custom presentations with prospect data
* **Email Campaigns**: Personalized outreach at scale
* **Marketing Content**: Data-driven blog posts and reports
* **Social Media**: Trending topic and news-driven content generation
* **Documentation**: Auto-updated technical content
* **Newsletters**: Curated updates from industry and competitor news
* **Visual Content**: Posts and reports enriched with extracted images and screenshots

## FAQs

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

## Related Use Cases

* [AI Platforms](/use-cases/ai-platforms) - Build AI-powered content tools
* [Lead Enrichment](/use-cases/lead-enrichment) - Personalize with prospect data
* [SEO Platforms](/use-cases/seo-platforms) - Optimize generated content


# Data Migration
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

## How It Works

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

## FAQs

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

## Related Use Cases

* [Product & E-commerce](/use-cases/product-ecommerce) - Catalog migrations
* [Content Generation](/use-cases/content-generation) - Content transformation
* [AI Platforms](/use-cases/ai-platforms) - Knowledge base migration


# Deep Research
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

## How It Works

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

## FAQs

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

## Related Use Cases

* [AI Platforms](/use-cases/ai-platforms) - Build AI research assistants
* [Content Generation](/use-cases/content-generation) - Research-based content
* [Competitive Intelligence](/use-cases/competitive-intelligence) - Market research


# Developers & MCP
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

## How It Works

Integrate Firecrawl directly into your AI coding workflow. Research documentation, fetch API specs, and access web data without leaving your development environment through Model Context Protocol.

## Why Developers Choose Firecrawl MCP

### Build Smarter AI Assistants

Give your AI real-time access to documentation, APIs, and web resources. Reduce outdated information and hallucinations by providing your assistant with the latest data.

### Zero Infrastructure Required

No servers to manage, no crawlers to maintain. Just configure once and your AI assistant can access websites instantly through the Model Context Protocol.

## Customer Stories

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

## FAQs

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

## Related Use Cases

* [AI Platforms](/use-cases/ai-platforms) - Build AI-powered dev tools
* [Deep Research](/use-cases/deep-research) - Complex technical research
* [Content Generation](/use-cases/content-generation) - Generate documentation


# Investment & Finance
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

## How It Works

Extract financial signals from across the web. Monitor portfolio companies, track market movements, and support due diligence workflows with real-time web data extraction.

## What You Can Track

* **Company Metrics**: Growth indicators, team changes, product launches, funding rounds
* **Market Signals**: Industry trends, competitor moves, sentiment analysis, regulatory changes
* **Risk Indicators**: Leadership changes, legal issues, regulatory mentions, customer complaints
* **Financial Data**: Pricing updates, revenue signals, partnership announcements
* **Alternative Data**: Job postings, web traffic, social signals, news mentions

## Customer Stories

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

## FAQs

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

## Related Use Cases

* [Competitive Intelligence](/use-cases/competitive-intelligence) - Track market competitors
* [Deep Research](/use-cases/deep-research) - Comprehensive market analysis
* [Lead Enrichment](/use-cases/lead-enrichment) - B2B investment opportunities


# Lead Enrichment
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

## How It Works

Turn the web into your most powerful prospecting tool. Extract company information, find decision makers, and enrich your CRM with real-time data from company websites.

## Why Sales Teams Choose Firecrawl

### Transform Directories into Pipeline

Every industry directory is a goldmine of potential customers. Firecrawl extracts thousands of qualified leads from business directories, trade associations, and conference attendee lists-complete with company details and contact information.

### Enrich CRM Data Automatically

Stop paying for stale data from traditional providers. Firecrawl pulls real-time information directly from company websites, ensuring your sales team always has the latest company news, team changes, and growth signals.

## Customer Stories

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

## Lead Sources

### Business Directories

* Industry-specific directories
* Chamber of commerce listings
* Trade association members
* Conference attendee lists

### Company Websites

* About pages and team sections
* Press releases and news
* Job postings for growth signals
* Customer case studies

## FAQs

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

## Related Use Cases

* [AI Platforms](/use-cases/ai-platforms) - Build AI sales assistants
* [Competitive Intelligence](/use-cases/competitive-intelligence) - Track competitors
* [Investment & Finance](/use-cases/investment-finance) - Investment opportunities


# Observability & Monitoring
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

## How It Works

Use Firecrawl's extraction capabilities to build observability systems for your websites. Extract page content, analyze changes over time, validate deployments, and create monitoring workflows that ensure your sites function correctly.

## What You Can Monitor

* **Availability**: Uptime, response times, error rates
* **Content**: Text changes, image updates, layout shifts
* **Performance**: Page load times, resource sizes, Core Web Vitals
* **Security**: SSL certificates, security headers, misconfigurations
* **SEO Health**: Meta tags, structured data, sitemap validity

## Monitoring Types

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

## FAQs

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

## Related Use Cases

* [Competitive Intelligence](/use-cases/competitive-intelligence) - Monitor competitor changes
* [Product & E-commerce](/use-cases/product-ecommerce) - Track inventory and pricing
* [Data Migration](/use-cases/data-migration) - Validate migrations


# Use Cases
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


# Product & E-commerce
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

## How It Works

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

## FAQs

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

## Related Use Cases

* [Lead Enrichment](/use-cases/lead-enrichment) - Enrich B2B e-commerce leads
* [Competitive Intelligence](/use-cases/competitive-intelligence) - Track competitor strategies
* [Data Migration](/use-cases/data-migration) - Migrate between platforms


# SEO Platforms
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

## How It Works

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

## FAQs

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

## Related Use Cases

* [AI Platforms](/use-cases/ai-platforms) - Build AI-powered SEO tools
* [Competitive Intelligence](/use-cases/competitive-intelligence) - Track competitor SEO
* [Content Generation](/use-cases/content-generation) - Create SEO content


# Event Types
Source: https://docs.firecrawl.dev/webhooks/events

Complete reference of all webhook events and when they trigger

This page covers all the different types of webhook events that Firecrawl can send to your endpoint. Each event type corresponds to a different stage in your scraping operations.

## Event Structure

All webhook events follow this basic structure:

```json  theme={null}
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [...],
  "metadata": {}
}
```

### Common Fields

| Field      | Type    | Description                                       |
| ---------- | ------- | ------------------------------------------------- |
| `success`  | boolean | Whether the operation was successful              |
| `type`     | string  | Event type identifier                             |
| `id`       | string  | Unique identifier for the job                     |
| `data`     | array   | Event-specific data (varies by event type)        |
| `metadata` | object  | Custom metadata from your webhook configuration   |
| `error`    | string  | Error message (present when `success` is `false`) |

## Crawl Events

Multi-page crawling operations that follow links.

### `crawl.started`

Sent when a crawl operation begins.

```json  theme={null}
{
  "success": true,
  "type": "crawl.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `crawl.page`

Sent for each individual page that gets scraped during a crawl.

```json  theme={null}
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Welcome to our website\n\nThis is the main content of the page...",
      "metadata": {
        "title": "Page Title",
        "description": "Page description",
        "url": "https://example.com/page",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com/page",
        "proxyUsed": "basic",
        "cacheState": "hit",
        "cachedAt": "2025-09-03T21:11:25.636Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

<Note>
  This is the most frequent event during crawls. You'll receive one `crawl.page`
  event for every page successfully scraped.
</Note>

### `crawl.completed`

Sent when the entire crawl operation finishes successfully.

```json  theme={null}
{
  "success": true,
  "type": "crawl.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

## Batch Scrape Events

Operations that scrape multiple specific URLs.

### `batch_scrape.started`

Sent when a batch scrape operation begins.

```json  theme={null}
{
  "success": true,
  "type": "batch_scrape.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `batch_scrape.page`

Sent for each individual URL that gets scraped in the batch.

```json  theme={null}
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Company Homepage\n\nWelcome to our company website...",
      "metadata": {
        "title": "Company Name - Homepage",
        "description": "Company description and overview",
        "url": "https://example.com",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com",
        "proxyUsed": "basic",
        "cacheState": "miss",
        "cachedAt": "2025-09-03T23:30:53.434Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

<Note>
  This is the most frequent event during batch scrapes. You'll receive one
  `batch_scrape.page` event for every URL successfully scraped.
</Note>

### `batch_scrape.completed`

Sent when the entire batch scrape operation finishes.

```json  theme={null}
{
  "success": true,
  "type": "batch_scrape.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

## Extract Events

LLM-powered data extraction operations.

### `extract.started`

Sent when an extract operation begins.

```json  theme={null}
{
  "success": true,
  "type": "extract.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `extract.completed`

Sent when an extract operation finishes successfully.

```json  theme={null}
{
  "success": true,
  "type": "extract.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "success": true,
      "data": { "siteName": "Example Site", "category": "Technology" },
      "extractId": "550e8400-e29b-41d4-a716-446655440000",
      "llmUsage": 0.0020118,
      "totalUrlsScraped": 1,
      "sources": {
        "siteName": ["https://example.com"],
        "category": ["https://example.com"]
      }
    }
  ],
  "metadata": {}
}
```

### `extract.failed`

Sent when an extract operation encounters an error.

```json  theme={null}
{
  "success": false,
  "type": "extract.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "error": "Failed to extract data: timeout exceeded",
  "metadata": {}
}
```

## Event Filtering

You can control which events you receive by specifying an `events` array in your webhook configuration:

```json  theme={null}
{
  "url": "https://your-app.com/webhook",
  "events": ["completed", "failed"]
}
```


# Overview
Source: https://docs.firecrawl.dev/webhooks/overview

Real-time notifications for your Firecrawl operations

Webhooks allow you to receive real-time notifications about your Firecrawl operations as they progress. Instead of polling for status updates, Firecrawl will automatically send HTTP POST requests to your specified endpoint when events occur.

## Supported Operations

Webhooks are supported for most major Firecrawl operations:

* **Crawl** - Get notified as pages are crawled and when crawls complete
* **Batch scrape** - Receive updates for each URL scraped in a batch
* **Extract** - Receive updates when extract jobs start, complete, or fail

## Quick Setup

Configure webhooks by adding a `webhook` object to your request:

```json JSON theme={null}
{
  "webhook": {
    "url": "https://your-domain.com/webhook",
    "metadata": {
      "any_key": "any_value"
    },
    "events": ["started", "page", "completed", "failed"]
  }
} 
```

### Configuration Options

| Field      | Type   | Required | Description                                   |
| ---------- | ------ | -------- | --------------------------------------------- |
| `url`      | string | ✅        | Your webhook endpoint URL                     |
| `headers`  | object | ❌        | Custom headers to include in webhook requests |
| `metadata` | object | ❌        | Custom data included in all webhook payloads  |
| `events`   | array  | ❌        | Event types to receive (default: all events)  |

## Basic Usage Examples

### Crawl with Webhook

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

### Batch Scrape with Webhook

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/batch/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
      ],
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }' 
```

## Handling Webhooks

Here's a simple example of handling webhooks in your application:

<CodeGroup>
  ```js Node/Express theme={null}
  import crypto from 'crypto';
  import express from 'express';

  const app = express();

  // Use raw body parser for signature verification
  app.use('/webhook/firecrawl', express.raw({ type: 'application/json' }));

  app.post('/webhook/firecrawl', (req, res) => {
    const signature = req.get('X-Firecrawl-Signature');
    const webhookSecret = process.env.FIRECRAWL_WEBHOOK_SECRET;
    
    if (!signature || !webhookSecret) {
      return res.status(401).send('Unauthorized');
    }
    
    // Extract hash from signature header
    const [algorithm, hash] = signature.split('=');
    if (algorithm !== 'sha256') {
      return res.status(401).send('Invalid signature algorithm');
    }
    
    // Compute expected signature
    const expectedSignature = crypto
      .createHmac('sha256', webhookSecret)
      .update(req.body)
      .digest('hex');
    
    // Verify signature using timing-safe comparison
    if (!crypto.timingSafeEqual(Buffer.from(hash, 'hex'), Buffer.from(expectedSignature, 'hex'))) {
      return res.status(401).send('Invalid signature');
    }
    
    // Parse and process verified webhook
    const event = JSON.parse(req.body);
    console.log('Verified Firecrawl webhook:', event);
    
    res.status(200).send('ok');
  });

  app.listen(3000, () => console.log('Listening on 3000'));
  ```

  ```python Python/Flask theme={null}
  import hmac
  import hashlib
  from flask import Flask, request, abort

  app = Flask(__name__)

  WEBHOOK_SECRET = 'your-webhook-secret-here'  # Get from Firecrawl dashboard

  @app.post('/webhook/firecrawl')
  def webhook():
      signature = request.headers.get('X-Firecrawl-Signature')
      
      if not signature:
          abort(401, 'Missing signature header')
      
      # Extract hash from signature header
      try:
          algorithm, hash_value = signature.split('=', 1)
          if algorithm != 'sha256':
              abort(401, 'Invalid signature algorithm')
      except ValueError:
          abort(401, 'Invalid signature format')
      
      # Compute expected signature
      expected_signature = hmac.new(
          WEBHOOK_SECRET.encode('utf-8'),
          request.data,
          hashlib.sha256
      ).hexdigest()
      
      # Verify signature using timing-safe comparison
      if not hmac.compare_digest(hash_value, expected_signature):
          abort(401, 'Invalid signature')
      
      # Parse and process verified webhook
      event = request.get_json(force=True)
      print('Verified Firecrawl webhook:', event)
      
      return 'ok', 200

  if __name__ == '__main__':
      app.run(port=3000)
  ```
</CodeGroup>

### Best Practices

1. **Respond quickly** – Always return a `2xx` status code within 30 seconds
2. **Process asynchronously** – For heavy processing, queue the work and respond immediately
3. **Validate authenticity** – Always verify the webhook signature (see [Security](/webhooks/security))


# Security
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

```
X-Firecrawl-Signature: sha256=abc123def456...
```

The signature is computed as follows:

1. Take the raw request body (JSON string)
2. Create HMAC-SHA256 hash using your secret key
3. Convert to hexadecimal string
4. Prefix with `sha256=`

### Implementation Examples

<CodeGroup>
  ```js Node/Express theme={null}
  import crypto from 'crypto';
  import express from 'express';

  const app = express();

  // Use raw body parser for signature verification
  app.use('/webhook/firecrawl', express.raw({ type: 'application/json' }));

  app.post('/webhook/firecrawl', (req, res) => {
    const signature = req.get('X-Firecrawl-Signature');
    const webhookSecret = process.env.FIRECRAWL_WEBHOOK_SECRET;
    
    if (!signature || !webhookSecret) {
      return res.status(401).send('Unauthorized');
    }
    
    // Extract hash from signature header
    const [algorithm, hash] = signature.split('=');
    if (algorithm !== 'sha256') {
      return res.status(401).send('Invalid signature algorithm');
    }
    
    // Compute expected signature
    const expectedSignature = crypto
      .createHmac('sha256', webhookSecret)
      .update(req.body)
      .digest('hex');
    
    // Verify signature using timing-safe comparison
    if (!crypto.timingSafeEqual(Buffer.from(hash, 'hex'), Buffer.from(expectedSignature, 'hex'))) {
      return res.status(401).send('Invalid signature');
    }
    
    // Parse and process verified webhook
    const event = JSON.parse(req.body);
    console.log('Verified Firecrawl webhook:', event);
    
    res.status(200).send('ok');
  });

  app.listen(3000, () => console.log('Listening on 3000'));
  ```

  ```python Python/Flask theme={null}
  import hmac
  import hashlib
  from flask import Flask, request, abort

  app = Flask(__name__)

  WEBHOOK_SECRET = 'your-webhook-secret-here'  # Get from Firecrawl dashboard

  @app.post('/webhook/firecrawl')
  def webhook():
      signature = request.headers.get('X-Firecrawl-Signature')
      
      if not signature:
          abort(401, 'Missing signature header')
      
      # Extract hash from signature header
      try:
          algorithm, hash_value = signature.split('=', 1)
          if algorithm != 'sha256':
              abort(401, 'Invalid signature algorithm')
      except ValueError:
          abort(401, 'Invalid signature format')
      
      # Compute expected signature
      expected_signature = hmac.new(
          WEBHOOK_SECRET.encode('utf-8'),
          request.data,
          hashlib.sha256
      ).hexdigest()
      
      # Verify signature using timing-safe comparison
      if not hmac.compare_digest(hash_value, expected_signature):
          abort(401, 'Invalid signature')
      
      # Parse and process verified webhook
      event = request.get_json(force=True)
      print('Verified Firecrawl webhook:', event)
      
      return 'ok', 200

  if __name__ == '__main__':
      app.run(port=3000)
  ```
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

```javascript  theme={null}
// ❌ BAD - No verification
app.post('/webhook', (req, res) => {
  processWebhook(req.body); // Dangerous!
  res.status(200).send('OK');
});

// ✅ GOOD - Verified first
app.post('/webhook', (req, res) => {
  if (!verifySignature(req)) {
    return res.status(401).send('Unauthorized');
  }
  processWebhook(req.body);
  res.status(200).send('OK');
});
```

### Use Timing-Safe Comparisons

Standard string comparison can leak timing information. Use dedicated functions:

* **Node.js**: `crypto.timingSafeEqual()`
* **Python**: `hmac.compare_digest()`
* **Other languages**: Look for "constant-time" or "timing-safe" comparison functions

### Require HTTPS

Always use HTTPS endpoints for webhooks:

```json  theme={null}
{
  "url": "https://your-app.com/webhook" // ✅ Secure
}
```

```json  theme={null}
{
  "url": "http://your-app.com/webhook" // ❌ Insecure
}
```


# Testing & Debugging
Source: https://docs.firecrawl.dev/webhooks/testing

Tools and techniques for developing and debugging webhooks

This page covers tools and techniques for testing webhook integrations during development and debugging issues in production.

## Local Development

### Exposing Local Servers

Since webhooks need to reach your server from the internet, you'll need to expose your local development server publicly.

#### Using Cloudflare Tunnels

[Cloudflare Tunnels](https://github.com/cloudflare/cloudflared/releases) provide a free way to securely expose your local development server to the internet without requiring account registration or opening firewall ports:

```bash  theme={null}
# Download cloudflared from GitHub releases or use a package manager

# Expose your local server
cloudflared tunnel --url localhost:3000

# Example output:
# Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):
# https://abc123.trycloudflare.com
```

Use the provided URL in your webhook configuration:

```json  theme={null}
{
  "url": "https://abc123.trycloudflare.com/webhook"
}
```

## Debugging Common Issues

### Webhooks Not Arriving

1. **Check URL accessibility** – Ensure your endpoint is publicly accessible
2. **Verify HTTPS** – Webhook URLs must use HTTPS
3. **Check firewall settings** – Allow incoming connections to your webhook port
4. **Review event filters** – Ensure you're subscribed to the correct event types

### Signature Verification Failing

1. **Check the secret key** – Ensure you're using the correct secret

2. **Verify raw body usage** – Make sure you're using the raw request body:

```javascript  theme={null}
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


# Running locally
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

```bash  theme={null}
docker build -t nuq-postgres .
```

and then run:

```bash  theme={null}
docker run --name nuqdb \          
  -e POSTGRES_PASSWORD=postgres \
  -p 5433:5432 \
  -v nuq-data:/var/lib/postgresql/data \
  -d nuq-postgres
```

Set environment variables in a .env in the /apps/api/ directory you can copy over the template in .env.example.

To start, we wont set up authentication, or any optional sub services (pdf parsing, JS blocking support, AI features )

.env:

```
# ===== Required ENVS ======
NUM_WORKERS_PER_QUEUE=8
PORT=3002
HOST=0.0.0.0
REDIS_URL=redis://localhost:6379
REDIS_RATE_LIMIT_URL=redis://localhost:6379

## To turn on DB authentication, you need to set up supabase.
USE_DB_AUTHENTICATION=false

## Using the PostgreSQL for queuing -- change if credentials, host, or DB is different
NUQ_DATABASE_URL=postgres://postgres:postgres@localhost:5433/postgres

# ===== Optional ENVS ======

# Supabase Setup (used to support DB authentication, advanced logging, etc.)
SUPABASE_ANON_TOKEN=
SUPABASE_URL=
SUPABASE_SERVICE_TOKEN=

# Other Optionals
TEST_API_KEY= # use if you've set up authentication and want to test with a real API key
OPENAI_API_KEY= # add for LLM dependednt features (image alt generation, etc.)
BULL_AUTH_KEY= @
PLAYWRIGHT_MICROSERVICE_URL=  # set if you'd like to run a playwright fallback
LLAMAPARSE_API_KEY= #Set if you have a llamaparse key you'd like to use to parse pdfs
SLACK_WEBHOOK_URL= # set if you'd like to send slack server health status messages
POSTHOG_API_KEY= # set if you'd like to send posthog events like job logs
POSTHOG_HOST= # set if you'd like to send posthog events like job logs


```

### Installing dependencies

First, install the dependencies using pnpm.

```bash  theme={null}
# cd apps/api # to make sure you're in the right folder
pnpm install # make sure you have pnpm version 9+!
```

### Running the project

You're going to need to open 3 terminals.

### Terminal 1 - setting up redis

Run the command anywhere within your project

```bash  theme={null}
redis-server
```

### Terminal 2 - setting up the service

Now, navigate to the apps/api/ directory and run:

```bash  theme={null}
pnpm start
# if you are going to use the [llm-extract feature](https://github.com/firecrawl/firecrawl/pull/586/), you should also export OPENAI_API_KEY=sk-______
```

This will start the workers who are responsible for processing crawl jobs.

### Terminal 3 - sending our first request.

Alright: now let’s send our first request.

```curl  theme={null}
curl -X GET http://localhost:3002/test
```

This should return the response Hello, world!

If you’d like to test the crawl endpoint, you can run this

```curl  theme={null}
curl -X POST http://localhost:3002/v1/crawl \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://mendable.ai"
    }'
```

### Alternative: Using Docker Compose

For a simpler setup, you can use Docker Compose to run all services:

1. Prerequisites: Make sure you have Docker and Docker Compose installed
2. Copy the `.env.example` file to `.env` in the `/apps/api/` directory and configure as needed
3. From the root directory, run:

```bash  theme={null}
docker compose up
```

This will start Redis, the API server, and workers automatically in the correct configuration.

## Tests:

The best way to do this is run the test with `npm run test:snips`.


# Open Source vs Cloud
Source: https://docs.firecrawl.dev/contributing/open-source-or-cloud

Understand the differences between Firecrawl's open-source and cloud offerings

Firecrawl is open source available under the [AGPL-3.0 license](https://github.com/mendableai/firecrawl/blob/main/LICENSE).

To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.

Firecrawl Cloud is available at [firecrawl.dev](https://firecrawl.dev) and offers a range of features that are not available in the open source version:

<img src="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=763a6e92c8605d06294ed7ed45df85d0" alt="Firecrawl Cloud vs Open Source" data-og-width="2808" width="2808" data-og-height="856" height="856" data-path="images/open-source-cloud.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=280&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2e9112d82aec51ca204ceee026b6bad3 280w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=560&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=9fabc257f1caa297b1b8ec68fb13eddc 560w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=840&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=e766290156ea4226df484ee815f5036f 840w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=1100&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=ed02646081bce28427156ba1d8bf4fa2 1100w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=1650&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=41d72e1c116d48ebc0cfa1a3499b3e9e 1650w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=2500&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=0f6f34e97633cabdc17cbc28d7af2bb9 2500w" />


# Self-hosting
Source: https://docs.firecrawl.dev/contributing/self-host

Learn how to self-host Firecrawl to run on your own and contribute to the project.

#### Contributor?

Welcome to [Firecrawl](https://firecrawl.dev) 🔥! Here are some instructions on how to get the project locally so you can run it on your own and contribute.

If you're contributing, note that the process is similar to other open-source repos, i.e., fork Firecrawl, make changes, run tests, PR.

If you have any questions or would like help getting on board, join our Discord community [here](https://discord.gg/gSmWdAkdwd) for more information or submit an issue on Github [here](https://github.com/mendableai/firecrawl/issues/new/choose)!

## Self-hosting Firecrawl

Refer to [SELF\_HOST.md](https://github.com/mendableai/firecrawl/blob/main/SELF_HOST.md) for instructions on how to run it locally.

## Why?

Self-hosting Firecrawl is particularly beneficial for organizations with stringent security policies that require data to remain within controlled environments. Here are some key reasons to consider self-hosting:

* **Enhanced Security and Compliance:** By self-hosting, you ensure that all data handling and processing complies with internal and external regulations, keeping sensitive information within your secure infrastructure. Note that Firecrawl is a Mendable product and relies on SOC2 Type2 certification, which means that the platform adheres to high industry standards for managing data security.
* **Customizable Services:** Self-hosting allows you to tailor the services, such as the Playwright service, to meet specific needs or handle particular use cases that may not be supported by the standard cloud offering.
* **Learning and Community Contribution:** By setting up and maintaining your own instance, you gain a deeper understanding of how Firecrawl works, which can also lead to more meaningful contributions to the project.

### Considerations

However, there are some limitations and additional responsibilities to be aware of:

1. **Limited Access to Fire-engine:** Currently, self-hosted instances of Firecrawl do not have access to Fire-engine, which includes advanced features for handling IP blocks, robot detection mechanisms, and more. This means that while you can manage basic scraping tasks, more complex scenarios might require additional configuration or might not be supported.
2. **Manual Configuration Required:** If you need to use scraping methods beyond the basic fetch and Playwright options, you will need to manually configure these in the `.env` file. This requires a deeper understanding of the technologies and might involve more setup time.

Self-hosting Firecrawl is ideal for those who need full control over their scraping and data processing environments but comes with the trade-off of additional maintenance and configuration efforts.

## Steps

1. First, start by installing the dependencies

* Docker [instructions](https://docs.docker.com/get-docker/)

2. Set environment variables

Create an `.env` in the root directory you can copy over the template in `apps/api/.env.example`

To start, we wont set up authentication, or any optional sub services (pdf parsing, JS blocking support, AI features)

```
# .env

# ===== Required ENVS ======
PORT=3002
HOST=0.0.0.0

# Note: PORT is used by both the main API server and worker liveness check endpoint

# To turn on DB authentication, you need to set up Supabase.
USE_DB_AUTHENTICATION=false

# ===== Optional ENVS ======

## === AI features (JSON format on scrape, /extract API) ===
# Provide your OpenAI API key here to enable AI features
# OPENAI_API_KEY=

# Experimental: Use Ollama
# OLLAMA_BASE_URL=http://localhost:11434/api
# MODEL_NAME=deepseek-r1:7b
# MODEL_EMBEDDING_NAME=nomic-embed-text

# Experimental: Use any OpenAI-compatible API
# OPENAI_BASE_URL=https://example.com/v1
# OPENAI_API_KEY=

## === Proxy ===
# PROXY_SERVER can be a full URL (e.g. http://0.1.2.3:1234) or just an IP and port combo (e.g. 0.1.2.3:1234)
# Do not uncomment PROXY_USERNAME and PROXY_PASSWORD if your proxy is unauthenticated
# PROXY_SERVER=
# PROXY_USERNAME=
# PROXY_PASSWORD=

## === /search API ===
# By default, the /search API will use Google search.

# You can specify a SearXNG server with the JSON format enabled, if you'd like to use that instead of direct Google.
# You can also customize the engines and categories parameters, but the defaults should also work just fine.
# SEARXNG_ENDPOINT=http://your.searxng.server
# SEARXNG_ENGINES=
# SEARXNG_CATEGORIES=

## === Other ===

# Supabase Setup (used to support DB authentication, advanced logging, etc.)
# SUPABASE_ANON_TOKEN=
# SUPABASE_URL=
# SUPABASE_SERVICE_TOKEN=

# Use if you've set up authentication and want to test with a real API key
# TEST_API_KEY=

# This key lets you access the queue admin panel. Change this if your deployment is publicly accessible.
BULL_AUTH_KEY=CHANGEME

# This is now autoconfigured by the docker-compose.yaml. You shouldn't need to set it.
# PLAYWRIGHT_MICROSERVICE_URL=http://playwright-service:3000/scrape
# REDIS_URL=redis://redis:6379
# REDIS_RATE_LIMIT_URL=redis://redis:6379

# Set if you have a llamaparse key you'd like to use to parse pdfs
# LLAMAPARSE_API_KEY=

# Set if you'd like to send server health status messages to Slack
# SLACK_WEBHOOK_URL=

# Set if you'd like to send posthog events like job logs
# POSTHOG_API_KEY=
# POSTHOG_HOST=

## === System Resource Configuration ===
# Maximum CPU usage threshold (0.0-1.0). Worker will reject new jobs when CPU usage exceeds this value.
# Default: 0.8 (80%)
# MAX_CPU=0.8

# Maximum RAM usage threshold (0.0-1.0). Worker will reject new jobs when memory usage exceeds this value.
# Default: 0.8 (80%)
# MAX_RAM=0.8

# Set if you'd like to allow local webhooks to be sent to your self-hosted instance
# ALLOW_LOCAL_WEBHOOKS=true
```

3. *(Optional) Running with TypeScript Playwright Service*

   * Update the `docker-compose.yml` file to change the Playwright service:

     ```plaintext  theme={null}
         build: apps/playwright-service
     ```

     TO

     ```plaintext  theme={null}
         build: apps/playwright-service-ts
     ```

   * Set the `PLAYWRIGHT_MICROSERVICE_URL` in your `.env` file:

     ```plaintext  theme={null}
     PLAYWRIGHT_MICROSERVICE_URL=http://localhost:3000/scrape
     ```

   * Don't forget to set the proxy server in your `.env` file as needed.

4. Build and run the Docker containers:

   ```bash  theme={null}
   docker compose build
   docker compose up
   ```

This will run a local instance of Firecrawl which can be accessed at `http://localhost:3002`.

You should be able to see the Bull Queue Manager UI on `http://localhost:3002/admin/@/queues`.

5. *(Optional)* Test the API

If you’d like to test the crawl endpoint, you can run this:

```bash  theme={null}
curl -X POST http://localhost:3002/v2/crawl \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'
```

## Troubleshooting

This section provides solutions to common issues you might encounter while setting up or running your self-hosted instance of Firecrawl.

### Supabase client is not configured

**Symptom:**

```bash  theme={null}
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Attempted to access Supabase client when it's not configured.
[YYYY-MM-DDTHH:MM:SS.SSSz]ERROR - Error inserting scrape event: Error: Supabase client is not configured.
```

**Explanation:**
This error occurs because the Supabase client setup is not completed. You should be able to scrape and crawl with no problems. Right now it's not possible to configure Supabase in self-hosted instances.

### You're bypassing authentication

**Symptom:**

```bash  theme={null}
[YYYY-MM-DDTHH:MM:SS.SSSz]WARN - You're bypassing authentication
```

**Explanation:**
This error occurs because the Supabase client setup is not completed. You should be able to scrape and crawl with no problems. Right now it's not possible to configure Supabase in self-hosted instances.

### Docker containers fail to start

**Symptom:**
Docker containers exit unexpectedly or fail to start.

**Solution:**
Check the Docker logs for any error messages using the command:

```bash  theme={null}
docker logs [container_name]
```

* Ensure all required environment variables are set correctly in the .env file.
* Verify that all Docker services defined in docker-compose.yml are correctly configured and the necessary images are available.

### Connection issues with Redis

**Symptom:**
Errors related to connecting to Redis, such as timeouts or "Connection refused".

**Solution:**

* Ensure that the Redis service is up and running in your Docker environment.
* Verify that the REDIS\_URL and REDIS\_RATE\_LIMIT\_URL in your .env file point to the correct Redis instance.
* Check network settings and firewall rules that may block the connection to the Redis port.

### API endpoint does not respond

**Symptom:**
API requests to the Firecrawl instance timeout or return no response.

**Solution:**

* Ensure that the Firecrawl service is running by checking the Docker container status.
* Verify that the PORT and HOST settings in your .env file are correct and that no other service is using the same port.
* Check the network configuration to ensure that the host is accessible from the client making the API request.

By addressing these common issues, you can ensure a smoother setup and operation of your self-hosted Firecrawl instance.

## Install Firecrawl on a Kubernetes Cluster (Simple Version)

Read the [examples/kubernetes-cluster-install/README.md](https://github.com/firecrawl/firecrawl/tree/main/examples/kubernetes/cluster-install#readme) for instructions on how to install Firecrawl on a Kubernetes Cluster.


# Extract
Source: https://docs.firecrawl.dev/features/extract

Extract structured data from pages using LLMs

The `/extract` endpoint simplifies collecting structured data from any number of URLs or entire domains. Provide a list of URLs, optionally with wildcards (e.g., `example.com/*`), and a prompt or schema describing the information you want. Firecrawl handles the details of crawling, parsing, and collating large or small datasets.

<Info>We've simplified billing so that Extract now uses credits, just like all of the other endpoints. Each credit is worth 15 tokens.</Info>

## Using `/extract`

You can extract structured data from one or multiple URLs, including wildcards:

* **Single Page**\
  Example: `https://firecrawl.dev/some-page`
* **Multiple Pages / Full Domain**\
  Example: `https://firecrawl.dev/*`

When you use `/*`, Firecrawl will automatically crawl and parse all URLs it can discover in that domain, then extract the requested data. This feature is experimental; email [help@firecrawl.com](mailto:help@firecrawl.com) if you have issues.

### Example Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  schema = {
      "type": "object",
      "properties": {"description": {"type": "string"}},
      "required": ["description"],
  }

  res = firecrawl.extract(
      urls=["https://docs.firecrawl.dev"],
      prompt="Extract the page description",
      schema=schema,
  )

  print(res.data["description"])
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const schema = {
    type: 'object',
    properties: {
      title: { type: 'string' }
    },
    required: ['title']
  };

  const res = await firecrawl.extract({
    urls: ['https://docs.firecrawl.dev'],
    prompt: 'Extract the page title',
    schema,
    scrapeOptions: { formats: [{ type: 'json', prompt: 'Extract', schema }] }
  });

  console.log(res.status || res.success, res.data);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/extract" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "urls": ["https://docs.firecrawl.dev"],
      "prompt": "Extract the page title",
      "schema": {
        "type": "object",
        "properties": {"title": {"type": "string"}},
        "required": ["title"]
      },
      "scrapeOptions": {
        "formats": [{"type": "json", "prompt": "Extract", "schema": {"type": "object"}}]
      }
    }'
  ```
</CodeGroup>

**Key Parameters:**

* **urls**: An array of one or more URLs. Supports wildcards (`/*`) for broader crawling.
* **prompt** (Optional unless no schema): A natural language prompt describing the data you want or specifying how you want that data structured.
* **schema** (Optional unless no prompt): A more rigid structure if you already know the JSON layout.
* **enableWebSearch** (Optional): When `true`, extraction can follow links outside the specified domain.

See [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/extract) for more details.

### Response (sdks)

```json JSON theme={null}
{
  "success": true,
  "data": {
    "company_mission": "Firecrawl is the easiest way to extract data from the web. Developers use us to reliably convert URLs into LLM-ready markdown or structured data with a single API call.",
    "supports_sso": false,
    "is_open_source": true,
    "is_in_yc": true
  }
}
```

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
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
      api_key="fc-YOUR_API_KEY"
  )

  # Start an extraction job first
  extract_job = firecrawl.start_extract([
      'https://docs.firecrawl.dev/*', 
      'https://firecrawl.dev/'
  ], prompt="Extract the company mission and features from these pages.")

  # Get the status of the extraction job
  job_status = firecrawl.get_extract_status(extract_job.id)

  print(job_status)
  # Example output:
  # id=None
  # status='completed'
  # expires_at=datetime.datetime(...)
  # success=True
  # data=[{ ... }]
  # error=None
  # warning=None
  # sources=None
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const started = await firecrawl.startExtract({
    urls: ['https://docs.firecrawl.dev'],
    prompt: 'Extract title',
    schema: { type: 'object', properties: { title: { type: 'string' } }, required: ['title'] },
  });

  if (started.id) {
    const done = await firecrawl.getExtractStatus(started.id);
    console.log(done.status, done.data);
  }
  ```

  ```bash cURL theme={null}
  curl -s -X GET "https://api.firecrawl.dev/v2/extract/<jobId>" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY"
  ```
</CodeGroup>

### Possible States

* **completed**: The extraction finished successfully.
* **processing**: Firecrawl is still processing your request.
* **failed**: An error occurred; data was not fully extracted.
* **cancelled**: The job was cancelled by the user.

#### Pending Example

```json JSON theme={null}
{
  "success": true,
  "data": [],
  "status": "processing",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

#### Completed Example

```json JSON theme={null}
{
  "success": true,
  "data": {
      "company_mission": "Firecrawl is the easiest way to extract data from the web. Developers use us to reliably convert URLs into LLM-ready markdown or structured data with a single API call.",
      "supports_sso": false,
      "is_open_source": true,
      "is_in_yc": true
    },
  "status": "completed",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

## Extracting without a Schema

If you prefer not to define a strict structure, you can simply provide a `prompt`. The underlying model will choose a structure for you, which can be useful for more exploratory or flexible requests.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  # Initialize the FirecrawlApp with your API key
  firecrawl = Firecrawl(api_key='your_api_key')

  data = firecrawl.extract([
    'https://docs.firecrawl.dev/',
    'https://firecrawl.dev/'
  ], prompt="Extract Firecrawl's mission from the page.")
  print(data)
  ```

  ```js Node theme={null}
  import Firecrawl from "@mendable/firecrawl-js";

  const firecrawl = new Firecrawl({
  apiKey: "fc-YOUR_API_KEY"
  });

  const scrapeResult = await firecrawl.extract([
  'https://docs.firecrawl.dev/',
  'https://firecrawl.dev/'
  ], {
  prompt: "Extract Firecrawl's mission from the page."
  });

  console.log(scrapeResult);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/extract \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "urls": [
          "https://docs.firecrawl.dev/",
          "https://firecrawl.dev/"
        ],
        "prompt": "Extract Firecrawl'\''s mission from the page."
      }'
  ```
</CodeGroup>

```json JSON theme={null}
{
  "success": true,
  "data": {
    "company_mission": "Turn websites into LLM-ready data. Power your AI apps with clean data crawled from any website."
  }
}
```

## Improving Results with Web Search

Setting `enableWebSearch = true` in your request will expand the crawl beyond the provided URL set. This can capture supporting or related information from linked pages.

Here's an example that extracts information about dash cams, enriching the results with data from related pages:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  # Initialize the FirecrawlApp with your API key

  firecrawl = Firecrawl(api_key='your_api_key')

  data = firecrawl.extract([
  'https://nextbase.com/dash-cams/622gw-dash-cam'
  ], prompt="Extract details about the best dash cams including prices, features, pros/cons and reviews.", enable_web_search=True)
  print(data)
  ```

  ```js Node theme={null}
  import Firecrawl from "@mendable/firecrawl-js";

  const firecrawl = new Firecrawl({
  apiKey: "fc-YOUR_API_KEY"
  });

  const scrapeResult = await firecrawl.extract([
  'https://nextbase.com/dash-cams/622gw-dash-cam'
  ], {
  prompt: "Extract details about the best dash cams including prices, features, pros/cons and reviews.",
  enableWebSearch: true // Enable web search for better context
  });

  console.log(scrapeResult);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/extract \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "urls": ["https://nextbase.com/dash-cams/622gw-dash-cam"],
        "prompt": "Extract details about the best dash cams including prices, features, pros/cons, and reviews.",
        "enableWebSearch": true
      }'
  ```
</CodeGroup>

### Example Response with Web Search

```json JSON theme={null}
{
  "success": true,
  "data": {
    "dash_cams": [
      {
        "name": "Nextbase 622GW",
        "price": "$399.99",
        "features": [
          "4K video recording",
          "Image stabilization",
          "Alexa built-in",
          "What3Words integration"
        ],
        /* Information below enriched with other websites like 
        https://www.techradar.com/best/best-dash-cam found 
        via enableWebSearch parameter */
        "pros": [
          "Excellent video quality",
          "Great night vision",
          "Built-in GPS"
        ],
        "cons": ["Premium price point", "App can be finicky"]
      }
    ],
  }

```

The response includes additional context gathered from related pages, providing more comprehensive and accurate information.

## Extracting without URLs

The `/extract` endpoint now supports extracting structured data using a prompt without needing specific URLs. This is useful for research or when exact URLs are unknown. Currently in Alpha.

<CodeGroup>
  ```python Python theme={null}
  from pydantic import BaseModel

  class ExtractSchema(BaseModel):
      company_mission: str


  # Define the prompt for extraction
  prompt = 'Extract the company mission from Firecrawl\'s website.'

  # Perform the extraction
  scrape_result = firecrawl.extract(prompt=prompt, schema=ExtractSchema)

  print(scrape_result)
  ```

  ```js Node theme={null}
  import { z } from "zod";

  // Define schema to extract contents into
  const schema = z.object({
    company_mission: z.string(),
  });

  const scrapeResult = await firecrawl.extract([], {
    prompt: "Extract the company mission from Firecrawl's website.",
    schema: schema
  });

  console.log(scrapeResult);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/extract \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "urls": [],
        "prompt": "Extract the company mission from the Firecrawl's website.",
        "schema": {
          "type": "object",
          "properties": {
            "company_mission": {
              "type": "string"
            }
          },
          "required": ["company_mission"]
        }
      }'
  ```
</CodeGroup>

## Known Limitations (Beta)

1. **Large-Scale Site Coverage**\
   Full coverage of massive sites (e.g., "all products on Amazon") in a single request is not yet supported.

2. **Complex Logical Queries**\
   Requests like "find every post from 2025" may not reliably return all expected data. More advanced query capabilities are in progress.

3. **Occasional Inconsistencies**\
   Results might differ across runs, particularly for very large or dynamic sites. Usually it captures core details, but some variation is possible.

4. **Beta State**\
   Since `/extract` is still in Beta, features and performance will continue to evolve. We welcome bug reports and feedback to help us improve.

## Using FIRE-1

FIRE-1 is an AI agent that enhances Firecrawl's scraping capabilities. It can controls browser actions and navigates complex website structures to enable comprehensive data extraction beyond traditional scraping methods.

You can leverage the FIRE-1 agent with the `/extract` endpoint for complex extraction tasks that require navigation across multiple pages or interaction with elements.

**Example (cURL):**

```bash  theme={null}
curl -X POST https://api.firecrawl.dev/v2/extract \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": ["https://example-forum.com/topic/123"],
      "prompt": "Extract all user comments from this forum thread.",
      "schema": {
        "type": "object",
        "properties": {
          "comments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "author": {"type": "string"},
                "comment_text": {"type": "string"}
              },
              "required": ["author", "comment_text"]
            }
          }
        },
        "required": ["comments"]
      },
      "agent": {
        "model": "FIRE-1"
      }
    }'
```

> FIRE-1 is already live and available under preview.

## Billing and Usage Tracking

We've simplified billing so that Extract now uses credits, just like all of the other endpoints. Each credit is worth 15 tokens.

You can monitor Extract usage via the [dashboard](https://www.firecrawl.dev/app/extract).

Have feedback or need help? Email [help@firecrawl.com](mailto:help@firecrawl.com).


# Search
Source: https://docs.firecrawl.dev/features/search

Search the web and get full content from results

Firecrawl's search API allows you to perform web searches and optionally scrape the search results in one operation.

* Choose specific output formats (markdown, HTML, links, screenshots)
* Search the web with customizable parameters (location, etc.)
* Optionally retrieve content from search results in various formats
* Control the number of results and set timeouts

For details, see the [Search Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/search).

## Performing a Search with Firecrawl

### /search endpoint

Used to perform web searches and optionally retrieve content from the results.

### Installation

<CodeGroup>
  ```python Python theme={null}
  # pip install firecrawl-py

  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
  ```

  ```js Node theme={null}
  # npm install @mendable/firecrawl-js

  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
  ```
</CodeGroup>

### Basic Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  results = firecrawl.search(
      query="firecrawl",
      limit=3,
  )
  print(results)
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const results = await firecrawl.search('firecrawl', {
    limit: 3,
    scrapeOptions: { formats: ['markdown'] }
  });
  console.log(results);
  ```

  ```bash  theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/search" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "query": "firecrawl",
      "limit": 3
    }'
  ```
</CodeGroup>

### Response

SDKs will return the data object directly. cURL will return the complete payload.

```json JSON theme={null}
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://www.firecrawl.dev/",
        "title": "Firecrawl - The Web Data API for AI",
        "description": "The web crawling, scraping, and search API for AI. Built for scale. Firecrawl delivers the entire internet to AI agents and builders.",
        "position": 1
      },
      {
        "url": "https://github.com/mendableai/firecrawl",
        "title": "mendableai/firecrawl: Turn entire websites into LLM-ready ... - GitHub",
        "description": "Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data.",
        "position": 2
      },
      ...
    ],
    "images": [
      {
        "title": "Quickstart | Firecrawl",
        "imageUrl": "https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png",
        "imageWidth": 5814,
        "imageHeight": 1200,
        "url": "https://docs.firecrawl.dev/",
        "position": 1
      },
      ...
    ],
    "news": [
      {
        "title": "Y Combinator startup Firecrawl is ready to pay $1M to hire three AI agents as employees",
        "url": "https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/",
        "snippet": "It's now placed three new ads on YC's job board for “AI agents only” and has set aside a $1 million budget total to make it happen.",
        "date": "3 months ago",
        "position": 1
      },
      ...
    ]
  }
}
```

## Search result types

In addition to regular web results, Search supports specialized result types via the `sources` parameter:

* `web`: standard web results (default)
* `news`: news-focused results
* `images`: image search results

## Search Categories

Filter search results by specific categories using the `categories` parameter:

* `github`: Search within GitHub repositories, code, issues, and documentation
* `research`: Search academic and research websites (arXiv, Nature, IEEE, PubMed, etc.)
* `pdf`: Search for PDFs

### GitHub Category Search

Search specifically within GitHub repositories:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "web scraping python",
    "categories": ["github"],
    "limit": 10
  }'
```

### Research Category Search

Search academic and research websites:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "machine learning transformers",
    "categories": ["research"],
    "limit": 10
  }'
```

### Mixed Category Search

Combine multiple categories in one search:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "neural networks",
    "categories": ["github", "research"],
    "limit": 15
  }'
```

### Category Response Format

Each search result includes a `category` field indicating its source:

```json  theme={null}
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/neural-network",
        "title": "Neural Network Implementation",
        "description": "A PyTorch implementation of neural networks",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "Advances in Neural Network Architecture",
        "description": "Research paper on neural network improvements",
        "category": "research"
      }
    ]
  }
}
```

Examples:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "openai",
    "sources": ["news"],
    "limit": 5
  }'
```

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "jupiter",
    "sources": ["images"],
    "limit": 8
  }'
```

### HD Image Search with Size Filtering

Use Google Images operators to find high-resolution images:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sunset imagesize:1920x1080",
    "sources": ["images"],
    "limit": 5
  }'
```

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "mountain wallpaper larger:2560x1440",
    "sources": ["images"],
    "limit": 8
  }'
```

**Common HD resolutions:**

* `imagesize:1920x1080` - Full HD (1080p)
* `imagesize:2560x1440` - QHD (1440p)
* `imagesize:3840x2160` - 4K UHD
* `larger:1920x1080` - HD and above
* `larger:2560x1440` - QHD and above

## Search with Content Scraping

Search and retrieve content from the search results in one operation.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Search and scrape content
  results = firecrawl.search(
      "firecrawl web scraping",
      limit=3,
      scrape_options={
          "formats": ["markdown", "links"]
      }
  )
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const results = await firecrawl.search('firecrawl', {
    limit: 3,
    scrapeOptions: { formats: ['markdown'] }
  });
  console.log(results);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer fc-YOUR_API_KEY" \
    -d '{
      "query": "firecrawl web scraping",
      "limit": 3,
      "scrapeOptions": {
        "formats": ["markdown", "links"]
      }
    }'
  ```
</CodeGroup>

Every option in scrape endpoint is supported by this search endpoint through the `scrapeOptions` parameter.

### Response with Scraped Content

```json  theme={null}
{
  "success": true,
  "data": [
    {
      "title": "Firecrawl - The Ultimate Web Scraping API",
      "description": "Firecrawl is a powerful web scraping API that turns any website into clean, structured data for AI and analysis.",
      "url": "https://firecrawl.dev/",
      "markdown": "# Firecrawl\n\nThe Ultimate Web Scraping API\n\n## Turn any website into clean, structured data\n\nFirecrawl makes it easy to extract data from websites for AI applications, market research, content aggregation, and more...",
      "links": [
        "https://firecrawl.dev/pricing",
        "https://firecrawl.dev/docs",
        "https://firecrawl.dev/guides"
      ],
      "metadata": {
        "title": "Firecrawl - The Ultimate Web Scraping API",
        "description": "Firecrawl is a powerful web scraping API that turns any website into clean, structured data for AI and analysis.",
        "sourceURL": "https://firecrawl.dev/",
        "statusCode": 200
      }
    }
  ]
}
```

## Advanced Search Options

Firecrawl's search API supports various parameters to customize your search:

### Location Customization

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Search with location settings (Germany)
  search_result = firecrawl.search(
      "web scraping tools",
      limit=5,
      location="Germany"
  )

  # Process the results
  for result in search_result.data:
      print(f"Title: {result['title']}")
      print(f"URL: {result['url']}")
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  // Search with location settings (Germany)
  const results = await firecrawl.search('web scraping tools', {
    limit: 5,
    location: "Germany"
  });

  // Process the results
  console.log(results);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer fc-YOUR_API_KEY" \
    -d '{
      "query": "web scraping tools",
      "limit": 5,
      "location": "Germany"
    }'
  ```
</CodeGroup>

### Time-Based Search

Use the `tbs` parameter to filter results by time:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  results = firecrawl.search(
      query="firecrawl",
      limit=5,
      tbs="qdr:d",
  )
  print(len(results.get('web', [])))
  ```

  ```js Node theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const results = await firecrawl.search('firecrawl', {
    limit: 5,
    tbs: 'qdr:d', // past day
  });

  console.log(results.web);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer fc-YOUR_API_KEY" \
    -d '{
      "query": "latest web scraping techniques",
      "limit": 5,
      "tbs": "qdr:w"
    }'
  ```
</CodeGroup>

Common `tbs` values:

* `qdr:h` - Past hour
* `qdr:d` - Past 24 hours
* `qdr:w` - Past week
* `qdr:m` - Past month
* `qdr:y` - Past year

For more precise time filtering, you can specify exact date ranges using the custom date range format:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  # Initialize the client with your API key
  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Search for results from December 2024
  search_result = firecrawl.search(
      "firecrawl updates",
      limit=10,
      tbs="cdr:1,cd_min:12/1/2024,cd_max:12/31/2024"
  )
  ```

  ```js JavaScript theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  // Initialize the client with your API key
  const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

  // Search for results from December 2024
  firecrawl.search("firecrawl updates", {
    limit: 10,
    tbs: "cdr:1,cd_min:12/1/2024,cd_max:12/31/2024"
  })
  .then(searchResult => {
    console.log(searchResult.data);
  });
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer fc-YOUR_API_KEY" \
    -d '{
      "query": "firecrawl updates",
      "limit": 10,
      "tbs": "cdr:1,cd_min:12/1/2024,cd_max:12/31/2024"
    }'
  ```
</CodeGroup>

### Custom Timeout

Set a custom timeout for search operations:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import FirecrawlApp

  # Initialize the client with your API key
  app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

  # Set a 30-second timeout
  search_result = app.search(
      "complex search query",
      limit=10,
      timeout=30000  # 30 seconds in milliseconds
  )
  ```

  ```js JavaScript theme={null}
  import FirecrawlApp from '@mendable/firecrawl-js';

  // Initialize the client with your API key
  const app = new FirecrawlApp({apiKey: "fc-YOUR_API_KEY"});

  // Set a 30-second timeout
  app.search("complex search query", {
    limit: 10,
    timeout: 30000  // 30 seconds in milliseconds
  })
  .then(searchResult => {
    // Process results
    console.log(searchResult.data);
  });
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer fc-YOUR_API_KEY" \
    -d '{
      "query": "complex search query",
      "limit": 10,
      "timeout": 30000
    }'
  ```
</CodeGroup>

## Cost Implications

When search results are not scraped (no scrape options specified), the cost is 2 credits per 10 search results. When scraping is enabled, there is no additional charge for basic scrapes of each search result beyond the standard scraping costs.

However, be aware of these cost factors:

* **PDF parsing**: 1 credit per PDF page (can significantly increase costs for multi-page PDFs)
* **Stealth proxy mode**: +4 additional credits per search result
* ***JSON mode***: +4 additional credits per search result

To control costs:

* Set `parsers: []` if you don't need PDF content
* Use `proxy: "basic"` instead of `"stealth"` when possible
* Limit the number of search results with the `limit` parameter

## Advanced Scraping Options

For more details about the scraping options, refer to the [Scrape Feature documentation](https://docs.firecrawl.dev/features/scrape). Everything except for the FIRE-1 Agent and Change-Tracking features are supported by this Search endpoint.


# Go
Source: https://docs.firecrawl.dev/sdks/go

Firecrawl Go SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.

<Warning>
  This SDK currently uses the **v1** version of the Firecrawl API, which is not the most recent (v2 is available). Some features and improvements may only be available in v2.
</Warning>

## Installation

To install the Firecrawl Go SDK, you can use go get:

```bash Go theme={null}
go get github.com/mendableai/firecrawl-go
```

## Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the `API key` as a parameter to the `FirecrawlApp` struct.
3. Set the `API URL` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `https://api.firecrawl.dev`.
4. Set the `version` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `v1`.

Here's an example of how to use the SDK with error handling:

```go Go theme={null}
import (
	"fmt"
	"log"
	"github.com/google/uuid"
	"github.com/mendableai/firecrawl-go"
)

func ptr[T any](v T) *T {
	return &v
}

func main() {
	// Initialize the FirecrawlApp with your API key
	apiKey := "fc-YOUR_API_KEY"
	apiUrl := "https://api.firecrawl.dev"
	version := "v1"

	app, err := firecrawl.NewFirecrawlApp(apiKey, apiUrl, version)
	if err != nil {
		log.Fatalf("Failed to initialize FirecrawlApp: %v", err)
	}

  // Scrape a website
  scrapeStatus, err := app.ScrapeUrl("https://firecrawl.dev", firecrawl.ScrapeParams{
    Formats: []string{"markdown", "html"},
  })
  if err != nil {
    log.Fatalf("Failed to send scrape request: %v", err)
  }

  fmt.Println(scrapeStatus)

	// Crawl a website
  idempotencyKey := uuid.New().String() // optional idempotency key
  crawlParams := &firecrawl.CrawlParams{
		ExcludePaths: []string{"blog/*"},
		MaxDepth:     ptr(2),
	}

	crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", crawlParams, &idempotencyKey)
	if err != nil {
		log.Fatalf("Failed to send crawl request: %v", err)
	}

	fmt.Println(crawlStatus) 
}
```

### Scraping a URL

To scrape a single URL with error handling, use the `ScrapeURL` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```go Go theme={null}
// Scrape a website
scrapeResult, err := app.ScrapeUrl("https://firecrawl.dev", map[string]any{
  "formats": []string{"markdown", "html"},
})
if err != nil {
  log.Fatalf("Failed to scrape URL: %v", err)
}

fmt.Println(scrapeResult)
```

### Crawling a Website

To crawl a website, use the `CrawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

```go Go theme={null}
crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", map[string]any{
  "limit": 100,
  "scrapeOptions": map[string]any{
    "formats": []string{"markdown", "html"},
  },
})
if err != nil {
  log.Fatalf("Failed to send crawl request: %v", err)
}

fmt.Println(crawlStatus) 
```

### Checking Crawl Status

To check the status of a crawl job, use the `CheckCrawlStatus` method. It takes the job ID as a parameter and returns the current status of the crawl job.

```go Go theme={null}
// Get crawl status
crawlStatus, err := app.CheckCrawlStatus("<crawl_id>")

if err != nil {
  log.Fatalf("Failed to get crawl status: %v", err)
}

fmt.Println(crawlStatus)
```

### Map a Website

Use `MapUrl` to generate a list of URLs from a website. The `params` argument let you customize the mapping process, including options to exclude subdomains or to utilize the sitemap.

```go Go theme={null}
// Map a website
mapResult, err := app.MapUrl("https://firecrawl.dev", nil)
if err != nil {
  log.Fatalf("Failed to map URL: %v", err)
}

fmt.Println(mapResult)
```

## Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.


# Node
Source: https://docs.firecrawl.dev/sdks/node

Firecrawl Node SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.

## Installation

To install the Firecrawl Node SDK, you can use npm:

```js Node theme={null}
# npm install @mendable/firecrawl-js

import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
```

## Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `FirecrawlApp` class.

Here's an example of how to use the SDK with error handling:

```js Node theme={null}
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

// Scrape a website
const scrapeResponse = await firecrawl.scrape('https://firecrawl.dev', {
  formats: ['markdown', 'html'],
});

console.log(scrapeResponse)

// Crawl a website
const crawlResponse = await firecrawl.crawl('https://firecrawl.dev', {
  limit: 100,
  scrapeOptions: {
    formats: ['markdown', 'html'],
  }
});

console.log(crawlResponse)
```

### Scraping a URL

To scrape a single URL with error handling, use the `scrapeUrl` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```js Node theme={null}
// Scrape a website:
const scrapeResult = await firecrawl.scrape('firecrawl.dev', { formats: ['markdown', 'html'] });

console.log(scrapeResult)
```

### Crawling a Website

To crawl a website with error handling, use the `crawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format. See [Pagination](#pagination) for auto/ manual pagination and limiting.

```js Node theme={null}
const job = await firecrawl.crawl('https://docs.firecrawl.dev', { limit: 5, pollInterval: 1, timeout: 120 });
console.log(job.status);
```

### Start a Crawl

Start a job without waiting using `startCrawl`. It returns a job `ID` you can use to check status. Use `crawl` when you want a waiter that blocks until completion. See [Pagination](#pagination) for paging behavior and limits.

```js Node theme={null}
const { id } = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 10 });
console.log(id);
```

### Checking Crawl Status

To check the status of a crawl job with error handling, use the `checkCrawlStatus` method. It takes the `ID` as a parameter and returns the current status of the crawl job.

```js Node theme={null}
const status = await firecrawl.getCrawlStatus("<crawl-id>");
console.log(status);
```

### Cancelling a Crawl

To cancel an crawl job, use the `cancelCrawl` method. It takes the job ID of the `startCrawl` as a parameter and returns the cancellation status.

```js Node theme={null}
const ok = await firecrawl.cancelCrawl("<crawl-id>");
console.log("Cancelled:", ok);
```

### Mapping a Website

To map a website with error handling, use the `mapUrl` method. It takes the starting URL as a parameter and returns the mapped data as a dictionary.

```js Node theme={null}
const res = await firecrawl.map('https://firecrawl.dev', { limit: 10 });
console.log(res.links);
```

### Crawling a Website with WebSockets

To crawl a website with WebSockets, use the `crawlUrlAndWatch` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

```js Node theme={null}
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

// Start a crawl and then watch it
const { id } = await firecrawl.startCrawl('https://mendable.ai', {
  excludePaths: ['blog/*'],
  limit: 5,
});

const watcher = firecrawl.watcher(id, { kind: 'crawl', pollInterval: 2, timeout: 120 });

watcher.on('document', (doc) => {
  console.log('DOC', doc);
});

watcher.on('error', (err) => {
  console.error('ERR', err?.error || err);
});

watcher.on('done', (state) => {
  console.log('DONE', state.status);
});

// Begin watching (WS with HTTP fallback)
await watcher.start();
```

### Pagination

Firecrawl endpoints for crawl and batch return a `next` URL when more data is available. The Node SDK auto-paginates by default and aggregates all documents; in that case `next` will be `null`. You can disable auto-pagination or set limits.

#### Crawl

Use the waiter method `crawl` for the simplest experience, or start a job and page manually.

##### Simple crawl (auto-pagination, default)

* See the default flow in [Crawling a Website](#crawling-a-website).

##### Manual crawl with pagination control (single page)

* Start a job, then fetch one page at a time with `autoPaginate: false`.

```js Node theme={null}
const crawlStart = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 5 });
const crawlJobId = crawlStart.id;

const crawlSingle = await firecrawl.getCrawlStatus(crawlJobId, { autoPaginate: false });
console.log('crawl single page:', crawlSingle.status, 'docs:', crawlSingle.data.length, 'next:', crawlSingle.next);
```

##### Manual crawl with limits (auto-pagination + early stop)

* Keep auto-pagination on but stop early with `maxPages`, `maxResults`, or `maxWaitTime`.

```js Node theme={null}
const crawlLimited = await firecrawl.getCrawlStatus(crawlJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 50,
  maxWaitTime: 15,
});
console.log('crawl limited:', crawlLimited.status, 'docs:', crawlLimited.data.length, 'next:', crawlLimited.next);
```

#### Batch Scrape

Use the waiter method `batchScrape`, or start a job and page manually.

##### Simple batch scrape (auto-pagination, default)

* See the default flow in [Batch Scrape](/features/batch-scrape).

##### Manual batch scrape with pagination control (single page)

* Start a job, then fetch one page at a time with `autoPaginate: false`.

```js Node theme={null}
const batchStart = await firecrawl.startBatchScrape([
  'https://docs.firecrawl.dev',
  'https://firecrawl.dev',
], { options: { formats: ['markdown'] } });
const batchJobId = batchStart.id;

const batchSingle = await firecrawl.getBatchScrapeStatus(batchJobId, { autoPaginate: false });
console.log('batch single page:', batchSingle.status, 'docs:', batchSingle.data.length, 'next:', batchSingle.next);
```

##### Manual batch scrape with limits (auto-pagination + early stop)

* Keep auto-pagination on but stop early with `maxPages`, `maxResults`, or `maxWaitTime`.

```js Node theme={null}
const batchLimited = await firecrawl.getBatchScrapeStatus(batchJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 100,
  maxWaitTime: 20,
});
console.log('batch limited:', batchLimited.status, 'docs:', batchLimited.data.length, 'next:', batchLimited.next);
```

## Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message. The examples above demonstrate how to handle these errors using `try/catch` blocks.


# Overview
Source: https://docs.firecrawl.dev/sdks/overview

Firecrawl SDKs are wrappers around the Firecrawl API to help you easily extract data from websites.

## Official SDKs

<CardGroup cols={2}>
  <Card title="Python SDK" icon="python" href="python">
    Explore the Python SDK for Firecrawl.
  </Card>

  <Card title="Node SDK" icon="node" href="node">
    Explore the Node SDK for Firecrawl.
  </Card>
</CardGroup>

## Community SDKs (v1 only)

<CardGroup cols={2}>
  <Card title="Go SDK" icon="golang" href="go">
    Explore the Go SDK for Firecrawl.
  </Card>

  <Card title="Rust SDK" icon="rust" href="rust">
    Explore the Rust SDK for Firecrawl.
  </Card>
</CardGroup>


# Python
Source: https://docs.firecrawl.dev/sdks/python

Firecrawl Python SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.

## Installation

To install the Firecrawl Python SDK, you can use pip:

```python Python theme={null}
# pip install firecrawl-py

from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
```

## Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `Firecrawl` class.

Here's an example of how to use the SDK:

```python Python theme={null}
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

# Scrape a website:
scrape_status = firecrawl.scrape(
  'https://firecrawl.dev', 
  formats=['markdown', 'html']
)
print(scrape_status)

# Crawl a website:
crawl_status = firecrawl.crawl(
  'https://firecrawl.dev', 
  limit=100, 
  scrape_options={
    'formats': ['markdown', 'html']
  }
)
print(crawl_status)
```

### Scraping a URL

To scrape a single URL, use the `scrape` method. It takes the URL as a parameter and returns the scraped document.

```python Python theme={null}
# Scrape a website:
scrape_result = firecrawl.scrape('firecrawl.dev', formats=['markdown', 'html'])
print(scrape_result)
```

### Crawl a Website

To crawl a website, use the `crawl` method. It takes the starting URL and optional options as arguments. The options allow you to specify additional settings for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format. See [Pagination](#pagination) for auto/manual pagination and limiting.

```python Python theme={null}
job = firecrawl.crawl(url="https://docs.firecrawl.dev", limit=5, poll_interval=1, timeout=120)
print(job)
```

### Start a Crawl

<Tip>Prefer non-blocking? Check out the [Async Class](#async-class) section below.</Tip>

Start a job without waiting using `start_crawl`. It returns a job `ID` you can use to check status. Use `crawl` when you want a waiter that blocks until completion. See [Pagination](#pagination) for paging behavior and limits.

```python Python theme={null}
job = firecrawl.start_crawl(url="https://docs.firecrawl.dev", limit=10)
print(job)
```

### Checking Crawl Status

To check the status of a crawl job, use the `get_crawl_status` method. It takes the job ID as a parameter and returns the current status of the crawl job.

```python Python theme={null}
status = firecrawl.get_crawl_status("<crawl-id>")
print(status)
```

### Cancelling a Crawl

To cancel an crawl job, use the `cancel_crawl` method. It takes the job ID of the `start_crawl` as a parameter and returns the cancellation status.

```python Python theme={null}
ok = firecrawl.cancel_crawl("<crawl-id>")
print("Cancelled:", ok)
```

### Map a Website

Use `map` to generate a list of URLs from a website. The options let you customize the mapping process, including excluding subdomains or utilizing the sitemap.

```python Python theme={null}
res = firecrawl.map(url="https://firecrawl.dev", limit=10)
print(res)
```

### Crawling a Website with WebSockets

To crawl a website with WebSockets, start the job with `start_crawl` and subscribe using the `watcher` helper. Create a watcher with the job ID and attach handlers (e.g., for page, completed, failed) before calling `start()`.

```python Python theme={null}
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
```

### Pagination

Firecrawl endpoints for crawl and batch return a `next` URL when more data is available. The Python SDK auto-paginates by default and aggregates all documents; in that case `next` will be `None`. You can disable auto-pagination or set limits.

#### Crawl

Use the waiter method `crawl` for the simplest experience, or start a job and page manually.

##### Simple crawl (auto-pagination, default)

* See the default flow in [Crawl a Website](#crawl-a-website).

##### Manual crawl with pagination control (single page)

* Start a job, then fetch one page at a time with `auto_paginate=False`.

```python Python theme={null}
crawl_job = client.start_crawl("https://example.com", limit=100)

status = client.get_crawl_status(crawl_job.id, pagination_config=PaginationConfig(auto_paginate=False))
print("crawl single page:", status.status, "docs:", len(status.data), "next:", status.next)
```

##### Manual crawl with limits (auto-pagination + early stop)

* Keep auto-pagination on but stop early with `max_pages`, `max_results`, or `max_wait_time`.

```python Python theme={null}
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=50, max_wait_time=15),
)
print("crawl limited:", status.status, "docs:", len(status.data), "next:", status.next)
```

#### Batch Scrape

Use the waiter method `batch_scrape`, or start a job and page manually.

##### Simple batch scrape (auto-pagination, default)

* See the default flow in [Batch Scrape](/features/batch-scrape).

##### Manual batch scrape with pagination control (single page)

* Start a job, then fetch one page at a time with `auto_paginate=False`.

```python Python theme={null}
batch_job = client.start_batch_scrape(urls)
status = client.get_batch_scrape_status(batch_job.id, pagination_config=PaginationConfig(auto_paginate=False))
print("batch single page:", status.status, "docs:", len(status.data), "next:", status.next)
```

##### Manual batch scrape with limits (auto-pagination + early stop)

* Keep auto-pagination on but stop early with `max_pages`, `max_results`, or `max_wait_time`.

```python Python theme={null}
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=100, max_wait_time=20),
)
print("batch limited:", status.status, "docs:", len(status.data), "next:", status.next)
```

## Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.

## Async Class

For async operations, use the `AsyncFirecrawl` class. Its methods mirror `Firecrawl`, but they don't block the main thread.

```python Python theme={null}
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


# Rust
Source: https://docs.firecrawl.dev/sdks/rust

Firecrawl Rust SDK is a library to help you easily scrape and crawl websites, and output the data in a format ready for use with language models (LLMs).

<Warning>
  This SDK currently uses the **v1** version of the Firecrawl API, which is not the most recent (v2 is available). Some features and improvements may only be available in v2.
</Warning>

## Installation

To install the Firecrawl Rust SDK, add the following to your `Cargo.toml`:

```yaml Rust theme={null}
# Add this to your Cargo.toml
[dependencies]
firecrawl = "^1.0"
tokio = { version = "^1", features = ["full"] }
```

## Usage

First, you need to obtain an API key from [firecrawl.dev](https://firecrawl.dev). Then, you need to initialize the `FirecrawlApp`. From there, you can access functions like `FirecrawlApp::scrape_url`, which let you use our API.

Here's an example of how to use the SDK in Rust:

```rust Rust theme={null}
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
```

### Scraping a URL

To scrape a single URL, use the `scrape_url` method. It takes the URL as a parameter and returns the scraped data as a `Document`.

```rust Rust theme={null}
let options = ScrapeOptions {
    formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
    ..Default::default()
};

let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

match scrape_result {
    Ok(data) => println!("Scrape Result:\n{}", data.markdown.unwrap()),
    Err(e) => eprintln!("Map failed: {}", e),
}
```

### Scraping with Extract

With Extract, you can easily extract structured data from any URL. You need to specify your schema in the JSON Schema format, using the `serde_json::json!` macro.

```rust Rust theme={null}
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
```

### Crawling a Website

To crawl a website, use the `crawl_url` method. This will wait for the crawl to complete, which may take a long time based on your starting URL and your options.

```rust Rust theme={null}
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
```

#### Crawling asynchronously

To crawl without waiting for the result, use the `crawl_url_async` method. It takes the same parameters, but it returns a `CrawlAsyncRespone` struct, containing the crawl's ID. You can use that ID with the `check_crawl_status` method to check the status at any time. Do note that completed crawls are deleted after 24 hours.

```rust Rust theme={null}
let crawl_id = app.crawl_url_async("https://mendable.ai", None).await?.id;

// ... later ...

let status = app.check_crawl_status(crawl_id).await?;

if status.status == CrawlStatusTypes::Completed {
    println!("Crawl is done: {:#?}", status.data);
} else {
    // ... wait some more ...
}
```

### Map a URL

Map all associated links from a starting URL.

```rust Rust theme={null}
let map_result = app.map_url("https://firecrawl.dev", None).await;

match map_result {
    Ok(data) => println!("Mapped URLs: {:#?}", data),
    Err(e) => eprintln!("Map failed: {}", e),
}
```

## Error Handling

The SDK handles errors returned by the Firecrawl API and by our dependencies, and combines them into the `FirecrawlError` enum, implementing `Error`, `Debug` and `Display`. All of our methods return a `Result<T, FirecrawlError>`.


# Event Types
Source: https://docs.firecrawl.dev/webhooks/events

Complete reference of all webhook events and when they trigger

This page covers all the different types of webhook events that Firecrawl can send to your endpoint. Each event type corresponds to a different stage in your scraping operations.

## Event Structure

All webhook events follow this basic structure:

```json  theme={null}
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [...],
  "metadata": {}
}
```

### Common Fields

| Field      | Type    | Description                                       |
| ---------- | ------- | ------------------------------------------------- |
| `success`  | boolean | Whether the operation was successful              |
| `type`     | string  | Event type identifier                             |
| `id`       | string  | Unique identifier for the job                     |
| `data`     | array   | Event-specific data (varies by event type)        |
| `metadata` | object  | Custom metadata from your webhook configuration   |
| `error`    | string  | Error message (present when `success` is `false`) |

## Crawl Events

Multi-page crawling operations that follow links.

### `crawl.started`

Sent when a crawl operation begins.

```json  theme={null}
{
  "success": true,
  "type": "crawl.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `crawl.page`

Sent for each individual page that gets scraped during a crawl.

```json  theme={null}
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Welcome to our website\n\nThis is the main content of the page...",
      "metadata": {
        "title": "Page Title",
        "description": "Page description",
        "url": "https://example.com/page",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com/page",
        "proxyUsed": "basic",
        "cacheState": "hit",
        "cachedAt": "2025-09-03T21:11:25.636Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

<Note>
  This is the most frequent event during crawls. You'll receive one `crawl.page`
  event for every page successfully scraped.
</Note>

### `crawl.completed`

Sent when the entire crawl operation finishes successfully.

```json  theme={null}
{
  "success": true,
  "type": "crawl.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

## Batch Scrape Events

Operations that scrape multiple specific URLs.

### `batch_scrape.started`

Sent when a batch scrape operation begins.

```json  theme={null}
{
  "success": true,
  "type": "batch_scrape.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `batch_scrape.page`

Sent for each individual URL that gets scraped in the batch.

```json  theme={null}
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Company Homepage\n\nWelcome to our company website...",
      "metadata": {
        "title": "Company Name - Homepage",
        "description": "Company description and overview",
        "url": "https://example.com",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com",
        "proxyUsed": "basic",
        "cacheState": "miss",
        "cachedAt": "2025-09-03T23:30:53.434Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

<Note>
  This is the most frequent event during batch scrapes. You'll receive one
  `batch_scrape.page` event for every URL successfully scraped.
</Note>

### `batch_scrape.completed`

Sent when the entire batch scrape operation finishes.

```json  theme={null}
{
  "success": true,
  "type": "batch_scrape.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

## Extract Events

LLM-powered data extraction operations.

### `extract.started`

Sent when an extract operation begins.

```json  theme={null}
{
  "success": true,
  "type": "extract.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `extract.completed`

Sent when an extract operation finishes successfully.

```json  theme={null}
{
  "success": true,
  "type": "extract.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "success": true,
      "data": { "siteName": "Example Site", "category": "Technology" },
      "extractId": "550e8400-e29b-41d4-a716-446655440000",
      "llmUsage": 0.0020118,
      "totalUrlsScraped": 1,
      "sources": {
        "siteName": ["https://example.com"],
        "category": ["https://example.com"]
      }
    }
  ],
  "metadata": {}
}
```

### `extract.failed`

Sent when an extract operation encounters an error.

```json  theme={null}
{
  "success": false,
  "type": "extract.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "error": "Failed to extract data: timeout exceeded",
  "metadata": {}
}
```

## Event Filtering

You can control which events you receive by specifying an `events` array in your webhook configuration:

```json  theme={null}
{
  "url": "https://your-app.com/webhook",
  "events": ["completed", "failed"]
}
```


# Overview
Source: https://docs.firecrawl.dev/webhooks/overview

Real-time notifications for your Firecrawl operations

Webhooks allow you to receive real-time notifications about your Firecrawl operations as they progress. Instead of polling for status updates, Firecrawl will automatically send HTTP POST requests to your specified endpoint when events occur.

## Supported Operations

Webhooks are supported for most major Firecrawl operations:

* **Crawl** - Get notified as pages are crawled and when crawls complete
* **Batch scrape** - Receive updates for each URL scraped in a batch
* **Extract** - Receive updates when extract jobs start, complete, or fail

## Quick Setup

Configure webhooks by adding a `webhook` object to your request:

```json JSON theme={null}
{
  "webhook": {
    "url": "https://your-domain.com/webhook",
    "metadata": {
      "any_key": "any_value"
    },
    "events": ["started", "page", "completed", "failed"]
  }
} 
```

### Configuration Options

| Field      | Type   | Required | Description                                   |
| ---------- | ------ | -------- | --------------------------------------------- |
| `url`      | string | ✅        | Your webhook endpoint URL                     |
| `headers`  | object | ❌        | Custom headers to include in webhook requests |
| `metadata` | object | ❌        | Custom data included in all webhook payloads  |
| `events`   | array  | ❌        | Event types to receive (default: all events)  |

## Basic Usage Examples

### Crawl with Webhook

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

### Batch Scrape with Webhook

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/batch/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
      ],
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }' 
```

## Handling Webhooks

Here's a simple example of handling webhooks in your application:

<CodeGroup>
  ```js Node/Express theme={null}
  import crypto from 'crypto';
  import express from 'express';

  const app = express();

  // Use raw body parser for signature verification
  app.use('/webhook/firecrawl', express.raw({ type: 'application/json' }));

  app.post('/webhook/firecrawl', (req, res) => {
    const signature = req.get('X-Firecrawl-Signature');
    const webhookSecret = process.env.FIRECRAWL_WEBHOOK_SECRET;
    
    if (!signature || !webhookSecret) {
      return res.status(401).send('Unauthorized');
    }
    
    // Extract hash from signature header
    const [algorithm, hash] = signature.split('=');
    if (algorithm !== 'sha256') {
      return res.status(401).send('Invalid signature algorithm');
    }
    
    // Compute expected signature
    const expectedSignature = crypto
      .createHmac('sha256', webhookSecret)
      .update(req.body)
      .digest('hex');
    
    // Verify signature using timing-safe comparison
    if (!crypto.timingSafeEqual(Buffer.from(hash, 'hex'), Buffer.from(expectedSignature, 'hex'))) {
      return res.status(401).send('Invalid signature');
    }
    
    // Parse and process verified webhook
    const event = JSON.parse(req.body);
    console.log('Verified Firecrawl webhook:', event);
    
    res.status(200).send('ok');
  });

  app.listen(3000, () => console.log('Listening on 3000'));
  ```

  ```python Python/Flask theme={null}
  import hmac
  import hashlib
  from flask import Flask, request, abort

  app = Flask(__name__)

  WEBHOOK_SECRET = 'your-webhook-secret-here'  # Get from Firecrawl dashboard

  @app.post('/webhook/firecrawl')
  def webhook():
      signature = request.headers.get('X-Firecrawl-Signature')
      
      if not signature:
          abort(401, 'Missing signature header')
      
      # Extract hash from signature header
      try:
          algorithm, hash_value = signature.split('=', 1)
          if algorithm != 'sha256':
              abort(401, 'Invalid signature algorithm')
      except ValueError:
          abort(401, 'Invalid signature format')
      
      # Compute expected signature
      expected_signature = hmac.new(
          WEBHOOK_SECRET.encode('utf-8'),
          request.data,
          hashlib.sha256
      ).hexdigest()
      
      # Verify signature using timing-safe comparison
      if not hmac.compare_digest(hash_value, expected_signature):
          abort(401, 'Invalid signature')
      
      # Parse and process verified webhook
      event = request.get_json(force=True)
      print('Verified Firecrawl webhook:', event)
      
      return 'ok', 200

  if __name__ == '__main__':
      app.run(port=3000)
  ```
</CodeGroup>

### Best Practices

1. **Respond quickly** – Always return a `2xx` status code within 30 seconds
2. **Process asynchronously** – For heavy processing, queue the work and respond immediately
3. **Validate authenticity** – Always verify the webhook signature (see [Security](/webhooks/security))


# Security
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

```
X-Firecrawl-Signature: sha256=abc123def456...
```

The signature is computed as follows:

1. Take the raw request body (JSON string)
2. Create HMAC-SHA256 hash using your secret key
3. Convert to hexadecimal string
4. Prefix with `sha256=`

### Implementation Examples

<CodeGroup>
  ```js Node/Express theme={null}
  import crypto from 'crypto';
  import express from 'express';

  const app = express();

  // Use raw body parser for signature verification
  app.use('/webhook/firecrawl', express.raw({ type: 'application/json' }));

  app.post('/webhook/firecrawl', (req, res) => {
    const signature = req.get('X-Firecrawl-Signature');
    const webhookSecret = process.env.FIRECRAWL_WEBHOOK_SECRET;
    
    if (!signature || !webhookSecret) {
      return res.status(401).send('Unauthorized');
    }
    
    // Extract hash from signature header
    const [algorithm, hash] = signature.split('=');
    if (algorithm !== 'sha256') {
      return res.status(401).send('Invalid signature algorithm');
    }
    
    // Compute expected signature
    const expectedSignature = crypto
      .createHmac('sha256', webhookSecret)
      .update(req.body)
      .digest('hex');
    
    // Verify signature using timing-safe comparison
    if (!crypto.timingSafeEqual(Buffer.from(hash, 'hex'), Buffer.from(expectedSignature, 'hex'))) {
      return res.status(401).send('Invalid signature');
    }
    
    // Parse and process verified webhook
    const event = JSON.parse(req.body);
    console.log('Verified Firecrawl webhook:', event);
    
    res.status(200).send('ok');
  });

  app.listen(3000, () => console.log('Listening on 3000'));
  ```

  ```python Python/Flask theme={null}
  import hmac
  import hashlib
  from flask import Flask, request, abort

  app = Flask(__name__)

  WEBHOOK_SECRET = 'your-webhook-secret-here'  # Get from Firecrawl dashboard

  @app.post('/webhook/firecrawl')
  def webhook():
      signature = request.headers.get('X-Firecrawl-Signature')
      
      if not signature:
          abort(401, 'Missing signature header')
      
      # Extract hash from signature header
      try:
          algorithm, hash_value = signature.split('=', 1)
          if algorithm != 'sha256':
              abort(401, 'Invalid signature algorithm')
      except ValueError:
          abort(401, 'Invalid signature format')
      
      # Compute expected signature
      expected_signature = hmac.new(
          WEBHOOK_SECRET.encode('utf-8'),
          request.data,
          hashlib.sha256
      ).hexdigest()
      
      # Verify signature using timing-safe comparison
      if not hmac.compare_digest(hash_value, expected_signature):
          abort(401, 'Invalid signature')
      
      # Parse and process verified webhook
      event = request.get_json(force=True)
      print('Verified Firecrawl webhook:', event)
      
      return 'ok', 200

  if __name__ == '__main__':
      app.run(port=3000)
  ```
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

```javascript  theme={null}
// ❌ BAD - No verification
app.post('/webhook', (req, res) => {
  processWebhook(req.body); // Dangerous!
  res.status(200).send('OK');
});

// ✅ GOOD - Verified first
app.post('/webhook', (req, res) => {
  if (!verifySignature(req)) {
    return res.status(401).send('Unauthorized');
  }
  processWebhook(req.body);
  res.status(200).send('OK');
});
```

### Use Timing-Safe Comparisons

Standard string comparison can leak timing information. Use dedicated functions:

* **Node.js**: `crypto.timingSafeEqual()`
* **Python**: `hmac.compare_digest()`
* **Other languages**: Look for "constant-time" or "timing-safe" comparison functions

### Require HTTPS

Always use HTTPS endpoints for webhooks:

```json  theme={null}
{
  "url": "https://your-app.com/webhook" // ✅ Secure
}
```

```json  theme={null}
{
  "url": "http://your-app.com/webhook" // ❌ Insecure
}
```


# Testing & Debugging
Source: https://docs.firecrawl.dev/webhooks/testing

Tools and techniques for developing and debugging webhooks

This page covers tools and techniques for testing webhook integrations during development and debugging issues in production.

## Local Development

### Exposing Local Servers

Since webhooks need to reach your server from the internet, you'll need to expose your local development server publicly.

#### Using Cloudflare Tunnels

[Cloudflare Tunnels](https://github.com/cloudflare/cloudflared/releases) provide a free way to securely expose your local development server to the internet without requiring account registration or opening firewall ports:

```bash  theme={null}
# Download cloudflared from GitHub releases or use a package manager

# Expose your local server
cloudflared tunnel --url localhost:3000

# Example output:
# Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):
# https://abc123.trycloudflare.com
```

Use the provided URL in your webhook configuration:

```json  theme={null}
{
  "url": "https://abc123.trycloudflare.com/webhook"
}
```

## Debugging Common Issues

### Webhooks Not Arriving

1. **Check URL accessibility** – Ensure your endpoint is publicly accessible
2. **Verify HTTPS** – Webhook URLs must use HTTPS
3. **Check firewall settings** – Allow incoming connections to your webhook port
4. **Review event filters** – Ensure you're subscribed to the correct event types

### Signature Verification Failing

1. **Check the secret key** – Ensure you're using the correct secret

2. **Verify raw body usage** – Make sure you're using the raw request body:

```javascript  theme={null}
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


