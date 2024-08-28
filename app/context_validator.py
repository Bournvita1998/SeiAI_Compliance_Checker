# context_validator.py

def check_context_compliance(text: str, context: str, rule: str) -> bool:
    """
    Check the compliance of the context in the text according to the given rule.

    Args:
        text (str): The text content to check.
        context (str): The context to validate.
        rule (str): The compliance rule to apply.

    Returns:
        bool: Whether the context in the text complies with the rule.
    """
    if context == "yield":
        return "subject to change" in text and "recent yield percentage" in text
    if context == "FDIC":
        return "250,000 usd" in text and "not an FDIC insured institution" in text
    return True
