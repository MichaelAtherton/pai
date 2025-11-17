# Firecrawl - Api Reference

**Pages:** 29

---

## TEST_API_KEY=

**URL:** llms-txt#test_api_key=

---

## Scrape

**URL:** llms-txt#scrape

**Contents:**
- Scraping a URL with Firecrawl
  - /scrape endpoint
  - Installation
  - Usage
  - Response
- Scrape Formats
- Extract brand identity
  - /scrape (with branding) endpoint
  - Response
  - Branding Profile Structure

Source: https://docs.firecrawl.dev/features/scrape

Turn any url into clean data

Firecrawl converts web pages into markdown, ideal for LLM applications.

* It manages complexities: proxies, caching, rate limits, js-blocked content
* Handles dynamic content: dynamic websites, js-rendered sites, PDFs, images
* Outputs clean markdown, structured data, screenshots or html.

For details, see the [Scrape Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## Scraping a URL with Firecrawl

Used to scrape a URL and get its content.

For more details about the parameters, refer to the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

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

The branding format returns a comprehensive `BrandingProfile` object with the following structure:

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

## Extract structured data

### /scrape (with json) endpoint

Used to extract structured data from scraped pages.

### Extracting without schema

You can now extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.

### JSON format options

When using the `json` format, pass an object inside `formats` with the following parameters:

* `schema`: JSON Schema for the structured output.
* `prompt`: Optional prompt to help guide extraction when a schema is present or when you prefer light guidance.

## Interacting with the page with Actions

Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.

Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.

It is important to almost always use the `wait` action before/after executing other actions to give enough time for the page to load.

<CodeGroup>
  
</CodeGroup>

For more details about the actions parameters, refer to the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## Location and Language

Specify country and preferred languages to get relevant content based on your target location and language preferences.

When you specify the location settings, Firecrawl will use an appropriate proxy if available and emulate the corresponding language and timezone settings. By default, the location is set to 'US' if not specified.

To use the location and language settings, include the `location` object in your request body with the following properties:

* `country`: ISO 3166-1 alpha-2 country code (e.g., 'US', 'AU', 'DE', 'JP'). Defaults to 'US'.
* `languages`: An array of preferred languages and locales for the request in order of priority. Defaults to the language of the specified location.

For more details about supported locations, refer to the [Proxies documentation](/features/proxies).

## Caching and maxAge

To make requests faster, Firecrawl serves results from cache by default when a recent copy is available.

* **Default freshness window**: `maxAge = 172800000` ms (2 days). If a cached page is newer than this, it’s returned instantly; otherwise, the page is scraped and then cached.
* **Performance**: This can speed up scrapes by up to 5x when data doesn’t need to be ultra-fresh.
* **Always fetch fresh**: Set `maxAge` to `0`.
* **Avoid storing**: Set `storeInCache` to `false` if you don’t want Firecrawl to cache/store results for this request.

Example (force fresh content):

Example (use a 10-minute cache window):

## Batch scraping multiple URLs

You can now batch scrape multiple URLs at the same time. It takes the starting URLs and optional parameters as arguments. The params argument allows you to specify additional options for the batch scrape job, such as the output formats.

It is very similar to how the `/crawl` endpoint works. It submits a batch scrape job and returns a job ID to check the status of the batch scrape.

The sdk provides 2 methods, synchronous and asynchronous. The synchronous method will return the results of the batch scrape job, while the asynchronous method will return a job ID that you can use to check the status of the batch scrape.

If you’re using the sync methods from the SDKs, it will return the results of the batch scrape job. Otherwise, it will return a job ID that you can use to check the status of the batch scrape.

You can then use the job ID to check the status of the batch scrape by calling the `/batch/scrape/{id}` endpoint. This endpoint is meant to be used while the job is still running or right after it has completed **as batch scrape jobs expire after 24 hours**.

For websites with advanced anti-bot protection, Firecrawl offers a stealth proxy mode that provides better success rates at scraping challenging sites.

Learn more about [Stealth Mode](/features/stealth-mode).

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

## Historical Token Usage

**URL:** llms-txt#historical-token-usage

Source: https://docs.firecrawl.dev/api-reference/endpoint/token-usage-historical

v2-openapi GET /team/token-usage/historical

Returns historical token usage on a month-by-month basis. The endpoint can also breaks usage down by API key optionally.

<Info>We've simplified billing so that Extract now uses credits, just like all of the other endpoints. Each credit is worth 15 tokens. Reported token usage now includes usage from all endpoints.</Info>

---

## Get Active Crawls

**URL:** llms-txt#get-active-crawls

Source: https://docs.firecrawl.dev/api-reference/endpoint/crawl-active

v2-openapi GET /crawl/active

---

## OPENAI_API_KEY=

**URL:** llms-txt#openai_api_key=

**Contents:**
- === Proxy ===

---

## npm install @mendable/firecrawl-js

**URL:** llms-txt#npm-install-@mendable/firecrawl-js

**Contents:**
- Usage
  - Scraping a URL
  - Crawling a Website
  - Start a Crawl
  - Checking Crawl Status
  - Cancelling a Crawl
  - Mapping a Website
  - Crawling a Website with WebSockets
  - Pagination
- Error Handling

import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
js Node theme={null}
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
js Node theme={null}
// Scrape a website:
const scrapeResult = await firecrawl.scrape('firecrawl.dev', { formats: ['markdown', 'html'] });

console.log(scrapeResult)
js Node theme={null}
const job = await firecrawl.crawl('https://docs.firecrawl.dev', { limit: 5, pollInterval: 1, timeout: 120 });
console.log(job.status);
js Node theme={null}
const { id } = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 10 });
console.log(id);
js Node theme={null}
const status = await firecrawl.getCrawlStatus("<crawl-id>");
console.log(status);
js Node theme={null}
const ok = await firecrawl.cancelCrawl("<crawl-id>");
console.log("Cancelled:", ok);
js Node theme={null}
const res = await firecrawl.map('https://firecrawl.dev', { limit: 10 });
console.log(res.links);
js Node theme={null}
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
js Node theme={null}
const crawlStart = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 5 });
const crawlJobId = crawlStart.id;

