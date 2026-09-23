
from config import client, MODEL, COURSE_FEES
from tools import find_course_combinations


def agent(question):
    """Answer questions using the Groq AI model."""

    course_information = "\n".join(
        f"{course}: Rs. {fee}"
        for course, fee in COURSE_FEES.items()
    )

    combinations = find_course_combinations(30000)

    tool_results = "\n".join(combinations)

    system_prompt = f"""
You are a helpful college fee assistant.

Course fees:
{course_information}

Course combinations within Rs. 30,000:
{tool_results}

Answer the user's question using the provided information.
Explain calculations clearly and briefly.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    question = input("Ask your question: ")
    print("\nAgent:", agent(question))
    
