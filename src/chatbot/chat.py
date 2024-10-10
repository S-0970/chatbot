import os

from dotenv import load_dotenv
from openai import OpenAI

from chatbot.analysis import get_sentiment_score

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
sentiment_log: list[float] = []


def get_user_input() -> str:
    user_input = input("User: ")

    if user_input != "exit":
        sentiment_score = get_sentiment_score(user_input)
        sentiment_log.append(sentiment_score)

    return user_input


def get_response(user_input: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ],
    )

    gpt_response = completion.choices[0].message.content

    if gpt_response is None:
        return "Error retrieving response from gpt-4o."
    else:
        return gpt_response
