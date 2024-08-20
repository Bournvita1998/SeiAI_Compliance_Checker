# compliance_rules.py

compliance_rules = {
    "terms_to_avoid": {
        "bank account": {
            "response": ["money management account", "cash management account"],
            "reason": "Terms like 'bank account' are prohibited for non-financial institutions."
        },
        "banking": {
            "response": ["financial services", "financial product"],
            "reason": "Avoid using 'banking' as it implies direct banking services."
        },
        "bank": {
            "response": ["financial institution", "financial services"],
            "reason": "'Bank' is reserved for licensed banks."
        },
        "deposits": {
            "response": ["store of funds", "wallet"],
            "reason": "'Deposits' is specific to banking institutions."
        }
    },
    "contextual_rules": {
        "yield": {
            "rule": "Yield should be referred to as 'yield' and accompanied by a disclaimer about variability.",
            "reason": "Yield can be misleading if referred to as 'interest'."
        },
        "FDIC insurance": {
            "rule": "Use approved terms for FDIC insurance eligibility, avoiding terms like 'FDIC insured'.",
            "reason": "Misuse of 'FDIC insured' may mislead about insurance coverage."
        }
    }
}
