# Gpt-Researcher - Core Concepts

**Pages:** 44

---

## Claude Desktop Integration

**URL:** https://docs.gptr.dev/docs/gpt-researcher/mcp-server/claude-integration

**Contents:**
- Claude Desktop Integration
- Prerequisites​
- Setting Up Claude Desktop with MCP​
  - 1. Install and Run the GPT Researcher MCP Server​
  - 2. Configure Claude Desktop​
  - 3. Restart Claude for Desktop​
  - 4. Verify the Integration​
- Using GPT Researcher in Claude Desktop​
- Troubleshooting​
- Next Steps​

This guide specifically focuses on how to integrate your locally running GPT Researcher MCP server with the Claude desktop application for Mac, providing a seamless research experience within the Claude interface.

Check out the official Anthropic MCP docs here

Before integrating with Claude desktop client, you'll need:

To integrate your locally running MCP server with Claude for Mac, follow these steps:

Make sure you have the GPT Researcher MCP server installed and running:

Verify that the server is running properly by checking the console output. The server should be listening on port 8000 by default.

Locate Claude's Configuration File:

Edit the Configuration File:

Replace /path/to/gptr-mcp/server.py with the absolute path to your server.py file.

Alternatively, if you prefer to manually start the server and just have Claude connect to it:

Close and reopen the Claude application to apply the new configuration.

Once integrated, you can use research capabilities by:

You can also directly prompt Claude to use the tools:

If you encounter issues with the integration:

Server Connection Issues:

Tool Availability Issues:

Configuration File Issues:

**Examples:**

Example 1 (bash):
```bash
# Clone the repository (if you haven't already)git clone https://github.com/assafelovic/gptr-mcp.git# Install dependenciespip install -r requirements.txt# Set up your environment variablescp .env.example .env# Edit the .env file with your API keys# Run the serverpython server.py
```

Example 2 (json):
```json
{  "mcpServers": {    "gpt-researcher": {      "command": "/path/to/python",      "args": ["/path/to/gptr-mcp/server.py"]    }  }}
```

Example 3 (json):
```json
{  "mcpServers": {},  "externalMCPServers": {    "gpt-researcher": "http://localhost:8000/mcp"  }}
```

Example 4 (text):
```text
I need to research the latest advancements in quantum computing. Please use the conduct_research tool to gather information, then create a comprehensive report.
```

---

## Deep Research ✨ NEW ✨

**URL:** https://docs.gptr.dev/docs/gpt-researcher/gptr/deep_research

**Contents:**
- Deep Research ✨ NEW ✨
- How It Works​
- Process Flow​
- Quick Start​
- Configuration​
- Progress Tracking​
- Error Handling​
- Best Practices​
- Limitations​

With the latest "Deep Research" trend in the AI community, we're excited to implement our own Open source deep research capability! Introducing GPT Researcher's Deep Research - an advanced recursive research system that explores topics with unprecedented depth and breadth.

Each deep research takes around 5 minutes to complete and costs around $0.4 (using o3-mini on "high" reasoning effort)

Deep Research employs a fascinating tree-like exploration pattern:

Think of it as deploying a team of AI researchers, each following their own research path while collaborating to build a comprehensive understanding of your topic.

Deep Research behavior can be customized through several parameters:

You can configure these parameters in multiple ways:

The on_progress callback provides real-time insights into the research process:

The deep research workflow is designed to be resilient:

**Examples:**

Example 1 (python):
```python
from gpt_researcher import GPTResearcherfrom gpt_researcher.utils.enum import ReportType, Toneimport asyncioasync def main():    # Initialize researcher with deep research type    researcher = GPTResearcher(        query="What are the latest developments in quantum computing?",        report_type="deep",  # This triggers deep research modd    )    # Run research    research_data = await researcher.conduct_research()    # Generate report    report = await researcher.write_report()    print(report)if __name__ == "__main__":    asyncio.run(main())
```

Example 2 (bash):
```bash
export DEEP_RESEARCH_BREADTH=4export DEEP_RESEARCH_DEPTH=2export DEEP_RESEARCH_CONCURRENCY=4export TOTAL_WORDS=2500
```

Example 3 (yaml):
```yaml
deep_research_breadth: 4deep_research_depth: 2deep_research_concurrency: 4total_words: 2500
```

Example 4 (python):
```python
researcher = GPTResearcher(    query="your query",    report_type="deep",    config_path="path/to/config.yaml"  # Configure deep research parameters here)
```

---

## Data Ingestion

**URL:** https://docs.gptr.dev/docs/gpt-researcher/context/data-ingestion

**Contents:**
- Data Ingestion
  - Step 1: Transform your content into Langchain Documents​
  - Step 2: Insert your Langchain Documents into a Langchain VectorStore​
  - Step 3: Pass your Langchain Vectorstore into your GPTR report​

When you're dealing with a large amount of context data, you may want to start meditating upon a standalone process for data ingestion.

Some signs that the system is telling you to move to a custom data ingestion process:

As mentioned in our YouTube Tutorial Series, GPTR is using Langchain Documents and Langchain VectorStores under the hood.

These are 2 beautiful abstractions that make the GPTR architecture highly configurable.

The current research flow, whether you're generating reports on web or local documents, is:

Assuming your .env variables are like so:

Below is a custom data ingestion process that you can use to ingest your data into a Langchain VectorStore. See a full working example here. In this example, we're using a Postgres VectorStore to embed data of a Github Branch, but you can use any supported Langchain VectorStore.

Note that when you create the Langchain Documents, you should include as metadata the source and title fields in order for GPTR to leverage your Documents seamlessly. In the example below, we're splitting the documents list into chunks of 100 & then inserting 1 chunk at a time into the vector store.

**Examples:**

Example 1 (bash):
```bash
Step 1: transform your content (web results or local documents) into Langchain Documents
```

Example 2 (bash):
```bash
Step 2: Insert your Langchain Documents into a Langchain VectorStore
```

Example 3 (bash):
```bash
Step 3: Pass your Langchain Vectorstore into your GPTR report ([more on that here](https://docs.gptr.dev/docs/gpt-researcher/context/vector-stores) and below)
```

Example 4 (bash):
```bash
OPENAI_API_KEY={Your OpenAI API Key here}TAVILY_API_KEY={Your Tavily API Key here}PGVECTOR_CONNECTION_STRING=postgresql://username:password...
```

---

## npm package

**URL:** https://docs.gptr.dev/docs/gpt-researcher/gptr/npm-package

**Contents:**
- npm package
- Installation​
- Usage​

The gpt-researcher npm package is a WebSocket client for interacting with GPT Researcher.

**Examples:**

Example 1 (bash):
```bash
npm install gpt-researcher
```

Example 2 (javascript):
```javascript
const GPTResearcher = require('gpt-researcher');const researcher = new GPTResearcher({  host: 'localhost:8000',  logListener: (data) => console.log('logListener logging data: ',data)});researcher.sendMessage({  query: 'Does providing better context reduce LLM hallucinations?',  moreContext: 'Provide a detailed answer'});
```

---

## FAQ

**URL:** https://docs.gptr.dev/docs/faq

**Contents:**
- FAQ
  - How do I get started?​
  - What is GPT Researcher?​
  - How much does each research run cost?​
  - How do you ensure the report is factual and accurate?​
  - What are your plans for the future?​

It really depends on what you're aiming for.

If you're looking to connect your AI application to the internet with Tavily tailored API, check out the Tavily API documentation. If you're looking to build and deploy our open source autonomous research agent GPT Researcher, please see GPT Researcher documentation. You can also check out demos and examples for inspiration here.

GPT Researcher is a popular open source autonomous research agent that takes care of the tedious task of research for you, by scraping, filtering and aggregating over 20+ web sources per a single research task.

GPT Researcher is built with best practices for leveraging LLMs (prompt engineering, RAG, chains, embeddings, etc), and is optimized for quick and efficient research. It is also fully customizable and can be tailored to your specific needs.

To learn more about GPT Researcher, check out the documentation page.

A research task using GPT Researcher costs around $0.01 per a single run (for GPT-4 usage). We're constantly optimizing LLM calls to reduce costs and improve performance.

we do our best to ensure that the information we provide is factual and accurate. We do this by using multiple sources, and by using proprietary AI to score and rank the most relevant and accurate information. We also use proprietary AI to filter out irrelevant information and sources.

Lastly, by using RAG and other techniques, we ensure that the information is relevant to the context of the research task, leading to more accurate generative AI content and reduced hallucinations.

We're constantly working on improving our products and services. We're currently working on improving our search API together with design partners, and adding more data sources to our search engine. We're also working on improving our research agent GPT Researcher, and adding more features to it while growing our amazing open source community.

If you're interested in our roadmap or looking to collaborate, check out our roadmap page.

Feel free to contact us if you have any further questions or suggestions!

---

## Advanced Usage

**URL:** https://docs.gptr.dev/docs/gpt-researcher/mcp-server/advanced-usage

**Contents:**
- Advanced Usage
- Custom Configuration​
  - Environment Variables​
  - Server Configuration File​
- Integrating with Claude​
- Advanced Tool Usage​
  - Conducting Deep Research​
  - Customizing Report Generation​
- Securing Your MCP Server​
- Deploying with Docker​

This guide covers advanced usage scenarios and configurations for the GPT Researcher MCP Server.

You can customize the MCP server behavior by modifying various configuration parameters:

Create a .env file with additional configuration options:

You can create a config.json file to customize server behavior:

To integrate with Claude effectively:

Example configuration for Claude:

For deeper research capabilities:

The write_report tool accepts several customization options:

To secure your MCP server deployment:

Add API key authentication:

Set up rate limiting:

For easy deployment with Docker:

Enable detailed logging to monitor server activity:

You can extend the MCP server with additional capabilities:

For example, to add a new tool:

If you encounter rate limits with external APIs:

For handling large research tasks:

**Examples:**

Example 1 (bash):
```bash
# Required API keysOPENAI_API_KEY=your_openai_api_keyTAVILY_API_KEY=your_tavily_api_key# Optional configurations assuming using OpenAISTRATEGIC_LLM=openai:gpt-4o-mini # Change default to faster reasoning modelMAX_ITERATIONS=2 # Make the research faster by reducing iterationsSCRAPER=tavily_extract # For production use, using hosted scraping methods (assuming you use tavily)
```

Example 2 (json):
```json
{  "host": "0.0.0.0",  "port": 8000,  "debug": false,  "timeout": 300,  "max_concurrent_requests": 10}
```

Example 3 (json):
```json
{  "tools": [    {      "name": "gptr-researcher",      "endpoint": "http://localhost:8000/mcp"    }  ]}
```

