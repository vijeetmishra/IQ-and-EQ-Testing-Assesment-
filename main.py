"""
main.py
-------
Entry point. Wires the three functional modules together:
  1. user_manager      -> who is using the tool, what do they want to do
  2. assessment_engine  -> run the chosen test(s), get raw scores
  3. report_generator   -> turn raw scores into a graded report

Run with: python main.py
"""

import user_manager
import assessment_engine
import report_generator


def main():
    session = user_manager.start_session()

    while True:
        choice = user_manager.show_menu_and_get_choice()

        if choice == "1":
            session.iq_score = assessment_engine.run_iq_test(session.name)
            report_generator.report_iq(session.name, session.iq_score)
            break

        elif choice == "2":
            session.eq_score = assessment_engine.run_eq_test(session.name)
            report_generator.report_eq(session.name, session.eq_score)
            break

        elif choice == "3":
            print(f"\n--- Starting Both IQ and EQ Assessments for {session.name} ---")
            print("\n[PART 1: IQ TEST]")
            session.iq_score = assessment_engine.run_iq_test(session.name)

            print("\n[PART 2: EQ TEST]")
            session.eq_score = assessment_engine.run_eq_test(session.name)

            report_generator.report_combined(session.name, session.iq_score, session.eq_score)
            break

        elif choice == "4":
            user_manager.exit_session(session)
            break


if __name__ == "__main__":
    main()
