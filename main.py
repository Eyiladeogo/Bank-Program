# TODO : 1. Account Registration
# TODO : 2. Deposit
# TODO : 3. Withdrawal
# TODO : 4. View Balance
# TODO : 5. Get Balance


def create_account(user_id):
    user_name = input("Enter your name: ")
    user_address = input("Enter your address: ")
    user_phone_no = input("Enter your Phone Number: ")
    user_profession = input("Enter your profession: ")
    user_password = int(input("Enter your 4-digit password: "))
    user_balance = 0
    global user_input
    user_input = {
        "Name": user_name,
        "Address": user_address,
        "Phone Number": user_phone_no,
        "Profession": user_profession,
        "Password": user_password,
        "Balance": user_balance,
    }
    global user_details
    user_details = {user_id: user_input}

    print(user_details)
    return user_details


def deposit(user_details):
    user_id = input("Enter your Account ID: ")
    deposit_amount = input("Enter you deposit amount: ")
    user_details["Balance"] += deposit_amount


def withdraw(user_details):
    user_id = input("Enter your Account ID: ")
    withdrawal_amount = input("Enter you deposit amount: ")
    balance = user_details["Balance"]
    if withdrawal_amount <= balance:
        user_details["Balance"] -= withdrawal_amount
        print ("Transaction Successful")
    else:
        print("Insufficient funds")


def get_balance(inner_user_dictionary):
    user_id = input("Enter your Account ID: ")
    balance = user_details["Balance"]
    print(user_details)
    print(f"Current balance is: {balance}")

def login(user_account_dictionary):
    user_id = input("Enter your Account ID: ")
    user_password = input("Enter you 4-digit password: ")
    # password = user_account_dictionary["Password"]
    # while user_account_dictionary != user_id or user_password != password:
    #     print("The Account ID does not exist or the password is incorrect")
    #     user_id = input("Enter your Account ID: ")
    #     user_password = input("Enter you 4-digit password: ")
    name = user_account_dictionary["Name"]
    print(f"Welcome {name}")
    login_operation = (input("D: Deposit\nW: Withdraw\nG: Get Account Balance\nPlease select the operation you want to perform: ")).lower()
    if login_operation == "d":
        deposit(user_account_dictionary)
    elif login_operation == "w":
        withdraw(user_account_dictionary)
    elif login_operation == "g":
        get_balance(user_account_dictionary)
    elif login_operation == "e":
        print("Bye bye, have a nice day!")
        exit()


def display_prompt(user_id):
    dict1 = {}
    keyword = (input("Welcome to Python Virtual Bank:\nC: To create an account\nL: Login to your account\nE: Exit\n")).lower()
    if keyword == "c":
        updated_user_id = user_id + 1
        dict1 = create_account(updated_user_id)
    elif keyword == "l":
        login(dict1)
    elif keyword == "e":
        print("Bye bye, have a nice day!")
        exit()
    else:
        print("Invalid Input")
    return updated_user_id


still_continue = True
account_id = 0
the_new_user_id = display_prompt(account_id)
while still_continue:
    new_keyword = input("Do you want to perform a new operation or exit? Type 'yes' or 'no'").lower()
    if new_keyword == "yes":
        display_prompt(the_new_user_id)
    elif new_keyword == "no":
        print("Bye bye, have a nice day!")
        exit()
        still_continue = False
    else:
        print("Invalid Input")
