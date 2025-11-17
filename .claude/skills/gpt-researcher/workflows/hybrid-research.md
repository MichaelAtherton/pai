---
description: Hybrid research workflow - Lucy combines web search with local/online documents for comprehensive context-aware research
globs: ""
alwaysApply: false
---

# 🔗 HYBRID RESEARCH WORKFLOW

**YOU (Lucy) are reading this because the user wants to combine internal documents with external web research.**

## 🎯 YOUR MISSION

Execute hybrid research combining:
- Local document analysis (processed on user's machine)
- Web search (external sources)
- Intelligent synthesis of both
- Privacy-safe execution
- Duration: 2-5 minutes
- Cost: $0.15-$0.30

## ⚡ WHEN TO USE THIS WORKFLOW

**User says:**
- "Research [topic] using our documents"
- "Compare our strategy to market trends"
- "Analyze our docs and current industry trends"
- "Internal + external research on [topic]"
- "How does our [X] compare to [industry standard]"

**Best for:**
- Product roadmap vs. market trends
- Internal policy vs. industry standards
- Competitive analysis with proprietary data
- Combining internal knowledge with external insights

## 📋 WORKFLOW STEPS

### Step 1: Setup Document Path

**For LOCAL documents:**
```python
import os
from pathlib import Path

# Set document path
doc_path = "./my-docs"  # or user-specified path
os.environ['DOC_PATH'] = doc_path

# Verify documents exist
if not Path(doc_path).exists():
    print(f"⚠️ Document path '{doc_path}' does not exist.")
    print("Creating directory...")
    Path(doc_path).mkdir(parents=True, exist_ok=True)
    print(f"✅ Created: {doc_path}")
    print(f"📝 Add your documents to this directory before running hybrid research.")
    # May need to fallback to web-only
```

**For ONLINE documents:**
```python
# User provides URLs to documents
document_urls = [
    "https://example.com/product-roadmap.pdf",
    "https://example.com/market-analysis.docx"
]
```

### Step 2: Initialize Hybrid Researcher

**With LOCAL documents:**
```python
from gpt_researcher import GPTResearcher

researcher = GPTResearcher(
    query="[User's research question]",
    report_type="research_report",
    report_source="hybrid",  # CRITICAL: Enables hybrid mode
    verbose=True
)
```

**With ONLINE documents:**
```python
researcher = GPTResearcher(
    query="[User's research question]",
    report_type="research_report",
    report_source="hybrid",
    document_urls=document_urls,  # Provide online doc URLs
    verbose=True
)
```

### Step 3: Execute Hybrid Research

**Research process:**
```python
print("🔗 Starting hybrid research...")
print("   Phase 1: Analyzing documents...")
print("   Phase 2: Conducting web research...")
print("   Phase 3: Synthesizing insights...\n")

await researcher.conduct_research()
```

**Internal Process:**

**Phase 1 - Document Analysis:**
1. Load documents from DOC_PATH or URLs
2. Chunk documents into manageable pieces
3. Create embeddings (locally)
4. Build vector store (locally)
5. Extract relevant passages based on query

**Phase 2 - Web Research:**
1. Generate complementary web queries
2. Execute parallel web searches
3. Scrape and extract web content
4. Filter for relevance

**Phase 3 - Synthesis:**
1. Compare document insights vs. web findings
2. Reconcile conflicting information
3. Prioritize recent/authoritative sources
4. Generate unified narrative

### Step 4: Generate Hybrid Report

```python
print("✍️  Writing hybrid report with internal + external insights...\n")

report = await researcher.write_report()
```

**Report structure:**
- Executive Summary
- Internal Document Findings
- External Research Findings
- Comparative Analysis
- Gaps and Discrepancies
- Recommendations
- References (internal + external)

### Step 5: Display and Save

```python
print("=" * 80)
print("HYBRID RESEARCH REPORT")
print("=" * 80)
print(f"Query: {query}")
print(f"Sources: Local docs + Web")
print("=" * 80)
print(report)
print("=" * 80)

# Save
output_file = f"hybrid_research_{query[:30].replace(' ', '_')}.md"
with open(output_file, "w") as f:
    f.write(f"# Hybrid Research Report\n\n")
    f.write(f"**Query:** {query}\n")
    f.write(f"**Sources:** Local documents + Web search\n\n")
    f.write("---\n\n")
    f.write(report)

print(f"\n✅ Report saved to: {output_file}")
```

## 🔒 PRIVACY MODEL

**Critical understanding for user:**

**What stays LOCAL:**
- ✅ Raw document content
- ✅ Document file paths
- ✅ Vector embeddings
- ✅ Vector store database
- ✅ Internal metadata

**What goes EXTERNAL:**
- ❌ Research queries (text only)
- ❌ Extracted relevant passages (context snippets)
- ❌ Synthesized summaries
- ❌ Generated report

**Privacy guarantee:**
- Raw document data NEVER transmitted
- Only query-relevant snippets sent to LLM
- Local processing for all document operations
- GDPR/compliance safe

## 🎛️ CONFIGURATION OPTIONS

### Hybrid with Deep Research

**Combine hybrid + deep for maximum comprehensiveness:**
```python
os.environ['DEEP_RESEARCH_BREADTH'] = '4'
os.environ['DEEP_RESEARCH_DEPTH'] = '2'

researcher = GPTResearcher(
    query=query,
    report_type="deep",     # Deep research mode
    report_source="hybrid", # With hybrid sources
    verbose=True
)
```

### Document-Heavy Hybrid

**Prioritize local documents:**
```python
# Reduce web search, focus on documents
os.environ['MAX_SEARCH_RESULTS'] = '5'  # Fewer web results
# Document analysis remains comprehensive
```

### Web-Heavy Hybrid

**Prioritize web with document validation:**
```python
# Full web search with document cross-reference
os.environ['MAX_SEARCH_RESULTS'] = '15'
# Use documents for validation/comparison
```

## ⚠️ ERROR HANDLING

### No Documents Found
```python
if not any(Path(doc_path).iterdir()):
    print("⚠️ No documents found in directory.")
    print("Falling back to web-only research...")
    researcher = GPTResearcher(
        query=query,
        report_source="web"  # Fallback
    )
```

### Document Loading Errors
```python
try:
    await researcher.conduct_research()
except Exception as e:
    if "document" in str(e).lower():
        print(f"⚠️ Document loading error: {e}")
        print("Check: file format, permissions, corruption")
```

### Online Document 404
```python
# GPT Researcher handles gracefully
# Failed URLs are skipped
# Research continues with available documents
```

## 📊 QUALITY CHECKS

**Verify hybrid integration:**
```python
# Check report mentions both sources
has_internal = "document" in report.lower() or "internal" in report.lower()
has_external = "source" in report.lower() or "http" in report.lower()

if not (has_internal and has_external):
    print("⚠️ Warning: Report may not integrate both sources effectively")
```

## 🎯 COMPLETE EXAMPLE

```python
from gpt_researcher import GPTResearcher
import asyncio
import os
from pathlib import Path

async def hybrid_research(query: str, doc_path: str = "./my-docs") -> str:
    """Execute hybrid research with local docs + web."""

    # Setup
    os.environ['DOC_PATH'] = doc_path

    # Verify docs
    if Path(doc_path).exists() and any(Path(doc_path).iterdir()):
        print(f"📁 Found documents in: {doc_path}")
        report_source = "hybrid"
    else:
        print("⚠️ No documents found, using web-only")
        report_source = "web"

    # Initialize
    researcher = GPTResearcher(
        query=query,
        report_type="research_report",
        report_source=report_source,
        verbose=True
    )

    # Execute
    print("🔗 Starting hybrid research...\n")
    await researcher.conduct_research()

    print("\n✍️  Generating report...\n")
    report = await researcher.write_report()

    # Results
    print("=" * 80)
    print("HYBRID RESEARCH COMPLETED")
    print("=" * 80)
    print(report)
    print("=" * 80)

    return report

# Execute
if __name__ == "__main__":
    query = input("Research query: ")
    doc_path = input("Document path (or press Enter for ./my-docs): ") or "./my-docs"
    report = asyncio.run(hybrid_research(query, doc_path))
```

## 📚 RELATED WORKFLOWS

- **quick-research.md** - Web-only alternative
- **deep-research.md** - Add depth to hybrid research
- **custom-report.md** - Format hybrid results

---

**END OF WORKFLOW** - Hybrid research complete.
