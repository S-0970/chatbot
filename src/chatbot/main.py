import chatbot.analysis as analysis
import chatbot.chat as chat


def main() -> None:
    user_input = chat.get_user_input()

    while user_input != "exit":
        score = analysis.get_sentiment_score(user_input=user_input)
        label = analysis.get_sentiment_label(sentiment_score=score)
        response = chat.get_response(sentiment_label=label)

        print(response)

        user_input = chat.get_user_input()

    print(chat.sentiment_log)


if __name__ == "__main__":
    main()
