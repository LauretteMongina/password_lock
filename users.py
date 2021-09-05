import random
import string
class Users:
  """
  class that generates new instance of user
  """
  users_list = []

  def save_users(self):
      Users.users_list.append(self)

  def delete_users(self):
        """
        deletes a saved user from the users list
        """ 
        Users.users_list.remove(self)

  def __init__(self,username,password):
    self.username = username
    self.password = password


class Credentials:
  """
  class that generates a new instance of credentials
  """
  credentials_list = []

  def save_credentials(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

  def delete_credentials(self):
        """
        method to delete a credential in the credentials list
        """
        Credentials.credentials_list.remove(self)

  def __init__(self,account,username,password):
    """
    method that defines credentials to be stored
    """
    self.account = account
    self.username = username
    self.password = password

  @classmethod
  def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a credential that matches that username.

        Args:
            number: Username to search for
        Returns :
            Credential of person that matches the username.
        '''

        for credential in cls.credentials_list:
            if credential.username == username:
                return credential

  @classmethod
  def if_credential_exist(cls, username):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.username == username:
                return True
        return False

  @classmethod
  def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list  

  def randompassword(stringlength=7):
    """
    to generate random passwords
    """
    password = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(password)for i in range(stringlength))
