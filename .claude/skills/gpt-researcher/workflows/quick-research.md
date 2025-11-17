---
description: Quick web-only research workflow - Lucy executes standard GPTResearcher research for fast results
globs: ""
alwaysApply: false
---

# 🔬 QUICK RESEARCH WORKFLOW

**YOU (Lucy) are reading this because the user requested quick web research.**

This workflow provides step-by-step instructions for executing standard GPT Researcher web-only research to generate comprehensive reports quickly.

## 🎯 YOUR MISSION

Execute GPT Researcher in standard mode to deliver:
- Comprehensive research report (1000-1500 words)
- 20+ aggregated sources
- Full citations
- Completion time: 1-3 minutes
- Cost: $0.05-$0.15

## ⚡ WHEN TO USE THIS WORKFLOW

**User says:**
- "Research [topic]"
- "Quick research on [topic]"
- "Find information about [topic]"
- "What can you tell me about [topic]"
- "Do research on [topic]"
- General research requests without specific format requirements

**NOT for:**
- Deep comprehensive analysis → use `deep-research.md`
- Local document analysis → use `hybrid-research.md`
- Custom formats → use `custom-report.md`

## 📋 WORKFLOW STEPS

### Step 1: Environment Check

**Verify API keys are set:**
```python
import os

required_keys = ["OPENAI_API_KEY", "TAVILY_API_KEY"]
missing = [k for k in required_keys if not os.getenv(k)]

if missing:
    # Inform user about missing keys
    print(f"❌ Missing API keys: {', '.join(missing)}")
    print("Please set these environment variables before proceeding.")
    # STOP - cannot proceed without keys
```

### Step 2: Initialize Researcher

**Create GPTResearcher instance with standard configuration:**
```python
from gpt_researcher import GPTResearcher
import asyncio

# Extract query from user request
query = "[User's research question]"

# Initialize with defaults
researcher = GPTResearcher(
    query=query,
    report_type="research_report",  # Standard comprehensive report
    report_source="web",            # Web-only (no local docs)
    config_path=None,               # Use defaults
    verbose=True                    # Show progress to user
)
```

**Parameter Rationale:**
- `report_type="research_report"` → Balanced depth and breadth
- `report_source="web"` → Fast, no document processing overhead
- `verbose=True` → User sees research progress in real-time

### Step 3: Conduct Research

**Execute research phase:**
```python
print("🔍 Conducting research...")
print("   - Generating sub-queries")
print("   - Searching multiple sources")
print("   - Aggregating findings\n")

await researcher.conduct_research()
```

**What happens internally:**
1. Query decomposition into 3-5 sub-queries
2. Parallel web searches across retriever(s)
3. Source scraping and content extraction
4. Context aggregation from 20+ sources
5. Relevance filtering and ranking

**Expected duration:** 1-2 minutes

### Step 4: Generate Report

**Write comprehensive report:**
```python
print("✍️  Writing comprehensive report...\n")

report = await researcher.write_report()
```

**Report includes:**
- Executive summary
- Organized sections
- Key findings
- Supporting evidence
- Full citations
- References section

**Expected duration:** 30-60 seconds

### Step 5: Display Results

**Show report to user:**
```python
print("=" * 80)
print("RESEARCH REPORT")
print("=" * 80)
print(report)
print("\n" + "=" * 80)

# Optional: Show cost
try:
    cost = researcher.get_costs()
    print(f"💰 Research cost: ${cost:.4f}")
except:
    pass

print("=" * 80)
```

### Step 6: Save Report (Optional)

**Save to file if useful:**
```python
# Save as markdown
output_file = f"research_{query[:30].replace(' ', '_')}.md"
with open(output_file, "w") as f:
    f.write(f"# Research Report\n\n")
    f.write(f"**Query:** {query}\n\n")
    f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
    f.write("---\n\n")
    f.write(report)

print(f"\n✅ Report saved to: {output_file}")
```

## 🔧 CONFIGURATION ADJUSTMENTS

### For Faster Results (Trade Quality)

```python
researcher = GPTResearcher(
    query=query,
    report_type="research_report",
    report_source="web",
    verbose=True
)

# Adjust via environment variables BEFORE initialization
os.environ['MAX_ITERATIONS'] = '2'          # Reduce from 3
os.environ['MAX_SEARCH_RESULTS'] = '5'      # Reduce from 10
os.environ['TOTAL_WORDS'] = '800'           # Shorter report
os.environ['FAST_LLM'] = 'openai:gpt-4o-mini'
os.environ['SMART_LLM'] = 'openai:gpt-4o-mini'
```

