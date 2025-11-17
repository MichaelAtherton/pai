# Firecrawl Scripts

**Runnable Python scripts demonstrating Firecrawl features.**

## 📋 Prerequisites

```bash
# Install Firecrawl
pip install firecrawl-py

# Set API key
export FIRECRAWL_API_KEY=fc-your-api-key-here
```

Get your API key from: https://firecrawl.dev/app/api-keys

## 📁 Available Scripts

1. **scrape.py** - Basic single URL scraping
2. **crawl.py** - Crawl website with URL pattern filtering
3. **batch.py** - Scrape multiple URLs in parallel
4. **auth_scrape.py** - Scrape behind authentication
5. **extract.py** - Extract structured data with schemas
6. **actions.py** - Browser automation before scraping
7. **map_then_scrape.py** - Map URLs then selective scrape

## 🚀 Quick Start

```bash
# Run simple scrape
python scrape.py

# Run with custom URL
python scrape.py https://example.com

# Run all scripts
for f in *.py; do python "$f"; done
```

## 📝 Script Descriptions

### scrape.py
Basic single URL scraping with multiple formats.
- Returns markdown + links
- Uses caching (1-day maxAge)
- Shows content preview and metadata

### crawl.py
Multi-page website crawling with options.
- Crawls up to 20 pages
- Uses URL pattern filtering
- Shows crawl progress and stats

### batch.py
Parallel batch scraping of multiple URLs.
- Scrapes 3 URLs simultaneously
- Shows per-page results
- Demonstrates efficient parallel processing

### auth_scrape.py
Authenticated scraping using cookies.
- Extracts from DevTools
- Environment variable storage
- Cookie expiration detection

### extract.py
AI-powered structured data extraction.
- Uses Pydantic schemas
- JSON mode extraction
- Shows both schema-based and prompt-based methods

### actions.py
Browser automation before scraping.
- Google search example
- Scroll-to-load example
- Wait/click/write actions demonstrated

### map_then_scrape.py
Two-step efficient scraping workflow.
- Map website URLs first (fast, cheap)
- Filter URLs by pattern
- Selective batch scrape (cost-effective)

## 📊 Structure

Each script includes:
- Clear comments explaining each step
- Error handling and validation
- Environment variable configuration
- Working code ready to run
- Output with results preview

## 🔗 Related Resources

- **SKILL.md**: `../SKILL.md` - Quick reference and 4 essential examples
- **Quick Start**: `../references/quick-start.md` - 6 additional examples
- **Parameters**: `../references/parameters.md` - Detailed parameter docs
- **Workflows**: `../workflows/` - Step-by-step execution guides
- **Deep Context**: `../CLAUDE.md` - Comprehensive documentation

## ⚠️ Notes

- All scripts require `FIRECRAWL_API_KEY` environment variable
- Scripts use default URLs - modify as needed for your use cases
- Check rate limits for your plan (Free: 10/min, Hobby: 100/min, Standard: 500/min)
- Store sensitive data (cookies, tokens) in `.env` files (never commit to git)

## 💡 Usage Tips

1. **Start simple**: Run `scrape.py` first to verify setup
2. **Test with your URLs**: Modify default URLs in scripts
3. **Check examples**: Scripts demonstrate best practices
4. **Read comments**: Each script has detailed inline documentation
5. **Combine approaches**: Mix techniques from different scripts

---

Execute these scripts to learn Firecrawl capabilities through working examples.