Example 4 (text):
```text
Use the conduct_research tool with these advanced parameters:{  "query": "quantum computing advancements 2024",  "depth": "deep",  "focus_areas": ["hardware", "algorithms", "applications"],  "timeline": "last 1 year"}
```

---

## MCP Integration

**URL:** https://docs.gptr.dev/docs/gpt-researcher/retrievers/mcp-configs

**Contents:**
- MCP Integration
- How MCP Works in GPT Researcher​
- MCP Research Flow​
  - Flow Breakdown:​
- Prerequisites​
- Essential Configuration: Enabling MCP​
  - Pure MCP Research​
  - Hybrid Strategy (Recommended)​
- Quick Start​
- Configuration Structure​

The Model Context Protocol (MCP) enables GPT Researcher to connect with diverse data sources and tools through a standardized interface. GPT Researcher features an intelligent two-stage MCP approach that automatically selects the best tools and generates contextual research, powered by LangChain's MCP adapters for seamless integration.

GPT Researcher uses a two stage intelligent approach for MCP integration:

This happens automatically behind the scenes, optimized for the best balance of speed, cost, and research quality. The integration leverages the langchain-mcp-adapters library, ensuring compatibility with the growing ecosystem of MCP tool servers.

The following diagram illustrates the hybrid strategy using RETRIEVER=tavily,mcp as an example:

MCP support is included with GPT Researcher installation:

Important: To use MCP with GPT Researcher, you must set the RETRIEVER environment variable:

Each MCP configuration dictionary supports these keys:

Local servers: Require name, command, and args Remote servers: Require name and connection_url

Perfect for current events, market research, and general information gathering:

Ideal for technical documentation, code examples, and software development research:

Combining academic papers with MCP tools:

Here's a real-world example combining multiple MCP servers for comprehensive business intelligence:

This example demonstrates how GPT Researcher intelligently:

Another practical multi-server scenario for business research:

MCP works seamlessly alongside traditional web search for comprehensive research:

Here's a production-ready example demonstrating MCP integration:

For advanced users who need more control over how MCP research is executed:

Set global defaults using environment variables:

Enable automatic tool selection for servers with multiple tools:

GPT Researcher automatically detects connection types:

"No retriever specified" or "MCP not working"

"Invalid retriever(s) found"

"No MCP server configurations found"

"MCP server connection failed"

"No tools available from MCP server"

"Tool execution failed"

Enable detailed logging to diagnose issues:

Quick test to verify MCP configuration:

For more examples and advanced use cases, check out the GPT Researcher examples repository. :-)

**Examples:**

Example 1 (bash):
```bash
pip install gpt-researcher# All MCP dependencies are included automatically
```

Example 2 (bash):
```bash
export RETRIEVER=mcp
```

Example 3 (bash):
```bash
# Combines web search with MCP for comprehensive researchexport RETRIEVER=tavily,mcp# Alternative hybrid combinationsexport RETRIEVER=tavily,mcpexport RETRIEVER=google,mcp,arxiv
```

Example 4 (python):
```python
from gpt_researcher import GPTResearcherimport os# Set retriever to enable MCPos.environ["RETRIEVER"] = "tavily,mcp"  # Hybrid approach# Simple MCP configuration - works automaticallyresearcher = GPTResearcher(    query="How does React's useState hook work?",    mcp_configs=[        {            "name": "github_api"            "command": "npx",            "args": ["-y", "@modelcontextprotocol/server-github"],            "env": {"GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")}        }    ])context = await researcher.conduct_research()report = await researcher.write_report()
```

---

## Agent Example

**URL:** https://docs.gptr.dev/docs/gpt-researcher/gptr/example

**Contents:**
- Agent Example

If you're interested in using GPT Researcher as a standalone agent, you can easily import it into any existing Python project. Below, is an example of calling the agent to generate a research report:

You can further enhance this example to use the returned report as context for generating valuable content such as news article, marketing content, email templates, newsletters, etc.

You can also use GPT Researcher to gather information about code documentation, business analysis, financial information and more. All of which can be used to complete much more complex tasks that require factual and high quality realtime information.

**Examples:**

Example 1 (python):
```python
from gpt_researcher import GPTResearcherimport asyncioasync def fetch_report(query):    """    Fetch a research report based on the provided query and report type.    """    researcher = GPTResearcher(query=query)    await researcher.conduct_research()    report = await researcher.write_report()    return reportasync def generate_research_report(query):    """    This is a sample script that executes an async main function to run a research report.    """    report = await fetch_report(query)    print(report)if __name__ == "__main__":    QUERY = "What happened in the latest burning man floods?"    asyncio.run(generate_research_report(query=QUERY))
```

---

## Running on Linux

**URL:** https://docs.gptr.dev/docs/gpt-researcher/getting-started/linux-deployment

**Contents:**
- Running on Linux
- Server Requirements​
- Deployment Steps​
  - Step 1: Update the System​
  - First, ensure your package index is up-to-date:​

This guide will walk you through the process of deploying GPT Researcher on a Linux server.

The default Ubuntu droplet option on DigitalOcean works well, but this setup should work on any hosting service with similar specifications:

Here's a screenshot of the recommended Ubuntu machine specifications:

After setting up your server, follow these steps to install Docker, Docker Compose, and Nginx.

Some more commands to achieve that:

Here's your nginx config file:

And if you're using SSL:

And the relevant commands:

**Examples:**

Example 1 (bash):
```bash
sudo apt update### Step 2: Install Git### Git is a version control system. Install it using:sudo apt install git -y### Verify the installation by checking the Git version:git --version### Step 3: Install Docker### Docker is a platform for developing, shipping, and running applications inside containers.### Install prerequisites:sudo apt install apt-transport-https ca-certificates curl software-properties-common -y### Add Docker’s official GPG key:curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg### Set up the stable repository:echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null### Update the package index again and install Docker:sudo apt updatesudo apt install docker-ce -y### Verify Docker installation:sudo systemctl status docker### Optionally, add your user to the docker group to run Docker without sudo:sudo usermod -aG docker ${USER}### Log out and back in for the group change to take effect.Step 4: Install Nginx### Nginx is a high-performance web server.### Install Nginx:sudo apt install nginx -y### Start and enable Nginx:sudo systemctl start nginxsudo systemctl enable nginx### Verify Nginx installation:sudo systemctl status nginx
```

Example 2 (bash):
```bash
events {}http {   server {       listen 80;       server_name name.example;              client_max_body_size 64M;       location / {           proxy_pass http://localhost:3000;           proxy_http_version 1.1;           proxy_set_header Upgrade $http_upgrade;           proxy_set_header Connection 'upgrade';           proxy_set_header Host $host;           proxy_cache_bypass $http_upgrade;       }       location ~ ^/(ws|upload|files|outputs|getConfig|setConfig) {           proxy_pass http://localhost:8000;           proxy_http_version 1.1;           proxy_set_header Upgrade $http_upgrade;           proxy_set_header Connection "Upgrade";           proxy_set_header Host $host;       }   }}
```

Example 3 (nginx):
```nginx
server {    server_name name.example;        client_max_body_size 64M;        location / {        proxy_pass http://localhost:3000;        proxy_http_version 1.1;        proxy_set_header Upgrade $http_upgrade;        proxy_set_header Connection 'upgrade';        proxy_set_header Host $host;        proxy_cache_bypass $http_upgrade;    }        location ~ ^/(ws|upload|files|outputs|getConfig|setConfig) {        proxy_pass http://localhost:8000;        proxy_http_version 1.1;        proxy_set_header Upgrade $http_upgrade;        proxy_set_header Connection "Upgrade";        proxy_set_header Host $host;    }        listen 443 ssl; # managed by Certbot    ssl_certificate /etc/letsencrypt/live/name.example/fullchain.pem; # managed by Certbot    ssl_certificate_key /etc/letsencrypt/live/name.example/privkey.pem; # managed by Certbot    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot}server {    if ($host = name.example) {        return 301 https://$host$request_uri;    } # managed by Certbot        listen 80;    server_name name.example;    return 404; # managed by Certbot}
```

Example 4 (bash):
```bash
vim /etc/nginx/nginx.conf### Edit it to reflect above. Then verify all is good with:sudo nginx -t# If there are no errors:sudo systemctl restart nginx# Clone .env.example as .env# Run from root: docker-compose up --build
```

---

## Tailored Research

**URL:** https://docs.gptr.dev/docs/gpt-researcher/context/tailored-research

**Contents:**
- Tailored Research
  - Research on Specific Sources 📚​
  - Specify Agent Prompt 📝​
  - Research on Local Documents 📄​
  - Hybrid Research 🔄​
  - Research on LangChain Documents 🦜️🔗​

The GPT Researcher package allows you to tailor the research to your needs such as researching on specific sources (URLs) or local documents, and even specify the agent prompt instruction upon which the research is conducted.

You can specify the sources you want the GPT Researcher to research on by providing a list of URLs. The GPT Researcher will then conduct research on the provided sources via source_urls.

If you want GPT Researcher to perform additional research outside of the URLs you provided, i.e., conduct research on various other websites that it finds suitable for the query/sub-query, you can set the parameter complement_source_urls as True. Default value of False will only scour the websites you provide via source_urls.

You can specify the agent prompt instruction upon which the research is conducted. This allows you to guide the research in a specific direction and tailor the report layout. Simply pass the prompt as the query argument to the GPTResearcher class and the "custom_report" report_type.

You can instruct the GPT Researcher to research on local documents by providing the path to those documents. Currently supported file formats are: PDF, plain text, CSV, Excel, Markdown, PowerPoint, and Word documents.

Step 1: Add the env variable DOC_PATH pointing to the folder where your documents are located.

Step 2: When you create an instance of the GPTResearcher class, pass the report_source argument as "local".

GPT Researcher will then conduct research on the provided documents.

You can combine the above methods to conduct hybrid research. For example, you can instruct the GPT Researcher to research on both web sources and local documents. Simply provide the sources and set the report_source argument as "hybrid" and watch the magic happen.

Please note! You should set the proper retrievers for the web sources and doc path for local documents for this to work. To learn more about retrievers check out the Retrievers documentation.

You can instruct the GPT Researcher to research on a list of langchain document instances.

**Examples:**

Example 1 (python):
```python
from gpt_researcher import GPTResearcherimport asyncioasync def get_report(query: str, report_type: str, sources: list) -> str:    researcher = GPTResearcher(query=query, report_type=report_type, source_urls=sources, complement_source_urls=False)    await researcher.conduct_research()    report = await researcher.write_report()    return reportif __name__ == "__main__":    query = "What are the biggest trends in AI lately?"    report_source = "static"    sources = [        "https://en.wikipedia.org/wiki/Artificial_intelligence",        "https://www.ibm.com/think/insights/artificial-intelligence-trends",        "https://www.forbes.com/advisor/business/ai-statistics"    ]    report = asyncio.run(get_report(query=query, report_source=report_source, sources=sources))    print(report)
```

