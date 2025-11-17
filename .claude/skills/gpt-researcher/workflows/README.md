# GPT Researcher Workflows

**Executable step-by-step workflows for Lucy (the AI) to execute GPT Researcher research.**

## 📁 Available Workflows

### Essential Workflows

1. **quick-research.md** - Standard web-only research
   - Duration: 1-3 minutes
   - Cost: $0.05-$0.15
   - Use: General research requests

2. **deep-research.md** - Comprehensive tree exploration
   - Duration: 5-10 minutes
   - Cost: $0.30-$0.50
   - Use: Complex topics, thorough analysis

3. **hybrid-research.md** - Web + local/online documents
   - Duration: 2-5 minutes
   - Cost: $0.15-$0.30
   - Use: Combining internal docs with market research

### Advanced Workflows

4. **mcp-integration.md** - Model Context Protocol sources
   - Duration: Similar to quick research
   - Use: GitHub, databases, custom APIs

5. **custom-report.md** - Custom format generation
   - Duration: Same as base research
   - Use: Executive summaries, bullet points, specific formats

6. **multi-agent.md** - LangGraph 7-agent team
   - Duration: 10-20 minutes
   - Cost: $0.50-$1.00
   - Use: Publication-quality reports

7. **cost-optimization.md** - Budget-conscious research
   - Duration: 1-2 minutes
   - Cost: $0.03-$0.05
   - Use: Minimize API costs

8. **troubleshooting.md** - Debug and fix issues
   - Use: Error diagnosis and resolution

## 🎯 How Lucy Uses These Workflows

1. **User makes request** → Lucy identifies which workflow applies
2. **Lucy loads workflow** → `Read /path/to/workflow/[name].md`
3. **Lucy executes steps** → Follows executable instructions
4. **Lucy delivers results** → Shows research report to user

## 📖 Workflow Format

Each workflow contains:
- **Frontmatter** - Metadata (description, globs, alwaysApply)
- **Mission** - What to accomplish
- **When to Use** - Activation triggers
- **Steps** - Executable procedures
- **Code Examples** - Copy-paste ready
- **Error Handling** - Common issues
- **Complete Example** - Full working code

## 🔗 Three-Tier Reference System

```
SKILL.md (Quick Ref)
    ↓
CLAUDE.md (Deep Context)
    ↓
workflows/[name].md (Executable)
```

---

For comprehensive context, see `../CLAUDE.md`
For quick reference, see `../SKILL.md`
