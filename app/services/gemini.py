from google import generativeai as genai
from app.config.gemini import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def analyze_sentiment(text: str) -> str:
    prompt = f"Determine the sentiment of the following text (positive, negative, neutral):\n\n{text}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"
