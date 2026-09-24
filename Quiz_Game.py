# --- Pro Quiz Game with Dictionaries for GKS Prep Portfolio ---

def run_quiz():
    print("\n=============================================")
    print("🧠 WELCOME TO THE ULTIMATE COMPUTER SCIENCE QUIZ 🚀")
    print("=============================================")
    print("Answer the following questions to test your logic.")
    print("=============================================")

    # Python Dictionary to store questions and answers
    questions = {
        "1. What is the correct extension of a Python file?": ".py",
        "2. Which keyword is used to create a function in Python?": "def",
        "3. Is Python an interpreted language? (yes/no)": "yes",
        "4. Which data structure stores data in key-value pairs?": "dictionary",
        "5. What does CPU stand for?": "Central Processing Uy
        nit"
    }

    score = 0

    # Loop through dictionary items
    for question, correct_answer in questions.items():
        print(f"\n{question}")
        user_answer = input("Your Answer: ").strip().lower()

        if user_answer == correct_answer:
            print("✅ Correct Answer! Good job.")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {correct_answer}")

    # Final Score Display
    print("\n=============================================")
    print("📊 QUIZ COMPLETED!")
    print(f"🏆 Your Final Score: {score}/{len(questions)}")
    
    percentage = (score / len(questions)) * 100
    print(f"📈 Percentage: {percentage}%")
    
    if percentage >= 80:
        print("🌟 Excellent! Outstanding logic.")
    elif percentage >= 50:
        print("👍 Good effort! Keep practicing.")
    else:
        print("📚 Need improvement. Keep learning!")
    print("=============================================")

if __name__ == "__main__":
    while True:
        run_quiz()
        replay = input("\nDo you want to take the quiz again? (y/n): ").strip().lower()
        if replay != 'y':
            print("\nThanks for playing! Keep building your portfolio. Annyeong! 👋")
            break
