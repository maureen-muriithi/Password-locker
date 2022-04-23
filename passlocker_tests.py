import unittest

from requests import delete
# import pyperclip
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
    


if __name__ == '__main__':
    unittest.main()



