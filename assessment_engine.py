"""
assessment_engine.py
---------------------
FUNCTIONAL MODULE 2: Assessment Engine (Data Input & Processing)
Responsible for actually running a test: showing each question from
questions_data.py, collecting a validated answer, and processing it into
a running score. This module knows nothing about grading tiers or
printing final reports -- that is report_generator.py's job (separation
of concerns supports "Maintainability").

Input  : the question bank (list of dicts) + keyboard answers
Output : an integer raw score
"""

from utils import get_answer_choice, log_event
from questions_data import IQ_QUESTIONS, EQ_QUESTIONS, IQ_CORRECT_POINTS, IQ_INCORRECT_POINTS


def run_iq_test(user_name):
    """Ask every IQ question in order and return the total IQ score."""
    print(f"\n--- Starting the IQ Test for {user_name} ---")
    score = 0

    for i, q in enumerate(IQ_QUESTIONS, start=1):
        print(f"\nQ{i}: {q['question']}")
        for label, text in q["options"]:
            print(f"{label}) {text}")

        answer = get_answer_choice()
        if answer == q["correct"]:
            print(f"Correct! +{IQ_CORRECT_POINTS} points")
            score += IQ_CORRECT_POINTS
        else:
            print(f"Incorrect! {IQ_INCORRECT_POINTS} point. (Correct answer was {q['correct']})")
            score += IQ_INCORRECT_POINTS

    log_event(f"IQ test completed for '{user_name}' — raw score {score}")
    return score


def run_eq_test(user_name):
    """Ask every EQ question in order and return the total EQ score."""
    print(f"\n--- Starting the EQ Test for {user_name} ---")
    score = 0

    for i, q in enumerate(EQ_QUESTIONS, start=1):
        print(f"\nQ{i}: {q['question']}")
        for label, (text, points) in q["options"].items():
            print(f"{label}) {text} (+{points})")

        answer = get_answer_choice("Your choice (A/B/C/D): ")
        _, points = q["options"][answer]
        score += points

    log_event(f"EQ test completed for '{user_name}' — raw score {score}")
    return score