const crawlSingle = await firecrawl.getCrawlStatus(crawlJobId, { autoPaginate: false });
console.log('crawl single page:', crawlSingle.status, 'docs:', crawlSingle.data.length, 'next:', crawlSingle.next);
js Node theme={null}
const crawlLimited = await firecrawl.getCrawlStatus(crawlJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 50,
  maxWaitTime: 15,
});
console.log('crawl limited:', crawlLimited.status, 'docs:', crawlLimited.data.length, 'next:', crawlLimited.next);
js Node theme={null}
const batchStart = await firecrawl.startBatchScrape([
  'https://docs.firecrawl.dev',
  'https://firecrawl.dev',
], { options: { formats: ['markdown'] } });
const batchJobId = batchStart.id;

const batchSingle = await firecrawl.getBatchScrapeStatus(batchJobId, { autoPaginate: false });
console.log('batch single page:', batchSingle.status, 'docs:', batchSingle.data.length, 'next:', batchSingle.next);
js Node theme={null}
const batchLimited = await firecrawl.getBatchScrapeStatus(batchJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 100,
  maxWaitTime: 20,
});
console.log('batch limited:', batchLimited.status, 'docs:', batchLimited.data.length, 'next:', batchLimited.next);
```

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message. The examples above demonstrate how to handle these errors using `try/catch` blocks.

**Examples:**

Example 1 (unknown):
```unknown
## Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `FirecrawlApp` class.

Here's an example of how to use the SDK with error handling:
```

Example 2 (unknown):
```unknown
### Scraping a URL

To scrape a single URL with error handling, use the `scrapeUrl` method. It takes the URL as a parameter and returns the scraped data as a dictionary.
```

Example 3 (unknown):
```unknown
### Crawling a Website

To crawl a website with error handling, use the `crawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format. See [Pagination](#pagination) for auto/ manual pagination and limiting.
```

Example 4 (unknown):
```unknown
### Start a Crawl

Start a job without waiting using `startCrawl`. It returns a job `ID` you can use to check status. Use `crawl` when you want a waiter that blocks until completion. See [Pagination](#pagination) for paging behavior and limits.
```

---

## POSTHOG_API_KEY=

**URL:** llms-txt#posthog_api_key=

---

## Get Crawl Errors

**URL:** llms-txt#get-crawl-errors

Source: https://docs.firecrawl.dev/api-reference/endpoint/crawl-get-errors

v2-openapi GET /crawl/{id}/errors

---

## OLLAMA_BASE_URL=http://localhost:11434/api

