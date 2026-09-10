"""
Optional AI integration point.

The application currently uses a deterministic local classifier so it runs
without an external API. This module is intentionally kept as an extension
point for an approved LLM provider.

When adding an API:
- keep credentials in environment variables;
- never hard-code API keys;
- send only synthetic/de-identified demo data;
- validate model output before updating workflow state.
"""

def summarize_with_ai(text: str) -> str:
    return text.strip()[:180]
