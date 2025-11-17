# Firecrawl - Advanced

**Pages:** 6

---

## You can also customize the engines and categories parameters, but the defaults should also work just fine.

**URL:** llms-txt#you-can-also-customize-the-engines-and-categories-parameters,-but-the-defaults-should-also-work-just-fine.

---

## Custom retry configuration

**URL:** llms-txt#custom-retry-configuration

**Contents:**
  - Custom configuration with Claude Desktop
  - System Configuration
  - Rate Limiting and Batch Processing
- Available Tools
  - 1. Scrape Tool (`firecrawl_scrape`)
  - 2. Batch Scrape Tool (`firecrawl_batch_scrape`)
  - 3. Check Batch Status (`firecrawl_check_batch_status`)
  - 4. Map Tool (`firecrawl_map`)
  - 5. Search Tool (`firecrawl_search`)
  - 6. Crawl Tool (`firecrawl_crawl`)

export FIRECRAWL_RETRY_MAX_ATTEMPTS=10
export FIRECRAWL_RETRY_INITIAL_DELAY=500     # Start with faster retries
json  theme={null}
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
typescript  theme={null}
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
json  theme={null}
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
json  theme={null}
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
json  theme={null}
{
  "content": [
    {
      "type": "text",
      "text": "Batch operation queued with ID: batch_1. Use firecrawl_check_batch_status to check progress."
    }
  ],
  "isError": false
}
json  theme={null}
{
  "name": "firecrawl_check_batch_status",
  "arguments": {
    "id": "batch_1"
  }
}
json  theme={null}
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
json  theme={null}
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
json  theme={null}
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
json  theme={null}
{
  "name": "firecrawl_check_crawl_status",
  "arguments": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
json  theme={null}
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
json  theme={null}
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

[INFO] Firecrawl MCP Server initialized successfully
[INFO] Starting scrape for URL: https://example.com
[INFO] Batch operation queued with ID: batch_1
[WARNING] Credit usage has reached warning threshold
[ERROR] Rate limit exceeded, retrying in 2s...
json  theme={null}
{
  "content": [
    {
      "type": "text",
      "text": "Error: Rate limit exceeded. Retrying in 2 seconds..."
    }
  ],
  "isError": true
}
bash  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
### Custom configuration with Claude Desktop

Add this to your `claude_desktop_config.json`:
```

Example 2 (unknown):
```unknown
### System Configuration

The server includes several configurable parameters that can be set via environment variables. Here are the default values if not configured:
```

Example 3 (unknown):
```unknown
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
```

Example 4 (unknown):
```unknown
### 2. Batch Scrape Tool (`firecrawl_batch_scrape`)

Scrape multiple URLs efficiently with built-in rate limiting and parallel processing.
```

---

## Required for self-hosted

**URL:** llms-txt#required-for-self-hosted

export FIRECRAWL_API_URL=https://firecrawl.your-domain.com

---

## Optional retry configuration

**URL:** llms-txt#optional-retry-configuration

export FIRECRAWL_RETRY_MAX_ATTEMPTS=5        # Increase max retry attempts
export FIRECRAWL_RETRY_INITIAL_DELAY=2000    # Start with 2s delay
export FIRECRAWL_RETRY_MAX_DELAY=30000       # Maximum 30s delay
export FIRECRAWL_RETRY_BACKOFF_FACTOR=3      # More aggressive backoff

---

## Self-hosting

**URL:** llms-txt#self-hosting

**Contents:**
- Self-hosting Firecrawl
- Why?
  - Considerations
- Steps

Source: https://docs.firecrawl.dev/contributing/self-host

Learn how to self-host Firecrawl to run on your own and contribute to the project.

Welcome to [Firecrawl](https://firecrawl.dev) 🔥! Here are some instructions on how to get the project locally so you can run it on your own and contribute.

If you're contributing, note that the process is similar to other open-source repos, i.e., fork Firecrawl, make changes, run tests, PR.

If you have any questions or would like help getting on board, join our Discord community [here](https://discord.gg/gSmWdAkdwd) for more information or submit an issue on Github [here](https://github.com/mendableai/firecrawl/issues/new/choose)!

## Self-hosting Firecrawl

Refer to [SELF\_HOST.md](https://github.com/mendableai/firecrawl/blob/main/SELF_HOST.md) for instructions on how to run it locally.

Self-hosting Firecrawl is particularly beneficial for organizations with stringent security policies that require data to remain within controlled environments. Here are some key reasons to consider self-hosting:

* **Enhanced Security and Compliance:** By self-hosting, you ensure that all data handling and processing complies with internal and external regulations, keeping sensitive information within your secure infrastructure. Note that Firecrawl is a Mendable product and relies on SOC2 Type2 certification, which means that the platform adheres to high industry standards for managing data security.
* **Customizable Services:** Self-hosting allows you to tailor the services, such as the Playwright service, to meet specific needs or handle particular use cases that may not be supported by the standard cloud offering.
* **Learning and Community Contribution:** By setting up and maintaining your own instance, you gain a deeper understanding of how Firecrawl works, which can also lead to more meaningful contributions to the project.

However, there are some limitations and additional responsibilities to be aware of:

1. **Limited Access to Fire-engine:** Currently, self-hosted instances of Firecrawl do not have access to Fire-engine, which includes advanced features for handling IP blocks, robot detection mechanisms, and more. This means that while you can manage basic scraping tasks, more complex scenarios might require additional configuration or might not be supported.
2. **Manual Configuration Required:** If you need to use scraping methods beyond the basic fetch and Playwright options, you will need to manually configure these in the `.env` file. This requires a deeper understanding of the technologies and might involve more setup time.

Self-hosting Firecrawl is ideal for those who need full control over their scraping and data processing environments but comes with the trade-off of additional maintenance and configuration efforts.

1. First, start by installing the dependencies

* Docker [instructions](https://docs.docker.com/get-docker/)

2. Set environment variables

Create an `.env` in the root directory you can copy over the template in `apps/api/.env.example`

To start, we wont set up authentication, or any optional sub services (pdf parsing, JS blocking support, AI features)

---

## Set if you'd like to allow local webhooks to be sent to your self-hosted instance

**URL:** llms-txt#set-if-you'd-like-to-allow-local-webhooks-to-be-sent-to-your-self-hosted-instance

---
