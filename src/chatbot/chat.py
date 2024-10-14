import os

from dotenv import load_dotenv
from openai import OpenAI

from chatbot.analysis import SentimentLabel, get_sentiment_score

load_dotenv()

type Messages = list[dict[str, str]]

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
sentiment_log: list[float] = []
messages: Messages = []


def get_user_input() -> str:
    user_input = input("User: ")

    if user_input != "exit":
        sentiment_score = get_sentiment_score(user_input)
        sentiment_log.append(sentiment_score)

    return user_input


def get_response(user_input: str, user_sentiment: SentimentLabel) -> str:
    system_prompts: dict[SentimentLabel, str] = {
        SentimentLabel.POSITIVE: "Show enthusiasm and compliment the user.",
        SentimentLabel.NEUTRAL: "Be calm, professional, and straightforward.",
        SentimentLabel.NEGATIVE: "Encourage the user to talk more about their feelings. ",
    }
    system_prompt = system_prompts[user_sentiment]

    current_messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]
    messages.extend(current_messages)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,  # type: ignore
    )

    assistant_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_reply})  # type: ignore

    if assistant_reply is None:
        return "Error retrieving response from gpt-4o."
    else:
        return assistant_reply
