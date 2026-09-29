"""
report_generator.py
--------------------
FUNCTIONAL MODULE 3: Reporting & Analytics
Responsible for turning raw scores (from assessment_engine.py) into
human-readable results: performance tiers, a combined summary table,
and an optional saved report file for the user's records.

Input  : raw IQ / EQ scores (int)
Output : printed report + results.txt on disk
"""

from questions_data import IQ_MAX_SCORE, EQ_MAX_SCORE
from utils import log_event


def iq_tier(score):
    if score >= 32:
        return "Superior (Grade A+) - Exceptional logical skills!"
    elif score >= 22:
        return "Above Average (Grade A) - Strong reasoning capabilities!"
    elif score >= 10:
        return "Average (Grade B) - Standard cognitive performance."
    elif score >= 0:
        return "Below Average (Grade C) - Room for improvement."
    else:
        return "Needs Practice (Grade D) - Keep practicing logic puzzles!"


def eq_tier(score):
    if score >= 64:
        return "High Emotional Intelligence (Grade A+) - Exceptional empathy and conflict resolution!"
    elif score >= 48:
        return "Good Emotional Intelligence (Grade A) - Strong self-awareness and social skills."
    elif score >= 30:
        return "Moderate Emotional Intelligence (Grade B) - Average ability to manage interpersonal reactions."
    else:
        return "Developing Emotional Intelligence (Grade C) - Room for growth in empathy and emotional control."


def report_iq(user_name, score):
    print(f"\n--- IQ Test Finished ---")
    print(f"Congratulations, {user_name}! Your total IQ score is: {score} out of {IQ_MAX_SCORE}")
    print(f"Performance Tier: {iq_tier(score)}")


def report_eq(user_name, score):
    print("\n--- EQ Test Finished ---")
    print(f"Congratulations, {user_name}! Your total EQ score is: {score} out of {EQ_MAX_SCORE}")
    print(f"Performance Tier: {eq_tier(score)}")


def report_combined(user_name, iq_score, eq_score):
    """Print the combined summary table and save it to results.txt."""
    lines = []
    lines.append("=" * 46)
    lines.append(f"          FINAL ASSESSMENT REPORT FOR {user_name.upper()}")
    lines.append("=" * 46)
    lines.append(f"{'Category':<10} | {'Score':<10} | {'Max Score':<10} | Performance Tier")
    lines.append("-" * 65)
    lines.append(f"{'IQ Test':<10} | {iq_score:<10} | {IQ_MAX_SCORE:<10} | {iq_tier(iq_score)}")
    lines.append(f"{'EQ Test':<10} | {eq_score:<10} | {EQ_MAX_SCORE:<10} | {eq_tier(eq_score)}")
    lines.append("=" * 46)

    report_text = "\n".join(lines)
    print("\n" + report_text)
    _save_report(user_name, report_text)


def _save_report(user_name, report_text):
    """
    Persist the report to disk (resource-efficient: append, don't reload
    the whole file). Wrapped in try/except per the error-handling
    non-functional requirement -- a failed save should never crash the app.
    """
    try:
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(report_text + "\n\n")
        log_event(f"Report for '{user_name}' saved to results.txt")
    except OSError as e:
        print(f"(Note: could not save report to file — {e})")
        log_event(f"Failed to save report for '{user_name}': {e}")
