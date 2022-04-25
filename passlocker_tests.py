from curses import use_default_colors
import unittest

from requests import delete
import pyperclip
from password_user import User, Credentials

class TestUser(unittest.TestCase):
    '''
        Test class that defines test cases for the User class behaviours.
        Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Setup method to run before each test method
        '''
        self.new_user = User ("MaureenM", "moh2wanja@gmail.com", "Moh22!")
    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_init(self):
        '''
        test case to check if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"MaureenM")
        self.assertEqual(self.new_user.email,"moh2wanja@gmail.com")
        self.assertEqual(self.new_user.password,"Moh22!")
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    
    def test_display_user(self):
        '''
        test_display_user test case to test if the user(s), will be displayed
        '''
        self.assertEqual(User.view_users(), User.user_list)

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("TestUser","test@user.com", "Testuser22") # Another new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_verify_user(self):
        '''
        test_verify_user test case to test if the username and password are correct
        '''
        self.new_user.save_user()
        userDetails = User ("MaureenM", "moh2wanja@gmail.com", "Moh22!")
        userDetails.save_user()

        verify_user = User.verify_user("moh2wanja@gmail.com", "Moh22!")
        self.assertTrue(verify_user)
    
# Tests for the second class (Credentials)

class TestCredentials(unittest.TestCase):
    '''
        Test class that defines test cases for the Credentials class behaviours.
        Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        
        self.new_credential = Credentials("Twitter", "Moh-Muriithi", "Moh22!" )

    def tearDown(self):
            
        Credentials.credentials_list = []
    
    def test_init(self):
        self.assertEqual(self.new_credential.account_name,"Twitter")
        self.assertEqual(self.new_credential.user_name,"Moh-Muriithi")
        self.assertEqual(self.new_credential.password,"Moh22!")
    
    def test_save_credentials(self):
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def test_save_multiple_credentials(self):
        self.new_credential.save_credentials()
        test_credential = Credentials("Gmail","moh2wanja@gmail.com", "Maureen22!") # Another new credentials
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        self.new_credential.save_credentials()
        test_credential = Credentials("Gmail","moh2wanja@gmail.com", "Maureen22!") # Deletes these credentials
        test_credential.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    
    def test_credential_exists(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credential.save_credentials()
        test_credential = Credentials("Twitter", "Moh-Muriithi", "Moh22!") 
        test_credential.save_credentials()
        credentials_exists = Credentials.if_credential_exists("Twitter")
        self.assertTrue(credentials_exists)
    
    def test_view_all_credentials(self):
        '''
        Test case if method displays all the credentials that have been saved by the user
        '''

        self.assertEqual(Credentials.view_all_credentials(), Credentials.credentials_list)

    def test_copy_credentials(self):
        '''
        Test to confirm that we are copying the password from a found account
        '''

        self.new_credential.save_credentials()
        Credentials.copy_credentials("Twitter")

        self.assertEqual(self.new_credential.password,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()



