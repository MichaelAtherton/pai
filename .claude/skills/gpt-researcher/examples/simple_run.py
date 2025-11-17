"""
GPT Researcher - Simple Run Example

This is the most basic example of using GPT Researcher.
It demonstrates a straightforward research workflow with minimal configuration.

Documentation: https://docs.gptr.dev/docs/examples
"""

from gpt_researcher import GPTResearcher
import asyncio
import os


async def main():
    """
    Simple research workflow example.

    This example shows how to:
    1. Initialize a GPTResearcher instance
    2. Conduct research on a query
    3. Generate a research report
    """

    # Define the research query
    query = "What happened in the latest burning man floods?"

    # Specify the report type
    # Options: research_report, outline_report, resource_report, custom_report, deep
    report_type = "research_report"

    print("=" * 80)
    print("GPT RESEARCHER - SIMPLE RUN EXAMPLE")
    print("=" * 80)
    print(f"\n📋 Query: {query}")
    print(f"📝 Report Type: {report_type}\n")

    # Initialize the researcher
    # config_path=None uses default configuration
    researcher = GPTResearcher(
        query=query,
        report_type=report_type,
        config_path=None
    )

    # Conduct research on the given query
    print("🔍 Conducting research...")
    print("   This may take 1-3 minutes depending on the query complexity\n")

    await researcher.conduct_research()

    # Write the report
    print("✍️  Writing report...\n")
    report = await researcher.write_report()

    # Display the report
    print("=" * 80)
    print("RESEARCH REPORT")
    print("=" * 80)
    print(report)
    print("\n" + "=" * 80)

    # Optional: Get research costs
    try:
        cost = researcher.get_costs()
        print(f"💰 Research cost: ${cost:.4f}")
    except:
        print("💰 Cost tracking not available")

    print("=" * 80)

    # Optional: Save report to file
    output_file = "research_report.md"
    with open(output_file, "w") as f:
        f.write(f"# Research Report\n\n")
        f.write(f"**Query:** {query}\n\n")
        f.write(f"**Report Type:** {report_type}\n\n")
        f.write("---\n\n")
        f.write(report)

    print(f"\n✅ Report saved to: {output_file}")

    return report


if __name__ == "__main__":
    """
    Run the simple research example.

    Prerequisites:
    1. Install GPT Researcher:
       pip install gpt-researcher

    2. Set environment variables:
       export OPENAI_API_KEY=your_openai_api_key
       export TAVILY_API_KEY=your_tavily_api_key

    Usage:
       python simple_run.py
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
