import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="336699",
    database="BankDB"
)

cursor = conn.cursor()

AccountBalance = 10453
AccountNumber = 1234

print("\nWelcome to the Bank Account program")
print("\nHere is your initial Account Information:")
print("Account for: Jake")
print(f"Account Number: {AccountNumber}")


def Menu():
    print("\n*******************")
    print("       Menu        ")
    print("*******************")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = int(input("\nWhat would you like to do?: "))
    if(choice == 1):
        CheckBalance()
    elif(choice ==2):
        Deposit()
    elif(choice == 3):
        Withdraw()
    elif(choice == 4):
        print("Thank you! Please come again")
        exit()




def Deposit():
    global AccountBalance
    while True:
        try:
            deposit = int(input("How much do you want to depost?: "))
            break
        except ValueError:
            print("Invalid input")
    AccountBalance += deposit
    print(f"Amount of {deposit:,} was successfully deposited")
    print(f"Account balance is now: {AccountBalance:,}")
    Menu()

def CheckBalance():
    global AccountBalance
    print(f"\nYour current account balance is: ${AccountBalance:,}")
    print()
    Menu()

def Withdraw():
    global AccountBalance
    withdraw = int(input("How much would you like to withdraw?: "))
    if(withdraw > AccountBalance):
        print("Withdraw ammount exceeds current account balance. Try again")
        Withdraw()
    AccountBalance -= withdraw
    print(f"\nYour account balance is now: ${AccountBalance:,}")
    Menu()

Menu()


