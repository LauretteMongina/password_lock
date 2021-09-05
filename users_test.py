import unittest
from users import Users
from users import Credentials

class TestUsers(unittest.TestCase):
  def setUp(self):
    """
    setUp method runs before tests
    """
    self.new_users = Users("laurah52","0345")

  def test_init(self):
    """
    test init test case to test for initialization
    """
    self.assertEqual(self.new_users.username,"laurah52")
    self.assertEqual(self.new_users.password,"0345")

  def test_save_users(self):
        '''
        test_save_users test case to test if the users object is saved into
         the users list
        '''
        self.assertEqual(len(Users.users_list),0)  
        self.new_users.save_users()
        self.assertEqual(len(Users.users_list),1)
        

  def test_delete_users(self):
        '''
        test_delete_users to test if we can remove a user from our users list
        '''
        self.assertEqual(len(Users.users_list),0)  
        self.new_users.save_users()
        self.assertEqual(len(Users.users_list),1)
        self.new_users.delete_users()

  

class TestCredentials(unittest.TestCase):
  def setUp(self):
    """
    setUp method runs before tests
    """
    self.new_credentials = Credentials("Quora","laurah52","0345")

  def test_init(self):
    """
    test init test case to test for initialization
    """
    self.assertEqual(self.new_credentials.account,"Quora")
    self.assertEqual(self.new_credentials.username,"laurah52")
    self.assertEqual(self.new_credentials.password,"0345")
    
  

if __name__ == '__main__':
    unittest.main()