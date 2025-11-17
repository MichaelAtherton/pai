# Firecrawl Workflows

**Executable step-by-step workflows for Lucy (the AI) to execute Firecrawl web scraping operations.**

## 📁 Available Workflows

### Essential Workflows (Core Features)

1. **basic-scrape.md** - Single URL scraping
   - Duration: 5-10 seconds
   - Cost: 1 credit
   - Use: Product pages, articles, documentation, screenshots

2. **crawl-site.md** - Multi-page website crawling
   - Duration: 30s-5min (depends on site size)
   - Cost: 1 credit per page
   - Use: Documentation sites, blog archives, e-commerce categories

3. **batch-scrape.md** - Scrape multiple URLs simultaneously
   - Duration: 1-3 minutes
   - Cost: 1 credit per URL
   - Use: Known URL lists, parallel processing

4. **map-urls.md** - Fast URL discovery
   - Duration: 1-5 seconds
   - Cost: 1 credit
   - Use: Site structure analysis, pre-crawl planning, URL lists

5. **extract-structured-data.md** - AI-powered data extraction
   - Duration: 10-30 seconds
   - Cost: Token-based
   - Use: Product data, contact info, event details, custom schemas

### Advanced Workflows

6. **authenticated-scrape.md** - Scraping behind authentication
   - Duration: 10-20 seconds
   - Cost: 1 credit
   - Use: Internal tools, authenticated content, private pages

7. **mcp-integration.md** - Using Firecrawl via MCP servers
   - Duration: Varies
   - Cost: API-based
   - Use: Claude Code, Cursor, VSCode, Windsurf, n8n integration

8. **actions-automation.md** - Browser interactions before scraping
   - Duration: 15-30 seconds
   - Cost: 1 credit
   - Use: Dynamic content, form filling, click-then-scrape, search automation

## 🎯 How Lucy Uses These Workflows

1. **User makes request** → Lucy identifies which workflow applies
2. **Lucy loads workflow** → `Read /path/to/workflow/[name].md`
3. **Lucy executes steps** → Follows executable instructions
4. **Lucy delivers results** → Shows scraped data to user

## 📖 Workflow Format

Each workflow contains:
- **Frontmatter** - Metadata (description, globs, alwaysApply)
- **Mission** - What to accomplish
- **When to Use** - Activation triggers
- **Steps** - Executable procedures
- **Code Examples** - Copy-paste ready Python code
- **Error Handling** - Common issues and solutions
- **Complete Example** - Full working code

## 🔗 Three-Tier Reference System

```
SKILL.md (Quick Ref)
    ↓
CLAUDE.md (Deep Context)
    ↓
workflows/[name].md (Executable)
```

## 📊 Workflow Selection Guide

| User Request | Workflow | Duration | Cost |
|--------------|----------|----------|------|
| "Scrape this URL" | basic-scrape.md | 5-10s | 1 credit |
| "Crawl website" | crawl-site.md | 30s-5min | 1/page |
| "Scrape these URLs" | batch-scrape.md | 1-3min | 1/URL |
| "Get all URLs from site" | map-urls.md | 1-5s | 1 credit |
| "Extract product data" | extract-structured-data.md | 10-30s | tokens |
| "Scrape behind login" | authenticated-scrape.md | 10-20s | 1 credit |
| "Use in Cursor/VSCode/Claude Code" | mcp-integration.md | varies | varies |
| "Click then scrape" | actions-automation.md | 15-30s | 1 credit |

## 🚀 Quick Start Examples

### Single URL
```python
result = app.scrape_url('https://example.com', params={'formats': ['markdown']})
```

### Crawl Site
```python
result = app.crawl_url('https://example.com', params={'limit': 100})
```

### Batch Scrape
```python
result = app.batch_scrape_urls(['url1', 'url2', 'url3'])
```

### Extract Structured Data
```python
result = app.scrape_url('url', params={
    'formats': [{'type': 'json', 'schema': schema}]
})
```

---

For comprehensive context, see `../CLAUDE.md`
For quick reference, see `../SKILL.md`
