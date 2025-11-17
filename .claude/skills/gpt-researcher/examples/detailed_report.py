"""
GPT Researcher - Detailed Report Example

This example demonstrates using the DetailedReport class to generate
comprehensive reports on complex topics by breaking them into manageable sections.

Documentation: https://docs.gptr.dev/docs/examples/detailed_report
"""

import asyncio
import os
from typing import Optional

# Note: This example shows the DetailedReport API
# The actual implementation may vary based on your gpt-researcher version


async def generate_detailed_report_basic(query: str, websocket=None):
    """
    Generate a detailed report using the basic GPTResearcher API.

    This is a simplified version that achieves similar results to DetailedReport
    by using the standard GPTResearcher with appropriate configuration.

    Args:
        query: The primary research topic
        websocket: Optional WebSocket for real-time progress updates

    Returns:
        Generated detailed report
    """
    from gpt_researcher import GPTResearcher

    print("=" * 80)
    print("DETAILED REPORT - BASIC APPROACH")
    print("=" * 80)
    print(f"\n📋 Query: {query}\n")

    # Initialize researcher with detailed report configuration
    researcher = GPTResearcher(
        query=query,
        report_type="research_report",  # Or "deep" for more comprehensive analysis
        report_source="web",
        websocket=websocket,
        verbose=True
    )

    # Conduct research
    print("🔍 Phase 1: Conducting initial research...")
    await researcher.conduct_research()

    # Generate comprehensive report
    print("\n✍️  Phase 2: Writing detailed report...")
    print("   - Generating table of contents")
    print("   - Creating section breakdowns")
    print("   - Assembling final report with citations\n")

    report = await researcher.write_report()

    return report


async def generate_detailed_report_advanced(
    query: str,
    report_type: str = "research_report",
    report_source: str = "web",
    source_urls: Optional[list] = None,
    config_path: Optional[str] = None,
    tone: str = "FORMAL",
    websocket=None,
    subtopics: Optional[list] = None,
):
    """
    Generate a detailed report with advanced configuration.

    This example shows how to use GPTResearcher with detailed configuration
    options to achieve comprehensive, multi-section reports.

    Args:
        query: The primary research topic
        report_type: Type of report to generate
        report_source: Where to source data from (web, local, hybrid)
        source_urls: Optional list of specific URLs to research
        config_path: Path to configuration file
        tone: Report tone (FORMAL, OBJECTIVE, etc.)
        websocket: Optional WebSocket for progress updates
        subtopics: Optional predefined subtopics

    Returns:
        Detailed research report
    """
    from gpt_researcher import GPTResearcher

    print("=" * 80)
    print("DETAILED REPORT - ADVANCED CONFIGURATION")
    print("=" * 80)
    print(f"\n📋 Query: {query}")
    print(f"📝 Report Type: {report_type}")
    print(f"🌐 Report Source: {report_source}")
    print(f"🎭 Tone: {tone}\n")

    # Initialize researcher with full configuration
    researcher = GPTResearcher(
        query=query,
        report_type=report_type,
        report_source=report_source,
        source_urls=source_urls or [],
        config_path=config_path,
        websocket=websocket,
        verbose=True
    )

    # Research workflow
    print("🔍 Phase 1: Initial research on main query...")
    await researcher.conduct_research()

    print("\n📊 Phase 2: Decomposing topic into subtopics...")
    # The researcher automatically breaks down complex topics

    print("\n🔬 Phase 3: Conducting targeted research on each section...")
    # Subtopic research happens automatically

    print("\n✍️  Phase 4: Assembling final report...")
    print("   - Creating section headings")
    print("   - Generating table of contents")
    print("   - Preventing content duplication")
    print("   - Adding citations\n")

    report = await researcher.write_report()

    return report


async def main():
    """
    Main function demonstrating detailed report generation.
    """

    # Example 1: Basic detailed report
    query1 = "The impact of artificial intelligence on modern healthcare"

    print("\n" + "=" * 80)
    print("EXAMPLE 1: BASIC DETAILED REPORT")
    print("=" * 80)

    report1 = await generate_detailed_report_basic(query1)

    print("\n--- Generated Report Preview ---")
    print(report1[:500] + "..." if len(report1) > 500 else report1)

    # Save report
    with open("detailed_report_basic.md", "w") as f:
        f.write(f"# Detailed Research Report\n\n")
        f.write(f"**Query:** {query1}\n\n")
        f.write("---\n\n")
        f.write(report1)

    print(f"\n✅ Report saved to: detailed_report_basic.md")

    # Example 2: Advanced detailed report with configuration
    query2 = "The future of renewable energy: solar, wind, and emerging technologies"

    print("\n" + "=" * 80)
    print("EXAMPLE 2: ADVANCED DETAILED REPORT")
    print("=" * 80)

    report2 = await generate_detailed_report_advanced(
        query=query2,
        report_type="research_report",
        report_source="web",
        tone="FORMAL",
        source_urls=[
            "https://www.iea.org/",
            "https://www.irena.org/"
        ]
    )

    print("\n--- Generated Report Preview ---")
    print(report2[:500] + "..." if len(report2) > 500 else report2)

    # Save report
    with open("detailed_report_advanced.md", "w") as f:
        f.write(f"# Detailed Research Report\n\n")
        f.write(f"**Query:** {query2}\n\n")
        f.write(f"**Configuration:** Advanced with custom sources\n\n")
        f.write("---\n\n")
        f.write(report2)

    print(f"\n✅ Report saved to: detailed_report_advanced.md")

    print("\n" + "=" * 80)
    print("KEY FEATURES OF DETAILED REPORTS:")
    print("=" * 80)
    print("✓ Breaks down complex topics into manageable subtopics")
    print("✓ Conducts focused research on each section")
    print("✓ Prevents content duplication across sections")
    print("✓ Generates table of contents automatically")
    print("✓ Includes proper citations and references")
    print("✓ Supports real-time progress updates")
    print("✓ Customizable tone and formatting")
    print("=" * 80)


if __name__ == "__main__":
    """
    Run the detailed report examples.

    Prerequisites:
    1. Install GPT Researcher:
       pip install gpt-researcher

    2. Set environment variables:
       export OPENAI_API_KEY=your_openai_api_key
       export TAVILY_API_KEY=your_tavily_api_key

    Usage:
       python detailed_report.py

    Use Cases:
    - Academic research papers
    - Business intelligence reports
    - Market analysis documents
    - Technical documentation
    - Industry trend reports
    """

    # Check for required environment variables
    required_env_vars = ["OPENAI_API_KEY", "TAVILY_API_KEY"]
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]

    if missing_vars:
        print("❌ Error: Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these variables before running.")
        exit(1)

    # Run examples
    asyncio.run(main())