Example 2 (python):
```python
from gpt_researcher import GPTResearcherimport asyncioasync def get_report(prompt: str, report_type: str) -> str:    researcher = GPTResearcher(query=prompt, report_type=report_type)    await researcher.conduct_research()    report = await researcher.write_report()    return report    if __name__ == "__main__":    report_type = "custom_report"    prompt = "Research the latest advancements in AI and provide a detailed report in APA format including sources."    report = asyncio.run(get_report(prompt=prompt, report_type=report_type))    print(report)
```

Example 3 (bash):
```bash
export DOC_PATH="./my-docs"
```

Example 4 (python):
```python
from gpt_researcher import GPTResearcherimport asyncioasync def get_report(query: str, report_source: str) -> str:    researcher = GPTResearcher(query=query, report_source=report_source)    await researcher.conduct_research()    report = await researcher.write_report()    return report    if __name__ == "__main__":    query = "What can you tell me about myself based on my documents?"    report_source = "local" # "local" or "web"    report = asyncio.run(get_report(query=query, report_source=report_source))    print(report)
```

---

## Roadmap

**URL:** https://docs.gptr.dev/docs/roadmap

**Contents:**
- Roadmap

We're constantly working on additional features and improvements to our products and services. We're also working on new products and services to help you build better AI applications using GPT Researcher.

Our vision is to build the #1 autonomous research agent for AI developers and researchers, and we're excited to have you join us on this journey!

The roadmap is prioritized based on the following goals: Performance, Quality, Modularity and Conversational flexibility. The roadmap is public and can be found here.

Interested in collaborating or contributing? Check out our contributing page for more information.

---

## Langsmith Logs

**URL:** https://docs.gptr.dev/docs/gpt-researcher/handling-logs/langsmith-logs

**Contents:**
- Langsmith Logs

With the help of Langsmith, you can easily visualize logs on cost and errors within your Langsmith Dashboard (calculated per LLM call or grouped by project)

Here are the steps to setup Langsmith:

Step 1: Setup a Langsmith account at: smith.langchain.com

Step 2: Create a new API key at: smith.langchain.com/settings

Step 3: Add these 2 environment variables:

Here's what this looks like in the Langsmith Dashboard:

This can be helpful for:

**Examples:**

Example 1 (bash):
```bash
LANGCHAIN_TRACING_V2=trueLANGCHAIN_API_KEY=Set this to your API key
```

---

## Automated Tests

**URL:** https://docs.gptr.dev/docs/gpt-researcher/gptr/automated-tests

**Contents:**
- Automated Tests
- Automated Testing with Github Actions​
- Running the Tests​
  - Via a docker command​
  - Via a Github Action​

This repository contains the code for the automated testing of the GPT-Researcher Repo using Github Actions.

The tests are triggered in a docker container which runs the tests via the pytest module.

You can run the tests:

Attaching here the required settings & screenshots on the github repo level:

Step 1: Within the repo, press the "Settings" tab

Step 2: Create a new environment named "tests" (all lowercase)

Step 3: Click into the "tests" environment & add environment secrets of OPENAI_API_KEY & TAVILY_API_KEY

Get the keys from here:

https://app.tavily.com/sign-in

https://platform.openai.com/api-keys

If configured correctly, here's what the Github action should look like when opening a new PR or committing to an open PR:

**Examples:**

Example 1 (bash):
```bash
docker-compose --profile test run --rm gpt-researcher-tests
```

---

## Search Engines

**URL:** https://docs.gptr.dev/docs/gpt-researcher/search-engines

**Contents:**
- Search Engines
- Web Search Engines​
- Custom Retrievers​
  - Example​
  - Response Format​

Search Engines are used to find the most relevant web sources and content for a given research task. You can specify your preferred web search or use any custom retriever of your choice.

GPT Researcher defaults to using the Tavily search engine for retrieving search results. But you can also use other search engines by specifying the RETRIEVER env var. Please note that each search engine has its own API Key requirements and usage limits.

You can also specify multiple retrievers by separating them with commas. The system will use each specified retriever in sequence. For example:

Thanks to our community, we have integrated the following web search engines:

You can also use any custom retriever of your choice by specifying the RETRIEVER=custom env var. Custom retrievers allow you to use any search engine that provides an API to retrieve documents and is widely used for enterprise research tasks.

In addition to setting the RETRIEVER env, you also need to set the following env vars:

For the custom retriever to work correctly, the response from the endpoint should be in the following format:

The system assumes this response format and processes the list of sources accordingly.

Missing a retriever? Feel free to contribute to this project by submitting issues or pull requests on our GitHub page.

**Examples:**

Example 1 (bash):
```bash
RETRIEVER=bing
```

Example 2 (bash):
```bash
RETRIEVER=tavily, arxiv
```

Example 3 (bash):
```bash
RETRIEVER=customRETRIEVER_ENDPOINT=https://api.myretriever.comRETRIEVER_ARG_API_KEY=YOUR_API_KEY
```

Example 4 (json):
```json
[  {    "url": "http://example.com/page1",    "raw_content": "Content of page 1"  },  {    "url": "http://example.com/page2",    "raw_content": "Content of page 2"  }]
```

---

## Discord Bot

**URL:** https://docs.gptr.dev/docs/gpt-researcher/frontend/discord-bot

**Contents:**
- Discord Bot
- Intro​
- To create your own discord bot with GPTR functionality​
  - Deploying the bot commands​
  - Running the bot via Docker​
  - Running the bot via CLI​
  - Installing NodeJS and NPM on Ubuntu​

You can either leverage the official GPTR Discord bot or create your own custom bot.

To add the official GPTR Discord bot, simply click here to invite GPTR to your Discord server.

Add a .env file in the root of the project and add the following:

You can fetch the token from the Discord Developer Portal by following these steps:

In our case, this will make the "ask" and "ping" commands available to users of the bot.

**Examples:**

Example 1 (text):
```text
DISCORD_BOT_TOKEN=DISCORD_CLIENT_ID=
```

Example 2 (bash):
```bash
node deploy-commands.js
```

Example 3 (bash):
```bash
docker compose --profile discord run --rm discord-bot
```

Example 4 (bash):
```bash
# install dependenciesnpm install# run the botnpm run dev
```

---

## Getting Started

**URL:** https://docs.gptr.dev/docs/gpt-researcher/mcp-server/getting-started

**Contents:**
- Getting Started
- Why GPT Researcher MCP?​
  - Resources​
  - Primary Tools​
  - Prompts​
- Prerequisites​
- Installation​
- Running the MCP Server​
  - Method 1: Directly using Python​
  - Method 2: Using the MCP CLI (if installed)​

The GPT Researcher MCP Server provides Model Context Protocol (MCP) integration for GPT Researcher, allowing AI assistants to perform autonomous, comprehensive web research and generate reports via the MCP protocol.

While many AI apps can access web search tools with MCP, GPT Researcher MCP delivers in-depth results. Standard search tools return raw results requiring manual filtering, often containing irrelevant sources and wasting context window space.

GPT Researcher performs autonomous, deep research - not just search. It intelligently explores and validates multiple sources, focusing only on relevant and up-to-date information. Though slightly slower (30-40 seconds) than standard search, it delivers higher quality information, optimized context, comprehensive results, and better reasoning for LLMs.

The MCP server exposes the following capabilities to AI assistants:

Before running the MCP server, make sure you have:

You can start the MCP server in two ways:

Once the server is running, you'll see output indicating that the server is ready to accept connections.

There are two primary ways to integrate your MCP server with Claude:

For detailed instructions on each method, follow the links above.

If you encounter issues while running the MCP server:

**Examples:**

Example 1 (bash):
```bash
git clone https://github.com/assafelovic/gptr-mcp.git
```

Example 2 (bash):
```bash
pip install -r requirements.txt
```

Example 3 (bash):
```bash
cp .env.example .env
```

Example 4 (bash):
```bash
OPENAI_API_KEY=your_openai_api_keyTAVILY_API_KEY=your_tavily_api_key
```

---

## Simple Logs Example

**URL:** https://docs.gptr.dev/docs/gpt-researcher/handling-logs/simple-logs-example

**Contents:**
- Simple Logs Example

Here is a snippet of code to help you handle the streaming logs of your Research tasks.

The data from the research process will be logged and stored in the CustomLogsHandler instance. You can customize the logging behavior as needed for your application.

Here's a sample of the output:

The metadata field will include whatever metadata is relevant to the log entry. Let the script above run to completion for the full logs output of a given research task.

**Examples:**

Example 1 (python):
```python
from typing import Dict, Anyimport asynciofrom gpt_researcher import GPTResearcherclass CustomLogsHandler:    """A custom Logs handler class to handle JSON data."""    def __init__(self):        self.logs = []  # Initialize logs to store data    async def send_json(self, data: Dict[str, Any]) -> None:        """Send JSON data and log it."""        self.logs.append(data)  # Append data to logs        print(f"My custom Log: {data}")  # For demonstration, print the logasync def run():    # Define the necessary parameters with sample values        query = "What happened in the latest burning man floods?"    report_type = "research_report"  # Type of report to generate    report_source = "online"  # Could specify source like 'online', 'books', etc.    tone = "informative"  # Tone of the report ('informative', 'casual', etc.)    config_path = None  # Path to a config file, if needed        # Initialize researcher with a custom WebSocket    custom_logs_handler = CustomLogsHandler()    researcher = GPTResearcher(        query=query,        report_type=report_type,        report_source=report_source,        tone=tone,        config_path=config_path,        websocket=custom_logs_handler    )    await researcher.conduct_research()  # Conduct the research    report = await researcher.write_report()  # Write the research report    return report# Run the asynchronous function using asyncioif __name__ == "__main__":    asyncio.run(run())
```

Example 2 (text):
```text
{    "type": "logs",    "content": "added_source_url",    "output": "✅ Added source url to research: https://www.npr.org/2023/09/28/1202110410/how-rumors-and-conspiracy-theories-got-in-the-way-of-mauis-fire-recovery\n",    "metadata": "https://www.npr.org/2023/09/28/1202110410/how-rumors-and-conspiracy-theories-got-in-the-way-of-mauis-fire-recovery"}
```

---

## Hybrid Research

**URL:** https://docs.gptr.dev/docs/examples/hybrid_research

**Contents:**
- Hybrid Research
- Introduction​
- Prerequisites​
- Installation​
- Setting Up the Environment​
- Preparing Documents​
  - 1. Local Documents​
  - 2. Online Documents​
- Running Hybrid Research By "Local Documents"​
- Running Hybrid Research By "Online Documents"​

