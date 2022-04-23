import random       # Enables the app to generate a random number for the passwords
import string       # Allows one to create and customize your own string for the password
# import pyperclip    # A third party module that allows one to copy and paste items to ther clipboard. 


class User:
    '''
    A class that generates new instances for a user.
    '''
    user_list = [] # Empty user list

    def __init__(self, username, email, password):
        '''
        init method that defines properties for the user class
        Args: username, email, password
        '''
        self.username = username
        self.email = email
        self.password = password
    
    def save_user(self):
        '''
        save_user method stores a user in the user_list
        '''
        User.user_list.append(self) # Append method adds an item in the 'empty user list'
    
    def delete_user(self):
        '''
        delete_user method deletes a user from the user_list
        '''
        User.user_list.remove(self) # Remove method deletes an item from a list
    
    @classmethod  # A decorator that is bound to the class and not the object of the class
    def find_by_username(cls, username):
        ''' 
        This method takes in the username inputted and returns a user that matches the username.
        '''
        for user in cls.user_list:      # Loops through the whole userlist to find a matching username
            if user.username == username:
                return user
    
    @classmethod
    def view_users_list(cls):
        '''
        This method enables one to view all the users available
        '''
        return cls.user_list

    @classmethod
    def verify_user (cls, email, password):
        '''
        This method verifies if a user exists, and if the details are correct
        '''
        for user in cls.user_list:
            if user.email==email and user.password == password:
                return True
        return False
    

class Credentials:
    '''
    A class that generates new instances for a user's credentials
    '''
    credentials_list = [] # Empty list for credentials

    def __init__(self, account_name, user_name, password):
        '''
        init method that defines properties for the credentials class
        Args: account_name, user_name, password
        '''
        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_credentials(self):
        '''
        save_credentials method stores user's credentials in the credentials_list
        '''
        Credentials.credentials_list.append(self)
    
    #def generate_password(self):
      #  '''
        #This method generates random passwords for users
      #  '''
        # stringLength = (input(print("Please enter the preferred length for your password: ")))
      #  gen_password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
      #  return gen_password
    
    def delete_credentials(self):
        '''
        delete_credentials method removes user's credentials in the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        This method takes in the account_name inputted and returns credentials that matches the account name.
        '''

        for credential in cls.credentials_list:     #Loops through the credentials list to find matchng credentials
            if credential.account_name == account_name:
                return credential
    
    @classmethod
    def view_credentials(cls):
        '''
        This method enables the user to view all the credentials available
        '''
        return cls.credentials_list

    @classmethod
    def copy_password(cls,account_name):
        '''
        Pyperclip method enables the user to copy paste the password of the account name provided
        '''
        credentials_found = Credentials.find_by_account_name(account_name)
        # pyperclip.copy(credentials_found.password)
    



    