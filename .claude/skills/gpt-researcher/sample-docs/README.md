# Sample Documents Directory

This directory is for testing hybrid research with local documents.

## Purpose

When using GPT Researcher's hybrid research mode, this directory serves as a location for local documents that will be analyzed alongside web search results.

## Supported File Formats

GPT Researcher can analyze the following document formats:

- **PDF** (.pdf) - Portable Document Format
- **Text** (.txt) - Plain text files
- **Word** (.docx, .doc) - Microsoft Word documents
- **CSV** (.csv) - Comma-separated values
- **Excel** (.xlsx, .xls) - Microsoft Excel spreadsheets
- **Markdown** (.md) - Markdown formatted text
- **PowerPoint** (.pptx, .ppt) - Microsoft PowerPoint presentations

## How to Use

### 1. Add Your Documents

Place your documents in this directory:

```bash
cp /path/to/your/document.pdf ./sample-docs/
cp /path/to/your/report.docx ./sample-docs/
```

### 2. Run Hybrid Research

Use the `hybrid_local.py` example:

```python
from gpt_researcher import GPTResearcher
import os

# Set document path
os.environ['DOC_PATH'] = './sample-docs'

# Initialize researcher
researcher = GPTResearcher(
    query="Your research question",
    report_type="research_report",
    report_source="hybrid"  # Combines web + local docs
)

# Conduct research
await researcher.conduct_research()
report = await researcher.write_report()
```

Or run the example script:

```bash
python examples/hybrid_local.py
```

## Example Document Types

### Business Documents
- Product roadmaps
- Strategic plans
- Internal reports
- Financial statements
- Business proposals

### Technical Documents
- Architecture documents
- API documentation
- Technical specifications
- Code documentation
- System designs

### Research Materials
- Academic papers
- Literature reviews
- Research notes
- Study results
- Data analysis reports

### Marketing Materials
- Marketing plans
- Campaign analysis
- Market research
- Customer feedback
- Competitive analysis

## Privacy & Security

**Important Notes:**

- ✅ Documents are processed **locally** on your machine
- ✅ Only **synthesized information** is sent to external LLM services
- ✅ **Raw document data never leaves** your system
- ✅ Full control over which documents are analyzed

## Best Practices

### 1. Organize Your Documents

Create subdirectories for different categories:

```
sample-docs/
├── product/
│   ├── roadmap-2024.pdf
│   └── feature-specs.docx
├── market/
│   ├── competitor-analysis.pdf
│   └── market-trends.xlsx
└── research/
    ├── customer-feedback.csv
    └── user-research.pdf
```

### 2. Document Naming

Use clear, descriptive names:
- ✅ `q4-2024-product-roadmap.pdf`
- ✅ `ai-market-trends-analysis.docx`
- ❌ `document1.pdf`
- ❌ `untitled.docx`

### 3. File Size Considerations

- Individual files: Up to 100MB recommended
- Total directory size: Consider memory constraints
- For large datasets: Use CSV/Excel for structured data

### 4. Document Quality

For best results:
- Use searchable PDFs (not scanned images)
- Ensure documents are not password-protected
- Use well-formatted, structured documents
- Include clear headings and sections

## Configuration

Set the document path in your environment:

```bash
# Default path
export DOC_PATH="./sample-docs"

# Custom path
export DOC_PATH="/path/to/your/documents"
```

Or in Python:

```python
import os
os.environ['DOC_PATH'] = './sample-docs'
```

## Troubleshooting

### Documents Not Being Found

```bash
# Check if DOC_PATH is set correctly
echo $DOC_PATH

# Verify documents exist
ls -la ./sample-docs
```

### Unsupported File Format

Check the supported formats list above. Convert unsupported formats:
- Images → Extract text using OCR first
- Scanned PDFs → Use OCR to create searchable PDFs
- Other formats → Convert to TXT, PDF, or DOCX

### Memory Issues

For very large document collections:
- Process documents in batches
- Use smaller subsets for testing
- Increase system memory allocation

## Example Workflow

### 1. Prepare Documents

```bash
# Create directory structure
mkdir -p sample-docs/product
mkdir -p sample-docs/market

# Add documents
cp ~/Documents/roadmap.pdf sample-docs/product/
cp ~/Documents/market-analysis.xlsx sample-docs/market/
```

### 2. Run Research

```bash
# Set environment
export DOC_PATH="./sample-docs"
export OPENAI_API_KEY="your_key"
export TAVILY_API_KEY="your_key"

# Run hybrid research
python examples/hybrid_local.py
```

### 3. Review Results

The research report will combine:
- Insights from your local documents
- Latest information from web search
- Synthesized analysis connecting both sources

## Sample Documents for Testing

If you don't have documents ready, you can create sample files:

### Sample Product Roadmap (Markdown)

Create `sample-product-roadmap.md`:

```markdown
# Product Roadmap 2024

## Q1 2024
- Feature A: AI-powered analytics
- Feature B: Enhanced security

## Q2 2024
- Feature C: Mobile app launch
- Feature D: Integration platform
```

### Sample Market Analysis (TXT)

Create `sample-market-analysis.txt`:

```
Market Analysis Summary

Industry: Technology
Focus: AI and Machine Learning

Key Trends:
- Increased adoption of generative AI
- Focus on AI safety and ethics
- Growing demand for AI infrastructure

Competitors:
- Company A: Strong in enterprise AI
- Company B: Leading in consumer AI
```

## Resources

- [GPT Researcher Documentation](https://docs.gptr.dev)
- [Hybrid Research Guide](https://docs.gptr.dev/docs/examples/hybrid_research)
- [Supported File Formats](https://docs.gptr.dev/docs/features)

## Questions?

For issues or questions:
- Check the [documentation](https://docs.gptr.dev)
- Join the [Discord community](https://discord.gg/QgZXvJAccX)
- Open an issue on [GitHub](https://github.com/assafelovic/gpt-researcher)
