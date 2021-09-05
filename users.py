
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
