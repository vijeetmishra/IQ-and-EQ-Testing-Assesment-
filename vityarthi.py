# Step 1: Get the user's name
n = input("Enter your name: ").strip()

# Step 2: Greet the user
print(f"\nHello, {n}! Welcome to the IQ and EQ Assessment Tool.")

# Step 3: Show the menu loop
while True:
    print("\n--- MAIN MENU ---")
    print("1. Take IQ Test")
    print("2. Take EQ Test")
    print("3. Take Both Tests")
    print("4. Exit")
    
    # Get user's choice
    choice = input("Enter your choice (1-4): ").strip()
    
    # ==================== OPTION 1: IQ TEST ====================
    if choice == '1':
        print(f"\n--- Starting the IQ Test for {n} ---")
        iq_score = 0
        
        # --- Question 1 ---
        print("\nQ1: What is the next number in the series: 2, 4, 6, 8, ...?")
        print("A) 9")
        print("B) 10")
        print("C) 12")
        print("D) 14")
        ans1 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans1 == 'B':
            print("Correct! +4 points")
            iq_score += 4
        else:
            print("Incorrect! -1 point. (Correct answer was B)")
            iq_score -= 1
            
        # --- Question 2 ---
        print("\nQ2: Which planet is known as the Red Planet?")
        print("A) Earth")
        print("B) Venus")
        print("C) Mars")
        print("D) Jupiter")
        ans2 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans2 == 'C':
            print("Correct! +4 points")
            iq_score += 4
        else:
            print("Incorrect! -1 point. (Correct answer was C)")
            iq_score -= 1
            
        # --- Question 3 ---
        print("\nQ3: What is 15 + 25 * 0?")
        print("A) 0")
        print("B) 15")
        print("C) 40")
        print("D) 25")
        ans3 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans3 == 'B':
            print("Correct! +4 points")
            iq_score += 4
        else:
            print("Incorrect! -1 point. (Correct answer was B)")
            iq_score -= 1
            
        # --- Question 4 ---
        print("\nQ4: Which of the following is the odd one out?")
        print("A) Dog")
        print("B) Cat")
        print("C) Cow")
        print("D) Carrot")
        ans4 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans4 == 'D':
            print("Correct! +4 points")
            iq_score += 4
        else:
            print("Incorrect! -1 point. (Correct answer was D)")
            iq_score -= 1
            
        # --- Question 5 ---
        print("\nQ5: Book is to Reading as Fork is to...?")
        print("A) Eating")
        print("B) Writing")
        print("C) Running")
        print("D) Sleeping")
        ans5 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans5 == 'A':
            print("Correct! +4 points")
            iq_score += 4
        else:
            print("Incorrect! -1 point. (Correct answer was A)")
            iq_score -= 1
            
        # --- Question 6 ---
        print("\nQ6: What is the next number in the series: 3, 6, 9, 12, ...?")
        print("A) 13")
        print("B) 14")
        print("C) 15")
        print("D) 18")
        ans6 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans6 == 'C':
            print("Correct! +4 points")
            iq_score += 4
        else:
            print("Incorrect! -1 point. (Correct answer was C)")
            iq_score -= 1
            
        # --- Question 7 ---
        print("\nQ7: If you are facing North and turn 90 degrees to your right, which direction are you facing?")
        print("A) North")
        print("B) East")
        print("C) South")
        print("D) West")
        ans7 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans7 == 'B':
            print("Correct! +4 points")
            iq_score += 4
        else:
            print("Incorrect! -1 point. (Correct answer was B)")
            iq_score -= 1
            
        # --- Question 8 ---
        print("\nQ8: What is 20% of 200?")
        print("A) 10")
        print("B) 20")
        print("C) 40")
        print("D) 50")
        ans8 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans8 == 'C':
            print("Correct! +4 points")
            iq_score += 4
        else:
            print("Incorrect! -1 point. (Correct answer was C)")
            iq_score -= 1
            
        # --- Question 9 ---
        print("\nQ9: Which word does not belong with the others?")
        print("A) Apple")
        print("B) Banana")
        print("C) Carrot")
        print("D) Grape")
        ans9 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans9 == 'C':
            print("Correct! +4 points")
            iq_score += 4
        else:
            print("Incorrect! -1 point. (Correct answer was C)")
            iq_score -= 1
            
        # --- Question 10 ---
        print("\nQ10: If a train travels at 60 km/h, how far will it travel in 2 hours?")
        print("A) 90 km")
        print("B) 120 km")
        print("C) 150 km")
        print("D) 180 km")
        ans10 = input("Your answer (A/B/C/D): ").strip().upper()
        if ans10 == 'B':
            print("Correct! +4 points")
            iq_score += 4
        else:
            print("Incorrect! -1 point. (Correct answer was B)")
            iq_score -= 1
            
        # --- Final IQ Result & Grading Scale ---
        print(f"\n--- IQ Test Finished ---")
        print(f"Congratulations, {n}! Your total IQ score is: {iq_score} out of 40")
        
        if iq_score >= 32:
            print("Performance Tier: Superior (Grade A+) - Exceptional logical skills!")
        elif iq_score >= 22:
            print("Performance Tier: Above Average (Grade A) - Strong reasoning capabilities!")
        elif iq_score >= 10:
            print("Performance Tier: Average (Grade B) - Standard cognitive performance.")
        elif iq_score >= 0:
            print("Performance Tier: Below Average (Grade C) - Room for improvement.")
        else:
            print("Performance Tier: Needs Practice (Grade D) - Keep practicing logic puzzles!")
            
        break
        
    # ==================== OPTION 2: EQ TEST ====================
    elif choice == '2':
        print(f"\n--- Starting the EQ Test for {n} ---")
        eq_score = 0
        
        # EQ Q1
        print("\nQ1: A colleague accidentally deletes a shared file you worked hard on.")
        print("A) Express frustration calmly and work together to recover it (+4)")
        print("B) Silently redo the work and ignore them (+2)")
        print("C) Report them immediately to HR (+1)")
        print("D) Panic and yell at them (0)")
        eq_ans1 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans1 == 'A': eq_score += 4
        elif eq_ans1 == 'B': eq_score += 2
        elif eq_ans1 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q2
        print("\nQ2: A friend cancels plans with you at the very last minute.")
        print("A) Understand that things happen and reschedule (+4)")
        print("B) Feel slightly hurt but accept it politely (+2)")
        print("C) Tell them they are unreliable and selfish (+1)")
        print("D) Get angry and stop talking to them (0)")
        eq_ans2 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans2 == 'A': eq_score += 4
        elif eq_ans2 == 'B': eq_score += 2
        elif eq_ans2 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q3
        print("\nQ3: You receive harsh constructive criticism on a project from your boss.")
        print("A) Listen openly, thank them, and ask for advice (+4)")
        print("B) Accept it silently while feeling resentful (+2)")
        print("C) Argue back immediately to defend your work (+1)")
        print("D) Take it personally and feel unmotivated for days (0)")
        eq_ans3 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans3 == 'A': eq_score += 4
        elif eq_ans3 == 'B': eq_score += 2
        elif eq_ans3 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q4
        print("\nQ4: A close friend is crying, but they won't tell you why.")
        print("A) Give them space and let them know you are there for them (+4)")
        print("B) Tell other friends to find out what's wrong (+2)")
        print("C) Pester them repeatedly until they tell you (+1)")
        print("D) Walk away so they can deal with it alone (0)")
        eq_ans4 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans4 == 'A': eq_score += 4
        elif eq_ans4 == 'B': eq_score += 2
        elif eq_ans4 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q5
        print("\nQ5: You notice a new team member sitting completely alone during lunch.")
        print("A) Walk over, introduce yourself, and invite them to join (+4)")
        print("B) Assume they prefer being alone and do nothing (+2)")
        print("C) Wait for someone else to talk to them first (+1)")
        print("D) Stare at them awkwardly from a distance (0)")
        eq_ans5 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans5 == 'A': eq_score += 4
        elif eq_ans5 == 'B': eq_score += 2
        elif eq_ans5 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q6
        print("\nQ6: During a team debate, someone strongly disagrees with your idea.")
        print("A) Listen to their perspective calmly and find common ground (+4)")
        print("B) Agree with them just to avoid conflict (+2)")
        print("C) Interrupt them to prove why your idea is better (+1)")
        print("D) Shut down and refuse to participate further (0)")
        eq_ans6 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans6 == 'A': eq_score += 4
        elif eq_ans6 == 'B': eq_score += 2
        elif eq_ans6 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q7
        print("\nQ7: You feel overwhelmed with heavy stress during a hectic work week.")
        print("A) Take a short break, prioritize tasks, and talk to a trusted person (+4)")
        print("B) Procrastinate and ignore your responsibilities (+2)")
        print("C) Bottle up your feelings and push through without resting (+1)")
        print("D) Take your frustration out on people around you (0)")
        eq_ans7 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans7 == 'A': eq_score += 4
        elif eq_ans7 == 'B': eq_score += 2
        elif eq_ans7 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q8
        print("\nQ8: A friend achieves a major success, but you are currently facing a tough time.")
        print("A) Genuinely celebrate and congratulate them regardless (+4)")
        print("B) Congratulate them half-heartedly and change the subject (+2)")
        print("C) Compare your struggles to their success (+1)")
        print("D) Ignore their success because you feel jealous (0)")
        eq_ans8 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans8 == 'A': eq_score += 4
        elif eq_ans8 == 'B': eq_score += 2
        elif eq_ans8 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q9
        print("\nQ9: Someone cuts right in front of you in a long public queue.")
        print("A) Politely point out that there is a line (+4)")
        print("B) Say nothing but glare at them angrily (+2)")
        print("C) Complain quietly to the person next to you (+1)")
        print("D) Start a loud shouting match with them (0)")
        eq_ans9 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans9 == 'A': eq_score += 4
        elif eq_ans9 == 'B': eq_score += 2
        elif eq_ans9 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q10
        print("\nQ10: You realize you made a major mistake that negatively affected your team.")
        print("A) Own up to it immediately, apologize, and propose a solution (+4)")
        print("B) Admit it only when someone else points it out (+2)")
        print("C) Blame someone else to protect your reputation (+1)")
        print("D) Hide the mistake and hope no one notices (0)")
        eq_ans10 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans10 == 'A': eq_score += 4
        elif eq_ans10 == 'B': eq_score += 2
        elif eq_ans10 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q11
        print("\nQ11: Your team wins an award, but you feel your individual contribution was overlooked.")
        print("A) Celebrate the team's success and discuss contributions constructively later (+4)")
        print("B) Grumble silently and feel resentful (+2)")
        print("C) Publicly demand individual recognition during the celebration (+1)")
        print("D) Refuse to attend the celebration (0)")
        eq_ans11 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans11 == 'A': eq_score += 4
        elif eq_ans11 == 'B': eq_score += 2
        elif eq_ans11 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q12
        print("\nQ12: A coworker takes credit for your idea in a meeting.")
        print("A) Calmly clarify your contribution with facts or speak to them privately (+4)")
        print("B) Let it go to avoid awkwardness, but feel bitter (+2)")
        print("C) Interrupt and angrily accuse them of stealing your idea (+1)")
        print("D) Start taking credit for their ideas out of spite (0)")
        eq_ans12 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans12 == 'A': eq_score += 4
        elif eq_ans12 == 'B': eq_score += 2
        elif eq_ans12 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q13
        print("\nQ13: You notice a friend is constantly posting negative, attention-seeking updates online.")
        print("A) Reach out privately to check if they are doing okay (+4)")
        print("B) Ignore their posts and scroll past (+2)")
        print("C) Leave a sarcastic comment on their post (+1)")
        print("D) Mock them to mutual friends (0)")
        eq_ans13 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans13 == 'A': eq_score += 4
        elif eq_ans13 == 'B': eq_score += 2
        elif eq_ans13 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q14
        print("\nQ14: You are leading a group project, and two members are arguing constantly.")
        print("A) Sit them down separately to understand views and mediate a compromise (+4)")
        print("B) Tell them to sort it out themselves without your help (+2)")
        print("C) Take one person's side completely (+1)")
        print("D) Threaten to kick both out of the group angrily (0)")
        eq_ans14 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans14 == 'A': eq_score += 4
        elif eq_ans14 == 'B': eq_score += 2
        elif eq_ans14 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q15
        print("\nQ15: Someone gives you feedback that feels unfair and overly harsh.")
        print("A) Take a deep breath, separate emotion, and look for constructive points (+4)")
        print("B) Accept it outwardly but dismiss it entirely in your mind (+2)")
        print("C) Snap back at them defensively (+1)")
        print("D) Hold a grudge against them for weeks (0)")
        eq_ans15 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans15 == 'A': eq_score += 4
        elif eq_ans15 == 'B': eq_score += 2
        elif eq_ans15 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q16
        print("\nQ16: You make a promise to a family member, but an unexpected work emergency pops up.")
        print("A) Inform them immediately, explain sincerely, and reschedule (+4)")
        print("B) Show up very late without calling ahead (+2)")
        print("C) Ignore their calls and text later (+1)")
        print("D) Cancel completely without any explanation (0)")
        eq_ans16 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans16 == 'A': eq_score += 4
        elif eq_ans16 == 'B': eq_score += 2
        elif eq_ans16 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q17
        print("\nQ17: You see someone struggling to carry heavy groceries through a doorway.")
        print("A) Offer a friendly hand to help them carry the load (+4)")
        print("B) Hold the door open briefly while walking past (+2)")
        print("C) Walk around them pretending not to notice (+1)")
        print("D) Laugh at their struggle (0)")
        eq_ans17 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans17 == 'A': eq_score += 4
        elif eq_ans17 == 'B': eq_score += 2
        elif eq_ans17 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q18
        print("\nQ18: A peer shares a piece of embarrassing news about themselves in confidence.")
        print("A) Keep it strictly confidential and offer a supportive ear (+4)")
        print("B) Forget about it and never mention it again (+2)")
        print("C) Tell one close friend under the guise of secret keeping (+1)")
        print("D) Share it openly as gossip with others (0)")
        eq_ans18 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans18 == 'A': eq_score += 4
        elif eq_ans18 == 'B': eq_score += 2
        elif eq_ans18 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q19
        print("\nQ19: You fail an important exam despite studying hard.")
        print("A) Review mistakes, acknowledge feelings, and plan a better strategy (+4)")
        print("B) Feel disappointed for a day and move on passively (+2)")
        print("C) Blame the teacher or the exam difficulty entirely (+1)")
        print("D) Give up studying altogether out of frustration (0)")
        eq_ans19 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans19 == 'A': eq_score += 4
        elif eq_ans19 == 'B': eq_score += 2
        elif eq_ans19 == 'C': eq_score += 1
        else: eq_score += 0

        # EQ Q20
        print("\nQ20: A stranger is rude to you in a service line.")
        print("A) Ignore their bad behavior, realizing they might be having a hard day (+4)")
        print("B) Give them a cold glare and look away (+2)")
        print("C) Make a snide remark back to them (+1)")
        print("D) Start a heated argument (0)")
        eq_ans20 = input("Your choice (A/B/C/D): ").strip().upper()
        if eq_ans20 == 'A': eq_score += 4
        elif eq_ans20 == 'B': eq_score += 2
        elif eq_ans20 == 'C': eq_score += 1
        else: eq_score += 0

        # --- Final EQ Result & Grading Scale ---
        print("\n--- EQ Test Finished ---")
        print("Congratulations, {n}! Your total EQ score is: {eq_score} out of 80")
        
        if eq_score >= 64:
            print("Performance Tier: High Emotional Intelligence (Grade A+) - Exceptional empathy and conflict resolution!")
        elif eq_score >= 48:
            print("Performance Tier: Good Emotional Intelligence (Grade A) - Strong self-awareness and social skills.")
        elif eq_score >= 30:
            print("Performance Tier: Moderate Emotional Intelligence (Grade B) - Average ability to manage interpersonal reactions.")
        else:
            print("Performance Tier: Developing Emotional Intelligence (Grade C) - Room for growth in empathy and emotional control.")
            
        break
        
    # ==================== OPTION 3: BOTH TESTS ====================
    elif choice == '3':
        print(f"\n--- Starting Both IQ and EQ Assessments for {n} ---")
        
        # Run IQ Test sequence inside Option 3
        iq_score = 0
        print("\n[PART 1: IQ TEST]")
        # Q1-Q10 for IQ
        ans1 = input("Q1 (2,4,6,8... Next? A/B/C/D): ").strip().upper()
        if ans1 == 'B': iq_score += 4 
        else: iq_score -= 1
        
        ans2 = input("Q2 (Red Planet? A/B/C/D): ").strip().upper()
        if ans2 == 'C': iq_score += 4 
        else: iq_score -= 1
        
        ans3 = input("Q3 (15 + 25 * 0? A/B/C/D): ").strip().upper()
        if ans3 == 'B': iq_score += 4 
        else: iq_score -= 1
        
        ans4 = input("Q4 (Odd one out: Dog, Cat, Cow, Carrot? A/B/C/D): ").strip().upper()
        if ans4 == 'D': iq_score += 4 
        else: iq_score -= 1
        
        ans5 = input("Q5 (Book:Reading as Fork:? A/B/C/D): ").strip().upper()
        if ans5 == 'A': iq_score += 4 
        else: iq_score -= 1
        
        ans6 = input("Q6 (3,6,9,12... Next? A/B/C/D): ").strip().upper()
        if ans6 == 'C': iq_score += 4 
        else: iq_score -= 1
        
        ans7 = input("Q7 (North + 90 deg right? A/B/C/D): ").strip().upper()
        if ans7 == 'B': iq_score += 4 
        else: iq_score -= 1
        
        ans8 = input("Q8 (20% of 200? A/B/C/D): ").strip().upper()
        if ans8 == 'C': iq_score += 4 
        else: iq_score -= 1
        
        ans9 = input("Q9 (Odd one: Apple, Banana, Carrot, Grape? A/B/C/D): ").strip().upper()
        if ans9 == 'C': iq_score += 4 
        else: iq_score -= 1
        
        ans10 = input("Q10 (Train 60 km/h in 2 hours? A/B/C/D): ").strip().upper()
        if ans10 == 'B': iq_score += 4 
        else: iq_score -= 1

        # Run EQ Test sequence inside Option 3
        eq_score = 0
        print("\n[PART 2: EQ TEST]")
        print("For EQ questions, choose A (+4), B (+2), C (+1), or D (0):")
        
        for i in range(1, 21):
            eq_ans = input(f"EQ Q{i} Choice (A/B/C/D): ").strip().upper()
            if eq_ans == 'A': eq_score += 4
            elif eq_ans == 'B': eq_score += 2
            elif eq_ans == 'C': eq_score += 1
            else: eq_score += 0

        # Final Combined Summary Table
        print(f"\n==============================================")
        print(f"          FINAL ASSESSMENT REPORT FOR {n.upper()}")
        print(f"==============================================")
        print(f"{'Category':<10} | {'Score':<10} | {'Max Score':<10} | {'Performance Tier'}")
        print(f"-" * 65)
        
        # Determine IQ tier string
        if iq_score >= 32: iq_tier = "Superior (Grade A+)"
        elif iq_score >= 22: iq_tier = "Above Average (Grade A)"
        elif iq_score >= 10: iq_tier = "Average (Grade B)"
        elif iq_score >= 0: iq_tier = "Below Average (Grade C)"
        else: iq_tier = "Needs Practice (Grade D)"

        # Determine EQ tier string
        if eq_score >= 64: eq_tier = "High EQ (Grade A+)"
        elif eq_score >= 48: eq_tier = "Good EQ (Grade A)"
        elif eq_score >= 30: eq_tier = "Moderate EQ (Grade B)"
        else: eq_tier = "Developing EQ (Grade C)"

        print(f"{'IQ Test':<10} | {iq_score:<10} | {'40':<10} | {iq_tier}")
        print(f"{'EQ Test':<10} | {eq_score:<10} | {'80':<10} | {eq_tier}")
        print(f"==============================================")
        break
        
    elif choice == '4':
        print(f"\nGoodbye, {n}!")
        break
        
    else:
        print("\nInvalid choice! Please enter a number between 1 and 4.")