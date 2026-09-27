def run_iq_questions():
    
        
        
        iq_score = 0
        # --- Question 1 ---
        print("\nQ1: What is the next number in the series: 2, 4, 6, 8, ...?")
        print("A) 9")
        print("B) 10")
        print("C) 12")
        print("D) 14")
        ans1 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans1 == 'B':
            print("Correct! +1 point")
            iq_score += 1
        else:
            print("Incorrect! 0 points. (Correct answer was B)")
            iq_score += 0
            
        # --- Question 2 ---
        print("\nQ2: Which planet is known as the Red Planet?")
        print("A) Earth")
        print("B) Venus")
        print("C) Mars")
        print("D) Jupiter")
        ans2 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans2 == 'C':
            print("Correct! +1 point")
            iq_score += 1
        else:
            print("Incorrect! 0 points. (Correct answer was C)")
            iq_score += 0
            
        # --- Question 3 ---
        print("\nQ3: What is 15 + 25 * 0?")
        print("A) 0")
        print("B) 15")
        print("C) 40")
        print("D) 25")
        ans3 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans3 == 'B':
            print("Correct! +1 point")
            iq_score += 1
        else:
            print("Incorrect! 0 points. (Correct answer was B)")
            iq_score += 0
            
        # --- Question 4 ---
        print("\nQ4: Which of the following is the odd one out?")
        print("A) Dog")
        print("B) Cat")
        print("C) Cow")
        print("D) Carrot")
        ans4 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans4 == 'D':
            print("Correct! +1 point")
            iq_score += 1
        else:
            print("Incorrect! 0 points. (Correct answer was D)")
            iq_score += 0
            
        # --- Question 5 ---
        print("\nQ5: Book is to Reading as Fork is to...?")
        print("A) Eating")
        print("B) Writing")
        print("C) Running")
        print("D) Sleeping")
        ans5 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans5 == 'A':
            print("Correct! +1 point")
            iq_score += 1
        else:
            print("Incorrect! 0 points. (Correct answer was A)")
            iq_score += 0
            
        # --- Question 6 ---
        print("\nQ6: What is the next number in the series: 3, 6, 9, 12, ...?")
        print("A) 13")
        print("B) 14")
        print("C) 15")
        print("D) 18")
        ans6 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans6 == 'C':
            print("Correct! +1 point")
            iq_score += 1
        else:
            print("Incorrect! 0 points. (Correct answer was C)")
            iq_score += 0
            
        # --- Question 7 ---
        print("\nQ7: If you are facing North and turn 90 degrees to your right, which direction are you facing?")
        print("A) North")
        print("B) East")
        print("C) South")
        print("D) West")
        ans7 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans7 == 'B':
            print("Correct! +1 point")
            iq_score += 1
        else:
            print("Incorrect! 0 points. (Correct answer was B)")
            iq_score += 0
            
        # --- Question 8 ---
        print("\nQ8: What is 20% of 200?")
        print("A) 10")
        print("B) 20")
        print("C) 40")
        print("D) 50")
        ans8 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans8 == 'C':
            print("Correct! +1 point")
            iq_score += 1
        else:
            print("Incorrect! 0 points. (Correct answer was C)")
            iq_score += 0
            
        # --- Question 9 ---
        print("\nQ9: Which word does not belong with the others?")
        print("A) Apple")
        print("B) Banana")
        print("C) Carrot")
        print("D) Grape")
        ans9 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans9 == 'C':
            print("Correct! +1 point")
            iq_score += 1
        else:
            print("Incorrect! 0 points. (Correct answer was C)")
            iq_score += 0
            
        # --- Question 10 ---
        print("\nQ10: If a train travels at 60 km/h, how far will it travel in 2 hours?")
        print("A) 90 km")
        print("B) 120 km")
        print("C) 150 km")
        print("D) 180 km")
        ans10 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans10 == 'B':
            print("Correct! +1 point")
            iq_score += 1
        else:
            print("Incorrect! 0 points. (Correct answer was B)")
            iq_score += 0
            
        # --- Final IQ Result & Grading Scale ---
        print(f"\n--- IQ Test Finished ---")
        print(f"Congratulations, {n}! Your total IQ score is: {iq_score} out of 10")
        
        if iq_score >= 9:
            print("Performance Tier: Superior (Grade A+) - Exceptional logical skills!")
        elif iq_score >= 7:
            print("Performance Tier: Above Average (Grade A) - Strong reasoning capabilities!")
        elif iq_score >= 4:
            print("Performance Tier: Average (Grade B) - Standard cognitive performance.")
        elif iq_score >= 1:
            print("Performance Tier: Below Average (Grade C) - Room for improvement.")
        else:
            print("Performance Tier: Needs Practice (Grade D) - Keep practicing logic puzzles!")
        return iq_score
        
    # ==================== OPTION 2: EQ TEST ====================

    
