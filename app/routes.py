from fastapi import APIRouter, HTTPException, Request
from app.web_scraper import fetch_webpage_content
from app.compliance_checker import check_compliance
from app.compliance_rules import compliance_rules

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/check_compliance")
async def check_compliance_api(request: Request):
    data = await request.json()
    url = data.get("url")

    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

    try:
        page_text = fetch_webpage_content(url)
    except ValueError as e:
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
