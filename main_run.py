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

# Class user functions 

def create_user_account(username,email,password):
    '''
    Function to create a new user account with a username, email and password
    '''
    new_user = User(username, email, password)
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
    print("Use these short codes to proceed with the desired action. \n CA --> Create an account.. \n LI --> Log in..")

    short_code_a = input().lower().strip()
    if short_code_a == "ca":
        print("Welcome to Pass-App. To create your new account, please fill in these details")
        print("Create a username")
        username = input("")
        print("Enter your email")
        email = input("")
        while True:
            print(" CP - Create your pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'cp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_user_account(username,email,password))
        print(f"Welcome aboard {username}. Your password is, {password}")
        print("\n")

    elif short_code_a == "li":
        print("\n")
        print("Please enter your Username and your Password to log in:")
        print('*' * 120)
        email = input("Email: ")
        password = input("Password: ")
        login = user_login(email,password)
        if user_login == login:
            print(f"Welcome back {username}. Let's proceed!")  
            print('\n')

        while True:
            print('*' * 120)
            print("Use these short codes to proceed with the desired action. \n CC --> Create new credentials.. \n FC --> Find credentials.. \n DC --> Display all credentials \n DLC --> Delete credentials \n EX --> Exit application\n ")

            short_code_b = input().lower().strip()
            if short_code_b == "cc":
                print("Enter details of the credentials you would like to create ")
                print("Account name: ")
                account_name = input()
                print("\n")
                print("User name / Email: ")
                user_name = input()
                print("\n")
                while True:
                    print("Password: ")
                    print(" CP - Create your pasword:\n GP - To generate random Password")
                    password_Choice = input().lower().strip()
                    if password_Choice == 'cp':
                        password = input("Enter Password\n")
                        break
                    elif password_Choice == 'gp':
                        password = generate_Password()
                        break
                    else:
                        print("Invalid password please try again")
                save_credentials(create_new_credentials(account_name,user_name,password))
                print('\n')
                print(f"Account Credential for: {account_name} - UserName: {user_name} - Password:{password} created succesfully")
            
            elif short_code_b == "fc":
                print("Enter account name for the credential you wish to find, Example Twitter/Gmail etc")
                input_name = input().lower()
                if find_credential == input_name:
                    search_credential = find_credential(input_name)
                    print(f"Account Name : {search_credential.account_name}")
                    print('\n')
                    print(f"User Name: {search_credential.user_name} \n Password :{search_credential.password}")
                    print('\n')
                else:
                    print("Oops! Seems like you have no such credentials")
                    print('\n')
            
            elif short_code_b == "dc":
                if display_accounts():
                    print("Here is a list of your credentials")
                    print('\n')

                    for credential in display_accounts():
                        print(f"Account: {credential.account_name}, Username {credential.user_name}, Password:  {credential.password}")
                        print('\n')
                else:
                    print('\n')
                    print("Empty!! Seems you currently have no any saved credentials")
                    print('\n')
            
            elif short_code_b == "dlc":
                print("Enter the account name of the Credentials you want to delete")
                input_name = input().lower()
                if find_credential(input_name):
                    search_credential = find_credential(input_name)
                    print("\n")
                    search_credential.delete_credentials()
                    print('\n')
                    print(f"{search_credential.account_name} credentials successfully deleted!!!")
                    print('\n')
                else:
                    print("Unable to delete. Account does not exist")

            elif short_code_b == 'ex':
                print(f"Good bye {username}. Thank you for using Pass-App.")
                break

            else:
                print("Incorrect entry. Please verify and input the correct code for your desired action.")
                print("Please use these short codes to proceed with the desired action. \n CC --> Create new credentials.. \n FC --> Find credentials.. \n DC --> Display all credentials \n DLC --> Delete credentials \n EX --> Exit application\n ")
    
    else:
        print("Please enter a valid input to continue")
            

if __name__ == '__main__':
    main()


                    
            


