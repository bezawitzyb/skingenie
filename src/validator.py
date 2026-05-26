"""
validator.py — Validates user inputs before sending to the API.

Catching bad input early = fewer wasted API calls = lower costs.
"""


def validate_inputs(products_raw: str, skin_type: str, concerns: list[str]) -> tuple[bool, str]:
    """
    Validate user inputs.

    Returns:
        (is_valid: bool, error_message: str)
    """
    if not products_raw or not products_raw.strip():
        return False, "Please enter at least one skincare product."

    products = parse_products(products_raw)
    if len(products) < 1:
        return False, "Please enter at least one product."

    if len(products) > 20:
        return False, "Please enter no more than 20 products."

    if not skin_type:
        return False, "Please select your skin type."

    if not concerns:
        return False, "Please select at least one skin concern."

    return True, ""


def parse_products(products_raw: str) -> list[str]:
    """
    Parse the raw product text input into a clean list.
    
    Handles both newline-separated and comma-separated input.
    E.g. "CeraVe Cleanser\nThe Ordinary Niacinamide" → ["CeraVe Cleanser", "The Ordinary Niacinamide"]
    """
    # Split on newlines first, then commas
    lines = products_raw.replace(",", "\n").split("\n")
    products = [line.strip() for line in lines if line.strip()]
    return products
