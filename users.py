
class Users:
  """
  class that generates new instance of user
  """
  users_list = []

  def save_users(self):
      Users.users_list.append(self)

  def __init__(self,username,password):
    self.username = username
    self.password = password