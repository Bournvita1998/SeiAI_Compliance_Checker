import pytest
from app.web_scraper import fetch_webpage_content

@pytest.mark.asyncio
async def test_fetch_webpage_content():
    url = "https://example.com"
    content = await fetch_webpage_content(url)
    assert "example" in content.lower()
