# Firecrawl - Sdks

**Pages:** 11

---

## Gemini

**URL:** llms-txt#gemini

**Contents:**
- Setup
- Scrape + Summarize
- Content Analysis
- Structured Extraction

Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/gemini

Use Firecrawl with Google's Gemini AI for web scraping + AI workflows

Integrate Firecrawl with Google's Gemini for AI applications powered by web data.

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Summarize

This example demonstrates a simple workflow: scrape a website and summarize the content using Gemini.

This example shows how to analyze website content using Gemini's multi-turn conversation capabilities.

## Structured Extraction

This example demonstrates how to extract structured data using Gemini's JSON mode from scraped website content.

For more examples, check the [Gemini documentation](https://ai.google.dev/docs).

**Examples:**

Example 1 (unknown):
```unknown
Create `.env` file:
```

Example 2 (unknown):
```unknown
> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Summarize

This example demonstrates a simple workflow: scrape a website and summarize the content using Gemini.
```

Example 3 (unknown):
```unknown
## Content Analysis

This example shows how to analyze website content using Gemini's multi-turn conversation capabilities.
```

Example 4 (unknown):
```unknown
## Structured Extraction

This example demonstrates how to extract structured data using Gemini's JSON mode from scraped website content.
```

---

## Building an AI Research Assistant with Firecrawl and AI SDK

**URL:** llms-txt#building-an-ai-research-assistant-with-firecrawl-and-ai-sdk

**Contents:**
- What You'll Build
- Prerequisites
- How It Works
  - Message Flow
  - Tool Calling Process
- Key Features
  - Model Selection
  - Web Search Toggle
- Customization Ideas
  - Add More Tools

Source: https://docs.firecrawl.dev/developer-guides/cookbooks/ai-research-assistant-cookbook

Build a complete AI-powered research assistant with web scraping and search capabilities

Build a complete AI-powered research assistant that can scrape websites and search the web to answer questions. The assistant automatically decides when to use web scraping or search tools to gather information, then provides comprehensive answers based on collected data.

<img src="https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif?s=cfcbad69aa3f087a474414c0763a260b" alt="AI research assistant chatbot interface showing real-time web scraping with Firecrawl and conversational responses powered by OpenAI" data-og-width="1044" width="1044" data-og-height="716" height="716" data-path="images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif" data-optimize="true" data-opv="3" />

An AI chat interface where users can ask questions about any topic. The AI assistant automatically decides when to use web scraping or search tools to gather information, then provides comprehensive answers based on the data it collects.

* Node.js 18 or later installed
* An OpenAI API key from [platform.openai.com](https://platform.openai.com)
* A Firecrawl API key from [firecrawl.dev](https://firecrawl.dev)
* Basic knowledge of React and Next.js

<Steps>
  <Step title="Create a New Next.js Project">
    Start by creating a fresh Next.js application and navigating into the project directory:

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

These packages provide:

* `ai`: Core SDK with streaming, tool calling, and response handling
    * `@ai-sdk/react`: React hooks like `useChat` for building chat interfaces
    * `zod`: Schema validation for tool inputs

Learn more at [ai-sdk.dev/docs](https://ai-sdk.dev/docs).

### Install AI Elements

AI Elements provides pre-built UI components for AI applications. Run the following command to scaffold all the necessary components:

This sets up AI Elements in your project, including conversation components, message displays, prompt inputs, and tool call visualizations.

Documentation: [ai-sdk.dev/elements/overview](https://ai-sdk.dev/elements/overview).

### Install OpenAI Provider

Install the OpenAI provider to connect with OpenAI's models:

<Step title="Build the Frontend Chat Interface">
    Create the main page at `app/page.tsx` and copy the code from the Code tab below. This will be the chat interface where users interact with the AI assistant.

<Tabs>
      <Tab title="Preview">
                <img src="https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif?s=cfcbad69aa3f087a474414c0763a260b" alt="AI research assistant chatbot interface showing real-time web scraping with Firecrawl and conversational responses powered by OpenAI" data-og-width="1044" width="1044" data-og-height="716" height="716" data-path="images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif" data-optimize="true" data-opv="3" />
      </Tab>

<Tab title="Code">
        
      </Tab>
    </Tabs>

### Understanding the Frontend

The frontend uses AI Elements components to provide a complete chat interface:

* **Conversation Display**: The `Conversation` component automatically handles message scrolling and display
    * **Message Rendering**: Each message part is rendered based on its type (text, reasoning, tool calls)
    * **Tool Visualization**: Tool calls are displayed with collapsible sections showing inputs and outputs
    * **Interactive Controls**: Users can toggle web search, select models, and attach files
    * **Message Actions**: Copy and retry actions for assistant messages
  </Step>

<Step title="Add Markdown Rendering Support">
    To ensure the markdown from the LLM is correctly rendered, add the following import to your `app/globals.css` file:

This imports the necessary styles for rendering markdown content in the message responses.
  </Step>

<Step title="Build the Basic API Route">
    Create the chat API endpoint at `app/api/chat/route.ts`. This route will handle incoming messages and stream responses from the AI.

* Receives messages from the frontend
    * Uses the OpenAI model selected by the user
    * Streams responses back to the client
    * Doesn't include tools yet - we'll add those next
  </Step>

<Step title="Configure Environment Variables">
    Create a `.env.local` file in your project root:

Add your OpenAI API key:

The `OPENAI_API_KEY` is required for the AI model to function.
  </Step>

<Step title="Test the Basic Chat">
    Now you can test the AI SDK chatbot without Firecrawl integration. Start the development server:

Open [localhost:3000](http://localhost:3000) in your browser and test the basic chat functionality. The assistant should respond to messages, but won't have web scraping or search capabilities yet.

<img src="https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/simple-ai-sdk-chatbot.gif?s=dd40938ec93fd0ad13568d2825d7552d" alt="Basic AI chatbot without web scraping capabilities" data-og-width="1192" width="1192" data-og-height="720" height="720" data-path="images/guides/cookbooks/ai-sdk-cookbook/simple-ai-sdk-chatbot.gif" data-optimize="true" data-opv="3" />
  </Step>

<Step title="Add Firecrawl Tools">
    Now let's enhance the assistant with web scraping and search capabilities using Firecrawl.

### Install Firecrawl SDK

Firecrawl converts websites into LLM-ready formats with scraping and search capabilities:

### Create the Tools File

Create a `lib` folder and add a `tools.ts` file inside it:

Add the following code to define the web scraping and search tools:

### Understanding the Tools

**Scrape Website Tool:**

* Accepts a URL as input (validated by Zod schema)
    * Uses Firecrawl's `scrape` method to fetch the page as markdown
    * Extracts only the main content to reduce token usage
    * Returns the scraped content for the AI to analyze

* Accepts a search query with optional filters
    * Uses Firecrawl's `search` method to find relevant web pages
    * Supports advanced filters like location, time range, and content categories
    * Returns structured results with titles, URLs, and descriptions

Learn more about tools: [ai-sdk.dev/docs/foundations/tools](https://ai-sdk.dev/docs/foundations/tools).
  </Step>

<Step title="Update the API Route with Firecrawl Tools">
    Now update your `app/api/chat/route.ts` to include the Firecrawl tools we just created.

<Accordion title="View complete app/api/chat/route.ts code">
      
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

Get your Firecrawl API key from [firecrawl.dev](https://firecrawl.dev).
  </Step>

<Step title="Test the Complete Application">
    Restart your development server:

<img src="https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/active-firecrawl-tools-ai-sdk.gif?s=015de571c2352a0cf6eb70ddb2eaec64" alt="AI chatbot with active Firecrawl tools" data-og-width="1084" width="1084" data-og-height="720" height="720" data-path="images/guides/cookbooks/ai-sdk-cookbook/active-firecrawl-tools-ai-sdk.gif" data-optimize="true" data-opv="3" />

Open [localhost:3000](http://localhost:3000) and test the enhanced assistant:

1. Toggle the "Search" button to enable web search
    2. Ask: "What are the latest features from firecrawl.dev?"
    3. Watch as the AI calls the `searchWeb` or `scrapeWebsite` tool
    4. See the tool execution in the UI with inputs and outputs
    5. Read the AI's analysis based on the scraped data
  </Step>
</Steps>

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

Extend the assistant with additional tools:

* Database lookups for internal company data
* CRM integration to fetch customer information
* Email sending capabilities
* Document generation

Each tool follows the same pattern: define a schema with Zod, implement the execute function, and register it in the `tools` object.

### Change the AI Model

Swap OpenAI for another provider:

The AI SDK supports 20+ providers with the same API. Learn more: [ai-sdk.dev/docs/foundations/providers-and-models](https://ai-sdk.dev/docs/foundations/providers-and-models).

AI Elements components are built on shadcn/ui, so you can:

* Modify component styles in the component files
* Add new variants to existing components
* Create custom components that match the design system

1. **Use appropriate tools**: Choose `searchWeb` to find relevant pages first, `scrapeWebsite` for single pages, or let the AI decide

2. **Monitor API usage**: Track your Firecrawl and OpenAI API usage to avoid unexpected costs

3. **Handle errors gracefully**: The tools include error handling, but consider adding user-facing error messages

4. **Optimize performance**: Use streaming to provide immediate feedback and consider caching frequently accessed content

5. **Set reasonable limits**: The `stopWhen: stepCountIs(5)` prevents excessive tool calls and runaway costs

<CardGroup cols={2}>
  <Card title="AI SDK Documentation" href="https://ai-sdk.dev/docs">
    Explore the AI SDK for building AI-powered applications with streaming, tool
    calling, and multi-provider support.
  </Card>

<Card title="AI Elements Components" href="https://ai-sdk.dev/elements/overview">
    Pre-built UI components for AI applications built on shadcn/ui.
  </Card>
</CardGroup>

**Examples:**

Example 1 (unknown):
```unknown
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
```

Example 2 (unknown):
```unknown
These packages provide:

    * `ai`: Core SDK with streaming, tool calling, and response handling
    * `@ai-sdk/react`: React hooks like `useChat` for building chat interfaces
    * `zod`: Schema validation for tool inputs

    Learn more at [ai-sdk.dev/docs](https://ai-sdk.dev/docs).

    ### Install AI Elements

    AI Elements provides pre-built UI components for AI applications. Run the following command to scaffold all the necessary components:
```

Example 3 (unknown):
```unknown
This sets up AI Elements in your project, including conversation components, message displays, prompt inputs, and tool call visualizations.

    Documentation: [ai-sdk.dev/elements/overview](https://ai-sdk.dev/elements/overview).

    ### Install OpenAI Provider

    Install the OpenAI provider to connect with OpenAI's models:
```

Example 4 (unknown):
```unknown
</Step>

  <Step title="Build the Frontend Chat Interface">
    Create the main page at `app/page.tsx` and copy the code from the Code tab below. This will be the chat interface where users interact with the AI assistant.

    <Tabs>
      <Tab title="Preview">
                <img src="https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif?s=cfcbad69aa3f087a474414c0763a260b" alt="AI research assistant chatbot interface showing real-time web scraping with Firecrawl and conversational responses powered by OpenAI" data-og-width="1044" width="1044" data-og-height="716" height="716" data-path="images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif" data-optimize="true" data-opv="3" />
      </Tab>

      <Tab title="Code">
```

---

## Python

**URL:** llms-txt#python

**Contents:**
- Installation

Source: https://docs.firecrawl.dev/sdks/python

Firecrawl Python SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.

To install the Firecrawl Python SDK, you can use pip:

```python Python theme={null}

---

## LangGraph

**URL:** llms-txt#langgraph

**Contents:**
- Setup
- Basic Workflow
- Multi-Step Workflow

Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/langgraph

Integrate Firecrawl with LangGraph for building agent workflows

This guide shows how to integrate Firecrawl with LangGraph to build AI agent workflows that can scrape and process web content.

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

This example demonstrates a basic LangGraph workflow that scrapes a website and analyzes the content.

## Multi-Step Workflow

This example demonstrates a more complex workflow that scrapes multiple URLs and processes them.

For more examples, check the [LangGraph documentation](https://langchain-ai.github.io/langgraphjs/).

**Examples:**

Example 1 (unknown):
```unknown
Create `.env` file:
```

Example 2 (unknown):
```unknown
> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Basic Workflow

This example demonstrates a basic LangGraph workflow that scrapes a website and analyzes the content.
```

Example 3 (unknown):
```unknown
## Multi-Step Workflow

This example demonstrates a more complex workflow that scrapes multiple URLs and processes them.
```

---

## LangChain

**URL:** llms-txt#langchain

**Contents:**
- Setup
- Scrape + Chat
- Chains
- Tool Calling
- Structured Data Extraction

Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/langchain

Use Firecrawl with LangChain for web scraping + AI workflows

Integrate Firecrawl with LangChain to build AI applications powered by web data.

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

This example demonstrates a simple workflow: scrape a website and process the content using LangChain.

This example shows how to build a LangChain chain to process and analyze scraped content.

This example demonstrates how to use LangChain's tool calling feature to let the model decide when to scrape websites.

## Structured Data Extraction

This example shows how to extract structured data using LangChain's structured output feature.

For more examples, check the [LangChain documentation](https://js.langchain.com/docs).

**Examples:**

Example 1 (unknown):
```unknown
Create `.env` file:
```

Example 2 (unknown):
```unknown
> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Chat

This example demonstrates a simple workflow: scrape a website and process the content using LangChain.
```

Example 3 (unknown):
```unknown
## Chains

This example shows how to build a LangChain chain to process and analyze scraped content.
```

Example 4 (unknown):
```unknown
## Tool Calling

This example demonstrates how to use LangChain's tool calling feature to let the model decide when to scrape websites.
```

---

## Node

**URL:** llms-txt#node

**Contents:**
- Installation

Source: https://docs.firecrawl.dev/sdks/node

Firecrawl Node SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.

To install the Firecrawl Node SDK, you can use npm:

```js Node theme={null}

---

## LlamaIndex

**URL:** llms-txt#llamaindex

**Contents:**
- Setup
- RAG with Vector Search

Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/llamaindex

Use Firecrawl with LlamaIndex for RAG applications

Integrate Firecrawl with LlamaIndex to build AI applications with vector search and embeddings powered by web content.

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## RAG with Vector Search

This example demonstrates how to use LlamaIndex with Firecrawl to crawl a website, create embeddings, and query the content using RAG.

For more examples, check the [LlamaIndex documentation](https://ts.llamaindex.ai/).

**Examples:**

Example 1 (unknown):
```unknown
Create `.env` file:
```

Example 2 (unknown):
```unknown
> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## RAG with Vector Search

This example demonstrates how to use LlamaIndex with Firecrawl to crawl a website, create embeddings, and query the content using RAG.
```

---

## OpenAI

**URL:** llms-txt#openai

**Contents:**
- Setup
- Scrape + Summarize
- Function Calling
- Structured Data Extraction
- Search + Analyze
- Responses API with MCP

Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/openai

Use Firecrawl with OpenAI for web scraping + AI workflows

Integrate Firecrawl with OpenAI to build AI applications powered by web data.

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Summarize

This example demonstrates a simple workflow: scrape a website and summarize the content using an OpenAI model.

This example shows how to use OpenAI's function calling feature to let the model decide when to scrape websites based on user requests.

## Structured Data Extraction

This example demonstrates how to use OpenAI models with structured outputs to extract specific data from scraped content.

This example combines Firecrawl's search capabilities with OpenAI model analysis to find and summarize information from multiple sources.

## Responses API with MCP

This example shows how to use OpenAI's Responses API with Firecrawl configured as an MCP (Model Context Protocol) server.

For more examples, check the [OpenAI documentation](https://platform.openai.com/docs).

**Examples:**

Example 1 (unknown):
```unknown
Create `.env` file:
```

Example 2 (unknown):
```unknown
> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Summarize

This example demonstrates a simple workflow: scrape a website and summarize the content using an OpenAI model.
```

Example 3 (unknown):
```unknown
## Function Calling

This example shows how to use OpenAI's function calling feature to let the model decide when to scrape websites based on user requests.
```

Example 4 (unknown):
```unknown
## Structured Data Extraction

This example demonstrates how to use OpenAI models with structured outputs to extract specific data from scraped content.
```

---

## Anthropic

**URL:** llms-txt#anthropic

**Contents:**
- Setup
- Scrape + Summarize
- Tool Use
- Structured Extraction

Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/anthropic

Use Firecrawl with Claude for web scraping + AI workflows

Integrate Firecrawl with Claude to build AI applications powered by web data.

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Summarize

This example demonstrates a simple workflow: scrape a website and summarize the content using Claude.

This example shows how to use Claude's tool use feature to let the model decide when to scrape websites based on user requests.

## Structured Extraction

This example demonstrates how to use Claude to extract structured data from scraped website content.

For more examples, check the [Claude documentation](https://docs.anthropic.com/claude/docs).

**Examples:**

Example 1 (unknown):
```unknown
Create `.env` file:
```

Example 2 (unknown):
```unknown
> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Summarize

This example demonstrates a simple workflow: scrape a website and summarize the content using Claude.
```

Example 3 (unknown):
```unknown
## Tool Use

This example shows how to use Claude's tool use feature to let the model decide when to scrape websites based on user requests.
```

Example 4 (unknown):
```unknown
## Structured Extraction

This example demonstrates how to use Claude to extract structured data from scraped website content.
```

---

## Mastra

**URL:** llms-txt#mastra

**Contents:**
- Setup
- Multi-Step Workflow

Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/mastra

Use Firecrawl with Mastra for building AI workflows

Integrate Firecrawl with Mastra, the TypeScript framework for building AI agents and workflows.

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Multi-Step Workflow

This example demonstrates a complete workflow that searches, scrapes, and summarizes documentation using Firecrawl and Mastra.

For more examples, check the [Mastra documentation](https://mastra.ai/docs).

**Examples:**

Example 1 (unknown):
```unknown
Create `.env` file:
```

Example 2 (unknown):
```unknown
> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Multi-Step Workflow

This example demonstrates a complete workflow that searches, scrapes, and summarizes documentation using Firecrawl and Mastra.
```

---

## Vercel AI SDK

**URL:** llms-txt#vercel-ai-sdk

**Contents:**
- Setup
- Scrape + Generate Text
- Scrape + Stream Text
- Tool Calling
- Structured Data Extraction

Source: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk

Use Firecrawl with Vercel AI SDK for web scraping + AI workflows

Integrate Firecrawl with Vercel AI SDK to build AI applications powered by web data.

> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Generate Text

This example demonstrates a simple workflow: scrape a website and generate text using the Vercel AI SDK.

## Scrape + Stream Text

This example shows how to stream AI responses for better user experience.

This example demonstrates how to use Vercel AI SDK's tool calling feature to let the model decide when to scrape websites.

## Structured Data Extraction

This example shows how to extract structured data using Vercel AI SDK's structured output feature.

For more examples, check the [Vercel AI SDK documentation](https://sdk.vercel.ai/docs).

**Examples:**

Example 1 (unknown):
```unknown
Create `.env` file:
```

Example 2 (unknown):
```unknown
> **Note:** If using Node \< 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Scrape + Generate Text

This example demonstrates a simple workflow: scrape a website and generate text using the Vercel AI SDK.
```

Example 3 (unknown):
```unknown
## Scrape + Stream Text

This example shows how to stream AI responses for better user experience.
```

Example 4 (unknown):
```unknown
## Tool Calling

This example demonstrates how to use Vercel AI SDK's tool calling feature to let the model decide when to scrape websites.
```

---
