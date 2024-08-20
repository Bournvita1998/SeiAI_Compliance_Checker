import pytest
from app.compliance_checker import check_compliance
from app.compliance_rules import compliance_rules


def test_check_compliance_terms():
    page_text = "We offer a bank account and banking services, but not as a bank."
    non_compliant_terms, (term_suggestions, context_suggestions) = check_compliance(page_text, compliance_rules)

    # Updated expected result to include 'bank'
    assert non_compliant_terms == ["bank account", "banking", "bank"]
    assert len(term_suggestions) == 3
    assert term_suggestions[0]["term"] == "bank account"
    assert term_suggestions[1]["term"] == "banking"
    assert term_suggestions[2]["term"] == "bank"
    assert len(context_suggestions) == 0


def test_check_compliance_context():
    page_text = "The yield on our investment is subject to change."
    non_compliant_terms, (term_suggestions, context_suggestions) = check_compliance(page_text, compliance_rules)

    assert len(non_compliant_terms) == 0
    assert len(term_suggestions) == 0
    assert len(context_suggestions) == 1
    assert context_suggestions[0]["context"] == "yield"
