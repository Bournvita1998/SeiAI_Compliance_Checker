import pytest
from fastapi.testclient import TestClient
from app.__init__ import app
from app.web_scraper import fetch_webpage_content
from app.routes import check_compliance
from app.models import ComplianceResponse

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_check_compliance_api(monkeypatch):
    # Mock the function that fetches the webpage content
    async def mock_fetch_webpage_content(url):
        return "Sample content for compliance check including FDIC insurance."

    # Mock the compliance check function to return a sample response
    def mock_check_compliance(page_text, rules):
        non_compliant_terms = ["FDIC insurance"]
        term_suggestions = [
            {
                "term": "FDIC insurance",
                "suggestions": ["Consider using alternative terms"],
                "reason": "Avoid explicit mentions of FDIC insurance"
            }
        ]
        context_suggestions = [
            {
                "context": "Mention of FDIC insurance",
                "rule": "Rule regarding FDIC insurance",
                "reason": "Avoid explicit mentions of FDIC insurance"
            }
        ]
        return non_compliant_terms, (term_suggestions, context_suggestions)

    # Apply the monkeypatches
    monkeypatch.setattr("app.web_scraper.fetch_webpage_content", mock_fetch_webpage_content)
    monkeypatch.setattr("app.routes.check_compliance", mock_check_compliance)

    # Test the API endpoint
    response = client.post("/check_compliance", json={"url": "http://example.com"})
    assert response.status_code == 200
    assert response.json() == {
        "non_compliant_terms": ["FDIC insurance"],
        "term_suggestions": [
            {
                "term": "FDIC insurance",
                "suggestions": ["Consider using alternative terms"],
                "reason": "Avoid explicit mentions of FDIC insurance"
            }
        ],
        "context_suggestions": [
            {
                "context": "Mention of FDIC insurance",
                "rule": "Rule regarding FDIC insurance",
                "reason": "Avoid explicit mentions of FDIC insurance"
            }
        ]
    }
