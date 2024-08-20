from fastapi import APIRouter, HTTPException
from app.web_scraper import fetch_webpage_content
from app.compliance_checker import check_compliance
from app.compliance_rules import compliance_rules
from app.models import ComplianceRequest, ComplianceResponse, ErrorResponse
import logging

router = APIRouter()

@router.get("/health")
async def health_check() -> dict:
    """
    Health check endpoint.

    Returns:
        dict: A simple status message.
    """
    return {"status": "ok"}

@router.post("/check_compliance", response_model=ComplianceResponse, responses={400: {"model": ErrorResponse}})
async def check_compliance_api(request: ComplianceRequest) -> ComplianceResponse:
    """
    Check compliance of a webpage against the defined rules.

    Args:
        request (ComplianceRequest): The request containing the URL.

    Returns:
        ComplianceResponse: The compliance check results.
    """
    url = request.url

    try:
        page_text = await fetch_webpage_content(url)
    except ValueError as e:
        logging.error(f"Error fetching webpage: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

    non_compliant_terms, (term_suggestions, context_suggestions) = check_compliance(page_text, compliance_rules)

    response = {
        "non_compliant_terms": non_compliant_terms,
        "term_suggestions": term_suggestions,
        "context_suggestions": context_suggestions
    }

    if not non_compliant_terms:
        return {"message": "No non-compliant terms found"}

    return response
