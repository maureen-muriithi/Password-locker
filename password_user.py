class User:
    '''
    A class that generates new instances for a user.
    '''
    user_list = [] # Empty user list

    def __init__(self, user_name, password):
        '''
        init method that defines properties for the user class
        Args: user_name, password
        '''
        self.user_name = user_name
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
    
    
    