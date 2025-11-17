---
description: Deep research workflow with tree exploration - Lucy executes comprehensive multi-level research for exhaustive coverage
globs: ""
alwaysApply: false
---

# 🌳 DEEP RESEARCH WORKFLOW

**YOU (Lucy) are reading this because the user requested deep, comprehensive research.**

This workflow executes GPT Researcher's tree-like exploration mode for maximum depth and breadth.

## 🎯 YOUR MISSION

Execute deep research mode to deliver:
- Comprehensive multi-section report (2500+ words)
- 50+ aggregated sources
- Tree-like exploration (breadth × depth)
- Full citations and references
- Completion time: 5-10 minutes
- Cost: $0.30-$0.50

## ⚡ WHEN TO USE THIS WORKFLOW

**User says:**
- "Deep research on [topic]"
- "Comprehensive analysis of [topic]"
- "Thorough research about [topic]"
- "Exhaustive research on [topic]"
- "I need detailed research on [topic]"

**Best for:**
- Complex topics requiring thorough analysis
- Academic research
- Strategic decision-making
- Market analysis
- Multi-faceted topics

**NOT for:**
- Quick answers → use `quick-research.md`
- Budget-limited research → use `cost-optimization.md`

## 📊 DEEP RESEARCH ARCHITECTURE

```
Level 0: Main Query
    │
    ├─ Breadth 1: Sub-query A
    │   ├─ Depth 1: Follow-up A1
    │   │   └─ Depth 2: Deep-dive A1.1
    │   └─ Depth 1: Follow-up A2
    │
    ├─ Breadth 2: Sub-query B
    │   ├─ Depth 1: Follow-up B1
    │   └─ Depth 1: Follow-up B2
    │
    ├─ Breadth 3: Sub-query C
    │   └─ Depth 1: Follow-up C1
    │
    └─ Breadth 4: Sub-query D
        └─ Depth 1: Follow-up D1
```

**Configuration:**
- **Breadth** = Number of parallel research paths at each level
- **Depth** = How many levels deep to explore
- **Concurrency** = Max parallel operations

## 📋 WORKFLOW STEPS

### Step 1: Configure Deep Research Parameters

**Set environment variables BEFORE initializing:**
```python
import os

# Deep research configuration
os.environ['DEEP_RESEARCH_BREADTH'] = '4'    # 4 parallel paths per level
os.environ['DEEP_RESEARCH_DEPTH'] = '2'      # 2 levels deep
os.environ['DEEP_RESEARCH_CONCURRENCY'] = '4' # Max 4 concurrent ops
os.environ['TOTAL_WORDS'] = '2500'           # Target report length

# LLM configuration (use reasoning models for deep research)
os.environ['STRATEGIC_LLM'] = 'openai:o4-mini'  # For planning
os.environ['SMART_LLM'] = 'openai:gpt-4o'       # For synthesis
os.environ['FAST_LLM'] = 'openai:gpt-4o-mini'   # For sub-queries
```

**Parameter Tuning Guide:**

| Goal | Breadth | Depth | Result |
|------|---------|-------|--------|
| Wider coverage | 6-8 | 2 | More topics, moderate depth |
| Deeper insights | 3-4 | 3-4 | Fewer topics, deep analysis |
| Balanced | 4 | 2 | Good balance (recommended) |
| Fast deep | 3 | 2 | Faster but still comprehensive |

### Step 2: Initialize Researcher

**Create GPTResearcher with deep research mode:**
```python
from gpt_researcher import GPTResearcher
import asyncio

query = "[User's research question]"

researcher = GPTResearcher(
    query=query,
    report_type="deep",  # CRITICAL: Activates deep research mode
    report_source="web",
    verbose=True
)
```

**Key difference from quick research:**
- `report_type="deep"` activates tree exploration
- Uses STRATEGIC_LLM for planning
- Automatically applies breadth/depth configuration

### Step 3: Execute Deep Research

