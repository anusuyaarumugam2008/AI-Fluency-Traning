import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "day1")
    )
)

from agent import agent 
QUESTION = ("Which is cheaper: CS101 and AI202 with a 10% scholarship, "
            "or all three courses with a 25% scholarship? By how much?")
 
print("QUESTION:", QUESTION, "\n")
print("--- the agent's actions and observations ---")
answer = agent(QUESTION)
print("\nFINAL ANSWER:", answer)