GPT Researcher can combine web search capabilities with local document analysis to provide comprehensive, context-aware research results.

This guide will walk you through the process of setting up and running hybrid research using GPT Researcher.

Before you begin, ensure you have the following:

Export your API keys as environment variables:

Alternatively, you can set these in your Python script:

Set the environment variable REPORT_SOURCE to an empty string "" in default.py

Here's a basic script to run hybrid research:

Here's a basic script to run hybrid research:

The output will be a comprehensive research report that combines insights from both web sources and your local documents. The report typically includes an executive summary, key findings, detailed analysis, comparisons between your internal data and external trends, and recommendations based on the combined insights.

Q: How long does a typical research session take? A: The duration varies based on the complexity of the query and the amount of data to process. It can range from 1-5 minutes for very comprehensive research.

Q: Can I use GPT Researcher with other language models? A: Currently, GPT Researcher is optimized for OpenAI's models. Support for other models can be found here.

Q: How does GPT Researcher handle conflicting information between local and web sources? A: The system attempts to reconcile differences by providing context and noting discrepancies in the final report. It prioritizes more recent or authoritative sources when conflicts arise.

Q: Is my local data sent to external servers during the research process? A: No, your local documents are processed on your machine. Only the generated queries and synthesized information (not raw data) are sent to external services for web research.

For more information and updates, please visit the GPT Researcher GitHub repository.

**Examples:**

Example 1 (bash):
```bash
pip install gpt-researcher
```

Example 2 (bash):
```bash
export OPENAI_API_KEY=your_openai_api_key_hereexport TAVILY_API_KEY=your_tavily_api_key_here
```

Example 3 (python):
```python
import osos.environ['OPENAI_API_KEY'] = 'your_openai_api_key_here'os.environ['TAVILY_API_KEY'] = 'your_tavily_api_key_here'
```

Example 4 (python):
```python
from gpt_researcher import GPTResearcherimport asyncioasync def get_research_report(query: str, report_type: str, report_source: str) -> str:    researcher = GPTResearcher(query=query, report_type=report_type, report_source=report_source)    research = await researcher.conduct_research()    report = await researcher.write_report()    return reportif __name__ == "__main__":    query = "How does our product roadmap compare to emerging market trends in our industry?"    report_source = "hybrid"    report = asyncio.run(get_research_report(query=query, report_type="research_report", report_source=report_source))    print(report)
```

---

## Testing your LLM

**URL:** https://docs.gptr.dev/docs/gpt-researcher/llms/testing-your-llm

**Contents:**
- Testing your LLM

Here is a snippet of code to help you verify that your LLM-related environment variables are set up correctly.

**Examples:**

Example 1 (python):
```python
from gpt_researcher.config.config import Configfrom gpt_researcher.utils.llm import create_chat_completionimport asynciofrom dotenv import load_dotenvload_dotenv()async def main():    cfg = Config()    try:        report = await create_chat_completion(            model=cfg.smart_llm_model,            messages = [{"role": "user", "content": "sup?"}],            temperature=0.35,            llm_provider=cfg.smart_llm_provider,            stream=True,            max_tokens=cfg.smart_token_limit,            llm_kwargs=cfg.llm_kwargs        )    except Exception as e:        print(f"Error in calling LLM: {e}")# Run the async functionasyncio.run(main())
```

---

## PIP Package

**URL:** https://docs.gptr.dev/docs/gpt-researcher/gptr/pip-package

**Contents:**
- PIP Package
- Steps to Install GPT Researcher​
- Example Usage​
- Specific Examples​
  - Example 1: Research Report​
  - Example 2: Resource Report​
  - Example 3: Outline Report​
- Integration with Web Frameworks​
  - FastAPI Example​
  - Flask Example​

🌟 Exciting News! Now, you can integrate gpt-researcher with your apps seamlessly!

Follow these easy steps to get started:

Pre-requisite: Install flask with the async extra.

GPT Researcher provides several methods to retrieve additional information about the research process:

Sources are the URLs that were used to gather information for the research.

Context is all the retrieved information from the research. It includes the sources and their corresponding content.

Costs are the number of tokens consumed during the research process.

Retrieves a list of images found during the research process.

Retrieves a list of research sources, including title, content, and images.

You can set the verbose mode to get more detailed logs.

You can also add costs to the research process if you want to track the costs from external usage.

You can customize various aspects of the research process by passing additional parameters when initializing the GPTResearcher:

After conducting research, you can process the results in various ways:

The write_report method accepts a custom_prompt parameter that gives you complete control over how your research is presented:

Custom prompts can be used for various purposes:

Format Control: Specify the structure, length, or style of your report

Audience Targeting: Tailor the content for specific readers

Specialized Outputs: Generate specific types of content

The custom prompt will be combined with the research context to generate your customized report.

You can use the research context for further processing or analysis:

This comprehensive documentation should help users understand and utilize the full capabilities of the GPT Researcher package.

**Examples:**

Example 1 (bash):
```bash
pip install gpt-researcher
```

Example 2 (bash):
```bash
export OPENAI_API_KEY={Your OpenAI API Key here}
```

Example 3 (bash):
```bash
export TAVILY_API_KEY={Your Tavily API Key here}
```

Example 4 (python):
```python
from gpt_researcher import GPTResearcherimport asyncioasync def get_report(query: str, report_type: str):    researcher = GPTResearcher(query, report_type)    research_result = await researcher.conduct_research()    report = await researcher.write_report()        # Get additional information    research_context = researcher.get_research_context()    research_costs = researcher.get_costs()    research_images = researcher.get_research_images()    research_sources = researcher.get_research_sources()        return report, research_context, research_costs, research_images, research_sourcesif __name__ == "__main__":    query = "what team may win the NBA finals?"    report_type = "research_report"    report, context, costs, images, sources = asyncio.run(get_report(query, report_type))        print("Report:")    print(report)    print("\nResearch Costs:")    print(costs)    print("\nNumber of Research Images:")    print(len(images))    print("\nNumber of Research Sources:")    print(len(sources))
```

---

## All About Logs

**URL:** https://docs.gptr.dev/docs/gpt-researcher/handling-logs/all-about-logs

**Contents:**
- All About Logs
- Log File Overview​
- Key Components:​
- Types of Events & Their Significance​
- How to Use the Logs​
- Example Usage​
- Logs for Developers​
  - Basic Log File (.log)​
  - JSON Log File (.json)​

This document explains how to interpret the log files generated for each report. These logs provide a detailed record of the research process, from initial task planning to the gathering of information, and finally, the report writing process. Reports may change over time as new features are developed.

The log file is a JSON file that contains a list of events that happened during the research process. Each event is an object with a timestamp, type, and data. The data contains the specific information about the event.

You can find the log file in the outputs folder.

Or you can access the log file from the report page itself by clicking the "Download Logs" button.

For developers, there is an additional logs folder that may be useful. See description below for more details.

Here's a complete breakdown of all the unique content types and what they mean. This is a comprehensive list of all the different actions the research tool will perform.

By looking at the timestamps, you can see the flow of the research task. The logs will show you the subqueries used by the tool to approach the main query, all the URLs used, if images were selected for the research, and all the steps the tool took to generate the report.

In addition to the user-facing log files (detailed and summary reports), the application also generates two types of log files specifically for developers:

---

## GPT Researcher

**URL:** https://docs.gptr.dev/

**Contents:**
  - GPT Researcher
  - Multi-Agent Assistant
  - Examples and Demos

GPT Researcher is an open source autonomous agent designed for comprehensive online research on a variety of tasks.

Learn how a team of AI agents can work together to conduct research on a given topic, from planning to publication.

Check out GPT Researcher in action across multiple frameworks and use cases such as hybrid research and long detailed reports.

---

## Run with CLI

**URL:** https://docs.gptr.dev/docs/gpt-researcher/getting-started/cli

**Contents:**
- Run with CLI
- Installation​
- Usage​
  - Arguments​
- Examples​
- Output​
- Note​

This command-line interface (CLI) tool allows you to generate research reports using the GPTResearcher class. It provides an easy way to conduct research on various topics and generate different types of reports.

Clone the repository:

Install the required dependencies:

Set up your environment variables: Create a .env file in the project root and add your API keys or other necessary configurations.

The basic syntax for using the CLI is:

Generate a quick research report on climate change:

Create a detailed report on artificial intelligence with an analytical tone:

Generate an outline report on renewable energy with a persuasive tone:

The generated report will be saved as a Markdown file in the outputs directory. The filename will be a unique UUID.

**Examples:**

Example 1 (text):
```text
git clone https://github.com/yourusername/gpt-researcher.gitcd gpt-researcher
```

Example 2 (text):
```text
pip install -r requirements.txt
```

Example 3 (text):
```text
python cli.py "<query>" --report_type <report_type> [--tone <tone>]
```

Example 4 (text):
```text
python cli.py "What are the main causes of climate change?" --report_type research_report
```

---

## Configure LLM

**URL:** https://docs.gptr.dev/docs/gpt-researcher/llms

**Contents:**
- Configure LLM
- OpenAI​
- Custom LLM​
- Azure OpenAI​
- Ollama​
  - Granite with Ollama​
- Groq​
  - Sign up​
  - Update env vars​
- Anthropic​

As described in the introduction, the default LLM and embedding is OpenAI due to its superior performance and speed. With that said, GPT Researcher supports various open/closed source LLMs and embeddings, and you can easily switch between them by updating the SMART_LLM, FAST_LLM and EMBEDDING env variables. You might also need to include the provider API key and corresponding configuration params.

Current supported LLMs are openai, anthropic, azure_openai, cohere, google_vertexai, google_genai, fireworks, ollama, together, mistralai, huggingface, groq, bedrock and litellm.

Current supported embeddings are openai, azure_openai, cohere, google_vertexai, google_genai, fireworks, ollama, together, mistralai, huggingface, nomic ,voyageai and bedrock.

To learn more about support customization options see here.

Please note: GPT Researcher is optimized and heavily tested on GPT models. Some other models might run into context limit errors, and unexpected responses. Please provide any feedback in our Discord community channel, so we can better improve the experience and performance.

Below you can find examples for how to configure the various supported LLMs.

Create a local OpenAI API using llama.cpp Server.

For custom LLM, specify "openai:{your-llm}"

For custom embedding, set "custom:{your-embedding}"

In Azure OpenAI you have to chose which models you want to use and make deployments for each model. You do this on the Azure OpenAI Portal.

In January 2025 the models that are recommended to use are:

Please then specify the model names/deployment names in your .env file.

Required Precondition

Add langchain-azure-dynamic-sessions to requirements.txt for Docker Support or pip install it

GPT Researcher supports both Ollama LLMs and embeddings. You can choose each or both. To use Ollama you can set the following environment variables

