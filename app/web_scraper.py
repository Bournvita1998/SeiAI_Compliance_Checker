import requests
from bs4 import BeautifulSoup


def fetch_webpage_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error fetching webpage: {str(e)}")

    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text().lower()
