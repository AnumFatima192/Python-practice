# --- Pro Secure Password Generator for GKS Prep Portfolio ---
import random
import string

def generate_password():
    print("\n=============================================")
    print("🔐 SECURE PASSWORD GENERATOR & ANALYZER 🚀")
    print("=============================================")
    print("Generate un-crackable passwords to protect your digital identity.")
    print("=============================================")

    try:
        length = int(input("Enter desired password length (Minimum 6): "))
        if length < 6:
            print("❌ Error: Password length must be at least 6 characters for strong security.")
            return
    except ValueError:
        print("❌ Error: Please enter a valid number for password length.")
        return

    # Character sets for generation
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = lower + upper + digits + symbols

    # Generate password by choosing random choices
    password_list = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length with random choices from all sets
    for _ in range(length - 4):
        password_list.append(random.choice(all_characters))

    # Shuffle the list to ensure randomness
    random.shuffle(password_list)
    secure_password = "".join(password_list)

    # Password Strength Analysis Logic
    print("\n=============================================")
    print("📋 SECURITY ANALYSIS REPORT")
    print("=============================================")
    print(f"🔑 Generated Password: {secure_password}")
    print(f"📏 Total Length: {length} Characters")
    
    if length >= 12:
        print("🛡️ Strength Level: 🌟 STRONG (Perfect Choice)")
    elif length >= 8:
        print("🛡️ Strength Level: ✨ MEDIUM (Good, but can be improved)")
    else:
        print("🛡️ Strength Level: ⚠ WEAK (Easy to crack with brute force)")
    print("=============================================")

if __name__ == "__main__":
    while True:
        generate_password()
        replay = input("\nDo you want to generate another password? (y/n): ").strip().lower()
        if replay != 'y':
            print("\nStay secure and keep coding! Annyeong! 👋")
            break
