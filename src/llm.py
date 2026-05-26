"""
llm.py — Handles all communication with the Claude API.

This is the core AI logic of SkinGenie. It takes the user's
products and skin concerns, builds a carefully crafted prompt,
calls Claude, and returns a structured routine.
"""

import os
import json
import anthropic
from dotenv import load_dotenv

load_dotenv()


def get_claude_client() -> anthropic.Anthropic:
    """Create and return an Anthropic client using the API key from .env"""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found. Did you set up your .env file?")
    return anthropic.Anthropic(api_key=api_key)


def build_prompt(products: list[str], skin_type: str, concerns: list[str]) -> str:
    """
    Build the user message for Claude.
    
    This is prompt engineering in action — the more structured and
    specific the prompt, the better and more consistent the output.
    """
    products_str = "\n".join(f"- {p}" for p in products)
    concerns_str = ", ".join(concerns)

    return f"""Here are my skincare details:

**My products:**
{products_str}

**My skin type:** {skin_type}

**My main skin concerns:** {concerns_str}

Please generate my personalized weekly skincare routine."""


# This is the system prompt — it defines Claude's role, rules, and output format.
# This is the most important piece of prompt engineering in the whole project.
SYSTEM_PROMPT = """You are SkinGenie, an expert skincare routine advisor with deep knowledge of dermatology and cosmetic chemistry.

Your job is to create a personalized 7-day AM and PM skincare routine using ONLY the products the user provides.

Rules you must follow:
1. Only use products the user listed — never suggest products they don't have
2. Not every product needs to be used every day — rotate actives safely
3. Never layer conflicting ingredients on the same session (e.g. Retinol + AHAs, Vitamin C + Niacinamide)
4. Always end AM routines with SPF if the user has a sunscreen
5. Flag any ingredient conflicts you notice as warnings

You must respond with ONLY valid JSON — no explanation, no markdown, just the JSON object.

Response format:
{
  "routine": {
    "monday":    { "am": ["product1", "product2"], "pm": ["product1", "product3"] },
    "tuesday":   { "am": [...], "pm": [...] },
    "wednesday": { "am": [...], "pm": [...] },
    "thursday":  { "am": [...], "pm": [...] },
    "friday":    { "am": [...], "pm": [...] },
    "saturday":  { "am": [...], "pm": [...] },
    "sunday":    { "am": [...], "pm": [...] }
  },
  "tips": ["tip1", "tip2", "tip3"],
  "warnings": ["warning1"]
}
"""


def generate_routine(products: list[str], skin_type: str, concerns: list[str]) -> dict:
    """
    Main function: call Claude and return a parsed routine dict.
    
    Args:
        products:  List of product names the user owns
        skin_type: e.g. "oily", "dry", "combination"
        concerns:  List of concerns e.g. ["acne", "dark spots"]
    
    Returns:
        A dict with keys: routine, tips, warnings
    """
    client = get_claude_client()

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",   # Haiku = fastest + cheapest for structured output
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": build_prompt(products, skin_type, concerns)}
        ]
    )

    raw_text = response.content[0].text

    # Parse the JSON response from Claude
    try:
        routine_data = json.loads(raw_text)
    except json.JSONDecodeError:
        # If Claude added any extra text, try to extract the JSON block
        start = raw_text.find("{")
        end = raw_text.rfind("}") + 1
        routine_data = json.loads(raw_text[start:end])

    return routine_data
