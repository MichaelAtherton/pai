"""
GPT Researcher - Custom Prompt Examples

This example demonstrates how to use custom prompts to control report formatting
and output style. Custom prompts allow you to tailor the final report to specific
needs without changing the underlying research process.

Documentation: https://docs.gptr.dev/docs/examples
"""

from gpt_researcher import GPTResearcher
import asyncio


async def generate_standard_report(query: str) -> str:
    """
    Generate a standard research report without custom prompts.

    Args:
        query: The research query

    Returns:
        Standard formatted research report
    """
    print("🔍 Generating standard report...")

    researcher = GPTResearcher(query=query, report_type="research_report")
    await researcher.conduct_research()
    report = await researcher.write_report()

    return report


async def generate_concise_summary(query: str) -> str:
    """
    Generate a concise 2-paragraph summary without citations.

    Args:
        query: The research query

    Returns:
        Concise summary report
    """
    print("📄 Generating concise summary...")

    researcher = GPTResearcher(query=query, report_type="research_report")
    await researcher.conduct_research()

    custom_prompt = "Provide a concise summary in 2 paragraphs without citations."
    report = await researcher.write_report(custom_prompt=custom_prompt)

    return report


async def generate_bullet_points(query: str) -> str:
    """
    Generate a bullet-point format report highlighting key findings.

    Args:
        query: The research query

    Returns:
        Bullet-point formatted report
    """
    print("📋 Generating bullet-point report...")

    researcher = GPTResearcher(query=query, report_type="research_report")
    await researcher.conduct_research()

    custom_prompt = "List the top 5 key findings as bullet points with brief explanations for each."
    report = await researcher.write_report(custom_prompt=custom_prompt)

    return report


async def generate_executive_brief(query: str) -> str:
    """
    Generate an executive-level brief suitable for leadership.

    Args:
        query: The research query

    Returns:
        Executive brief format report
    """
    print("💼 Generating executive brief...")

    researcher = GPTResearcher(query=query, report_type="research_report")
    await researcher.conduct_research()

    custom_prompt = """
    Create an executive brief with the following structure:
    1. Executive Summary (2-3 sentences)
    2. Key Findings (3-5 bullet points)
    3. Strategic Implications (brief paragraph)
    4. Recommended Actions (numbered list)
    Keep it under 500 words and use professional business language.
    """
    report = await researcher.write_report(custom_prompt=custom_prompt)

    return report


async def generate_technical_analysis(query: str) -> str:
    """
    Generate a technical analysis with detailed explanations and citations.

    Args:
        query: The research query

    Returns:
        Technical analysis report
    """
    print("🔬 Generating technical analysis...")

    researcher = GPTResearcher(query=query, report_type="research_report")
    await researcher.conduct_research()

    custom_prompt = """
    Write a detailed technical analysis including:
    - Methodology explanation
    - Data sources and reliability assessment
    - Detailed findings with supporting evidence
    - Technical conclusions
    - Full citations in APA format
    Use technical terminology and assume an expert audience.
    """
    report = await researcher.write_report(custom_prompt=custom_prompt)

    return report


async def generate_comparison_report(query: str) -> str:
    """
    Generate a comparative analysis report.

    Args:
        query: The research query (should include comparison elements)

    Returns:
        Comparison report
    """
    print("⚖️ Generating comparison report...")

    researcher = GPTResearcher(query=query, report_type="research_report")
    await researcher.conduct_research()

    custom_prompt = """
    Create a comparison report with:
    1. Overview of items being compared
    2. Side-by-side comparison table
    3. Pros and cons for each option
    4. Recommendation based on findings
    Use clear, objective language and cite sources.
    """
    report = await researcher.write_report(custom_prompt=custom_prompt)

    return report


async def main():
    """
    Main function demonstrating various custom prompt examples.
    """
    # Define the research query
    query = "What are the latest advancements in renewable energy technology?"

    print("=" * 80)
    print("GPT RESEARCHER - CUSTOM PROMPT EXAMPLES")
    print("=" * 80)
    print(f"\nResearch Query: {query}\n")

    # Example 1: Standard Report
    print("\n" + "=" * 80)
    print("EXAMPLE 1: STANDARD REPORT")
    print("=" * 80)
    standard_report = await generate_standard_report(query)
    print("\n--- Standard Report ---")
    print(standard_report[:500] + "..." if len(standard_report) > 500 else standard_report)

    # Example 2: Concise Summary
    print("\n" + "=" * 80)
    print("EXAMPLE 2: CONCISE SUMMARY")
    print("=" * 80)
    concise_report = await generate_concise_summary(query)
    print("\n--- Concise Summary ---")
    print(concise_report)

    # Example 3: Bullet Points
    print("\n" + "=" * 80)
    print("EXAMPLE 3: BULLET-POINT FORMAT")
    print("=" * 80)
    bullet_report = await generate_bullet_points(query)
    print("\n--- Bullet-Point Report ---")
    print(bullet_report)

    # Example 4: Executive Brief
    print("\n" + "=" * 80)
    print("EXAMPLE 4: EXECUTIVE BRIEF")
    print("=" * 80)
    executive_report = await generate_executive_brief(query)
    print("\n--- Executive Brief ---")
    print(executive_report)

    # Example 5: Technical Analysis
    print("\n" + "=" * 80)
    print("EXAMPLE 5: TECHNICAL ANALYSIS")
    print("=" * 80)
    technical_report = await generate_technical_analysis(query)
    print("\n--- Technical Analysis ---")
    print(technical_report[:500] + "..." if len(technical_report) > 500 else technical_report)

    print("\n" + "=" * 80)
    print("All examples completed successfully!")
    print("=" * 80)


if __name__ == "__main__":
    """
    Run all custom prompt examples.

    Prerequisites:
    - pip install gpt-researcher
    - Set OPENAI_API_KEY environment variable
    - Set TAVILY_API_KEY environment variable

    Usage:
    python custom_prompt.py
    """
    asyncio.run(main())
