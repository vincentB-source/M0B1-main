from fastapi import FastAPI, HTTPException, Form
from loguru import logger
from pydantic import BaseModel
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

app = FastAPI()

class Phrase(BaseModel):
    phrase: str

logger.add("logs/sentiment_api.log")

@app.post("/analyse_sentiment/")
async def analyse_sentiment(phrase: Phrase) -> dict[str, str]:
    logger.info(f"Route '/analyse_sentiment/' (POST) appelée avec la phrase {phrase.phrase}")

    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(phrase.phrase)

    return {"message": f"Sentiment pour la phrase {phrase.phrase} : {sentiment}"}