# Gpt-Researcher - Examples

**Pages:** 1

---

## Simple Run

**URL:** https://docs.gptr.dev/docs/examples

**Contents:**
- Simple Run
  - Run PIP Package​

**Examples:**

Example 1 (python):
```python
from gpt_researcher import GPTResearcher
import asyncio

### Using Quick Run
async def main():
    """
    This is a sample script that shows how to run a research report.
    """
    # Query
    query = "What happened in the latest burning man floods?"
    # Report Type
    report_type = "research_report"
    # Initialize the researcher
    researcher = GPTResearcher(query=query, report_type=report_type, config_path=None)
    # Conduct research on the given query
    await researcher.conduct_research()
    # Write the report
    report = await researcher.write_report()

    return report

if __name__ == "__main__":
    asyncio.run(main())
```

## Custom Report Formatting

### Using Custom Prompts

```python
from gpt_researcher import GPTResearcher
import asyncio

async def main():
    """
    This example shows how to use custom prompts to control report formatting.
    """
    # Query
    query = "What are the latest advancements in renewable energy?"
    # Report Type
    report_type = "research_report"
    # Initialize the researcher
    researcher = GPTResearcher(query=query, report_type=report_type)

    # Conduct research on the given query
    await researcher.conduct_research()

    # Generate a standard report
    standard_report = await researcher.write_report()
    print("Standard Report Generated")

    # Generate a short, concise report using custom_prompt
    custom_prompt = "Provide a concise summary in 2 paragraphs without citations."
    short_report = await researcher.write_report(custom_prompt=custom_prompt)
    print("Short Report Generated")

    # Generate a bullet-point format report
    bullet_prompt = "List the top 5 advancements as bullet points with brief explanations."
    bullet_report = await researcher.write_report(custom_prompt=bullet_prompt)
    print("Bullet-Point Report Generated")

    return standard_report, short_report, bullet_report

if __name__ == "__main__":
    asyncio.run(main())
```

For more comprehensive examples of using custom prompts, see the `custom_prompt.py` file included in the examples directory.

---

## Detailed Report

**URL:** https://docs.gptr.dev/docs/examples/detailed_report

**Overview:**
The `DetailedReport` class generates comprehensive reports on complex topics by breaking them into manageable sections and conducting focused research on each area.

### Key Components

**Main Parameters:**
- `query`: The primary research topic
- `report_type`: Specifies the report format
- `report_source`: Indicates where data originates
- `source_urls`: Initial reference URLs
- `config_path`: Configuration file location
- `tone`: Report voice (using Tone enum)
- `websocket`: Real-time communication channel
- `subtopics`: Optional predefined sections
- `headers`: HTTP request headers

### Operational Process

The DetailedReport system follows this workflow:

1. Conducts initial research on the main query
2. Decomposes the topic into focused subtopics
3. For each subtopic:
   - Performs targeted research
   - Creates draft section headings
   - Retrieves existing content to prevent duplication
   - Generates the section content
4. Assembles final report with table of contents and citations

### Implementation Code

```python
import asyncio
from fastapi import WebSocket
from gpt_researcher.utils.enum import Tone
from backend.report_type import DetailedReport

async def generate_report(websocket: WebSocket):
    detailed_report = DetailedReport(
        query="The impact of artificial intelligence on modern healthcare",
        report_type="research_report",
        report_source="web_search",
        source_urls=[],
        config_path="path/to/config.yaml",
        tone=Tone.FORMAL,
        websocket=websocket,
        subtopics=[],
        headers={}
    )
    final_report = await detailed_report.run()
    return final_report

@app.websocket("/generate_report")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    report = await generate_report(websocket)
    await websocket.send_text(report)
```

**Key Features:**
- Breaks down complex topics into manageable subtopics
- Conducts focused research on each section
- Prevents content duplication across sections
- Generates table of contents automatically
- Includes proper citations and references
- Supports real-time progress updates via WebSocket
- Customizable tone and formatting

**Use Cases:**
- Academic research papers
- Business intelligence reports
- Market analysis documents
- Technical documentation
- Industry trend reports

---

## Hybrid Research

**URL:** https://docs.gptr.dev/docs/examples/hybrid_research

**Overview:**
Hybrid research combines web search capabilities with local or online document analysis to provide comprehensive, context-aware research results. This approach enables you to blend external web knowledge with your internal documents or specific online sources.

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- OpenAI API key (or other supported LLM providers)
- Tavily API key (or other supported retrievers)

### Installation

```bash
pip install gpt-researcher
```

### Environment Configuration

Set your API credentials as environment variables:

```bash
export OPENAI_API_KEY=your_openai_api_key_here
export TAVILY_API_KEY=your_tavily_api_key_here
```

