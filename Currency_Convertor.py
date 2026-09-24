# --- Pro Global Currency Converter (PKR / KRW / USD) for GKS Prep Portfolio ---

def run_converter():
    print("\n=============================================")
    print("💱 GLOBAL CURRENCY CONVERTER (GKS EDITION) 🚀")
    print("=============================================")
    print("Convert between PKR, South Korean Won (KRW), and USD.")
    print("=============================================")

    # Hardcoded exchange rates (Sample standard rates for logic building)
    # 1 USD = 278 PKR | 1 KRW = 0.21 PKR | 1 USD = 1330 KRW
    rates = {
        "PKR_TO_KRW": 4.80,   # 1 PKR = ~4.80 KRW
        "KRW_TO_PKR": 0.21,   # 1 KRW = ~0.21 PKR
        "USD_TO_KRW": 1330.0, # 1 USD = ~1330 KRW
        "KRW_TO_USD": 0.00075 # 1 KRW = ~0.00075 USD
    }

    print("Available Conversion Options:")
    print("1. Pakistani Rupee (PKR) ➡️ South Korean Won (KRW)")
    print("2. South Korean Won (KRW) ➡️ Pakistani Rupee (PKR)")
    print("3. US Dollar (USD) ➡️ South Korean Won (KRW)")
    print("4. South Korean Won (KRW) ➡️ US Dollar (USD)")
    print("5. Exit Program (e)")
    print("---------------------------------------------")

    choice = input("Select an option (1-5 or 'e'): ").strip().lower()

    if choice == 'e' or choice == '5':
        print("\nThank you for using the Global Converter! Annyeong! 👋")
        return False # This will break the main loop

    if choice in ('1', '2', '3', '4'):
        try:
            amount = float(input("\nEnter the amount to convert: "))
            if amount <= 0:
                print("❌ Invalid Amount: Please enter a value greater than 0.")
                return True
        except ValueError:
            print("❌ Error: Please enter a valid numeric amount.")
            return True

        if choice == '1':
            converted = amount * rates["PKR_TO_KRW"]
            print(f"💰 Result: {amount} PKR = {converted:.2f} KRW 🇰🇷")
        elif choice == '2':
            converted = amount * rates["KRW_TO_PKR"]
            print(f"💰 Result: {amount} KRW = {converted:.2f} PKR 🇵🇰")
        elif choice == '3':
            converted = amount * rates["USD_TO_KRW"]
            print(f"💰 Result: {amount} USD = {converted:.2f} KRW 🇰🇷")
        elif choice == '4':
            converted = amount * rates["KRW_TO_USD"]
            print(f"💰 Result: {amount} KRW = {converted:.5f} USD 🇺🇸")
            
        print("=============================================")
    else:
        print("❌ Invalid Option! Please choose a valid number from the menu.")
        
    return True

if __name__ == "__main__":
    is_running = True
    while is_running:
        is_running = run_converter()
        if is_running:
            replay = input("\nDo you want to perform another conversion? (y/n): ").strip().lower()
            if replay != 'y':
                print("\nSafe travels and successful portfolio building! Annyeong! 👋")
                break
