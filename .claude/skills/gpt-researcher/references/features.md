# Gpt-Researcher - Features

**Pages:** 1

---

## Detailed Report

**URL:** https://docs.gptr.dev/docs/examples/detailed_report

**Contents:**
- Detailed Report
- Overview​
- Key Features​
- Class Structure​
  - Initialization​
- How It Works​
- Usage Example​
- Conclusion​

The DetailedReport class inspired by the recent STORM paper, is a powerful component of GPT Researcher, designed to generate comprehensive reports on complex topics. It's particularly useful for creating long-form content that exceeds the typical limits of LLM outputs. This class orchestrates the research process, breaking down the main query into subtopics, conducting in-depth research on each, and combining the results into a cohesive, detailed report.

Located in backend/report_types/detailed_report.py in the GPT Researcher GitHub repository, this class leverages the capabilities of the GPTResearcher agent to perform targeted research and generate content.

The DetailedReport class is initialized with the following parameters:

Here's how you can use the DetailedReport class in your project:

This example demonstrates how to create a DetailedReport instance and run it to generate a comprehensive report on the impact of AI on healthcare.

The DetailedReport class is a sophisticated tool for generating in-depth, well-structured reports on complex topics. By breaking down the main query into subtopics and leveraging the power of GPT Researcher, it can produce content that goes beyond the typical limitations of LLM outputs. This makes it an invaluable asset for researchers, content creators, and anyone needing detailed, well-researched information on a given topic.

**Examples:**

Example 1 (python):
```python
import asynciofrom fastapi import WebSocketfrom gpt_researcher.utils.enum import Tonefrom backend.report_type import DetailedReportasync def generate_report(websocket: WebSocket):    detailed_report = DetailedReport(        query="The impact of artificial intelligence on modern healthcare",        report_type="research_report",        report_source="web_search",        source_urls=[],  # You can provide initial source URLs if available        config_path="path/to/config.yaml",        tone=Tone.FORMAL,        websocket=websocket,        subtopics=[],  # You can provide predefined subtopics if desired        headers={}  # Add any necessary HTTP headers    )    final_report = await detailed_report.run()    return final_report# In your FastAPI app@app.websocket("/generate_report")async def websocket_endpoint(websocket: WebSocket):    await websocket.accept()    report = await generate_report(websocket)    await websocket.send_text(report)
```

---
