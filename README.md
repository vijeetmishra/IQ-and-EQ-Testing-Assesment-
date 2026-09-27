# IQ & EQ Assessment Tool

## Overview
The **IQ & EQ Assessment Tool** is a command-line Python application that lets users test their logical reasoning (IQ) and emotional intelligence (EQ) through a series of multiple-choice questions. After completing a test, the user receives a score along with a performance tier and, when both tests are taken, a combined final report.

## Features
- **IQ Test** — 10 logic, math, and reasoning questions, each scored with instant correct/incorrect feedback.
- **EQ Test** — 20 real-life social and emotional scenarios that assess empathy, self-control, and interpersonal judgment.
- **Combined Assessment** — Run both tests back-to-back and receive a full IQ + EQ report.
- **Performance Tiers** — Automatic grading (e.g., Superior, Above Average, Average, Below Average) based on score ranges.
- **Personalized Experience** — Greets the user by name and tailors all result messages accordingly.
- **Simple Menu-Driven Interface** — Easy navigation between IQ Test, EQ Test, Both Tests, or Exit.

## Technologies/Tools Used
- **Language:** Python 3
- **Libraries:** None (uses only Python's built-in `input()` and `print()` functions — no external dependencies)
- **Interface:** Command-Line Interface (CLI)

## Installation & Setup

### Prerequisites
- Python 3.6 or higher installed on your machine

### Steps
1. **Clone or download the project**
   ```bash
   git clone https://github.com/FrostlyDeD/iq-and-eq-tester.git
   cd iq-and-eq-tester
   ```
   *(Or simply download the `.py` script file directly.)*

2. **Verify Python is installed**
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

3. **Run the application**
   ```bash
   python iq_eq_test.py
   ```
   or
   ```bash
   python3 iq_eq_test.py
   ```
   *(Replace `iq_eq_test.py` with the actual filename if different.)*

4. **Follow the on-screen prompts**
   - Enter your name when prompted.
   - Choose an option from the menu (1–4) to begin.

## Testing Instructions
Since this is an interactive CLI application, testing is done manually by running the program and exercising each path:

1. **Test the IQ flow**
   - Run the script and select option `1`.
   - Answer all 10 questions with a mix of correct and incorrect answers.
   - Confirm the score and performance tier displayed match the expected marking scheme (+1 per correct answer).

2. **Test the EQ flow**
   - Select option `2`.
   - Answer all 20 scenario-based questions.
   - Confirm the final EQ score (out of 20) and performance tier are calculated correctly.

3. **Test the combined flow**
   - Select option `3`.
   - Complete both the IQ and EQ tests in sequence.
   - Confirm the final combined report displays both scores accurately.

4. **Test input handling**
   - Enter lowercase letters (e.g., `a` instead of `A`) to confirm answers are accepted case-insensitively.
   - Enter an invalid menu choice (e.g., `5` or a letter) to confirm the "Invalid choice!" message appears.
   - Enter an invalid answer choice (e.g., `E` or a number) to confirm it is marked incorrect rather than crashing the program.

5. **Test the exit flow**
   - Select option `4` and confirm the program exits gracefully with a goodbye message.



```
----------------------------------------
        IQ & EQ ASSESSMENT PORTAL
----------------------------------------
1. 🧠 Take the IQ Test      (10 Questions)
2. 💙 Take the EQ Test      (20 Scenarios)
3. 📊 Take Both & Get Report (Full Analysis)
4. 🚪 Exit application
----------------------------------------
```