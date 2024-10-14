from enum import Enum

from nltk.sentiment import SentimentIntensityAnalyzer


class SentimentLabel(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


sentiment_analyzer = SentimentIntensityAnalyzer()


def get_sentiment_score(user_input: str) -> float:
    sentiment_scores = sentiment_analyzer.polarity_scores(user_input)
    return sentiment_scores["compound"]


def get_sentiment_label(sentiment_score: float) -> SentimentLabel:
    if sentiment_score >= 0.05:
        return SentimentLabel.POSITIVE

    elif sentiment_score <= -0.05:
        return SentimentLabel.NEGATIVE

    return SentimentLabel.NEUTRAL
