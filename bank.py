def show_balance():
    print(f"Your balance is Rs {balance:.2f}")

def deposit():
    amount = int(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That's not a valid amount. Please try entering a correct amount.")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient balance.")
        return 0  # Returning 0 to avoid subtracting anything from the balance
    elif amount < 0:
        print("Amount should be greater than 0.")
        return 0  # Returning 0 as it's an invalid withdrawal
    else:
        return amount  # Valid withdrawal

balance = 0
is_running = True

while is_running:
    print("\nBanking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("That is not a valid choice.")

print("Thank you! Have a nice day.")
