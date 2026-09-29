"""
user_manager.py
----------------
FUNCTIONAL MODULE 1: User Management
Responsible for everything about the *person* using the tool: collecting
their name, greeting them, and driving the main menu loop that decides
which assessment to hand off to.

Input  : keyboard input (name, menu choice)
Output : a validated UserSession object handed to main.py
"""

from utils import get_non_empty_name, get_menu_choice, log_event

MENU_TEXT = """
--- MAIN MENU ---
1. Take IQ Test
2. Take EQ Test
3. Take Both Tests
4. Exit
"""


class UserSession:
    """Tiny data holder for the current user (keeps state out of main.py)."""

    def __init__(self, name):
        self.name = name
        self.iq_score = None
        self.eq_score = None


def start_session():
    """Greet the user and return a new UserSession. Entry point of Module 1."""
    name = get_non_empty_name("Enter your name: ")
    print(f"\nHello, {name}! Welcome to the IQ and EQ Assessment Tool.")
    log_event(f"Session started for user '{name}'")
    return UserSession(name)


def show_menu_and_get_choice():
    """Display the main menu and return a validated choice ('1'-'4')."""
    print(MENU_TEXT)
    return get_menu_choice("Enter your choice (1-4): ")


def exit_session(session):
    """Clean exit message; also where you'd persist/close resources later."""
    print(f"\nGoodbye, {session.name}!")
    log_event(f"Session ended for user '{session.name}'")
