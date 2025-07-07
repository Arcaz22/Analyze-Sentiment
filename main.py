from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.sentiment_analyze import router as sentiment_analyze_router

app = FastAPI(
    title="GOOGLE AI STUDIO + POLYGON AI",
    description="Made by Google AI Studio and Polygon AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sentiment_analyze_router, tags=["analyze"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to AI API",
    }
