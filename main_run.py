import email
from password_user import User, Credentials


def function():
	print("               ____                               ___                                    ")
	print("              |  _ \                             /   \                                   ")
	print("              | |_) )  ____  ___   ___          / ___ \    __     __                     ")
	print("              |  __/  / _  |/ __  / __   ___   | /___\ |  |  _\  |  _\                   ")               
	print("              | |    / (_| |\__ \ \__ \ |___|  | |   | |  | |_)) | |_))                  ")
	print("              |_|    \_____| ___/  ___/        | |   | |  |_|    | |                     ")

function()

print("PASS-APP is a cool application that enables you to save your credentials, accounts and their passwords!!")
print('*' *30)

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
    User.find_by_username()

def user_login(email, password):
    '''
    Function to verify and log in a user with their specific details
    '''
    check_user = User.verify_user(email,password)
    return check_user

def display(user):
    User.view_users()

#CREDENTIALS

