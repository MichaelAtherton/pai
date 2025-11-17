---
description: Multi-agent workflow - Lucy orchestrates 7-agent LangGraph team for publication-quality reports
globs: ""
alwaysApply: false
---

# 🤖 MULTI-AGENT RESEARCH WORKFLOW

**YOU (Lucy) are reading this for publication-quality multi-agent research.**

## 🎯 THE 7-AGENT TEAM

1. **Chief Editor** - Orchestrates process
2. **Researcher** (GPT Researcher) - Deep research
3. **Editor** - Plans outline
4. **Reviewer** - Validates quality
5. **Revisor** - Revises based on feedback
6. **Writer** - Compiles final report
7. **Publisher** - Exports to multiple formats

## ⚡ WHEN TO USE

**User says:**
- "Publication quality report"
- "Multi-agent research"
- "Academic paper"
- "Comprehensive business report"
- Requests PDF/DOCX output

## 📋 SETUP

### Step 1: Install Dependencies

```bash
pip install langgraph-cli
```

### Step 2: Configure task.json

```json
{
  "query": "Is AI in a hype cycle?",
  "model": "gpt-4o",
  "max_sections": 3,
  "publish_formats": {
    "markdown": true,
    "pdf": true,
    "docx": true
  },
  "include_human_feedback": false,
  "source": "web",
  "follow_guidelines": true,
  "guidelines": [
    "Report MUST fully answer the question",
    "Report MUST be written in APA format",
    "Report MUST be in English"
  ],
  "verbose": true
}
```

### Step 3: Run Multi-Agent Research

```bash
# Deploy locally
python main.py

# Or deploy with LangGraph
langgraph up
```

## 📊 OUTPUT

- **Duration:** 10-20 minutes
- **Output:** 5-6 page report
- **Formats:** Markdown, PDF, DOCX
- **Quality:** Publication-ready
- **Cost:** $0.50-$1.00

---

**END OF WORKFLOW**
