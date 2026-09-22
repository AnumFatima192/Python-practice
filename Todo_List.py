# --- Pro Terminal To-Do List Application for GKS Prep ---

def show_menu():
    print("\n=============================================")
    print("📝 SMART TO-DO LIST MANAGER 🚀")
    print("=============================================")
    print("1. View To-Do List")
    print("2. Add Naya Task (+)")
    print("3. Delete Completed Task (-)")
    print("4. Exit Program (e)")
    print("=============================================")

# Khali list banayein jahan tasks save honge
todo_list = []

while True:
    show_menu()
    choice = input("\nEnter your choice (1/2/3/4 or 'e'): ").strip().lower()
    
    if choice == 'e' or choice == '4':
        print("\nThank you for organizing your day! Annyeong! 👋")
        break
        
    elif choice == '1':
        print("\n--- 📋 YOUR CURRENT TASKS ---")
        if not todo_list:
            print("✨ Aap ki list abhi khali hai! Chill karein.")
        else:
            # Enumerate loop har task ko number dega (1, 2, 3...)
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. [ ] {task}")
        print("-----------------------------")
        
    elif choice == '2':
        new_task = input("\nEnter naya task jo add karna hai: ").strip()
        if new_task:
            todo_list.append(new_task) # Append se list ke end mein item add hota hai
            print(f"✅ Success: '{new_task}' list mein add ho gaya!")
        else:
            print("❌ Error: Task khali nahi ho sakta!")
            
    elif choice == '3':
        print("\n--- 🗑️ DELETE TASK ---")
        if not todo_list:
            print("❌ Delete karne ke liye koi task nahi hai.")
        else:
            # Pehle list show karenge taake user number dekh sake
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
                
            try:
                task_num = int(input("\nDelete karne ke liye task number likhein: "))
                if 1 <= task_num <= len(todo_list):
                    # pop() list se item ko nikal deta hai index ke mutabiq
                    removed_task = todo_list.pop(task_num - 1)
                    print(f"🗑️ Removed: '{removed_task}' successfully delete ho gaya!")
                else:
                    print("❌ Error: Yeh task number list mein nahi hai!")
            except ValueError:
                print("❌ Error: Please sirf valid number enter karein!")
                
    else:
        print("❌ Invalid Option! Sahi number select karein.")
