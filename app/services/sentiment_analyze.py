from app.services.polygon import get_financial_news
from app.schemas.news_sentiment import SentimentAnalyzeRequest, SentimentAnalyzeResponse, ArticleSentimentDetail, OverallSentimentSummary
from app.services.gemini import analyze_sentiment
from app.utils.article import extract_sentiment_score, get_article_url, clean_symbols, normalize_whitespace, remove_html_tags

def analyze_sentiment_articles(payload: SentimentAnalyzeRequest):
    articles = get_financial_news(
        ticker=payload.ticker,
        limit=payload.limit,
        start_date=payload.start_date,
        end_date=payload.end_date
    )

    article_details = []
    pos, neg, neu = 0, 0, 0

    for article in articles:
        title = clean_symbols(normalize_whitespace(remove_html_tags(article.get("title", ""))))
        summary = clean_symbols(normalize_whitespace(remove_html_tags(article.get("description", ""))))
        combined_text = f"{title}. {summary}"
        sentiment_response = analyze_sentiment(combined_text)
        sentiment = sentiment_response.lower()
        sentiment_score = extract_sentiment_score(sentiment_response)

        if "positif" in sentiment or "positive" in sentiment:
            sentiment = "positive"
            pos += 1
        elif "negatif" in sentiment or "negative" in sentiment:
            sentiment = "negative"
            neg += 1
        elif "neutral" in sentiment:
            sentiment = "neutral"
            neu += 1
        else:
            sentiment = "unknown"

        article_details.append(ArticleSentimentDetail(
            title=title,
            url=get_article_url(article),
            published_utc=article.get("published_utc"),
            sentiment=sentiment,
            sentiment_score=sentiment_score,
            summary=summary
        ))

    total = len(article_details)
    score = (pos - neg) / total if total else 0.0

    overall = OverallSentimentSummary(
        positive_count=pos,
        negative_count=neg,
        neutral_count=neu,
        score=score
    )

    return SentimentAnalyzeResponse(
        query=payload.ticker,
        total_articles_analyzed=total,
        overall_sentiment_summary=overall,
        articles=article_details
    )