Add langchain-ollama to requirements.txt for Docker Support or pip install it

GPT Researcher has custom prompt formatting for the Granite family of models. To use the right formatting, you can set the following environment variables:

GroqCloud provides advanced AI hardware and software solutions designed to deliver amazingly fast AI inference performance. To leverage Groq in GPT-Researcher, you will need a GroqCloud account and an API Key. (NOTE: Groq has a very generous free tier.)

You can signup here: https://console.groq.com/login

Once you are logged in, you can get an API Key here: https://console.groq.com/keys

Once you have an API key, you will need to add it to your systems environment using the variable name: GROQ_API_KEY=*********************

And finally, you will need to configure the GPT-Researcher Provider and Model variables:

Add langchain-groq to requirements.txt for Docker Support or pip install it

NOTE: As of the writing of this Doc (May 2024), the available Language Models from Groq are:

Refer to Anthropic Getting started page to obtain Anthropic API key. Update the corresponding env vars, for example:

Add langchain-anthropic to requirements.txt for Docker Support or pip install it

Anthropic does not offer its own embedding model, therefore, you'll want to either default to the OpenAI embedding model, or find another.

Sign up for a Mistral API key. Then update the corresponding env vars, for example:

Add langchain-mistralai to requirements.txt for Docker Support or pip install it

Together AI offers an API to query 50+ leading open-source models in a couple lines of code. Then update corresponding env vars, for example:

Add langchain-together to requirements.txt for Docker Support or pip install it

This integration requires a bit of extra work. Follow this guide to learn more. After you've followed the tutorial above, update the env vars:

Add langchain-huggingface to requirements.txt for Docker Support or pip install it

Sign up here for obtaining a Google Gemini API Key and update the following env vars:

Add langchain-google-genai to requirements.txt for Docker Support or pip install it

Add langchain-google-vertexai to requirements.txt for Docker Support or pip install it

Add langchain-cohere to requirements.txt for Docker Support or pip install it

Add langchain-fireworks to requirements.txt for Docker Support or pip install it

Add langchain_aws to requirements.txt for Docker Support or pip install it

Add langchain_community to requirements.txt for Docker Support or pip install it

Add langchain_xai to requirements.txt for Docker Support or pip install it

You can check provider docs here

And models overview is here

Add langchain-voyageai to requirements.txt for Docker Support or pip install it

**Examples:**

Example 1 (env):
```env
# set the custom OpenAI API keyOPENAI_API_KEY=[Your Key]# specify llmsFAST_LLM=openai:gpt-4o-miniSMART_LLM=openai:gpt-4.1STRATEGIC_LLM=openai:o4-mini# specify embeddingEMBEDDING=openai:text-embedding-3-small
```

Example 2 (env):
```env
# set the custom OpenAI API urlOPENAI_BASE_URL=http://localhost:1234/v1# set the custom OpenAI API keyOPENAI_API_KEY=dummy_key# specify custom llms  FAST_LLM=openai:your_fast_llmSMART_LLM=openai:your_smart_llmSTRATEGIC_LLM=openai:your_strategic_llm
```

Example 3 (env):
```env
# set the custom OpenAI API urlOPENAI_BASE_URL=http://localhost:1234/v1# set the custom OpenAI API keyOPENAI_API_KEY=dummy_key# specify the custom embedding model   EMBEDDING=custom:your_embedding
```

Example 4 (env):
```env
# set the azure api key and deployment as you have configured it in Azure Portal. There is no default access point unless you configure it yourself!AZURE_OPENAI_API_KEY=[Your Key]AZURE_OPENAI_ENDPOINT=https://&#123;your-endpoint&#125;.openai.azure.com/OPENAI_API_VERSION=2024-05-01-preview# each string is "azure_openai:deployment_name". ensure that your deployment have the same name as the model you use!FAST_LLM=azure_openai:gpt-4o-miniSMART_LLM=azure_openai:gpt-4oSTRATEGIC_LLM=azure_openai:o1-preview# specify embeddingEMBEDDING=azure_openai:text-embedding-3-large
```

---

## Supported LLMs

**URL:** https://docs.gptr.dev/docs/gpt-researcher/llms/supported-llms

**Contents:**
- Supported LLMs

The following LLMs are supported by GPTR (though you'll need to install the relevant langchain package separately if you're not using OpenAI).

If you'd like to know the name of the langchain package for each LLM, you can check the Langchain documentation, or run GPTR as is and inspect the error message.

The GPTR LLM Module is built on top of the Langchain LLM Module.

If you'd like to add a new LLM into GPTR, you can start with the langchain documentation and then look into integrating it into the GPTR LLM Module.

---

## Filtering by Domain

**URL:** https://docs.gptr.dev/docs/gpt-researcher/context/filtering-by-domain

**Contents:**
- Filtering by Domain
- Using the Pip Package​
- Using the NextJS Frontend​
- Using the Vanilla JS Frontend​
- Filtering by Domain based on URL Param​
  - Single Domain:​
  - Multiple Domains:​

You can filter web search results by specific domains when using either the Tavily or Google Search retrievers. This functionality is available across all interfaces - pip package, NextJS frontend, and vanilla JS frontend.

Note: We welcome contributions to add domain filtering to other retrievers!

To set Tavily as a retriever, you'll need to set the RETRIEVER environment variable to tavily and set the TAVILY_API_KEY environment variable to your Tavily API key.

To set Google as a retriever, you'll need to set the RETRIEVER environment variable to google and set the GOOGLE_API_KEY and GOOGLE_CX_KEY environment variables to your Google API key and Google Custom Search Engine ID.

When using the pip package, you can pass a list of domains to filter results:

When using the NextJS frontend, you can pass a list of domains to filter results via the Settings Modal:

When using the Vanilla JS frontend, you can pass a list of domains to filter results via the relevant input field:

If you'd like to show off for your work pals how GPTR is the ultra-customizable Deep Research Agent, you can send them a link to your hosted GPTR app with the domain filter included in the URL itself.

This can be handle for demonstrating a proof of concept of the Research Agent tailored to a specific domain. Some examples below:

https://app.gptr.dev/?domains=wikipedia.org

https://app.gptr.dev/?domains=wired.com,forbes.com,wikipedia.org

The https://app.gptr.dev part of the URL can be replaces with the domain that you deployed GPTR on.

**Examples:**

Example 1 (bash):
```bash
RETRIEVER=tavilyTAVILY_API_KEY=your_tavily_api_key
```

Example 2 (bash):
```bash
RETRIEVER=googleGOOGLE_API_KEY=your_google_api_keyGOOGLE_CX_KEY=your_google_custom_search_engine_id
```

Example 3 (python):
```python
report = GPTResearcher(    query="Latest AI Startups",    report_type="research_report",    report_source="web",    domains=["forbes.com", "techcrunch.com"])
```

---

## Visualizing Websockets

**URL:** https://docs.gptr.dev/docs/gpt-researcher/frontend/visualizing-websockets

**Contents:**
- Visualizing Websockets
- Inspecting Websockets​
- Am I polling the right URL?​

The GPTR Frontend is powered by Websockets streaming back from the Backend. This allows for real-time updates on the status of your research tasks, as well as the ability to interact with the Backend directly from the Frontend.

When running reports via the frontend, you can inspect the websocket messages in the Network Tab.

If you're concerned that your frontend isn't hitting the right API Endpoint, you can check the URL in the Network Tab.

Click into the WS request & go to the "Headers" tab

For debugging, have a look at the getHost function.

---

## Local Documents

**URL:** https://docs.gptr.dev/docs/gpt-researcher/context/local-docs

**Contents:**
- Local Documents
- Just Local Docs​
- Local Docs + Web (Hybrid)​

You can instruct the GPT Researcher to run research tasks based on your local documents. Currently supported file formats are: PDF, plain text, CSV, Excel, Markdown, PowerPoint, and Word documents.

Step 1: Add the env variable DOC_PATH pointing to the folder where your documents are located.

Check out the blog post on Hybrid Research to learn more about how to combine local documents with web research.

**Examples:**

Example 1 (bash):
```bash
export DOC_PATH="./my-docs"
```

---

## Troubleshooting

**URL:** https://docs.gptr.dev/docs/gpt-researcher/gptr/troubleshooting

**Contents:**
- Troubleshooting
  - model: gpt-4 does not exist​
  - cannot load library 'gobject-2.0-0'​
  - cannot load library 'pango'​
  - Error processing the url​
  - Chrome version issues​

We're constantly working to provide a more stable version. If you're running into any issues, please first check out the resolved issues or ask us via our Discord community.

This relates to not having permission to use gpt-4 yet. Based on OpenAI, it will be widely available for all by end of July.

The issue relates to the library WeasyPrint (which is used to generate PDFs from the research report). Please follow this guide to resolve it: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html

Or you can install this package manually

In case of MacOS you can install this lib using brew install glib pango If you face an issue with linking afterward, you can try running brew link glib

In case of Linux you can install this lib using sudo apt install libglib2.0-dev

In case of MacOS you can install this lib using brew install pango

In case of Linux you can install this lib using sudo apt install libpango-1.0-0

Workaround for Mac M chip users

If the above solutions don't work, you can try the following:

We're using Selenium for site scraping. Some sites fail to be scraped. In these cases, restart and try running again.

Many users have an issue with their chromedriver because the latest chrome browser version doesn't have a compatible chrome driver yet.

To downgrade your Chrome web browser using slimjet, follow these steps. First, visit the website and scroll down to find the list of available older Chrome versions. Choose the version you wish to install making sure it's compatible with your operating system. Once you've selected the desired version, click on the corresponding link to download the installer. Before proceeding with the installation, it's crucial to uninstall your current version of Chrome to avoid conflicts.

It's important to check if the version you downgrade to, has a chromedriver available in the official chrome driver website

If none of the above work, you can try out our hosted beta

---

## Running with Ollama

**URL:** https://docs.gptr.dev/docs/gpt-researcher/llms/running-with-ollama

**Contents:**
- Running with Ollama
- Fetching the Desired LLM Models​
- Querying your Custom LLM with GPT-Researcher​
- Deploy Ollama on Elestio​
- Run LLM Test Script for GPTR​
    - Disable Elestio Authentication or Add Auth Headers​

Ollama is a platform that allows you to deploy and manage custom language models. This guide will walk you through deploying a custom language model on Ollama.

Read on to understand how to install a Custom LLM with the Ollama WebUI, and how to query it with GPT-Researcher.

After deploying Ollama WebUI, you'll want to enter the Open WebUI Admin App & download a custom LLM.

Choose a model from Ollama's Library of LLM's

Paste the model name & size into the Web UI:

For our example, let's choose to download the qwen2:1.5b from the chat completion model & nomic-embed-text for the embeddings model.

