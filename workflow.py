
from config import COURSE_FEES


def workflow(question):
    question = question.lower()

    if "ai202" in question and "fee" in question:
        return "The fee for AI202 is Rs. 18,000."

    if "total" in question and "scholarship" in question:
        total = COURSE_FEES["CS101"] + COURSE_FEES["AI202"]
        discounted_fee = total * 0.90
        return f"Total after 10% scholarship: Rs. {discounted_fee:.0f}"

    if "ds303" in question and "cs101" in question:
        difference = COURSE_FEES["DS303"] - COURSE_FEES["CS101"]
        return f"DS303 is Rs. {difference} more expensive than CS101."

    return "The workflow has no rule for this question."