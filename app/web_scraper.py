import httpx
from bs4 import BeautifulSoup

async def fetch_webpage_content(url: str) -> str:
    """
    Fetch the content of a webpage.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The text content of the webpage.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
        except httpx.RequestError as e:
            raise ValueError(f"Error fetching webpage: {str(e)}")

    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text().lower()
