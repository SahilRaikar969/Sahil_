def Show_balance(balance):
    print(f"your balance is {balance:.2f}Rs ")

def Deposit():
    amount = float(input("Enter an amount to be deposited:"))

    if amount < 0:
        print("Thats not a valid amount. ")
        return 0
    else:
        print("Amount deposited succesfully")
        return amount
   

def withdraw(balance):
    amount = float(input("Enter amount to be Withdrawn:"))

    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0 :
        print("Amount must be greater than 0.")
        return 0
    else:
        print("Amount withdrawm succesfully")
        return amount

def main():
    balance = 0
    is_running = True 


    while is_running:
        print("Welcome to the banking system! ")
        print("***************************")
        print("      Banking Deposit     ")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice from (1-4):")

        if choice == '1':
            Show_balance(balance)
        elif choice == '2':
            balance += Deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running= False
            print("Thankyou! for using the banking system")
        else:
            print("That is not a valid choice! ")

if __name__ == '__main__':
    main()