def run_eq_questions():
        # EQ Q1
        eq_score = 0
        print("\nQ1: A colleague accidentally deletes a shared file you worked hard on.")
        print("A) Express frustration calmly and work together to recover it")
        print("B) Silently redo the work and ignore them")
        print("C) Report them immediately to HR")
        print("D) Panic and yell at them")
        eq_ans1 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans1 == 'A': eq_score += 1

        # EQ Q2
        print("\nQ2: A friend cancels plans with you at the very last minute.")
        print("A) Understand that things happen and reschedule")
        print("B) Feel slightly hurt but accept it politely")
        print("C) Tell them they are unreliable and selfish")
        print("D) Get angry and stop talking to them")
        eq_ans2 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans2 == 'A': eq_score += 1

        # EQ Q3
        print("\nQ3: You receive harsh constructive criticism on a project from your boss.")
        print("A) Listen openly, thank them, and ask for advice")
        print("B) Accept it silently while feeling resentful")
        print("C) Argue back immediately to defend your work")
        print("D) Take it personally and feel unmotivated for days")
        eq_ans3 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans3 == 'A': eq_score += 1

        # EQ Q4
        print("\nQ4: A close friend is crying, but they won't tell you why.")
        print("A) Give them space and let them know you are there for them")
        print("B) Tell other friends to find out what's wrong")
        print("C) Pester them repeatedly until they tell you")
        print("D) Walk away so they can deal with it alone")
        eq_ans4 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans4 == 'A': eq_score += 1

        # EQ Q5
        print("\nQ5: You notice a new team member sitting completely alone during lunch.")
        print("A) Walk over, introduce yourself, and invite them to join")
        print("B) Assume they prefer being alone and do nothing")
        print("C) Wait for someone else to talk to them first")
        print("D) Stare at them awkwardly from a distance")
        eq_ans5 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans5 == 'A': eq_score += 1

        # EQ Q6
        print("\nQ6: During a team debate, someone strongly disagrees with your idea.")
        print("A) Listen to their perspective calmly and find common ground")
        print("B) Agree with them just to avoid conflict")
        print("C) Interrupt them to prove why your idea is better")
        print("D) Shut down and refuse to participate further")
        eq_ans6 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans6 == 'A': eq_score += 1

        # EQ Q7
        print("\nQ7: You feel overwhelmed with heavy stress during a hectic work week.")
        print("A) Take a short break, prioritize tasks, and talk to a trusted person")
        print("B) Procrastinate and ignore your responsibilities")
        print("C) Bottle up your feelings and push through without resting")
        print("D) Take your frustration out on people around you")
        eq_ans7 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans7 == 'A': eq_score += 1

        # EQ Q8
        print("\nQ8: A friend achieves a major success, but you are currently facing a tough time.")
        print("A) Genuinely celebrate and congratulate them regardless")
        print("B) Congratulate them half-heartedly and change the subject")
        print("C) Compare your struggles to their success")
        print("D) Ignore their success because you feel jealous")
        eq_ans8 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans8 == 'A': eq_score += 1

        # EQ Q9
        print("\nQ9: Someone cuts right in front of you in a long public queue.")
        print("A) Politely point out that there is a line")
        print("B) Say nothing but glare at them angrily")
        print("C) Complain quietly to the person next to you")
        print("D) Start a loud shouting match with them")
        eq_ans9 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans9 == 'A': eq_score += 1

        # EQ Q10
        print("\nQ10: You realize you made a major mistake that negatively affected your team.")
        print("A) Own up to it immediately, apologize, and propose a solution")
        print("B) Admit it only when someone else points it out")
        print("C) Blame someone else to protect your reputation")
        print("D) Hide the mistake and hope no one notices")
        eq_ans10 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans10 == 'A': eq_score += 1

        # EQ Q11
        print("\nQ11: Your team wins an award, but you feel your individual contribution was overlooked.")
        print("A) Celebrate the team's success and discuss contributions constructively later")
        print("B) Grumble silently and feel resentful")
        print("C) Publicly demand individual recognition during the celebration")
        print("D) Refuse to attend the celebration")
        eq_ans11 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans11 == 'A': eq_score += 1

        # EQ Q12
        print("\nQ12: A coworker takes credit for your idea in a meeting.")
        print("A) Calmly clarify your contribution with facts or speak to them privately")
        print("B) Let it go to avoid awkwardness, but feel bitter")
        print("C) Interrupt and angrily accuse them of stealing your idea")
        print("D) Start taking credit for their ideas out of spite")
        eq_ans12 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans12 == 'A': eq_score += 1

        # EQ Q13
        print("\nQ13: You notice a friend is constantly posting negative, attention-seeking updates online.")
        print("A) Reach out privately to check if they are doing okay")
        print("B) Ignore their posts and scroll past")
        print("C) Leave a sarcastic comment on their post")
        print("D) Mock them to mutual friends")
        eq_ans13 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans13 == 'A': eq_score += 1

        # EQ Q14
        print("\nQ14: You are leading a group project, and two members are arguing constantly.")
        print("A) Sit them down separately to understand views and mediate a compromise")
        print("B) Tell them to sort it out themselves without your help")
        print("C) Take one person's side completely")
        print("D) Threaten to kick both out of the group angrily")
        eq_ans14 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans14 == 'A': eq_score += 1

        # EQ Q15
        print("\nQ15: Someone gives you feedback that feels unfair and overly harsh.")
        print("A) Take a deep breath, separate emotion, and look for constructive points")
        print("B) Accept it outwardly but dismiss it entirely in your mind")
        print("C) Snap back at them defensively")
        print("D) Hold a grudge against them for weeks")
        eq_ans15 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans15 == 'A': eq_score += 1

        # EQ Q16
        print("\nQ16: You make a promise to a family member, but an unexpected work emergency pops up.")
        print("A) Inform them immediately, explain sincerely, and reschedule")
        print("B) Show up very late without calling ahead")
        print("C) Ignore their calls and text later")
        print("D) Cancel completely without any explanation")
        eq_ans16 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans16 == 'A': eq_score += 1

        # EQ Q17
        print("\nQ17: You see someone struggling to carry heavy groceries through a doorway.")
        print("A) Offer a friendly hand to help them carry the load")
        print("B) Hold the door open briefly while walking past")
        print("C) Walk around them pretending not to notice")
        print("D) Laugh at their struggle")
        eq_ans17 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans17 == 'A': eq_score += 1

        # EQ Q18
        print("\nQ18: A peer shares a piece of embarrassing news about themselves in confidence.")
        print("A) Keep it strictly confidential and offer a supportive ear")
        print("B) Forget about it and never mention it again")
        print("C) Tell one close friend under the guise of secret keeping")
        print("D) Share it openly as gossip with others")
        eq_ans18 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans18 == 'A': eq_score += 1

        # EQ Q19
        print("\nQ19: You fail an important exam despite studying hard.")
        print("A) Review mistakes, acknowledge feelings, and plan a better strategy")
        print("B) Feel disappointed for a day and move on passively")
        print("C) Blame the teacher or the exam difficulty entirely")
        print("D) Give up studying altogether out of frustration")
        eq_ans19 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans19 == 'A': eq_score += 1

        # EQ Q20
        print("\nQ20: A stranger is rude to you in a service line.")
        print("A) Ignore their bad behavior, realizing they might be having a hard day")
        print("B) Give them a cold glare and look away")
        print("C) Make a snide remark back to them")
        print("D) Start a heated argument")
        eq_ans20 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans20 == 'A': eq_score += 1

        return eq_score
        # --- Final EQ Result & Clearer Grading Scale (out of 20) ---
        print("\n--- EQ Test Finished ---")
        print(f"Congratulations, {n}! Your total EQ score is: {eq_score} out of 20")

        if eq_score >= 17:          # 85% - 100%
            print("Performance Tier: High Emotional Intelligence (Grade A+) - Exceptional empathy and conflict resolution!")
        elif eq_score >= 13:        # 65% - 84%
            print("Performance Tier: Good Emotional Intelligence (Grade A) - Strong self-awareness and social skills.")
        elif eq_score >= 8:         # 40% - 64%
            print("Performance Tier: Moderate Emotional Intelligence (Grade B) - Average ability to manage interpersonal reactions.")
        else:                       # 0% - 39%
            print("Performance Tier: Developing Emotional Intelligence (Grade C) - Room for growth in empathy and emotional control.")
        return eq_score
        
        
    # ==================== OPTION 3: BOTH TESTS ====================
        # ==================== OPTION 3: BOTH TESTS ====================



