# import email
import email
from password_user import User, Credentials

def function():
	print("                       ____                               ___                                    ")
	print("                      |  _ \                             /   \                                   ")
	print("                      | |_) )  ____  ___   ___          / ___ \    __     __                     ")
	print("                      |  __/  / _  |/ __  / __   ___   | /___\ |  |  _\  |  _\                   ")               
	print("                      | |    / (_| |\__ \ \__ \ |___|  | |   | |  | |_)) | |_))                  ")
	print("                      |_|    \_____| ___/  ___/        | |   | |  |_|    | |                     ")
function()

print(" ")
print("                                       Hello, welcome to Pass-App!")
print(" ")
print(" PASS-APP is a cool application that enables you to save your credentials, that is various accounts, usernames and their passwords!!")
print('*' *125)

def create_user_account(username,email,password):
    '''
    Function to create a new user account with a username, email and password
    '''
    new_user = User(username,email, password)
    return new_user

def save_user(user):
    '''
    Function to save a user
    '''
    user.save_user()

def delete_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_by_username(user):
    '''
    Function to find a user by their username
    '''
    return User.find_by_username()

def user_login(email, password):
    '''
    Function to verify and log in a user with their specific details
    '''
    check_user = User.verify_user(email,password)
    return check_user

def display(user):
    return User.view_users()

#Class Credentials functions

def create_new_credentials(account_name,user_name,password):
    '''
    Function to create a new account credentials with an account_name, a user_name and password
    '''
    new_credential = Credentials( account_name, user_name, password)
    return new_credential

def save_credentials(credentials):

    credentials.save_credentials()

#def generate_password():
    
def delete_credentials(credentials):

    credentials.delete_credentials()

def find_credential(account_name):

    return Credentials.find_by_account_name(account_name)

def check_credentials(account_name):

    return Credentials.if_credential_exists(account_name)

def display_accounts():
    """
    Function that returns all the saved credential.
    """
    return Credentials.view_all_credentials()

def copy_password(account_name):
    """
    This function copies the password using the pyperclip module
    """
    return Credentials.copy_password(account_name)

def main():
    print("Please create an account to get started. \nAlready have an account? Please log in to continue ")
    print("Use these short codes to proceed with the desired action. \n CA -> Create an account.. \n LI -> Log in..")

    short_code = input().lower().strip()
    if short_code == "ca":
        print("Welcome to Pass-App. To create your new account, please fill in these details")
        print("Create a username")
        username = input("")
        print("Enter your email")
        email = input("")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_user_account(username,email,password))
        print("Welcome aboard {username}. Your password is, {password}")
        print("\n")

    elif short_code == "li":
        print("\n")
        print("Please enter your Username and your Password to log in:")
        print('*' * 120)
        username = input("User name: ")
        password = input("password: ")
        login = user_login(username,password)
        if user_login == login:
            print(f"Welcome back {username}. Let's proceed!")  
            print('\n')
        
        
            