**Conduct multi-level research:**
```python
print("🌳 Starting deep research with tree exploration...")
print(f"   Configuration: {os.getenv('DEEP_RESEARCH_BREADTH')} breadth × {os.getenv('DEEP_RESEARCH_DEPTH')} depth")
print(f"   Expected duration: 5-10 minutes")
print(f"   Expected sources: 50+ sources\n")

print("📊 Level 0: Analyzing main query...")
print("📊 Level 1: Generating sub-queries (breadth exploration)...")
print("📊 Level 2: Following promising leads (depth exploration)...\n")

await researcher.conduct_research()
```

**What happens internally:**

**Level 0 (Main Query):**
1. Strategic analysis of query
2. Topic decomposition
3. Identify key research dimensions

**Level 1 (Breadth):**
1. Generate N sub-queries (N = BREADTH)
2. Execute parallel research on each
3. Identify promising leads

**Level 2+ (Depth):**
1. For each promising sub-query
2. Generate follow-up questions
3. Dive deeper recursively
4. Aggregate findings at each level

**Expected duration:** 4-8 minutes depending on breadth × depth

### Step 4: Generate Comprehensive Report

**Write detailed report:**
```python
print("✍️  Synthesizing findings into comprehensive report...")
print("   - Organizing multi-level insights")
print("   - Creating table of contents")
print("   - Generating citations")
print("   - Assembling final report\n")

report = await researcher.write_report()
```

**Report structure typically includes:**
- Executive Summary
- Table of Contents
- Multiple main sections (based on breadth)
- Detailed subsections (based on depth)
- Key Findings
- Conclusions
- Full References (50+ sources)

**Expected duration:** 1-2 minutes

### Step 5: Display Results with Metadata

**Show comprehensive results:**
```python
print("=" * 80)
print("DEEP RESEARCH REPORT")
print("=" * 80)
print(f"Query: {query}")
print(f"Configuration: {os.getenv('DEEP_RESEARCH_BREADTH')}×{os.getenv('DEEP_RESEARCH_DEPTH')} tree")
print(f"Report Length: {len(report.split())} words")
print("=" * 80)
print()
print(report)
print()
print("=" * 80)

# Show cost and statistics
try:
    cost = researcher.get_costs()
    print(f"💰 Research cost: ${cost:.4f}")
    print(f"📊 Configuration used:")
    print(f"   - Breadth: {os.getenv('DEEP_RESEARCH_BREADTH')} parallel paths")
    print(f"   - Depth: {os.getenv('DEEP_RESEARCH_DEPTH')} levels")
    print(f"   - Concurrency: {os.getenv('DEEP_RESEARCH_CONCURRENCY')} max parallel")
except:
    pass

print("=" * 80)
```

### Step 6: Save Comprehensive Report

**Save with metadata:**
```python
from datetime import datetime

output_file = f"deep_research_{query[:30].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.md"

with open(output_file, "w") as f:
    f.write(f"# Deep Research Report\n\n")
    f.write(f"**Query:** {query}\n\n")
    f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write(f"**Configuration:**\n")
    f.write(f"- Breadth: {os.getenv('DEEP_RESEARCH_BREADTH')}\n")
    f.write(f"- Depth: {os.getenv('DEEP_RESEARCH_DEPTH')}\n")
    f.write(f"- Concurrency: {os.getenv('DEEP_RESEARCH_CONCURRENCY')}\n\n")
    f.write("---\n\n")
    f.write(report)

print(f"\n✅ Deep research report saved to: {output_file}")
```

## 🎛️ CONFIGURATION TUNING

### Maximum Depth Configuration

**For exhaustive research (10-15 minutes, ~$0.80):**
```python
os.environ['DEEP_RESEARCH_BREADTH'] = '6'
os.environ['DEEP_RESEARCH_DEPTH'] = '3'
os.environ['DEEP_RESEARCH_CONCURRENCY'] = '6'
os.environ['TOTAL_WORDS'] = '4000'
```

**Result:** 18 research paths (6 breadth × 3 depth), 100+ sources

### Fast Deep Configuration

**For faster results with good depth (3-5 minutes, ~$0.20):**
```python
os.environ['DEEP_RESEARCH_BREADTH'] = '3'
os.environ['DEEP_RESEARCH_DEPTH'] = '2'
os.environ['DEEP_RESEARCH_CONCURRENCY'] = '4'
os.environ['TOTAL_WORDS'] = '1500'
```

