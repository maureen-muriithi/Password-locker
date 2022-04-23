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
        save_user method stores a users details in the user_list
        '''
        User.user_list.append(self) # Append adds the new istance in the 'empty user list'
    
    
    