Or configure within your Python script:

```python
import os
os.environ['OPENAI_API_KEY'] = 'your_openai_api_key_here'
os.environ['TAVILY_API_KEY'] = 'your_tavily_api_key_here'
```

### Document Preparation

**1. Local Documents:**
- Create a directory named `my-docs` in your project folder
- Place all relevant local documents (PDFs, TXTs, DOCXs, etc.) in this directory
- Set the `DOC_PATH` environment variable (optional - defaults to `./my-docs`)

**2. Online Documents:**
- Prepare URLs to online documents
- Supported formats: PDFs, TXTs, DOCXs, and more
- Example: `https://example.com/document.pdf`

### Implementation Examples

#### Hybrid Research with Local Documents

```python
from gpt_researcher import GPTResearcher
import asyncio

async def get_research_report(query: str, report_type: str, report_source: str) -> str:
    researcher = GPTResearcher(
        query=query,
        report_type=report_type,
        report_source=report_source  # Set to "hybrid"
    )
    research = await researcher.conduct_research()
    report = await researcher.write_report()
    return report

if __name__ == "__main__":
    query = "How does our product roadmap compare to emerging market trends in our industry?"
    report_source = "hybrid"  # Combines web search + local documents

    report = asyncio.run(get_research_report(
        query=query,
        report_type="research_report",
        report_source=report_source
    ))
    print(report)
```

#### Hybrid Research with Online Documents

```python
from gpt_researcher import GPTResearcher
import asyncio

async def get_research_report(query: str, report_type: str, report_source: str, document_urls: list) -> str:
    researcher = GPTResearcher(
        query=query,
        report_type=report_type,
        document_urls=document_urls,  # Provide online document URLs
        report_source=report_source
    )
    research = await researcher.conduct_research()
    report = await researcher.write_report()
    return report

if __name__ == "__main__":
    query = "How does our product roadmap compare to emerging market trends in our industry?"
    report_source = "hybrid"
    document_urls = [
        "https://example.com/product-roadmap.pdf",
        "https://example.com/market-analysis.doc"
    ]

    report = asyncio.run(get_research_report(
        query=query,
        report_type="research_report",
        document_urls=document_urls,
        report_source=report_source
    ))
    print(report)
```

### Running the Script

1. Save your script as `run_research.py`
2. Execute it with:

```bash
python run_research.py
```

### Understanding the Results

The hybrid research output will be a comprehensive report that combines insights from both web sources and your documents. The report typically includes:

- **Executive Summary** - High-level overview of findings
- **Key Findings** - Main insights from both sources
- **Detailed Analysis** - In-depth examination of the topic
- **Comparisons** - How your internal data relates to external trends
- **Recommendations** - Actionable insights based on combined research
- **Citations** - References to both web and document sources

### Key Features

**Privacy & Security:**
- Local documents are processed on your machine
- Only synthesized information (not raw data) is sent to external services
- Full control over which documents are analyzed

**Intelligent Reconciliation:**
- Handles conflicting information between local and web sources
- Provides context and notes discrepancies
- Prioritizes more recent or authoritative sources

**Performance:**
- Typical research duration: 1-5 minutes
- Duration varies based on query complexity and document volume
- Concurrent processing of web and document sources

### Troubleshooting

**API Key Issues:**
- Ensure API keys are correctly set and have necessary permissions
- Verify keys are active and not rate-limited

**Document Loading Errors:**
- Check that local documents are in supported formats
- Verify documents are not corrupted or password-protected
- Ensure file paths are correct

**Memory Issues:**
- For large documents, increase system memory allocation
- Consider processing fewer documents at once
- Adjust chunk size for document processing if needed

### FAQ

**Q: How long does a typical hybrid research session take?**
A: Duration ranges from 1-5 minutes depending on query complexity and document volume. Very comprehensive research may take longer.

**Q: Can I use GPT Researcher with other language models?**
A: Yes! GPT Researcher supports multiple LLM providers including Anthropic, Azure OpenAI, Ollama, Groq, and more. See the LLM configuration documentation.

**Q: How does GPT Researcher handle conflicting information?**
A: The system reconciles differences by providing context and noting discrepancies. It prioritizes more recent or authoritative sources when conflicts arise.

**Q: Is my local data sent to external servers?**
A: No! Local documents are processed on your machine. Only synthesized information and generated queries (not raw document data) are sent to external services for web research.

**Q: What document formats are supported?**
A: Supported formats include PDF, TXT, DOCX, CSV, Excel, Markdown, PowerPoint, and more.

**Report Source Options:**
- `"web"` - Web search only
- `"local"` - Local documents only
- `"hybrid"` - Combines both (recommended for comprehensive research)

---
