
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

  