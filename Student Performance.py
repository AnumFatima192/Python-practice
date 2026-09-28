# --- Pro Student Performance Analyzer for GKS Prep Portfolio ---

def analyze_performance():
    print("\n=============================================")
    print("📊 STUDENT PERFORMANCE & GRADING ANALYZER 🚀")
    print("=============================================")
    print("Track your marks, calculate averages, and secure your 90%+ goals!")
    print("=============================================")

    # Subject dictionary to store marks
    report_card = {}
    
    print("Enter the names of your subjects followed by your marks.")
    print("Type 'done' when you are finished entering subjects.")
    
    while True:
        subject = input("\nEnter Subject Name (or 'done' to finish): ").strip()
        if subject.lower() == 'done':
            break
            
        if not subject:
            print("❌ Subject name cannot be empty!")
            continue
            
        try:
            marks = float(input(f"Enter marks obtained in {subject} (out of 100): "))
            if marks < 0 or marks > 100:
                print("❌ Invalid Marks: Please enter a score between 0 and 100.")
                continue
            report_card[subject] = marks
        except ValueError:
            print("❌ Error: Please enter a valid numeric value for marks.")

    if not report_card:
        print("\n❌ Error: No subjects entered! Cannot generate performance analysis.")
        return

    # Processing and Calculations
    total_subjects = len(report_card)
    obtained_total = sum(report_card.values())
    max_total = total_subjects * 100
    percentage = (obtained_total / max_total) * 100

    print("\n=============================================")
    print("📋 OFFICIAL PERFORMANCE REPORT CARD")
    print("=============================================")
    
    # Loop through items to display custom status for each subject
    for sub, score in report_card.items():
        if score >= 90:
            status = "🌟 Elite"
        elif score >= 80:
            status = "✨ Excellent"
        elif score >= 60:
            status = "👍 Good"
        else:
            status = "📚 Needs Focus"
        print(f"🎯 {sub}: {score}/100 ➡️ Status: {status}")

    print("---------------------------------------------")
    print(f"📊 Total Subjects Evaluated: {total_subjects}")
    print(f"📈 Aggregate Percentage: {percentage:.2f}%")

    # Final Academic Standings & GKS Feedback Logic
    if percentage >= 90:
        print("\n🏆 Final Grade: A+ (Outstanding Profile)")
        print("💡 GKS Insight: Your academic tier is exceptionally competitive for the University Track!")
    elif percentage >= 80:
        print("\n🏆 Final Grade: A (Very Strong Profile)")
        print("💡 GKS Insight: Highly eligible! Keep refining your GitHub portfolio to stand out.")
    elif percentage >= 60:
        print("\n🏆 Final Grade: B (Good Effort)")
        print("💡 GKS Insight: Solid base, but aim to push your scores higher for top tier selection.")
    else:
        print("\n🏆 Final Grade: C (Needs Academic Improvement)")
        print("💡 GKS Insight: Focus heavily on intermediate board scores to meet core criteria.")
    print("=============================================")

if __name__ == "__main__":
    while True:
        analyze_performance()
        replay = input("\nDo you want to analyze another report card? (y/n): ").strip().lower()
        if replay != 'y':
            print("\nKeep pushing for that 90%+ milestone! Annyeong! 👋")
            break
