"""
GPT Researcher - Hybrid Research with Online Documents

This example demonstrates combining web search with specific online documents
(URLs) for targeted, comprehensive research.

Documentation: https://docs.gptr.dev/docs/examples/hybrid_research
"""

from gpt_researcher import GPTResearcher
import asyncio
import os


async def get_research_report(
    query: str,
    report_type: str,
    report_source: str,
    document_urls: list
) -> str:
    """
    Generate a hybrid research report using web search and online documents.

    Args:
        query: The research query
        report_type: Type of report to generate
        report_source: Should be "hybrid" for combining web + online docs
        document_urls: List of URLs to online documents

    Returns:
        Comprehensive research report
    """
    print("=" * 80)
    print("HYBRID RESEARCH - ONLINE DOCUMENTS")
    print("=" * 80)
    print(f"\n📋 Query: {query}")
    print(f"🌐 Document URLs ({len(document_urls)}):")
    for i, url in enumerate(document_urls, 1):
        print(f"   {i}. {url}")
    print(f"\n🔄 Report Source: {report_source}\n")

    # Initialize researcher
    researcher = GPTResearcher(
        query=query,
        report_type=report_type,
        document_urls=document_urls,  # Provide online document URLs
        report_source=report_source    # "hybrid" combines web + online docs
    )

    # Conduct research
    print("📥 Phase 1: Fetching and analyzing online documents...")
    print("   Downloading and processing specified URLs")
    print("\n🌐 Phase 2: Conducting web research...")
    print("   Gathering additional external sources")
    print("\n🔗 Phase 3: Synthesizing findings...")
    print("   Combining insights from documents and web sources\n")

    research = await researcher.conduct_research()

    # Generate report
    print("✍️  Phase 4: Writing comprehensive report...\n")
    report = await researcher.write_report()

    return report


async def main():
    """
    Main function demonstrating hybrid research with online documents.
    """

    # Define research query
    query = "How does our product roadmap compare to emerging market trends in our industry?"

    # Specify report configuration
    report_source = "hybrid"  # Combines web search + online documents
    report_type = "research_report"

    # Example online document URLs
    # Note: Replace these with actual URLs to your documents
    document_urls = [
        # Example URLs (replace with real documents)
        "https://arxiv.org/pdf/2401.00001.pdf",  # Example: Academic paper
        "https://example.com/product-roadmap.pdf",  # Example: Product roadmap
        "https://example.com/market-analysis.doc",  # Example: Market analysis
    ]

    print("=" * 80)
    print("HYBRID RESEARCH WITH ONLINE DOCUMENTS")
    print("=" * 80)
    print("\n📝 Note: This example uses placeholder URLs.")
    print("   For real research, replace with actual document URLs.\n")

    # Run hybrid research
    try:
        report = await get_research_report(
            query=query,
            report_type=report_type,
            report_source=report_source,
            document_urls=document_urls
        )

        # Display report preview
        print("=" * 80)
        print("RESEARCH REPORT PREVIEW")
        print("=" * 80)
        print(report[:500] + "..." if len(report) > 500 else report)
        print("\n" + "=" * 80)

        # Save full report
        output_file = "hybrid_research_online.md"
        with open(output_file, "w") as f:
            f.write("# Hybrid Research Report\n\n")
            f.write(f"**Query:** {query}\n\n")
            f.write(f"**Report Source:** {report_source}\n\n")
            f.write("**Online Documents:**\n")
            for i, url in enumerate(document_urls, 1):
                f.write(f"{i}. {url}\n")
            f.write("\n---\n\n")
            f.write("## Research Findings\n\n")
            f.write(report)

        print(f"\n✅ Full report saved to: {output_file}")

    except Exception as e:
        print(f"\n⚠️  Error during research: {str(e)}")
        print("\nThis is expected if using placeholder URLs.")
        print("Replace document_urls with actual URLs for real research.\n")

    # Display examples of supported document formats
    print("\n" + "=" * 80)
    print("SUPPORTED ONLINE DOCUMENT FORMATS:")
    print("=" * 80)
    print("✓ PDF (.pdf)         - https://example.com/document.pdf")
    print("✓ Word (.doc, .docx) - https://example.com/document.docx")
    print("✓ Text (.txt)        - https://example.com/document.txt")
    print("✓ CSV (.csv)         - https://example.com/data.csv")
    print("✓ Excel (.xlsx)      - https://example.com/spreadsheet.xlsx")
    print("✓ Markdown (.md)     - https://example.com/readme.md")
    print("=" * 80)

    # Display key features
    print("\n" + "=" * 80)
    print("KEY FEATURES:")
    print("=" * 80)
    print("✓ Fetches and analyzes specific online documents")
    print("✓ Combines document insights with web research")
    print("✓ Supports multiple document formats")
    print("✓ Handles document authentication if needed")
    print("✓ Intelligent synthesis of multiple sources")
    print("✓ Typical duration: 1-5 minutes")
    print("=" * 80)

    # Display use cases
    print("\n" + "=" * 80)
    print("USE CASES:")
    print("=" * 80)
    print("• Competitive analysis using public company reports")
    print("• Academic research from published papers")
    print("• Market analysis using industry whitepapers")
    print("• Technical research from documentation sites")
    print("• Policy analysis from government documents")
    print("=" * 80)


async def example_real_world_urls():
    """
    Example with more realistic document URLs.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE: REAL-WORLD DOCUMENT RESEARCH")
    print("=" * 80)

    query = "What are the latest trends in AI safety and ethics?"

    # Real-world accessible documents
    document_urls = [
        "https://arxiv.org/pdf/1606.06565.pdf",  # Concrete Problems in AI Safety
        "https://www.nist.gov/system/files/documents/2023/01/26/AI_RMF_Knowledge_Base.pdf",  # NIST AI Risk Management
    ]

    print(f"\n📋 Query: {query}")
    print("\n🌐 Real Documents:")
    for i, url in enumerate(document_urls, 1):
        print(f"   {i}. {url}")

    print("\n💡 Tip: This example uses real, publicly accessible documents.")
    print("   Uncomment the code below to run actual research.\n")

    # Uncomment to run:
    # report = await get_research_report(
    #     query=query,
    #     report_type="research_report",
    #     report_source="hybrid",
    #     document_urls=document_urls
    # )
    # print(report)


if __name__ == "__main__":
    """
    Run hybrid research with online documents.

    Prerequisites:
    1. Install GPT Researcher:
       pip install gpt-researcher

    2. Set environment variables:
       export OPENAI_API_KEY=your_openai_api_key
       export TAVILY_API_KEY=your_tavily_api_key

    3. Prepare document URLs:
       - URLs to PDF, DOCX, TXT, or other supported formats
       - Publicly accessible or with proper authentication

    Usage:
       python hybrid_online.py

    Examples of Document URLs:
    - Academic papers: https://arxiv.org/pdf/XXXX.XXXXX.pdf
    - Company reports: https://company.com/annual-report.pdf
    - Whitepapers: https://industry.org/whitepaper.pdf
    - Documentation: https://docs.example.com/guide.pdf
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

    # Run the examples
    asyncio.run(main())

    # Optional: Run real-world example
    # asyncio.run(example_real_world_urls())