**URL:** llms-txt#ollama_base_url=http://localhost:11434/api

---

## if you are going to use the [llm-extract feature](https://github.com/firecrawl/firecrawl/pull/586/), you should also export OPENAI_API_KEY=sk-______

**URL:** llms-txt#if-you-are-going-to-use-the-[llm-extract-feature](https://github.com/firecrawl/firecrawl/pull/586/),-you-should-also-export-openai_api_key=sk-______

**Contents:**
  - Terminal 3 - sending our first request.
  - Alternative: Using Docker Compose
- Tests:

curl  theme={null}
curl -X GET http://localhost:3002/test
curl  theme={null}
curl -X POST http://localhost:3002/v1/crawl \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://mendable.ai"
    }'
bash  theme={null}
docker compose up
```

This will start Redis, the API server, and workers automatically in the correct configuration.

The best way to do this is run the test with `npm run test:snips`.

**Examples:**

Example 1 (unknown):
```unknown
This will start the workers who are responsible for processing crawl jobs.

### Terminal 3 - sending our first request.

Alright: now let’s send our first request.
```

Example 2 (unknown):
```unknown
This should return the response Hello, world!

If you’d like to test the crawl endpoint, you can run this
```

Example 3 (unknown):
```unknown
### Alternative: Using Docker Compose

For a simpler setup, you can use Docker Compose to run all services:

1. Prerequisites: Make sure you have Docker and Docker Compose installed
2. Copy the `.env.example` file to `.env` in the `/apps/api/` directory and configure as needed
3. From the root directory, run:
```

---

## Rate Limits

**URL:** llms-txt#rate-limits

**Contents:**
- Concurrent Browser Limits
  - Standard Plans (most API endpoints)
  - Extract plans (/extract API)
- Standard API
  - Batch Endpoints
- Extract API
- FIRE-1 Agent
- Legacy Plans

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

Batch endpoints follow the /crawl rate limit.

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

Requests involving the FIRE-1 agent requests have separate rate limits that are counted independently for each endpoint:

| Endpoint   | Rate Limit (requests/min) |
| ---------- | ------------------------- |
| `/scrape`  | 10                        |
| `/extract` | 10                        |

| Plan            | /scrape (requests/min) | /crawl (concurrent req) | /search (requests/min) |
| --------------- | ---------------------- | ----------------------- | ---------------------- |
| Starter         | 100                    | 15                      | 100                    |
| Standard Legacy | 200                    | 200                     | 200                    |
| Scaled Legacy   | 250                    | 100                     | 250                    |

If you require higher limits, please contact us at [help@firecrawl.com](mailto:help@firecrawl.com) to discuss custom plans.

---

## SEARXNG_ENDPOINT=http://your.searxng.server

**URL:** llms-txt#searxng_endpoint=http://your.searxng.server

---

## LLAMAPARSE_API_KEY=

**URL:** llms-txt#llamaparse_api_key=

---

## Crawl Params Preview

**URL:** llms-txt#crawl-params-preview

**Contents:**
- What's New in v2
  - Crawl Params Preview
  - Response

Source: https://docs.firecrawl.dev/api-reference/endpoint/crawl-params-preview

v2-openapi POST /crawl/params-preview

### Crawl Params Preview

**Examples:**

Example 1 (unknown):
```unknown
### Response
```

---

## Token Usage

**URL:** llms-txt#token-usage

Source: https://docs.firecrawl.dev/api-reference/endpoint/token-usage

v2-openapi GET /team/token-usage

<Info>We've simplified billing so that Extract now uses credits, just like all of the other endpoints. Each credit is worth 15 tokens. Reported token usage now includes usage from all endpoints.</Info>

---

## Experimental: Use any OpenAI-compatible API

**URL:** llms-txt#experimental:-use-any-openai-compatible-api

---

## Get Extract Status

**URL:** llms-txt#get-extract-status

Source: https://docs.firecrawl.dev/api-reference/endpoint/extract-get

v2-openapi GET /extract/{id}

---

## Queue Status

**URL:** llms-txt#queue-status

Source: https://docs.firecrawl.dev/api-reference/endpoint/queue-status

v2-openapi GET /team/queue-status

Metrics about your team's scrape queue.

---

## Event Types

**URL:** llms-txt#event-types

**Contents:**
- Event Structure
  - Common Fields
- Crawl Events
  - `crawl.started`
  - `crawl.page`
  - `crawl.completed`
- Batch Scrape Events
  - `batch_scrape.started`
  - `batch_scrape.page`
  - `batch_scrape.completed`

Source: https://docs.firecrawl.dev/webhooks/events

Complete reference of all webhook events and when they trigger

This page covers all the different types of webhook events that Firecrawl can send to your endpoint. Each event type corresponds to a different stage in your scraping operations.

All webhook events follow this basic structure:

| Field      | Type    | Description                                       |
| ---------- | ------- | ------------------------------------------------- |
| `success`  | boolean | Whether the operation was successful              |
| `type`     | string  | Event type identifier                             |
| `id`       | string  | Unique identifier for the job                     |
| `data`     | array   | Event-specific data (varies by event type)        |
| `metadata` | object  | Custom metadata from your webhook configuration   |
| `error`    | string  | Error message (present when `success` is `false`) |

Multi-page crawling operations that follow links.

Sent when a crawl operation begins.

Sent for each individual page that gets scraped during a crawl.

<Note>
  This is the most frequent event during crawls. You'll receive one `crawl.page`
  event for every page successfully scraped.
</Note>

### `crawl.completed`

Sent when the entire crawl operation finishes successfully.

## Batch Scrape Events

Operations that scrape multiple specific URLs.

### `batch_scrape.started`

Sent when a batch scrape operation begins.

### `batch_scrape.page`

Sent for each individual URL that gets scraped in the batch.

<Note>
  This is the most frequent event during batch scrapes. You'll receive one
  `batch_scrape.page` event for every URL successfully scraped.
</Note>

### `batch_scrape.completed`

Sent when the entire batch scrape operation finishes.

LLM-powered data extraction operations.

### `extract.started`

Sent when an extract operation begins.

### `extract.completed`

Sent when an extract operation finishes successfully.

Sent when an extract operation encounters an error.

You can control which events you receive by specifying an `events` array in your webhook configuration:

**Examples:**

Example 1 (unknown):
```unknown
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
```

Example 2 (unknown):
```unknown
### `crawl.page`

