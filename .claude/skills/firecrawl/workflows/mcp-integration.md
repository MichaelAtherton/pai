---
description: MCP integration workflow - Lucy sets up and uses Firecrawl via Model Context Protocol servers
globs: ""
alwaysApply: false
---

# 🔌 MCP INTEGRATION WORKFLOW

**YOU (Lucy) are reading this to integrate Firecrawl via MCP.**

## 🎯 WHEN TO USE

**User says:**
- "Use Firecrawl in Cursor"
- "Setup Firecrawl MCP"
- "Integrate Firecrawl with VSCode/Claude Code"
- "Use Firecrawl in n8n"

## 📋 MISSION

Set up Firecrawl MCP server for use in AI coding assistants.

## ⚡ INSTALLATION METHODS

### For Cursor

**Add to Cursor settings (Features → MCP Servers):**
```json
{
  "firecrawl": {
    "command": "npx",
    "args": ["-y", "firecrawl-mcp"],
    "env": {
      "FIRECRAWL_API_KEY": "fc-your-api-key"
    }
  }
}
```

### For Claude Code

```bash
# Add MCP server
claude code mcp add firecrawl --key fc-your-api-key
```

### For VSCode

**Add to User Settings (JSON):**
```json
{
  "mcp": {
    "servers": {
      "firecrawl": {
        "command": "npx",
        "args": ["-y", "firecrawl-mcp"],
        "env": {
          "FIRECRAWL_API_KEY": "fc-your-api-key"
        }
      }
    }
  }
}
```

### For n8n (Streamable HTTP)

**Step 1: Start MCP server**
```bash
HTTP_STREAMABLE_SERVER=true \
FIRECRAWL_API_KEY=fc-your-key \
npx -y firecrawl-mcp
```

**Step 2: In n8n workflow:**
- Add AI Agent node
- Add Tool → MCP Client Tool
- Endpoint: `http://localhost:3000/v2/mcp`
- Transport: HTTP Streamable
- Auth: None

## 🎯 USAGE VIA MCP

Once installed, use Firecrawl directly in chat:

```
User: "Use Firecrawl to scrape https://example.com"
AI: [Automatically calls firecrawl_scrape tool via MCP]
```

**Available MCP tools:**
- `firecrawl_scrape` - Scrape single URL
- `firecrawl_crawl` - Crawl website
- `firecrawl_map` - Map URLs
- `firecrawl_search` - Search web
- `firecrawl_batch_scrape` - Batch scrape

## ⚠️ TROUBLESHOOTING

### Issue: MCP server not appearing

**Solution:**
1. Verify API key is set
2. Restart IDE
3. Test server: `FIRECRAWL_API_KEY=fc-key npx -y firecrawl-mcp`

### Issue: Connection refused

**Solution:**
Check config file path is correct for your IDE.

---

**END OF WORKFLOW**
