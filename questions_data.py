"""
questions_data.py
------------------
Pure data module: the IQ and EQ question banks.
Deliberately separated from logic so the question set can grow or be
loaded from a file/DB later without touching assessment_engine.py
(supports "Maintainability" and "Scalability" non-functional requirements).

Data structures used (ties into the CSE-1 syllabus: list, dict, tuple, set):
- IQ_QUESTIONS: a list of dicts. Each dict's "options" is a tuple of
  (label, text) tuples, kept in a fixed, immutable order.
- EQ_QUESTIONS: a list of dicts. Each option maps a label to a
  (text, points) tuple, since each EQ answer awards a different score.
- IQ_ANSWER_KEY: a set of the correct labels used only for a quick
  "how many did they get right" pass in report_generator.py.
"""

IQ_QUESTIONS = [
    {
        "question": "What is the next number in the series: 2, 4, 6, 8, ...?",
        "options": (("A", "9"), ("B", "10"), ("C", "12"), ("D", "14")),
        "correct": "B",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": (("A", "Earth"), ("B", "Venus"), ("C", "Mars"), ("D", "Jupiter")),
        "correct": "C",
    },
    {
        "question": "What is 15 + 25 * 0?",
        "options": (("A", "0"), ("B", "15"), ("C", "40"), ("D", "25")),
        "correct": "B",
    },
    {
        "question": "Which of the following is the odd one out?",
        "options": (("A", "Dog"), ("B", "Cat"), ("C", "Cow"), ("D", "Carrot")),
        "correct": "D",
    },
    {
        "question": "Book is to Reading as Fork is to...?",
        "options": (("A", "Eating"), ("B", "Writing"), ("C", "Running"), ("D", "Sleeping")),
        "correct": "A",
    },
    {
        "question": "What is the next number in the series: 3, 6, 9, 12, ...?",
        "options": (("A", "13"), ("B", "14"), ("C", "15"), ("D", "18")),
        "correct": "C",
    },
    {
        "question": "If you are facing North and turn 90 degrees to your right, which direction are you facing?",
        "options": (("A", "North"), ("B", "East"), ("C", "South"), ("D", "West")),
        "correct": "B",
    },
    {
        "question": "What is 20% of 200?",
        "options": (("A", "10"), ("B", "20"), ("C", "40"), ("D", "50")),
        "correct": "C",
    },
    {
        "question": "Which word does not belong with the others?",
        "options": (("A", "Apple"), ("B", "Banana"), ("C", "Carrot"), ("D", "Grape")),
        "correct": "C",
    },
    {
        "question": "If a train travels at 60 km/h, how far will it travel in 2 hours?",
        "options": (("A", "90 km"), ("B", "120 km"), ("C", "150 km"), ("D", "180 km")),
        "correct": "B",
    },
]

# Quick-lookup set of correct labels is not meaningful across questions
# (each question has its own correct label), so instead we expose the
# scoring rule as constants used by assessment_engine.py.
IQ_CORRECT_POINTS = 4
IQ_INCORRECT_POINTS = -1

