current_balance = 10000

while True:
    print("\n=== ATM MENU ===")
    print("")
    
    print("1. CHECK BALANCE")
    print("2. WITHDRAW MONEY")
    print("3. DEPOSIT MONEY")
    print("4. EXIT")
    print("")
    
    choice = int(input("Enter a number 1-4: "))

    if choice == 1:
        print(f"The current balance is ${current_balance}")
    elif choice == 2:
        withdraw_money = float(input("Enter amount you'd like to withdraw: "))
        final_balance = current_balance - withdraw_money
        print(f"The amount is ${final_balance}")
    elif choice == 3:
        deposit_money = float(input("Enter amount you'd like to deposit: "))
        deposit = current_balance + deposit_money
        print(f"The updated balance is ${deposit}")
    elif choice == 4:
        print("THANK YOU FOR USING THE ATM, BYE!")
        break
    else:
        print("Incorrect CHOICE, try again")