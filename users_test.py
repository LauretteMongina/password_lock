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
    
  def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the users object is saved into
         the credentials list
        ''' 
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
  
  def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

  def test_save_many_credentials(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Quora","laurah52","0345") 
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
  def test_delete_credentials(self):
    """
    test_delete_credentials to test if a credential can be deleted from the list
    """
    self.new_credentials.save_credentials()
    test_credential = Credentials("Quora","laurah52","0345") 
    test_credential.save_credentials()

    self.new_credentials.delete_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)

  def test_find_by_username(self):
        '''
        test to check if we can find a credential by username and display information
        '''
        self.new_credentials.save_credentials()
        test_credential = Credentials("Quora","laurah52","0345") 
        test_credential.save_credentials()

        

        found_credential = Credentials.find_by_username("laurah52")

        self.assertEqual(found_credential.username,test_credential.username)

  def test_credentials_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """

        self.new_credentials.save_credentials()
        test_credential = Credentials("Quora","laurah52","0345") 
        test_credential.save_credentials()

        
        credentials_found = Credentials.if_credential_exist("laurah52")
        self.assertTrue(credentials_found)

  

  

if __name__ == '__main__':
    unittest.main()