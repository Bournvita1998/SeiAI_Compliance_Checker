# compliance_checker.py

from app.compliance_rules import compliance_rules
from typing import List, Dict, Tuple

def check_compliance(page_text: str, rules: dict) -> Tuple[List[str], Tuple[List[Dict[str, str]], List[Dict[str, str]]]]:
    """
    Check the compliance of the given page text against the provided rules.

    Args:
        page_text (str): The text content of the webpage.
        rules (dict): The compliance rules to check against.

    Returns:
        Tuple[List[str], Tuple[List[Dict[str, str]], List[Dict[str, str]]]]:
            - List of non-compliant terms found in the page text.
            - Tuple containing:
                - List of term suggestions with details for non-compliant terms.
                - List of context suggestions with details for contextual rules.
    """
    non_compliant_terms = []
    term_suggestions = []
    context_suggestions = []

    # Check for terms to avoid
    for term, details in rules["terms_to_avoid"].items():
        if term in page_text.lower():
            non_compliant_terms.append(term)
            term_suggestions.append({
                "term": term,
                "suggestions": details["response"],
                "reason": details["reason"]
            })

    # Check for contextual rules
    for context, details in rules["contextual_rules"].items():
        if context.lower() in page_text.lower():
            context_suggestions.append({
                "context": context,
                "rule": details["rule"],
                "reason": details["reason"]
            })

    return non_compliant_terms, (term_suggestions, context_suggestions)

def check_disclosure_presence(page_text: str, disclosure: str) -> bool:
    """
    Check if the specific disclosure text is present in the webpage text.

    Args:
        page_text (str): The text content of the webpage.
        disclosure (str): The disclosure text to check for.

    Returns:
        bool: True if the disclosure is present, False otherwise.
    """
    return disclosure.lower() in page_text.lower()
