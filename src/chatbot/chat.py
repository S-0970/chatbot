import os
import random

from dotenv import load_dotenv
from openai import OpenAI

from chatbot.analysis import SentimentLabel, get_sentiment_score

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
sentiment_log: list[float] = []


def get_user_input() -> str:
    user_input = input("Please enter a sentence: ")

    if user_input != "exit":
        sentiment_score = get_sentiment_score(user_input)
        sentiment_log.append(sentiment_score)

    return user_input


def get_response(sentiment_label: SentimentLabel) -> str:
    responses = {
        SentimentLabel.POSITIVE: ["nice", "great"],
        SentimentLabel.NEGATIVE: ["womp womp", "u suck"],
        SentimentLabel.NEUTRAL: ["ok cool", "how uneventful"],
    }

    # get the list of responses for the associated sentiment label
    choices = responses[sentiment_label]

    # pick one of the options in the list of responses for that sentiment label
    choice = random.choice(choices)
    return choice
