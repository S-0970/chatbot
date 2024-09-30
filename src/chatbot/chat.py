import random

from chatbot.analysis import SentimentLabel


def get_user_input() -> str:
    user_input = input("Please enter a sentence: ")
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
