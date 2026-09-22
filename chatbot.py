
from config import client, MODEL, banner


def ask_chatbot(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful college FAQ chatbot."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    banner("Basic Chatbot")

    while True:
        question = input("You: ")

        if question.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        answer = ask_chatbot(question)
        print("Chatbot:", answer)