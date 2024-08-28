# models.py

from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class ComplianceRequest(BaseModel):
    url: HttpUrl

class TermSuggestion(BaseModel):
    term: str
    suggestions: List[str]
    reason: str

class ContextSuggestion(BaseModel):
    context: str
    rule: str
    reason: str

class ComplianceResponse(BaseModel):
    non_compliant_terms: List[str]
    term_suggestions: List[TermSuggestion]
    context_suggestions: List[ContextSuggestion]

class ErrorResponse(BaseModel):
    detail: str

class DisclosureCheckRequest(BaseModel):
    url: HttpUrl
    disclosure_text: str

class DisclosureCheckResponse(BaseModel):
    disclosure_present: bool
