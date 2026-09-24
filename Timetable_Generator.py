# --- Pro Automated Study Timetable Generator for GKS Prep Portfolio ---

def generate_timetable():
    print("\n=============================================")
    print("📅 AUTOMATED STUDY TIMETABLE GENERATOR 🚀")
    print("=============================================")
    print("Plan your day efficiently and smash your 90%+ goals!")
    print("=============================================")

    # Get user constraints
    try:
        total_hours = float(input("\nHow many hours do you want to study daily?"))
        if total_hours <= 0 or total_hours > 16:
            print("❌ Invalid Input: Please enter a realistic number of hours (1-16).")
            return
    except ValueError:
        print("❌ Error: Please enter numbers only for hours.")
        return

    print("\nEnter the names of the subjects you need to study today.")
    print("Type 'done' when you are finished entering subjects.")
    
    subjects = []
    while True:
        sub = input("- Subject Name (or 'done'): ").strip()
        if sub.lower() == 'done':
            break
        if sub:
            subjects.append(sub)

    if not subjects:
        print("❌ Error: Timetable banane ke liye kam az kam ek subject lazmi hai!")
        return

    # Calculate time per subject
    time_per_subject = total_hours / len(subjects)

    # Dictionary to map time slots (Assuming study starts at 4:00 PM after college/rest)
    print("\n=============================================")
    print("📋 YOUR GENERATED STUDY SCHEDULE FOR TODAY")
    print("=============================================")
    
    start_time = 16.0  # 16.0 means 4:00 PM in 24-hour format

    for index, subject in enumerate(subjects, start=1):
        # Convert decimal hours to hours and minutes
        start_hour = int(start_time)
        start_min = int((start_time - start_hour) * 60)
        
        end_time = start_time + time_per_subject
        end_hour = int(end_time)
        end_min = int((end_time - end_hour) * 60)

        # Standard AM/PM formatting logic
        def format_time(h, m):
            period = "PM" if h >= 12 else "AM"
            display_h = h - 12 if h > 12 else h
            if display_h == 0: display_h = 12
            return f"{display_h:02d}:{m:02d} {period}"

        time_slot = f"{format_time(start_hour, start_min)} - {format_time(end_hour, end_min)}"
        
        print(f"🎯 Slot {index} | {time_slot} ➡️ Focus on: {subject}")
        print(f"⏱ Duration: {time_per_subject:.1f} Hours")
        print("-" * 45)
        
        # Next slot starts exactly when this one ends
        start_time = end_time

    print("\n💡 Tip: Take a 5-10 minute break between slots to keep your mind fresh!")
    print("=============================================")

if __name__ == "__main__":
    while True:
        generate_timetable()
        replay = input("\nDo you want to generate another timetable? (y/n): ").strip().lower()
        if replay != 'y':
            print("\nGood luck with your studies! Keep building consistency. Annyeong! 👋")
            break
