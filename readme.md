# GOOGLE AI STUDIO + POLYGON AI

This API combines Google AI Studio (model Gemini-1.5-flash) and Polygon AI for FastAPI-based financial news sentiment analysis

## Feature

- **Text Sentiment Analysis**:Determines the sentiment (positive, negative, neutral) of input text
- **Financial News Ticker**: Fetching the latest financial news based on stock tickers from Polygon API
- **Ticker News Sentiment Analysis**: Analyze sentiment from a collection of news related to a particular ticker

## Installation

1. **Clone repository and install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Configuration environment:**
    - Copy `.env.example` to `.env` and fill in your API key:
        ```
        GOOGLE_API_KEY=...
        POLYGON_API_KEY=...
        BASE_REFERENCE_URL=https://api.polygon.io/v2/reference/news
        ```

## Running the Server

```sh
uvicorn main:app --reload
```

## Endpoint API

### 1. Random Text Sentiment Analysis(title, content, etc) using Google AI

- **POST** `/sentiment/analyze-sentiment`
- **Body:**
    ```json
    {
      "text": "Oversubscribed 400 Times, On FOMO CDIA IPO Stocks?"
    }
    ```
- **Response:**
    ```json
    {
      "sentiment": "The sentiment is **positive**. \"Oversubscribed 400 times\" indicates high demand and is generally considered a positive sign for an IPO. The question at the end adds a bit of speculation (\"FOMO?\"), but the overall tone is optimistic."
    }
    ```

### 2. Financial News By Ticker using Polygon AI

- **GET** `/sentiment/news/{ticker}?limit=2&start_date=2025-04-07&end_date=2025-04-07`
- **Contoh:**
    ```
    http://127.0.0.1:8000/sentiment/news/AAPL?limit=2&start_date=2025-04-07&end_date=2025-04-07
    ```
- **Response:**
    ```json
    [
      {
        "id": "...",
        "publisher": { "name": "...", ... },
        "title": "...",
        "author": "...",
        "published_utc": "...",
        "article_url": "...",
        "tickers": ["AAPL", "AMZN"],
        "description": "...",
        "insights": [
          {
            "ticker": "AMZN",
            "sentiment": "positive",
            "sentiment_reasoning": "..."
          },
          ...
        ]
      },
      ...
    ]
    ```

### 3. Take data from Polygon AI and provide sentiment assessment using Google AI

- **POST** `/sentiment/analyze-news-ticker`
- **Body:**
    ```json
    {
      "ticker": "NVDA",
      "limit": 3,
      "start_date": "2025-04-07",
      "end_date": "2025-04-07"
    }
    ```
- **Response:**
    ```json
    {
      "query": "NVDA",
      "total_articles_analyzed": 3,
      "overall_sentiment_summary": {
        "positive_count": 3,
        "negative_count": 0,
        "neutral_count": 0,
        "score": 1
      },
      "articles": [
        {
          "title": "...",
          "url": "...",
          "published_utc": "...",
          "sentiment": "positive",
          "sentiment_score": 3.5,
          "summary": "..."
        },
        ...
      ]
    }
    ```
