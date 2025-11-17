---
description: Cost optimization workflow - Lucy executes budget-conscious research with minimal API costs
globs: ""
alwaysApply: false
---

# 💰 COST OPTIMIZATION WORKFLOW

**YOU (Lucy) are reading this for budget-conscious research.**

## 🎯 WHEN TO USE

**User says:**
- "Cheap research"
- "Minimize cost"
- "Budget-friendly"
- "Cost-effective research"
- Has budget constraints

## 📋 COST REDUCTION STRATEGIES

### Strategy 1: Use Cheaper Models

```python
import os

# Use gpt-4o-mini for everything
os.environ['FAST_LLM'] = 'openai:gpt-4o-mini'
os.environ['SMART_LLM'] = 'openai:gpt-4o-mini'
os.environ['STRATEGIC_LLM'] = 'openai:gpt-4o-mini'
```

**Impact:** 50-70% cost reduction

### Strategy 2: Reduce Iterations

```python
os.environ['MAX_ITERATIONS'] = '2'  # Down from 3
```

**Impact:** 33% cost reduction

### Strategy 3: Fewer Sources

```python
os.environ['MAX_SEARCH_RESULTS'] = '5'  # Down from 10
```

**Impact:** ~30% cost reduction

### Strategy 4: Shorter Reports

```python
os.environ['TOTAL_WORDS'] = '800'  # Down from 1500
```

**Impact:** ~30% cost reduction

### Strategy 5: Use Free/Local LLMs

```python
# Ollama (local, $0 cost)
os.environ['OLLAMA_BASE_URL'] = 'http://localhost:11434'
os.environ['FAST_LLM'] = 'ollama:llama3'
os.environ['SMART_LLM'] = 'ollama:llama3'
```

**Impact:** $0 cost (development only)

### Strategy 6: Enable Caching

```python
os.environ['ENABLE_CACHE'] = 'true'
```

**Impact:** Up to 50% savings on repeated queries

## 🎯 OPTIMIZED CONFIGURATION

```python
from gpt_researcher import GPTResearcher
import os

# Cost-optimized settings
os.environ['FAST_LLM'] = 'openai:gpt-4o-mini'
os.environ['SMART_LLM'] = 'openai:gpt-4o-mini'
os.environ['MAX_ITERATIONS'] = '2'
os.environ['MAX_SEARCH_RESULTS'] = '5'
os.environ['TOTAL_WORDS'] = '800'
os.environ['ENABLE_CACHE'] = 'true'

researcher = GPTResearcher(
    query="[User's query]",
    report_type="research_report",
    verbose=True
)

await researcher.conduct_research()
report = await researcher.write_report()

# Check cost
cost = researcher.get_costs()
print(f"💰 Total cost: ${cost:.4f}")  # Should be ~$0.03-$0.05
```

## 💸 COST COMPARISON

| Configuration | Cost | Quality | Duration |
|---------------|------|---------|----------|
| Default | $0.10-$0.15 | High | 2-3 min |
| Optimized | $0.03-$0.05 | Good | 1-2 min |
| Local (Ollama) | $0.00 | Fair | 2-4 min |

---

**END OF WORKFLOW**
