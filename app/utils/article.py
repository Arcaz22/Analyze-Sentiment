import re

def remove_html_tags(text: str) -> str:
    return re.sub(r'<[^>]+>', '', text or "")

def normalize_whitespace(text: str) -> str:
    return re.sub(r'\s+', ' ', text or "").strip()

def clean_symbols(text: str) -> str:
    return re.sub(r'[^\w\s.,:;!?\'"-]', '', text)

def extract_sentiment_score(response_text: str):

    match = re.search(r'([-+]?\d*\.\d+|\d+)', response_text)
    if match:
        try:
            return float(match.group(0))
        except Exception:
            return None
    return None

def get_article_url(article: dict):
    for key in ["url", "article_url", "source_url"]:
        if key in article and article[key]:
            return article[key]
    return ""