**Impact:** ~40% faster, $0.03-$0.08 cost, slightly less comprehensive

### For Better Quality (Trade Speed)

```python
os.environ['MAX_ITERATIONS'] = '4'          # Increase from 3
os.environ['MAX_SEARCH_RESULTS'] = '15'     # Increase from 10
os.environ['TOTAL_WORDS'] = '2000'          # Longer report
os.environ['SMART_LLM'] = 'anthropic:claude-3-opus-20240229'
```

**Impact:** ~50% slower, $0.20-$0.30 cost, more comprehensive

## ⚠️ ERROR HANDLING

### Common Errors & Solutions

**Error: "No retriever specified"**
```python
# Solution: Ensure default retriever is set
os.environ['RETRIEVER'] = 'tavily'
```

**Error: Rate limiting (429)**
```python
# Solution: Switch to cheaper model or add delays
os.environ['FAST_LLM'] = 'openai:gpt-4o-mini'
os.environ['SMART_LLM'] = 'openai:gpt-4o-mini'
# Or use Groq for faster inference
os.environ['GROQ_API_KEY'] = 'your_key'
os.environ['FAST_LLM'] = 'groq:mixtral-8x7b-32768'
```

**Error: Timeout or hanging**
```python
# Add timeout wrapper
import asyncio

try:
    report = await asyncio.wait_for(
        researcher.write_report(),
        timeout=300  # 5 minute timeout
    )
except asyncio.TimeoutError:
    print("⚠️ Research timed out. Try with simpler query or fewer iterations.")
```

## 📊 QUALITY CHECKS

**Before delivering report to user:**

1. **Length check:**
   ```python
   if len(report) < 500:
       print("⚠️ Warning: Report is unusually short. Research may be incomplete.")
   ```

2. **Citation check:**
   ```python
   if "##" not in report and "References" not in report:
       print("⚠️ Warning: Report missing structure or citations.")
   ```

3. **Cost check:**
   ```python
   cost = researcher.get_costs()
   if cost > 0.20:
       print(f"⚠️ Warning: Research cost (${cost:.4f}) higher than expected for quick research.")
   ```

## 📈 SUCCESS METRICS

**A successful quick research delivers:**
- ✅ Report length: 1000-1500 words
- ✅ Sources: 20+ cited sources
- ✅ Duration: 1-3 minutes
- ✅ Cost: $0.05-$0.15
- ✅ Structure: Organized sections with headings
- ✅ Citations: Full reference list
- ✅ Accuracy: Claims backed by sources

## 🎯 COMPLETE EXAMPLE

**Full executable code:**
```python
from gpt_researcher import GPTResearcher
import asyncio
import os

async def quick_research(query: str) -> str:
    """Execute quick web research on given query."""

    # Verify environment
    if not os.getenv("OPENAI_API_KEY") or not os.getenv("TAVILY_API_KEY"):
        raise ValueError("Missing required API keys")

    # Initialize researcher
    researcher = GPTResearcher(
        query=query,
        report_type="research_report",
        report_source="web",
        verbose=True
    )

    # Conduct research
    print("🔍 Conducting research...")
    await researcher.conduct_research()

    # Generate report
    print("✍️  Writing report...")
    report = await researcher.write_report()

    # Show results
    print("\n" + "=" * 80)
    print("RESEARCH REPORT")
    print("=" * 80)
    print(report)

    # Show cost
    try:
        cost = researcher.get_costs()
        print(f"\n💰 Cost: ${cost:.4f}")
    except:
        pass

    return report

# Execute
if __name__ == "__main__":
    query = input("Enter your research query: ")
    report = asyncio.run(quick_research(query))
```

## 🔄 NEXT STEPS

**After completing quick research:**

1. **If user needs more depth:** Suggest `deep-research.md` workflow
2. **If user wants custom format:** Suggest `custom-report.md` workflow
3. **If user has local docs:** Suggest `hybrid-research.md` workflow
4. **If user mentions cost concerns:** Suggest `cost-optimization.md` workflow

## 📚 RELATED WORKFLOWS

- **deep-research.md** - For comprehensive tree exploration
- **hybrid-research.md** - For combining with local documents
- **custom-report.md** - For specific output formats
- **cost-optimization.md** - For budget-conscious research

---

**END OF WORKFLOW** - You have completed quick research execution.