EQ_QUESTIONS = [
    {
        "question": "A colleague accidentally deletes a shared file you worked hard on.",
        "options": {
            "A": ("Express frustration calmly and work together to recover it", 4),
            "B": ("Silently redo the work and ignore them", 2),
            "C": ("Report them immediately to HR", 1),
            "D": ("Panic and yell at them", 0),
        },
    },
    {
        "question": "A friend cancels plans with you at the very last minute.",
        "options": {
            "A": ("Understand that things happen and reschedule", 4),
            "B": ("Feel slightly hurt but accept it politely", 2),
            "C": ("Tell them they are unreliable and selfish", 1),
            "D": ("Get angry and stop talking to them", 0),
        },
    },
    {
        "question": "You receive harsh constructive criticism on a project from your boss.",
        "options": {
            "A": ("Listen openly, thank them, and ask for advice", 4),
            "B": ("Accept it silently while feeling resentful", 2),
            "C": ("Argue back immediately to defend your work", 1),
            "D": ("Take it personally and feel unmotivated for days", 0),
        },
    },
    {
        "question": "A close friend is crying, but they won't tell you why.",
        "options": {
            "A": ("Give them space and let them know you are there for them", 4),
            "B": ("Tell other friends to find out what's wrong", 2),
            "C": ("Pester them repeatedly until they tell you", 1),
            "D": ("Walk away so they can deal with it alone", 0),
        },
    },
    {
        "question": "You notice a new team member sitting completely alone during lunch.",
        "options": {
            "A": ("Walk over, introduce yourself, and invite them to join", 4),
            "B": ("Assume they prefer being alone and do nothing", 2),
            "C": ("Wait for someone else to talk to them first", 1),
            "D": ("Stare at them awkwardly from a distance", 0),
        },
    },
    {
        "question": "During a team debate, someone strongly disagrees with your idea.",
        "options": {
            "A": ("Listen to their perspective calmly and find common ground", 4),
            "B": ("Agree with them just to avoid conflict", 2),
            "C": ("Interrupt them to prove why your idea is better", 1),
            "D": ("Shut down and refuse to participate further", 0),
        },
    },
    {
        "question": "You feel overwhelmed with heavy stress during a hectic work week.",
        "options": {
            "A": ("Take a short break, prioritize tasks, and talk to a trusted person", 4),
            "B": ("Procrastinate and ignore your responsibilities", 2),
            "C": ("Bottle up your feelings and push through without resting", 1),
            "D": ("Take your frustration out on people around you", 0),
        },
    },
    {
        "question": "A friend achieves a major success, but you are currently facing a tough time.",
        "options": {
            "A": ("Genuinely celebrate and congratulate them regardless", 4),
            "B": ("Congratulate them half-heartedly and change the subject", 2),
            "C": ("Compare your struggles to their success", 1),
            "D": ("Ignore their success because you feel jealous", 0),
        },
    },
    {
        "question": "Someone cuts right in front of you in a long public queue.",
        "options": {
            "A": ("Politely point out that there is a line", 4),
            "B": ("Say nothing but glare at them angrily", 2),
            "C": ("Complain quietly to the person next to you", 1),
            "D": ("Start a loud shouting match with them", 0),
        },
    },
    {
        "question": "You realize you made a major mistake that negatively affected your team.",
        "options": {
            "A": ("Own up to it immediately, apologize, and propose a solution", 4),
            "B": ("Admit it only when someone else points it out", 2),
            "C": ("Blame someone else to protect your reputation", 1),
            "D": ("Hide the mistake and hope no one notices", 0),
        },
    },
    {
        "question": "Your team wins an award, but you feel your individual contribution was overlooked.",
        "options": {
            "A": ("Celebrate the team's success and discuss contributions constructively later", 4),
            "B": ("Grumble silently and feel resentful", 2),
            "C": ("Publicly demand individual recognition during the celebration", 1),
            "D": ("Refuse to attend the celebration", 0),
        },
    },
    {
        "question": "A coworker takes credit for your idea in a meeting.",
        "options": {
            "A": ("Calmly clarify your contribution with facts or speak to them privately", 4),
            "B": ("Let it go to avoid awkwardness, but feel bitter", 2),
            "C": ("Interrupt and angrily accuse them of stealing your idea", 1),
            "D": ("Start taking credit for their ideas out of spite", 0),
        },
    },
    {
        "question": "You notice a friend is constantly posting negative, attention-seeking updates online.",
        "options": {
            "A": ("Reach out privately to check if they are doing okay", 4),
            "B": ("Ignore their posts and scroll past", 2),
            "C": ("Leave a sarcastic comment on their post", 1),
            "D": ("Mock them to mutual friends", 0),
        },
    },
    {
        "question": "You are leading a group project, and two members are arguing constantly.",
        "options": {
            "A": ("Sit them down separately to understand views and mediate a compromise", 4),
            "B": ("Tell them to sort it out themselves without your help", 2),
            "C": ("Take one person's side completely", 1),
            "D": ("Threaten to kick both out of the group angrily", 0),
        },
    },
    {
        "question": "Someone gives you feedback that feels unfair and overly harsh.",
        "options": {
            "A": ("Take a deep breath, separate emotion, and look for constructive points", 4),
            "B": ("Accept it outwardly but dismiss it entirely in your mind", 2),
            "C": ("Snap back at them defensively", 1),
            "D": ("Hold a grudge against them for weeks", 0),
        },
    },
    {
        "question": "You make a promise to a family member, but an unexpected work emergency pops up.",
        "options": {
            "A": ("Inform them immediately, explain sincerely, and reschedule", 4),
            "B": ("Show up very late without calling ahead", 2),
            "C": ("Ignore their calls and text later", 1),
            "D": ("Cancel completely without any explanation", 0),
        },
    },
    {
        "question": "You see someone struggling to carry heavy groceries through a doorway.",
        "options": {
            "A": ("Offer a friendly hand to help them carry the load", 4),
            "B": ("Hold the door open briefly while walking past", 2),
            "C": ("Walk around them pretending not to notice", 1),
            "D": ("Laugh at their struggle", 0),
        },
    },
    {
        "question": "A peer shares a piece of embarrassing news about themselves in confidence.",
        "options": {
            "A": ("Keep it strictly confidential and offer a supportive ear", 4),
            "B": ("Forget about it and never mention it again", 2),
            "C": ("Tell one close friend under the guise of secret keeping", 1),
            "D": ("Share it openly as gossip with others", 0),
        },
    },
    {
        "question": "You fail an important exam despite studying hard.",
        "options": {
            "A": ("Review mistakes, acknowledge feelings, and plan a better strategy", 4),
            "B": ("Feel disappointed for a day and move on passively", 2),
            "C": ("Blame the teacher or the exam difficulty entirely", 1),
            "D": ("Give up studying altogether out of frustration", 0),
        },
    },
    {
        "question": "A stranger is rude to you in a service line.",
        "options": {
            "A": ("Ignore their bad behavior, realizing they might be having a hard day", 4),
            "B": ("Give them a cold glare and look away", 2),
            "C": ("Make a snide remark back to them", 1),
            "D": ("Start a heated argument", 0),
        },
    },
]

IQ_MAX_SCORE = len(IQ_QUESTIONS) * IQ_CORRECT_POINTS  # 40
EQ_MAX_SCORE = len(EQ_QUESTIONS) * 4  # 80