Sent for each individual page that gets scraped during a crawl.
```

Example 3 (unknown):
```unknown
<Note>
  This is the most frequent event during crawls. You'll receive one `crawl.page`
  event for every page successfully scraped.
</Note>

### `crawl.completed`

Sent when the entire crawl operation finishes successfully.
```

Example 4 (unknown):
```unknown
## Batch Scrape Events

Operations that scrape multiple specific URLs.

### `batch_scrape.started`

Sent when a batch scrape operation begins.
```

---

## Cancel Crawl

**URL:** llms-txt#cancel-crawl

Source: https://docs.firecrawl.dev/api-reference/endpoint/crawl-delete

v2-openapi DELETE /crawl/{id}

---

## Credit Usage

**URL:** llms-txt#credit-usage

Source: https://docs.firecrawl.dev/api-reference/endpoint/credit-usage

v2-openapi GET /team/credit-usage

---

## Note: PORT is used by both the main API server and worker liveness check endpoint

**URL:** llms-txt#note:-port-is-used-by-both-the-main-api-server-and-worker-liveness-check-endpoint

---

## cd apps/api # to make sure you're in the right folder

**URL:** llms-txt#cd-apps/api-#-to-make-sure-you're-in-the-right-folder

**Contents:**
  - Running the project
  - Terminal 1 - setting up redis
  - Terminal 2 - setting up the service

pnpm install # make sure you have pnpm version 9+!
bash  theme={null}
redis-server
bash  theme={null}
pnpm start

**Examples:**

Example 1 (unknown):
```unknown
### Running the project

You're going to need to open 3 terminals.

### Terminal 1 - setting up redis

Run the command anywhere within your project
```

Example 2 (unknown):
```unknown
### Terminal 2 - setting up the service

