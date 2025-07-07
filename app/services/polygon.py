import os
import requests
from dotenv import load_dotenv

load_dotenv()
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
BASE_URL = os.getenv("BASE_REFERENCE_URL")

def get_financial_news(ticker: str, limit: int = 3, start_date: str = None, end_date: str = None):
    params = {
        "ticker": ticker.upper(),
        "limit": limit,
        "apiKey": POLYGON_API_KEY
    }
    if start_date:
        params["published_utc.gte"] = start_date
    if end_date:
        params["published_utc.lte"] = end_date

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json().get("results", [])
