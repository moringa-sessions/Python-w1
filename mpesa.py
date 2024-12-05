import os 
from q1 import numbers
from q2 import sort_num


user_pin = "1234"

def safaricom():
    print("""
    SIM 2
    1. M-Banking services
    2. My Account
    """)

#send mone function
def send_money():
    os.system("clear")
    phone_number = input("Enter phone number : ")
    #Loop to validate length of phone number 
    while len(phone_number) < 10 or len(phone_number) > 13:
        os.system("clear")
        phone_number = input("Re-Enter phone number : ")
    os.system("clear")
    send_amount = int(input(f"Enter amount to send : "))
    os.system("clear")
    pin = input ("Enter pin number : ")
    if pin == user_pin:
        os.system("clear")
        print("******")
        confirm = int(input(f"Do you want to send {send_amount} to {phone_number} ? 1. Yes or 2. No :"))
        
        if confirm == 1:
            os.system("clear")
            print("Sent Successfully")
        else:
            os.system("clear")
            print("Transaction canceled")
    else:
        print(f"You have entered wrong pin.")

def m_pesa():
    os.system("clear")
    print("""
    SIM 2
    1. Send Money
    2. Withdraw Cash
    3. Buy Airtime
    4. Lipa na M-PESA
    5. Back
    """)
    mpesa_choice = int( input("Enter your choice : ") )

    if mpesa_choice == 5:
        os.system("clear")
        first_menu()
    elif mpesa_choice == 1:
        send_money()
    elif mpesa_choice == 2:
        os.system("clear")
        print(f"Enter Agent number :")
    


def first_menu():
    print("""
    SIM 2
    1. Safaricom+
    2. M-PESA
    """)
    choice1 = int( input("Enter your choice : ") )
    if choice1==2:
        m_pesa()

    elif choice1==1:
        safaricom()
first_menu()


    