This model now automatically becomes available via your Server's out-of-the-box API - we'll leverage it within our GPT-Researcher .env file in the next step.

If you deploy ollama locally, a .env like so, should enable powering GPT-Researcher with Ollama:

Replace FAST_LLM & SMART_LLM with the model you downloaded from the Elestio Web UI in the previous step.

Elestio is a platform that allows you to deploy and manage custom language models. This guide will walk you through deploying a custom language model on Elestio.

You can deploy an Open WebUI server with Elestio

You can leverage the global test-your-llm function with tests/test-your-llm. Here are the steps to do so:

Step 1: Set the following values in your .env. Note: replace the base urls with the custom domain that your web app is available on - for example: if the web app is available on https://ollama-2d52b-u21899.vm.elestio.app/ within the browser, that becomes the value to use in your .env file.

Note: to verify you're pointing at the correct API URL, you can run something like this in your terminal:

You should get an LLM response, such as:

To remove the basic auth you have to follow the below steps:

Go to your service -> Security in your Elestio admin panel.

Step 1: Disable the Firewall.

Step 2: Edit your Nginx Configuration. You'll want to comment both these both these lines out:

Step 2: Click the button "Update & Restart" to apply your nginx changes.

**Examples:**

Example 1 (bash):
```bash
OPENAI_API_KEY="123"OPENAI_API_BASE="http://127.0.0.1:11434/v1"OLLAMA_BASE_URL="http://127.0.0.1:11434/"FAST_LLM="ollama:qwen2:1.5b"SMART_LLM="ollama:qwen2:1.5b"STRATEGIC_LLM="ollama:qwen2:1.5b"EMBEDDING_PROVIDER="ollama"OLLAMA_EMBEDDING_MODEL="nomic-embed-text"
```

Example 2 (bash):
```bash
OPENAI_API_KEY="123"OPENAI_API_BASE="https://ollama-2d52b-u21899.vm.elestio.app:57987/v1"OLLAMA_BASE_URL="https://ollama-2d52b-u21899.vm.elestio.app:57987/"FAST_LLM="openai:qwen2.5"SMART_LLM="openai:qwen2.5"STRATEGIC_LLM="openai:qwen2.5"EMBEDDING_PROVIDER="ollama"OLLAMA_EMBEDDING_MODEL="nomic-embed-text"
```

Example 3 (bash):
```bash
nslookup ollama-2d52b-u21899.vm.elestio.app
```

Example 4 (bash):
```bash
cd testspython -m test-your-llm
```

---

## LangGraph

**URL:** https://docs.gptr.dev/docs/gpt-researcher/multi_agents/langgraph

**Contents:**
- LangGraph
- Use case​
- The Multi Agent Team​
- How it works​
  - Architecture​
  - Steps​
- How to run​
- Usage​
    - Task.json contains the following fields:​
    - For example:​

LangGraph is a library for building stateful, multi-actor applications with LLMs. This example uses Langgraph to automate the process of an in depth research on any given topic.

By using Langgraph, the research process can be significantly improved in depth and quality by leveraging multiple agents with specialized skills. Inspired by the recent STORM paper, this example showcases how a team of AI agents can work together to conduct research on a given topic, from planning to publication.

An average run generates a 5-6 page research report in multiple formats such as PDF, Docx and Markdown.

Please note: This example uses the OpenAI API only for optimized performance.

The research team is made up of 7 AI agents:

Generally, the process is based on the following stages:

More specifically (as seen in the architecture diagram) the process is as follows:

To change the research query and customize the report, edit the task.json file in the main directory.

From there, see documentation here on how to use the streaming and async endpoints, as well as the playground.

The React app (located in frontend directory) is our Frontend 2.0 which we hope will enable us to display the robustness of the backend on the frontend, as well.

It comes with loads of added features, such as:

Step 1 - Install Docker

Step 2 - Clone the '.env.example' file, add your API Keys to the cloned file and save the file as '.env'

Step 3 - Within the docker-compose file comment out services that you don't want to run with Docker.

Step 4 - By default, if you haven't uncommented anything in your docker-compose file, this flow will start 2 processes:

Visit localhost:3000 on any browser and enjoy researching!

**Examples:**

Example 1 (bash):
```bash
pip install -r requirements.txt
```

Example 2 (bash):
```bash
export OPENAI_API_KEY={Your OpenAI API Key here}export TAVILY_API_KEY={Your Tavily API Key here}
```

Example 3 (bash):
```bash
python main.py
```

Example 4 (json):
```json
{  "query": "Is AI in a hype cycle?",  "model": "gpt-4o",  "max_sections": 3,   "publish_formats": {     "markdown": true,    "pdf": true,    "docx": true  },  "include_human_feedback": false,  "source": "web",  "follow_guidelines": true,  "guidelines": [    "The report MUST fully answer the original question",    "The report MUST be written in apa format",    "The report MUST be written in english"  ],  "verbose": true}
```

---

## Vanilla JS Frontend

**URL:** https://docs.gptr.dev/docs/gpt-researcher/frontend/vanilla-js-frontend

**Contents:**
- Vanilla JS Frontend
  - Demo​
    - Prerequisites​
    - Setup and Running​

The VanillaJS frontend is a lightweight solution leveraging FastAPI to serve static files.

Install required packages:

Access at http://localhost:8000

**Examples:**

Example 1 (text):
```text
pip install -r requirements.txt
```

Example 2 (text):
```text
python -m uvicorn main:app
```

---

## React Package

**URL:** https://docs.gptr.dev/docs/gpt-researcher/frontend/react-package

**Contents:**
- React Package
- Installation​
- Usage​
- Publishing to a private npm registry​

The GPTR React package is an abstraction on top of the NextJS app meant to empower users to easily import the GPTR frontend into any React App. The package is available on npm.

If you'd like to build and publish the package into your own private npm registry, you can do so by running the following commands:

**Examples:**

Example 1 (bash):
```bash
npm install gpt-researcher-ui
```

Example 2 (javascript):
```javascript
import React from 'react';import { GPTResearcher } from 'gpt-researcher-ui';function App() {  return (    <div className="App">      <GPTResearcher         apiUrl="http://localhost:8000"        defaultPrompt="What is quantum computing?"        onResultsChange={(results) => console.log('Research results:', results)}      />    </div>  );}export default App;
```

Example 3 (bash):
```bash
cd frontend/nextjs/npm run build:libnpm run build:typesnpm publish
```

---

## Querying the Backend

**URL:** https://docs.gptr.dev/docs/gpt-researcher/gptr/querying-the-backend

**Contents:**
- Querying the Backend
- Introduction​

In this section, we will discuss how to query the GPTR backend server. The GPTR backend server is a Python server that runs the GPTR Python package. The server listens for WebSocket connections and processes incoming messages to generate reports, streaming back logs and results to the client.

An example WebSocket client is implemented in the gptr-webhook.js file below.

This function sends a Webhook Message to the GPTR Python backend running on localhost:8000, but this example can also be modified to query a GPTR Server hosted on Linux.

And here's how you can leverage this helper function:

**Examples:**

