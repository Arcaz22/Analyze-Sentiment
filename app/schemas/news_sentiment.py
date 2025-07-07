from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class TextInput(BaseModel):
    text: str

class ArticleSentiment(BaseModel):
    title: str
    url: str
    summary: str
    sentiment: str

class SentimentAnalyzeRequest(BaseModel):
    ticker: str
    limit: Optional[int] = 1
    start_date: Optional[str] = None
    end_date: Optional[str] = None

class ArticleSentimentDetail(BaseModel):
    title: str
    url: str
    published_utc: Optional[str] = None
    sentiment: str
    sentiment_score: Optional[float] = None
    summary: Optional[str] = None

class OverallSentimentSummary(BaseModel):
    positive_count: int
    negative_count: int
    neutral_count: int
    score: float

class SentimentAnalyzeResponse(BaseModel):
    query: str
    total_articles_analyzed: int
    overall_sentiment_summary: OverallSentimentSummary
    articles: List[ArticleSentimentDetail]
