---
description: Troubleshooting workflow - Lucy diagnoses and fixes common GPT Researcher issues
globs: ""
alwaysApply: false
---

# 🔧 TROUBLESHOOTING WORKFLOW

**YOU (Lucy) are reading this because the user encountered an error.**

## 🎯 WHEN TO USE

**User says:**
- "Not working"
- "Error"
- "Failed"
- "Broken"
- Reports any GPT Researcher issue

## 📋 DIAGNOSTIC DECISION TREE

### Issue 1: "No retriever specified" / "MCP not working"

**Symptoms:** MCP configs provided but not used

**Diagnosis:**
```python
import os
print(f"RETRIEVER: {os.getenv('RETRIEVER')}")
# If None or doesn't include 'mcp' → FOUND THE PROBLEM
```

**Solution:**
```python
os.environ['RETRIEVER'] = 'mcp'
# OR
os.environ['RETRIEVER'] = 'tavily,mcp'
```

---

### Issue 2: "Invalid retriever(s) found"

**Symptoms:** Error on initialization

**Valid retrievers:** `tavily`, `mcp`, `google`, `bing`, `arxiv`, `semantic_scholar`, `pubmed_central`, `exa`, `searx`, `duckduckgo`

**Diagnosis:**
```python
retriever = os.getenv('RETRIEVER')
print(f"Current: {retriever}")
# Check for typos
```

**Solution:**
```python
# Fix typo
os.environ['RETRIEVER'] = 'tavily,arxiv'  # ✓ Correct
```

---

### Issue 3: "No MCP server configurations found"

**Symptoms:** RETRIEVER=mcp set but no MCP servers

**Diagnosis:**
```python
# Check if mcp_configs provided
assert mcp_configs, "mcp_configs is empty or None"
assert isinstance(mcp_configs, list), "mcp_configs must be list"
assert len(mcp_configs) > 0, "mcp_configs is empty"
```

**Solution:**
```python
mcp_configs = [
    {
        "name": "server_name",
        "command": "npx",
        "args": ["-y", "package-name"],
        "env": {"API_KEY": os.getenv("KEY")}
    }
]
```

---

### Issue 4: "MCP server connection failed"

**Symptoms:** Server timeout or connection refused

**Diagnosis Steps:**
```python
# 1. Test server independently
import subprocess
result = subprocess.run(
    ["npx", "-y", "@modelcontextprotocol/server-github"],
    capture_output=True,
    timeout=10
)
print(result.stderr)

# 2. Check env vars
assert os.getenv("GITHUB_TOKEN"), "Missing token"

# 3. Test network
import requests
r = requests.get("https://api.github.com")
assert r.status_code == 200, "Network issue"
```

**Solutions:**
- Verify command/args are correct
- Check environment variables set
- Test network connectivity
- Ensure dependencies installed

---

### Issue 5: Rate Limiting (429 errors)

**Symptoms:** "Rate limit exceeded"

**Solutions:**

**Option 1: Switch to cheaper model**
```python
os.environ['FAST_LLM'] = 'openai:gpt-4o-mini'
os.environ['SMART_LLM'] = 'openai:gpt-4o-mini'
```

**Option 2: Use different provider**
```python
os.environ['GROQ_API_KEY'] = 'your_key'
os.environ['FAST_LLM'] = 'groq:mixtral-8x7b-32768'
```

**Option 3: Reduce iterations**
```python
os.environ['MAX_ITERATIONS'] = '2'
```

---

### Issue 6: Document Loading Errors

**Symptoms:** "Failed to load document"

**Diagnosis:**
```bash
# Check file exists
ls -la ./my-docs/

# Check file format
file ./my-docs/document.pdf

# Check permissions
ls -l ./my-docs/document.pdf
```

**Solutions:**
- Re-download corrupted files
- Ensure not password-protected
- Convert unsupported formats to PDF/TXT/DOCX
- Fix permissions: `chmod 644 ./my-docs/*.pdf`

---

### Issue 7: Memory Issues

**Symptoms:** Process killed, out of memory

**Solutions:**

**Option 1: Process fewer documents**
```bash
# Move large files temporarily
mkdir ./my-docs/archive
mv ./my-docs/large-file.pdf ./my-docs/archive/
```

**Option 2: Reduce concurrency**
```python
os.environ['DEEP_RESEARCH_CONCURRENCY'] = '2'
```

---

### Issue 8: Missing API Keys

**Symptoms:** Authentication errors

**Diagnosis:**
```python
required_keys = ["OPENAI_API_KEY", "TAVILY_API_KEY"]
missing = [k for k in required_keys if not os.getenv(k)]

if missing:
    print(f"❌ Missing: {', '.join(missing)}")
```

**Solution:**
```bash
export OPENAI_API_KEY=your_key
export TAVILY_API_KEY=your_key
```

---

## 🎯 COMPLETE DIAGNOSTIC SCRIPT

```python
import os
import sys

def diagnose_gpt_researcher():
    """Run full diagnostic check."""

    print("=" * 80)
    print("GPT RESEARCHER DIAGNOSTIC")
    print("=" * 80)

    # Check 1: API Keys
    print("\n1. API Keys:")
    keys = ["OPENAI_API_KEY", "TAVILY_API_KEY"]
    for key in keys:
        status = "✓" if os.getenv(key) else "✗"
        print(f"   {status} {key}")

    # Check 2: Retriever
    print("\n2. Retriever Configuration:")
    retriever = os.getenv("RETRIEVER")
    print(f"   RETRIEVER = {retriever if retriever else 'NOT SET'}")

    # Check 3: Document Path
    print("\n3. Document Path:")
    doc_path = os.getenv("DOC_PATH", "./my-docs")
    from pathlib import Path
    exists = Path(doc_path).exists()
    print(f"   DOC_PATH = {doc_path}")
    print(f"   Exists: {'✓' if exists else '✗'}")

    # Check 4: Import Test
    print("\n4. Import Test:")
    try:
        from gpt_researcher import GPTResearcher
        print("   ✓ GPT Researcher import successful")
    except ImportError as e:
        print(f"   ✗ Import failed: {e}")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    diagnose_gpt_researcher()
```

---

**END OF WORKFLOW** - Troubleshooting complete.
