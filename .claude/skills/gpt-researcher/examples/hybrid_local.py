"""
GPT Researcher - Hybrid Research with Local Documents

This example demonstrates combining web search with local document analysis
for comprehensive, context-aware research.

Documentation: https://docs.gptr.dev/docs/examples/hybrid_research
"""

from gpt_researcher import GPTResearcher
import asyncio
import os
from pathlib import Path


async def get_research_report(
    query: str,
    report_type: str,
    report_source: str,
    doc_path: str = "./my-docs"
) -> str:
    """
    Generate a hybrid research report using web search and local documents.

    Args:
        query: The research query
        report_type: Type of report to generate
        report_source: Should be "hybrid" for combining web + local docs
        doc_path: Path to local documents directory

    Returns:
        Comprehensive research report
    """
    print("=" * 80)
    print("HYBRID RESEARCH - LOCAL DOCUMENTS")
    print("=" * 80)
    print(f"\n📋 Query: {query}")
    print(f"📁 Document Path: {doc_path}")
    print(f"🔄 Report Source: {report_source}\n")

    # Set DOC_PATH environment variable
    os.environ['DOC_PATH'] = doc_path

    # Initialize researcher
    researcher = GPTResearcher(
        query=query,
        report_type=report_type,
        report_source=report_source  # "hybrid" combines web + local docs
    )

    # Conduct research
    print("🔍 Phase 1: Analyzing local documents...")
    print("   Supported formats: PDF, TXT, DOCX, CSV, XLSX, MD, PPTX")
    print("\n🌐 Phase 2: Conducting web research...")
    print("   Gathering external sources and latest information")
    print("\n🔗 Phase 3: Synthesizing findings...")
    print("   Combining insights from local and web sources\n")

    research = await researcher.conduct_research()

    # Generate report
    print("✍️  Phase 4: Writing comprehensive report...\n")
    report = await researcher.write_report()

    return report


async def main():
    """
    Main function demonstrating hybrid research with local documents.
    """

    # Define research query
    query = "How does our product roadmap compare to emerging market trends in our industry?"

    # Specify report configuration
    report_source = "hybrid"  # Combines web search + local documents
    report_type = "research_report"

    # Path to local documents
    doc_path = "./my-docs"

    # Check if document directory exists
    if not Path(doc_path).exists():
        print(f"⚠️  Warning: Document directory '{doc_path}' does not exist.")
        print(f"   Creating directory and adding sample instructions...\n")

        # Create directory
        Path(doc_path).mkdir(parents=True, exist_ok=True)

        # Create a README with instructions
        readme_path = Path(doc_path) / "README.md"
        with open(readme_path, "w") as f:
            f.write("# Local Documents Directory\n\n")
            f.write("Place your documents here for hybrid research.\n\n")
            f.write("## Supported Formats\n\n")
            f.write("- PDF (.pdf)\n")
            f.write("- Text (.txt)\n")
            f.write("- Word (.docx)\n")
            f.write("- CSV (.csv)\n")
            f.write("- Excel (.xlsx)\n")
            f.write("- Markdown (.md)\n")
            f.write("- PowerPoint (.pptx)\n\n")
            f.write("## Example Files to Add\n\n")
            f.write("- Product roadmap documents\n")
            f.write("- Internal strategy documents\n")
            f.write("- Market research reports\n")
            f.write("- Competitive analysis\n")
            f.write("- Customer feedback\n")

        print(f"✅ Created: {readme_path}\n")
        print(f"📝 Note: Add your documents to '{doc_path}' directory")
        print(f"   For this demo, we'll proceed with web-only research.\n")

        # If no documents, fall back to web-only research
        report_source = "web"
        print(f"🔄 Switching to web-only research (no local documents found)\n")

    # Run hybrid research
    report = await get_research_report(
        query=query,
        report_type=report_type,
        report_source=report_source,
        doc_path=doc_path
    )

    # Display report preview
    print("=" * 80)
    print("RESEARCH REPORT PREVIEW")
    print("=" * 80)
    print(report[:500] + "..." if len(report) > 500 else report)
    print("\n" + "=" * 80)

    # Save full report
    output_file = "hybrid_research_local.md"
    with open(output_file, "w") as f:
        f.write(f"# Hybrid Research Report\n\n")
        f.write(f"**Query:** {query}\n\n")
        f.write(f"**Report Source:** {report_source}\n\n")
        f.write(f"**Document Path:** {doc_path}\n\n")
        f.write("---\n\n")
        f.write("## Research Findings\n\n")
        f.write(report)

    print(f"\n✅ Full report saved to: {output_file}")

    # Display key features
    print("\n" + "=" * 80)
    print("KEY FEATURES OF HYBRID RESEARCH:")
    print("=" * 80)
    print("✓ Combines external web knowledge with internal documents")
    print("✓ Local documents processed on your machine (privacy)")
    print("✓ Only synthesized information sent to external services")
    print("✓ Handles conflicting information intelligently")
    print("✓ Provides context and notes discrepancies")
    print("✓ Typical duration: 1-5 minutes")
    print("=" * 80)

    return report


if __name__ == "__main__":
    """
    Run hybrid research with local documents.

    Prerequisites:
    1. Install GPT Researcher:
       pip install gpt-researcher

    2. Set environment variables:
       export OPENAI_API_KEY=your_openai_api_key
       export TAVILY_API_KEY=your_tavily_api_key

    3. Prepare local documents:
       - Create ./my-docs directory
       - Add your documents (PDF, DOCX, TXT, etc.)

    Usage:
       python hybrid_local.py

    Privacy Notes:
    - Local documents are processed on your machine
    - Only synthesized information is sent externally
    - Raw document data never leaves your system
    """

    # Check for required environment variables
    required_env_vars = ["OPENAI_API_KEY", "TAVILY_API_KEY"]
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]

    if missing_vars:
        print("❌ Error: Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these variables before running:")
        print("   export OPENAI_API_KEY=your_key")
        print("   export TAVILY_API_KEY=your_key")
        exit(1)

    # Run the example
    asyncio.run(main())