Example 1 (javascript):
```javascript
const WebSocket = require('ws');let socket = null;let responseCallback = null;async function initializeWebSocket() {  if (!socket) {    const host = 'localhost:8000';    const ws_uri = `ws://${host}/ws`;    socket = new WebSocket(ws_uri);    socket.onopen = () => {      console.log('WebSocket connection established');    };    socket.onmessage = (event) => {      const data = JSON.parse(event.data);      console.log('WebSocket data received:', data);      if (data.content === 'dev_team_result'           && data.output.rubber_ducker_thoughts != undefined          && data.output.tech_lead_review != undefined) {        if (responseCallback) {          responseCallback(data.output);          responseCallback = null; // Clear callback after use        }      } else {        console.log('Received data:', data);      }    };    socket.onclose = () => {      console.log('WebSocket connection closed');      socket = null;    };    socket.onerror = (error) => {      console.error('WebSocket error:', error);    };  }}async function sendWebhookMessage(message) {  return new Promise((resolve, reject) => {    if (!socket || socket.readyState !== WebSocket.OPEN) {      initializeWebSocket();    }    const data = {      task: message,      report_type: 'dev_team',      report_source: 'web',      tone: 'Objective',      headers: {},      repo_name: 'elishakay/gpt-researcher'    };    const payload = "start " + JSON.stringify(data);    responseCallback = (response) => {      resolve(response); // Resolve the promise with the WebSocket response    };    if (socket.readyState === WebSocket.OPEN) {      socket.send(payload);      console.log('Message sent:', payload);    } else {      socket.onopen = () => {        socket.send(payload);        console.log('Message sent after connection:', payload);      };    }  });}module.exports = {  sendWebhookMessage};
```

Example 2 (javascript):
```javascript
const { sendWebhookMessage } = require('./gptr-webhook');async function main() {  const message = 'How do I get started with GPT-Researcher Websockets?';  const response = await sendWebhookMessage(message);  console.log('Response:', response);}
```

---

## NextJS Frontend

**URL:** https://docs.gptr.dev/docs/gpt-researcher/frontend/nextjs-frontend

**Contents:**
- NextJS Frontend
    - Demo​
- NextJS Frontend App​
  - Run the NextJS React App with Docker​
- Running NextJS Frontend via CLI​
    - Prerequisites​
    - Setup and Running​
  - Adding Google Analytics​

This frontend project aims to enhance the user experience of GPT Researcher, providing an intuitive and efficient interface for automated research. It offers two deployment options to suit different needs and environments.

View an in-depth Product Tutorial here: GPT-Researcher Frontend Tutorial

The React app (located in the frontend directory) is our Frontend 2.0 which we hope will enable us to display the robustness of the backend on the frontend, as well.

It comes with loads of added features, such as:

Step 1 - Install Docker

Step 2 - Clone the '.env.example' file, add your API Keys to the cloned file and save the file as '.env'

Step 3 - Within the docker-compose file comment out services that you don't want to run with Docker.

If that doesn't work, try running it without the dash:

Step 4 - By default, if you haven't uncommented anything in your docker-compose file, this flow will start 2 processes:

Visit localhost:3000 on any browser and enjoy researching!

If, for some reason, you don't want to run the GPTR API Server on localhost:8000, no problem! You can set the NEXT_PUBLIC_GPTR_API_URL environment variable in your .env file to the URL of your GPTR API Server.

A more robust solution with enhanced features and performance.

Navigate to NextJS directory:

Install dependencies:

Start development server:

Access at http://localhost:3000

Note: Requires backend server on localhost:8000 as detailed in option 1.

To add Google Analytics to your NextJS frontend, simply add the following to your .env file:

**Examples:**

Example 1 (bash):
```bash
docker compose up --build
```

Example 2 (bash):
```bash
docker compose up --build
```

Example 3 (text):
```text
NEXT_PUBLIC_GPTR_API_URL=https://app.gptr.dev
```

Example 4 (text):
```text
NEXT_PUBLIC_GPTR_API_URL=http://localhost:7000
```

---

## Embed Script

**URL:** https://docs.gptr.dev/docs/gpt-researcher/frontend/embed-script

**Contents:**
- Embed Script

The embed script enables you to embed the latest GPTR NextJS app into your web app.

To achieve this, simply add these 2 script tags into your HTML:

Here's a minmalistic HTML example (P.S. You can also save this as an index.html file and open it with your Web Browser)

This example relies on setting a custom localstorage value for GPTR_API_URL. To point your embedded frontend at a custom GPTR API Server, feel free to edit http://localhost:8000 to your custom GPTR server address.

**Examples:**

Example 1 (javascript):
```javascript
<script>localStorage.setItem("GPTR_API_URL", "http://localhost:8000");</script><script src="https://app.gptr.dev/embed.js"></script>
```

Example 2 (html):
```html
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <title>GPT Researcher Embed Demo</title></head><body style="margin: 0; padding: 0;">    <!-- GPT Researcher Embed -->    <script>localStorage.setItem("GPTR_API_URL", "http://localhost:8000");</script>    <script src="https://app.gptr.dev/embed.js"></script></body></html>
```

---

## Testing your Retriever

**URL:** https://docs.gptr.dev/docs/gpt-researcher/search-engines/test-your-retriever

**Contents:**
- Testing your Retriever

To test your retriever, you can use the following code snippet. The script will search for a sub-query and display the search results.

The output of the search results will include the title, body, and href of each search result. For example:

**Examples:**

Example 1 (python):
```python
import asynciofrom dotenv import load_dotenvfrom gpt_researcher.config.config import Configfrom gpt_researcher.actions.retriever import get_retrieversfrom gpt_researcher.skills.researcher import ResearchConductorimport pprint# Load environment variables from .env fileload_dotenv()async def test_scrape_data_by_query():    # Initialize the Config object    config = Config()    # Retrieve the retrievers based on the current configuration    retrievers = get_retrievers({}, config)    print("Retrievers:", retrievers)    # Create a mock researcher object with necessary attributes    class MockResearcher:        def init(self):            self.retrievers = retrievers            self.cfg = config            self.verbose = True            self.websocket = None            self.scraper_manager = None  # Mock or implement scraper manager            self.vector_store = None  # Mock or implement vector store    researcher = MockResearcher()    research_conductor = ResearchConductor(researcher)    # print('research_conductor',dir(research_conductor))    # print('MockResearcher',dir(researcher))    # Define a sub-query to test    sub_query = "design patterns for autonomous ai agents"    # Iterate through all retrievers    for retriever_class in retrievers:        # Instantiate the retriever with the sub-query        retriever = retriever_class(sub_query)        # Perform the search using the current retriever        search_results = await asyncio.to_thread(            retriever.search, max_results=10        )        print("\033[35mSearch results:\033[0m")        pprint.pprint(search_results, indent=4, width=80)if __name__ == "__main__":    asyncio.run(test_scrape_data_by_query())
```

Example 2 (json):
```json
[{       "body": "Jun 5, 2024 ... Three AI Design Patterns of Autonomous "                "Agents. Overview of the Three Patterns. Three notable AI "                "design patterns for autonomous agents include:.",    "href": "https://accredianpublication.medium.com/building-smarter-systems-the-role-of-agentic-design-patterns-in-genai-13617492f5df",    "title": "Building Smarter Systems: The Role of Agentic Design "                "Patterns in ..."},    ...]
```

---

## Getting Started

**URL:** https://docs.gptr.dev/docs/gpt-researcher/getting-started

**Contents:**
- Getting Started
- Quickstart​
- Using Virtual Environment or Poetry​
  - Virtual Environment​
    - Establishing the Virtual Environment with Activate/Deactivate configuration​
    - Install the dependencies for a Virtual environment​
  - Poetry​
    - Establishing the Poetry dependencies and virtual environment with Poetry version ~1.7.1​
    - Activate the virtual environment associated with a Poetry project​
  - Run the app​

Step 0 - Install Python 3.11 or later. See here for a step-by-step guide.

Step 1 - Download the project and navigate to its directory

Step 3 - Set up API keys using two methods: exporting them directly or storing them in a .env file.

For Linux/Temporary Windows Setup, use the export method:

For a more permanent setup, create a .env file in the current gpt-researcher directory and input the env vars (without export).

Step 1 - Install dependencies

Step 2 - Run the agent with FastAPI

Step 3 - Go to http://localhost:8000 on any browser and enjoy researching!

Select either based on your familiarity with each:

Create a virtual environment using the venv package with the environment name <your_name>, for example, env. Execute the following command in the PowerShell/CMD terminal:

To activate the virtual environment, use the following activation script in PowerShell/CMD terminal:

To deactivate the virtual environment, run the following deactivation script in PowerShell/CMD terminal:

After activating the env environment, install dependencies using the requirements.txt file with the following command:

Install project dependencies and simultaneously create a virtual environment for the specified project. By executing this command, Poetry reads the project's "pyproject.toml" file to determine the required dependencies and their versions, ensuring a consistent and isolated development environment. The virtual environment allows for a clean separation of project-specific dependencies, preventing conflicts with system-wide packages and enabling more straightforward dependency management throughout the project's lifecycle.

By running this command, the user enters a shell session within the isolated environment associated with the project, providing a dedicated space for development and execution. This virtual environment ensures that the project dependencies are encapsulated, avoiding conflicts with system-wide packages. Activating the Poetry shell is essential for seamlessly working on a project, as it ensures that the correct versions of dependencies are used and provides a controlled environment conducive to efficient development and testing.

Launch the FastAPI application agent on a Virtual Environment or Poetry setup by executing the following command:

Visit http://localhost:8000 in any web browser and explore your research!

**Examples:**

Example 1 (bash):
```bash
$ git clone https://github.com/assafelovic/gpt-researcher.git$ cd gpt-researcher
```

Example 2 (bash):
```bash
export OPENAI_API_KEY={Your OpenAI API Key here}export TAVILY_API_KEY={Your Tavily API Key here}
```

Example 3 (bash):
```bash
$ pip install -r requirements.txt
```

Example 4 (bash):
```bash
$ uvicorn main:app --reload
```

---

## How to Choose

**URL:** https://docs.gptr.dev/docs/gpt-researcher/getting-started/how-to-choose

**Contents:**
- How to Choose
- Options​
- Usage Options​
  - 1. PIP Package​
  - 2. End-to-End Application​
  - 3. Multi Agent System with LangGraph​
- Comparison Table​
- Deep Dive​
- Versioning and Updates​
- Troubleshooting and FAQs​

GPT Researcher is a powerful autonomous research agent designed to enhance and streamline your research processes. Whether you're a developer looking to integrate research capabilities into your project or an end-user seeking a comprehensive research solution, GPT Researcher offers flexible options to meet your needs.

We envision a future where AI agents collaborate to complete complex tasks, with research being a critical step in the process. GPT Researcher aims to be your go-to agent for any research task, regardless of complexity. It can be easily integrated into existing agent workflows, eliminating the need to create your own research agent from scratch.

GPT Researcher offers multiple ways to leverage its capabilities:

The PIP package is ideal for leveraging GPT Researcher as an agent in your preferred environment and code.

Learn More: PIP Documentation

For a complete out-of-the-box experience, including a sleek frontend, you can clone our repository.

Advanced Usage Example: Detailed Report Implementation

We've collaborated with LangChain to support multi-agents with LangGraph and GPT Researcher, offering the most complex and comprehensive version of GPT Researcher.

This version is recommended for local, experimental, and educational use. We're working on providing a lighter version soon!

Learn More: GPT Researcher x LangGraph

Please note that all options have been optimized and refined for production use.

To learn more about each of the options, check out these docs and code snippets:

End-to-End Application:

GPT Researcher is actively maintained and updated. To ensure you're using the latest version:

For common issues and questions, please refer to our FAQ section in the documentation.

**Examples:**

Example 1 (text):
```text
pip install gpt-researcher
```

---

## Vector Stores

**URL:** https://docs.gptr.dev/docs/gpt-researcher/context/vector-stores

**Contents:**
- Vector Stores
- Faiss​
- PGVector​
- Adding Scraped Data to your vector store​

The GPT Researcher package allows you to integrate with existing langchain vector stores that have been populated. For a complete list of supported langchain vector stores, please refer to this link.

You can create a set of embeddings and langchain documents and store them in any supported vector store of your choosing. GPT-Researcher will work with any langchain vector store that implements the asimilarity_search method.

If you want to use the existing knowledge in your vector store, make sure to set report_source="langchain_vectorstore". Any other settings will add additional information from scraped data and might contaminate your vectordb (See How to add scraped data to your vector store for more context)

In some cases in which you want to store the scraped data and documents into your own vector store for future usages, GPT-Researcher also allows you to do so seamlessly just by inputting your vector store (make sure to set report_source value to something other than langchain_vectorstore)

**Examples:**

Example 1 (python):
```python
from gpt_researcher import GPTResearcherfrom langchain.text_splitter import CharacterTextSplitterfrom langchain_openai import OpenAIEmbeddingsfrom langchain_community.vectorstores import FAISSfrom langchain_core.documents import Document# exerpt taken from - https://paulgraham.com/wealth.htmlessay = """May 2004(This essay was originally published in Hackers & Painters.)If you wanted to get rich, how would you do it? I think your best bet would be to start or join a startup.That's been a reliable way to get rich for hundreds of years. The word "startup" dates from the 1960s,but what happens in one is very similar to the venture-backed trading voyages of the Middle Ages.Startups usually involve technology, so much so that the phrase "high-tech startup" is almost redundant.A startup is a small company that takes on a hard technical problem.Lots of people get rich knowing nothing more than that. You don't have to know physics to be a good pitcher.But I think it could give you an edge to understand the underlying principles. Why do startups have to be small?Will a startup inevitably stop being a startup as it grows larger?And why do they so often work on developing new technology? Why are there so many startups selling new drugs or computer software,and none selling corn oil or laundry detergent?The PropositionEconomically, you can think of a startup as a way to compress your whole working life into a few years.Instead of working at a low intensity for forty years, you work as hard as you possibly can for four.This pays especially well in technology, where you earn a premium for working fast.Here is a brief sketch of the economic proposition. If you're a good hacker in your mid twenties,you can get a job paying about $80,000 per year. So on average such a hacker must be able to do atleast $80,000 worth of work per year for the company just to break even. You could probably work twiceas many hours as a corporate employee, and if you focus you can probably get three times as much done in an hour.[1]You should get another multiple of two, at least, by eliminating the drag of the pointy-haired middle manager whowould be your boss in a big company. Then there is one more multiple: how much smarter are you than your jobdescription expects you to be? Suppose another multiple of three. Combine all these multipliers,and I'm claiming you could be 36 times more productive than you're expected to be in a random corporate job.[2]If a fairly good hacker is worth $80,000 a year at a big company, then a smart hacker working very hard without any corporate bullshit to slow him down should be able to do work worth about $3 million a year.........."""document = [Document(page_content=essay)]text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=30, separator="\n")docs = text_splitter.split_documents(documents=document)vector_store = FAISS.from_documents(documents, OpenAIEmbeddings())query = """    Summarize the essay into 3 or 4 succinct sections.    Make sure to include key points regarding wealth creation.    Include some recommendations for entrepreneurs in the conclusion."""# Create an instance of GPTResearcherresearcher = GPTResearcher(    query=query,    report_type="research_report",    report_source="langchain_vectorstore",    vector_store=vector_store,)# Conduct research and write the reportawait researcher.conduct_research()report = await researcher.write_report()
```

Example 2 (python):
```python
from gpt_researcher import GPTResearcherfrom langchain_postgres.vectorstores import PGVectorfrom langchain_openai import OpenAIEmbeddingsCONNECTION_STRING = 'postgresql://someuser:somepass@localhost:5432/somedatabase'# assuming the vector store exists and contains the relevent documents# also assuming embeddings have been or will be generatedvector_store = PGVector.from_existing_index(    use_jsonb=True,    embedding=OpenAIEmbeddings(),    collection_name='some collection name',    connection=CONNECTION_STRING,    async_mode=True,)query = """    Create a short report about apples.    Include a section about which apples are considered best    during each season."""# Create an instance of GPTResearcherresearcher = GPTResearcher(    query=query,    report_type="research_report",    report_source="langchain_vectorstore",    vector_store=vector_store, )# Conduct research and write the reportawait researcher.conduct_research()report = await researcher.write_report()
```

Example 3 (python):
```python
from gpt_researcher import GPTResearcherfrom langchain_community.vectorstores import InMemoryVectorStorefrom langchain_openai import OpenAIEmbeddingsvector_store = InMemoryVectorStore(embedding=OpenAIEmbeddings())query = "The best LLM"# Create an instance of GPTResearcherresearcher = GPTResearcher(    query=query,    report_type="research_report",    report_source="web",    vector_store=vector_store, )# Conduct research, the context will be chunked and stored in the vector_storeawait researcher.conduct_research()# Query the 5 most relevant context in our vector storerelated_contexts = await vector_store.asimilarity_search("GPT-4", k = 5) print(related_contexts)print(len(related_contexts)) #Should be 5
```

---

## Azure Storage

**URL:** https://docs.gptr.dev/docs/gpt-researcher/context/azure-storage

**Contents:**
- Azure Storage

If you want to use Azure Blob Storage as the source for your GPT Researcher report context, follow these steps:

Step 1 - Set these environment variables with a .env file in the root folder

Step 2 - Add the azure-storage-blob dependency to your requirements.txt file

Step 3 - When running the GPTResearcher class, pass the report_source as azure

**Examples:**

Example 1 (bash):
```bash
AZURE_CONNECTION_STRING=AZURE_CONTAINER_NAME=
```

Example 2 (bash):
```bash
azure-storage-blob
```

Example 3 (python):
```python
report = GPTResearcher(    query="What happened in the latest burning man floods?",    report_type="research_report",    report_source="azure",)
```

---

## Running with Azure

**URL:** https://docs.gptr.dev/docs/gpt-researcher/llms/running-with-azure

**Contents:**
- Running with Azure
- Example: Azure OpenAI Configuration​

If you are not using OpenAI's models, but other model providers, besides the general configuration above, also additional environment variables are required.

Here is an example for Azure OpenAI configuration:

For more details on what each variable does, you can check out the GPTR Config Docs

**Examples:**

Example 1 (bash):
```bash
OPENAI_API_VERSION="2024-05-01-preview" # or whatever you are usingAZURE_OPENAI_ENDPOINT="https://CHANGEMEN.openai.azure.com/" # change to the name of your deploymentAZURE_OPENAI_API_KEY="[Your Key]" # change to your API keyEMBEDDING="azure_openai:text-embedding-ada-002" # change to the deployment of your embedding modelFAST_LLM="azure_openai:gpt-4o-mini" # change to the name of your deployment (not model-name)FAST_TOKEN_LIMIT=4000SMART_LLM="azure_openai:gpt-4o" # change to the name of your deployment (not model-name)SMART_TOKEN_LIMIT=4000RETRIEVER="bing" # if you are using Bing as your search engine (which is likely if you use Azure)BING_API_KEY="[Your Key]"
```

---

## Configuration

**URL:** https://docs.gptr.dev/docs/gpt-researcher/gptr/config

**Contents:**
- Configuration
- Deep Research Configuration​

The config.py enables you to customize GPT Researcher to your specific needs and preferences.

Thanks to our amazing community and contributions, GPT Researcher supports multiple LLMs and Retrievers. In addition, GPT Researcher can be tailored to various report formats (such as APA), word count, research iterations depth, etc.

GPT Researcher defaults to our recommended suite of integrations: OpenAI for LLM calls and Tavily API for retrieving real-time web information.

As seen below, OpenAI still stands as the superior LLM. We assume it will stay this way for some time, and that prices will only continue to decrease, while performance and speed increase over time.

The default config.py file can be found in /gpt_researcher/config/. It supports various options for customizing GPT Researcher to your needs. You can also include your own external JSON file config.json by adding the path in the config_file param. Please follow the config.py file for additional future support.

Below is a list of current supported options:

The deep research parameters allow you to fine-tune how GPT Researcher explores complex topics that require extensive knowledge gathering. These parameters work together to determine the thoroughness and efficiency of the research process:

DEEP_RESEARCH_BREADTH: Controls how many parallel research paths are explored simultaneously. A higher value (e.g., 5) causes the researcher to investigate more diverse subtopics at each step, resulting in broader coverage but potentially less focus on core themes. The default value of 3 provides a balanced approach between breadth and depth.

DEEP_RESEARCH_DEPTH: Determines how many sequential search iterations GPT Researcher performs for each research path. A higher value (e.g., 3-4) allows for following citation trails and diving deeper into specialized information, but increases research time substantially. The default value of 2 ensures reasonable depth while maintaining practical completion times.

DEEP_RESEARCH_CONCURRENCY: Sets how many concurrent operations can run during deep research. Higher values speed up the research process on capable systems but may increase API rate limit issues or resource consumption. The default value of 4 is suitable for most environments, but can be increased on systems with more resources or decreased if you experience performance issues.

For academic or highly specialized research, consider increasing both breadth and depth (e.g., BREADTH=4, DEPTH=3). For quick exploratory research, lower values (e.g., BREADTH=2, DEPTH=1) will provide faster results with less detail.

To change the default configurations, you can simply add env variables to your .env file as named above or export manually in your local project directory.

For example, to manually change the search engine and report format:

Please note that you might need to export additional env vars and obtain API keys for other supported search retrievers and LLM providers. Please follow your console logs for further assistance. To learn more about additional LLM support you can check out the docs here.

You can also include your own external JSON file config.json by adding the path in the config_file param.

**Examples:**

Example 1 (bash):
```bash
export RETRIEVER=bingexport REPORT_FORMAT=IEEE
```

---

## Scraping Options

**URL:** https://docs.gptr.dev/docs/gpt-researcher/gptr/scraping

**Contents:**
- Scraping Options
- Configuring Scraping Method​
- Scraping Methods Explained​
  - BeautifulSoup (Static Scraping)​
  - Selenium (Browser Scraping)​
  - NoDriver (Browser Scraping)​
  - Tavily Extract (Recommended for Production)​
  - FireCrawl (Recommended for Production)​
- Additional Setup for Selenium​
- Choosing the Right Method​

GPT Researcher now offers various methods for web scraping: static scraping with BeautifulSoup, dynamic scraping with Selenium, and High scale scraping with Tavily Extract. This document explains how to switch between these methods and the benefits of each approach.

You can choose your preferred scraping method by setting the SCRAPER environment variable:

For BeautifulSoup (static scraping):

For dynamic browser scraping, either with Selenium:

Or with NoDriver (ZenDriver):

For production use cases, you can set the Scraper to tavily_extract or firecrawl. Tavily allows you to scrape sites at scale without the hassle of setting up proxies, managing cookies, or dealing with CAPTCHAs. Please note that you need to have a Tavily account and API key to use this option. To learn more about Tavily Extract see here. Make sure to first install the pip package tavily-python. Then:

FireCrawl is also allows you to scrape sites at scale. FireCrawl also provides open source code to self hosted server which provided better scrape quality compared to BeautifulSoup by passing markdown version of the scraped sites to LLMs. You will needs to have FireCrawl account (official service) to get API key or you needs self host URL and API key (if you set for your self host server) to use this option. Make sure to install the pip package firecrawl-py. Then:

Note: If not set, GPT Researcher will default to BeautifulSoup for scraping.

When SCRAPER="bs", GPT Researcher uses BeautifulSoup for static scraping. This method:

When SCRAPER="browser", GPT Researcher uses Selenium for dynamic scraping. This method:

Alternative to Selenium for potentially better performance.

When SCRAPER="tavily_extract", GPT Researcher uses Tavily's Extract API for web scraping. This method:

Usage Considerations:

When SCRAPER="firecrawl", GPT Researcher uses FireCrawl Scrape API for web scraping in markdown format. This method:

Setup (official service by FireCrawl):

Setup (with self-hosted server):

Note: FIRECRAWL_API_KEY can be empty if you not setup authentication for your self host server (FIRECRAWL_API_KEY=""). There will be some difference between their cloud service and open source service. To understand differences between FireCrawl option read here.

Usage Considerations:

If you choose to use Selenium (SCRAPER="browser"), you'll need to:

Install the Selenium package:

Download the appropriate WebDriver for your browser:

Ensure the WebDriver is in your system's PATH.

Use BeautifulSoup (static) for:

Use Selenium (dynamic) for:

Remember, the choice between static and dynamic scraping can significantly impact the quality and completeness of the data GPT Researcher can gather. Choose the method that best suits your research needs and the websites you're targeting.

**Examples:**

Example 1 (text):
```text
export SCRAPER="bs"
```

Example 2 (text):
```text
export SCRAPER="browser"
```

Example 3 (text):
```text
export SCRAPER="nodriver"pip install zendriver
```

Example 4 (text):
```text
export SCRAPER="tavily_extract"
```

---
