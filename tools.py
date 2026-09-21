
from config import COURSE_FEES


def get_course_fee(course_code):
    """Return the fee for a course."""
    course_code = course_code.upper()

    if course_code in COURSE_FEES:
        return COURSE_FEES[course_code]

    return None


def find_course_combinations(budget):
    """Find pairs of courses within the given budget."""
    courses = list(COURSE_FEES.items())
    combinations = []

    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            course1, fee1 = courses[i]
            course2, fee2 = courses[j]

            total = fee1 + fee2

            if total <= budget:
                combinations.append(
                    f"{course1} + {course2} = Rs. {total}"
                )

    return combinations