Now, navigate to the apps/api/ directory and run:
```

---

## Required for cloud API

**URL:** llms-txt#required-for-cloud-api

export FIRECRAWL_API_KEY=your-api-key

---

## Get Crawl Status

**URL:** llms-txt#get-crawl-status

Source: https://docs.firecrawl.dev/api-reference/endpoint/crawl-get

v2-openapi GET /crawl/{id}

---

## Provide your OpenAI API key here to enable AI features

**URL:** llms-txt#provide-your-openai-api-key-here-to-enable-ai-features

---

## Historical Credit Usage

**URL:** llms-txt#historical-credit-usage

Source: https://docs.firecrawl.dev/api-reference/endpoint/credit-usage-historical

v2-openapi GET /team/credit-usage/historical

Returns historical credit usage on a month-by-month basis. The endpoint can also breaks usage down by API key optionally.

---

## Firecrawl + Zapier

**URL:** llms-txt#firecrawl-+-zapier

**Contents:**
- Official Blog Post
- Popular Integrations
- Firecrawl Actions
- Quick Reference
- Industry Use Cases
- Zapier vs n8n

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

→ [View Integration](https://zapier.com/apps/airtable/integrations/firecrawl)

Build lead generation databases and content aggregation systems with structured storage.

**Best For:** Sales teams, project managers

→ [View Integration](https://zapier.com/apps/zapier-tables/integrations/firecrawl)

No-code database automation for employee onboarding and centralized lead management.

**Best For:** HR teams, operations
  </Accordion>

<Accordion title="Communication & Notifications" icon="bell">
    ### Slack

→ [View Integration](https://zapier.com/apps/slack/integrations/firecrawl)

Get website change notifications, competitor monitoring alerts, and market intelligence updates.

**Best For:** Marketing teams, product managers

→ [View Integration](https://zapier.com/apps/telegram/integrations/firecrawl)

Instant price alerts, breaking news notifications, and real-time monitoring.

**Best For:** Traders, news enthusiasts
  </Accordion>

<Accordion title="CRM & Sales" icon="briefcase">
    ### HubSpot

→ [View Integration](https://zapier.com/apps/hubspot/integrations/firecrawl)

Contact enrichment, lead scoring with web data, and marketing automation.

**Best For:** Marketing ops, sales ops

→ [View Integration](https://zapier.com/apps/pipedrive/integrations/firecrawl)

Lead enrichment from websites and competitor intelligence tracking.

**Best For:** Sales teams, account executives

→ [View Integration](https://zapier.com/apps/attio/integrations/firecrawl)

Modern CRM data enrichment and relationship intelligence.

**Best For:** Modern sales teams
  </Accordion>

<Accordion title="Productivity & Documentation" icon="file-lines">
    ### Google Docs

→ [View Integration](https://zapier.com/apps/google-docs/integrations/firecrawl)

Automated report generation, research documentation, and content aggregation.

**Best For:** Researchers, content creators

→ [View Integration](https://zapier.com/apps/notion/integrations/firecrawl)

Knowledge base updates, research library building, and content curation.

**Best For:** Product teams, researchers
  </Accordion>

<Accordion title="Zapier Native Tools" icon="zap">
    ### Schedule by Zapier

→ [View Integration](https://zapier.com/apps/schedule/integrations/firecrawl)

Run hourly, daily, weekly, or monthly scraping automatically.

### Zapier Interfaces

→ [View Integration](https://zapier.com/apps/interfaces/integrations/firecrawl)

Build custom internal tools with form-based scraping and team dashboards.

**Best For:** Operations teams

→ [View Integration](https://zapier.com/apps/zapier-chatbots/integrations/firecrawl)

AI chatbots with live web knowledge for customer support and lead generation.

<Info>Official Zapier product uses Firecrawl internally</Info>
  </Accordion>
</AccordionGroup>

| Action                      | Use Case                                  |
| --------------------------- | ----------------------------------------- |
| **Scrape URL**              | Quick single-page data capture            |
| **Crawl Website**           | Full site scraping with multiple pages    |
| **Extract Structured Data** | AI-powered extraction with custom schemas |
| **Search Web**              | Research automation with search + scrape  |
| **Map Website**             | SEO analysis and site structure mapping   |

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

| Feature          | Zapier                                | n8n                      |
| ---------------- | ------------------------------------- | ------------------------ |
| **Setup**        | No-code, cloud-based                  | Self-hosted or cloud     |
| **Pricing**      | Per-task pricing                      | Flat monthly             |
| **Integrations** | 8,000+ apps                           | 400+ integrations        |
| **Best For**     | Quick automation, non-technical users | Custom logic, developers |

<Tip>
  **Pro Tip:** Start with Zapier's pre-built templates and customize as needed. Perfect for quick, no-code automation!
</Tip>

---

## By default, the /search API will use Google search.

**URL:** llms-txt#by-default,-the-/search-api-will-use-google-search.

---
