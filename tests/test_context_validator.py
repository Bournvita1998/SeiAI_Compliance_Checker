from app.context_validator import check_context_compliance

def test_check_context_compliance_yield():
    text = "The yield on our investment is subject to change and reflects recent yield percentage."
    assert check_context_compliance(text, "yield", "Yield should be referred to as 'yield' and accompanied by a disclaimer about variability.")

def test_check_context_compliance_fdic():
    text = "Our institution is FDIC insured and coverage is up to 250,000 USD."
    assert not check_context_compliance(text, "FDIC", "Use approved terms for FDIC insurance eligibility, avoiding terms like 'FDIC insured'.")
