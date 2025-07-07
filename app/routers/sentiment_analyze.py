from fastapi import APIRouter, status, Query
from app.schemas.news_sentiment import (
    TextInput,
    SentimentAnalyzeRequest,
    SentimentAnalyzeResponse
)
from app.services.gemini import analyze_sentiment
from app.services.polygon import get_financial_news
from app.services.sentiment_analyze import analyze_sentiment_articles

router = APIRouter(prefix="/sentiment")

@router.post("/analyze-sentiment", status_code=status.HTTP_200_OK)
def analyze_text_sentiment(input: TextInput):
    result = analyze_sentiment(input.text)
    return {"sentiment": result}

@router.get("/news/{ticker}", status_code=status.HTTP_200_OK)
def get_ticker_news(
    ticker: str,
    limit: int = Query(3, ge=1, le=20),
    start_date: str = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: str = Query(None, description="End date (YYYY-MM-DD)")
):
    return get_financial_news(ticker, limit=limit, start_date=start_date, end_date=end_date)

@router.post("/analyze-news-ticker", response_model=SentimentAnalyzeResponse, status_code=status.HTTP_200_OK)
def analyze_sentiment_route(payload: SentimentAnalyzeRequest):
    return analyze_sentiment_articles(payload)
