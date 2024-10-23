import matplotlib.pyplot as plt
import chatbot.analysis as analysis
import chatbot.chat as chat


def main() -> None:
    user_input = chat.get_user_input()

    while user_input != "exit":
        score = analysis.get_sentiment_score(user_input=user_input)
        label = analysis.get_sentiment_label(sentiment_score=score)
        response = chat.get_response(user_input, label)

        print("Assistant: " + response)

        user_input = chat.get_user_input()

    # Create visualization
    plt.figure(figsize=(10, 6))
    plt.plot(chat.sentiment_log, marker='o')
    plt.axhline(y=0, color='r', linestyle='-', alpha=0.3)
    plt.title('Sentiment Analysis Over Time')
    plt.xlabel('Message Number')
    plt.ylabel('Sentiment Score')
    plt.grid(True, alpha=0.3)
    plt.ylim(-1, 1)  # Sentiment scores range from -1 to 1
    plt.savefig('sentiment_analysis.png')
    plt.close()
    print("\nSentiment analysis graph has been saved as 'sentiment_analysis.png'")
    print("Sentiment log:", chat.sentiment_log)


if __name__ == "__main__":
    main()