**Result:** 6 research paths (3 × 2), 30+ sources

### Balanced Configuration (Recommended)

**Default settings provide good balance:**
```python
os.environ['DEEP_RESEARCH_BREADTH'] = '4'
os.environ['DEEP_RESEARCH_DEPTH'] = '2'
os.environ['DEEP_RESEARCH_CONCURRENCY'] = '4'
os.environ['TOTAL_WORDS'] = '2500'
```

**Result:** 8 research paths (4 × 2), 50+ sources

## ⚠️ ERROR HANDLING

### Memory Issues

**If system runs out of memory:**
```python
# Reduce concurrency
os.environ['DEEP_RESEARCH_CONCURRENCY'] = '2'

# Or reduce breadth
os.environ['DEEP_RESEARCH_BREADTH'] = '3'
```

### Cost Overruns

**If cost exceeds budget:**
```python
# Monitor cost during research
cost_so_far = researcher.get_costs()
if cost_so_far > MAX_BUDGET:
    print(f"⚠️ Cost (${cost_so_far:.4f}) approaching budget limit")
    # Consider stopping or reducing depth
```

### Timeout Issues

**If research takes too long:**
```python
import asyncio

# Set timeout
try:
    report = await asyncio.wait_for(
        researcher.write_report(),
        timeout=900  # 15 minute timeout
    )
except asyncio.TimeoutError:
    print("⚠️ Deep research timed out. Try reducing breadth or depth.")
```

## 📊 QUALITY METRICS

**A successful deep research delivers:**
- ✅ Report length: 2500+ words
- ✅ Sources: 50+ cited sources
- ✅ Structure: Multi-level hierarchy
- ✅ Table of contents: Auto-generated
- ✅ Depth: Multiple levels of analysis
- ✅ Breadth: Multiple perspectives covered
- ✅ Citations: Comprehensive reference list

## 🎯 COMPLETE EXAMPLE

```python
from gpt_researcher import GPTResearcher
import asyncio
import os
from datetime import datetime

async def deep_research(query: str) -> str:
    """Execute deep tree-exploration research."""

    # Configure deep research
    os.environ['DEEP_RESEARCH_BREADTH'] = '4'
    os.environ['DEEP_RESEARCH_DEPTH'] = '2'
    os.environ['DEEP_RESEARCH_CONCURRENCY'] = '4'
    os.environ['TOTAL_WORDS'] = '2500'

    # Use reasoning models
    os.environ['STRATEGIC_LLM'] = 'openai:o4-mini'
    os.environ['SMART_LLM'] = 'openai:gpt-4o'

    # Initialize
    researcher = GPTResearcher(
        query=query,
        report_type="deep",  # Activates deep research
        report_source="web",
        verbose=True
    )

    # Execute
    print("🌳 Starting deep research...")
    print(f"   Configuration: 4 breadth × 2 depth\n")

    await researcher.conduct_research()

    print("\n✍️  Generating comprehensive report...\n")
    report = await researcher.write_report()

    # Results
    print("=" * 80)
    print("DEEP RESEARCH COMPLETED")
    print("=" * 80)
    print(f"Words: {len(report.split())}")
    print(f"Cost: ${researcher.get_costs():.4f}")
    print("=" * 80)
    print(report)

    return report

# Execute
if __name__ == "__main__":
    query = input("Enter complex research query: ")
    report = asyncio.run(deep_research(query))
```

## 🔄 NEXT STEPS

**After deep research:**

1. **If user needs even more depth:** Increase depth to 3-4
2. **If user wants custom format:** Use `custom-report.md` with deep research results
3. **If cost is concern:** Show cost breakdown, suggest `cost-optimization.md`
4. **If adding local docs:** Combine with `hybrid-research.md` approach

## 📚 RELATED WORKFLOWS

- **quick-research.md** - For faster, lighter research
- **hybrid-research.md** - Add local documents to deep research
- **custom-report.md** - Format deep research results
- **cost-optimization.md** - Reduce deep research costs

---

**END OF WORKFLOW** - Deep research execution complete.