n = input("Enter your name: ").strip()


print(f"\nHello, {n}! Welcome to the IQ and EQ Assessment Tool.")


while True:
    print("\n----------------------------------------")
    print("        IQ & EQ ASSESSMENT PORTAL")
    print("----------------------------------------")
    print("1. 🧠 Take the IQ Test      (10 Questions)")
    print("2. 💙 Take the EQ Test      (20 Scenarios)")
    print("3. 📊 Take Both & Get Report (Full Analysis)")
    print("4. 🚪 Exit application")
    print("----------------------------------------")

    
    
    # Get user's choice
    choice = input("Enter your choice (1-4): ").strip()
    if choice == '1':
        print(f"\n--- Starting the IQ Test for {n} ---")
        print("[Marking Scheme: Correct Answer = +1 point | Incorrect/Wrong = 0 points]")
        iq_score = run_iq_questions()
    elif choice == '2':
        print(f"\n--- Starting the EQ Test for {n} ---")
        eq_score = run_eq_questions()
    elif choice == '3':
        print(f"\n--- Starting Both IQ and EQ Assessments for {n} ---")
 
        # Run IQ Test sequence inside Option 3 -- shares the same question bank
        # and function as Option 1, with full options shown, just without
        # per-question Correct!/Incorrect! feedback.
        print("\n[PART 1: IQ TEST]")
        iq_score = run_iq_questions()
        print(f"\nIQ Part Finished: {iq_score} out of 10")
 
        # Run EQ Test sequence inside Option 3 -- shares the same question
        # bank and function as Option 2, with full options shown.
        print("\n[PART 2: EQ TEST]")
        eq_score = run_eq_questions()
        print(f"\nEQ Part Finished: {eq_score} out of 20")
 
        # --- Combined Final Report ---
        print("\n==================== FINAL REPORT ====================")
        print(f"{n}'s IQ Score: {iq_score} / 10")
        print(f"{n}'s EQ Score: {eq_score} / 20")
        print("=======================================================")

        

    elif choice == '4':
        print(f"\nGoodbye, {n}!")
        break
    else:
        print("\nInvalid choice! Please enter a number between 1 and 4.")
