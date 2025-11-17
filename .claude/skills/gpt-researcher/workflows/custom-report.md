---
description: Custom report workflow - Lucy generates reports in specific formats using custom prompts
globs: ""
alwaysApply: false
---

# 📝 CUSTOM REPORT WORKFLOW

**YOU (Lucy) are reading this because the user needs a specific report format.**

## 🎯 WHEN TO USE

**User requests:**
- "Executive summary"
- "Bullet points"
- "APA format"
- "Technical analysis"
- "2-paragraph summary"
- Any specific format requirement

## 📋 WORKFLOW

### Step 1: Conduct Research

```python
from gpt_researcher import GPTResearcher

researcher = GPTResearcher(
    query="[User's query]",
    report_type="custom_report",  # or "research_report"
    verbose=True
)

await researcher.conduct_research()
```

### Step 2: Generate with Custom Prompt

**Concise Summary:**
```python
custom_prompt = "Provide a concise 2-paragraph summary without citations."
report = await researcher.write_report(custom_prompt=custom_prompt)
```

**Executive Brief:**
```python
custom_prompt = """
Create executive brief with:
1. Executive Summary (2-3 sentences)
2. Key Findings (3-5 bullet points)
3. Strategic Implications (brief paragraph)
4. Recommended Actions (numbered list)
Keep under 500 words. Use professional business language.
"""
report = await researcher.write_report(custom_prompt=custom_prompt)
```

**Bullet Points:**
```python
custom_prompt = "List the top 5 key findings as bullet points with brief explanations for each."
report = await researcher.write_report(custom_prompt=custom_prompt)
```

**Technical Analysis:**
```python
custom_prompt = """
Write detailed technical analysis including:
- Methodology explanation
- Data sources and reliability assessment
- Detailed findings with supporting evidence
- Technical conclusions
- Full citations in APA format
Use technical terminology. Assume expert audience.
"""
report = await researcher.write_report(custom_prompt=custom_prompt)
```

**Comparison Report:**
```python
custom_prompt = """
Create comparison report with:
1. Overview of items being compared
2. Side-by-side comparison table
3. Pros and cons for each option
4. Recommendation based on findings
Use clear, objective language. Cite sources.
"""
report = await researcher.write_report(custom_prompt=custom_prompt)
```

## 🎯 COMMON FORMATS

| Format | Custom Prompt Template |
|--------|------------------------|
| Executive Summary | "2-3 sentence summary for executives" |
| Bullet Points | "Top 5 findings as bullets" |
| APA Format | "Detailed report in APA format with full citations" |
| MLA Format | "Research report in MLA format" |
| Technical | "Technical analysis for expert audience" |
| Non-technical | "Explain for non-technical audience" |
| Comparison | "Side-by-side comparison with pros/cons" |
| Decision Brief | "Decision brief with recommendation" |

## 🎯 COMPLETE EXAMPLE

```python
from gpt_researcher import GPTResearcher
import asyncio

async def custom_format_research(query: str, format_type: str) -> str:
    """Research with custom output format."""

    formats = {
        "executive": "Create 500-word executive brief with summary, findings, implications, actions.",
        "bullets": "List top 5 findings as bullet points.",
        "technical": "Technical analysis with methodology, sources, findings, conclusions, APA citations.",
        "simple": "2-paragraph summary without citations for general audience."
    }

    researcher = GPTResearcher(query=query, report_type="research_report", verbose=True)
    await researcher.conduct_research()

    custom_prompt = formats.get(format_type, formats["simple"])
    report = await researcher.write_report(custom_prompt=custom_prompt)

    print(f"=" * 80)
    print(f"{format_type.upper()} FORMAT REPORT")
    print("=" * 80)
    print(report)

    return report

# Execute
if __name__ == "__main__":
    query = input("Research query: ")
    format_type = input("Format (executive/bullets/technical/simple): ")
    report = asyncio.run(custom_format_research(query, format_type))
```

---

**END OF WORKFLOW**
