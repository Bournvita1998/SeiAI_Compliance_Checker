def check_context_compliance(text, context, rule):
    if context == "yield":
        if "subject to change" not in text or "recent yield percentage" not in text:
            return False
    if context == "FDIC":
        if "250,000 usd" not in text or "not an FDIC insured institution" not in text:
            return False
    return True
