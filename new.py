balance_current = 10000

while True:
    print("\n=== ATM MENU ===")
    print("")
    
    print("1. CHECK BALANCE")
    print("2. WITHDRAW MONEY")
    print("3. DEPOSIT MONEY")
    print("4. EXIT")
    print("")
    
    choice = int(input("Enter a choice form 1-4: "))
    
    if choice == 1:
        print(f"The current balance is ${balance_current}")
    elif choice == 2:
        withdrawl_amount = float(input("Enter the amount you'd like withdraw: "))
        final_balance = balance_current - withdrawl_amount
        print(f"The final is ${final_balance}")
    elif choice == 3:
        deposit_amount = float(input("Enter the amount you'd like deposit: "))
        updated_balance = balance_current + deposit_amount
        print(f"The updated balance is ${updated_balance}")
    elif choice == 4:
        print("Thank you for using the atm, bye!")
        break
    else:
        print("Try again and enter a number from 1-4")