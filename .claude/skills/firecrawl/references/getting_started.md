# Firecrawl - Getting Started

**Pages:** 6

---

## Quickstart

**URL:** llms-txt#quickstart

**Contents:**
- Welcome to Firecrawl
- How to use it?
  - API Key
  - Features
  - Powerful Capabilities
- Installing Firecrawl
- Scraping
  - Response
- Crawling
  - Usage

Source: https://docs.firecrawl.dev/introduction

Firecrawl allows you to turn entire websites into LLM-ready markdown

<img className="block" src="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=4e7b593752a4ff638c1d1dbfddb54a9a" alt="Hero Light" data-og-width="1200" width="1200" data-og-height="675" height="675" data-path="images/turn-websites-into-llm-ready-data--firecrawl.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?w=280&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=e80d7c4a694a930342577283249d461a 280w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?w=560&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=1344a5340ddad90ee50ccf66b088b430 560w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?w=840&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=060bf67f6a5b76002c4b416b165d0dce 840w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?w=1100&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=f89c070acdb98f7e2b91f58209f7a628 1100w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?w=1650&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=0486baeea836b83b6c84e28635b20604 1650w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/turn-websites-into-llm-ready-data--firecrawl.png?w=2500&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=1fe62bc4843cf736d0462e93ae0610c8 2500w" />

## Welcome to Firecrawl

[Firecrawl](https://firecrawl.dev?ref=github) is an API service that takes a URL, crawls it, and converts it into clean markdown. We crawl all accessible subpages and give you clean markdown for each. No sitemap required.

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

To use the API, you need to sign up on [Firecrawl](https://firecrawl.dev) and get an API key.

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

To scrape a single URL, use the `scrape` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

The crawl feature allows you to automatically discover and extract content from a URL and all of its accessible subpages. With our SDKs, simply call the crawl method—this will submit a crawl job, wait for it to finish, and return the complete results for the entire site.

If you're using our API directly, cURL or `start crawl` functions on SDKs, this will return an `ID` where you can use to check the status of the crawl.

Used to check the status of a crawl job and get its result.

The response will be different depending on the status of the crawl. For not completed or large responses exceeding 10MB, a `next` URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the `next` parameter is absent, it indicates the end of the crawl data.

With JSON mode, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:

Firecrawl's search API allows you to perform web searches and optionally scrape the search results in one operation.

* Choose specific output formats (markdown, HTML, links, screenshots)
* Choose specific sources (web, news, images)
* Search the web with customizable parameters (location, etc.)

For details, see the [Search Endpoint API Reference](/api-reference/endpoint/search).

SDKs will return the data object directly. cURL will return the complete payload.

### Extracting without schema

You can now extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.

## Interacting with the page with Actions

Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.

Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.

It is important to almost always use the `wait` action before/after executing other actions to give enough time for the page to load.

<CodeGroup>
  
</CodeGroup>

## Open Source vs Cloud

Firecrawl is open source available under the [AGPL-3.0 license](https://github.com/mendableai/firecrawl/blob/main/LICENSE).

To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.

Firecrawl Cloud is available at [firecrawl.dev](https://firecrawl.dev) and offers a range of features that are not available in the open source version:

<img src="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=763a6e92c8605d06294ed7ed45df85d0" alt="Firecrawl Cloud vs Open Source" data-og-width="2808" width="2808" data-og-height="856" height="856" data-path="images/open-source-cloud.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=280&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=2e9112d82aec51ca204ceee026b6bad3 280w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=560&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=9fabc257f1caa297b1b8ec68fb13eddc 560w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=840&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=e766290156ea4226df484ee815f5036f 840w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=1100&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=ed02646081bce28427156ba1d8bf4fa2 1100w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=1650&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=41d72e1c116d48ebc0cfa1a3499b3e9e 1650w, https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/open-source-cloud.png?w=2500&fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=0f6f34e97633cabdc17cbc28d7af2bb9 2500w" />

We love contributions! Please read our [contributing guide](https://github.com/mendableai/firecrawl/blob/main/CONTRIBUTING.md) before submitting a pull request.

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

## Scraping

To scrape a single URL, use the `scrape` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

<CodeGroup>
```

Example 3 (unknown):
```unknown

```

Example 4 (unknown):
```unknown

```

---

## Optional authentication for self-hosted

**URL:** llms-txt#optional-authentication-for-self-hosted

export FIRECRAWL_API_KEY=your-api-key  # If your instance requires auth

---

## Use if you've set up authentication and want to test with a real API key

**URL:** llms-txt#use-if-you've-set-up-authentication-and-want-to-test-with-a-real-api-key

---

## Introduction

**URL:** llms-txt#introduction

**Contents:**
- Features
- Agentic Features
- Base URL
- Authentication
- Response codes
- Rate limit

Source: https://docs.firecrawl.dev/api-reference/v2-introduction

Firecrawl API Reference (v2)

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

<CardGroup cols={3}>
  <Card title="Extract" icon="barcode-read" href="/api-reference/endpoint/extract" color="FF713C">
    Extract structured data from entire webpages using natural language.
  </Card>
</CardGroup>

All requests contain the following base URL:

For authentication, it's required to include an Authorization header. The header should contain `Bearer fc-123456789`, where `fc-123456789` represents your API Key.

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

The Firecrawl API has a rate limit to ensure the stability and reliability of the service. The rate limit is applied to all endpoints and is based on the number of requests made within a specific time frame.

When you exceed the rate limit, you will receive a 429 response code.

**Examples:**

Example 1 (unknown):
```unknown
## Authentication

For authentication, it's required to include an Authorization header. The header should contain `Bearer fc-123456789`, where `fc-123456789` represents your API Key.
```

---

## To turn on DB authentication, you need to set up Supabase.

**URL:** llms-txt#to-turn-on-db-authentication,-you-need-to-set-up-supabase.

USE_DB_AUTHENTICATION=false

---

## Supabase Setup (used to support DB authentication, advanced logging, etc.)

**URL:** llms-txt#supabase-setup-(used-to-support-db-authentication,-advanced-logging,-etc.)

---
