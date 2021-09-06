#!/usr/bin/env python3.8
from users import Users
from users import Credentials

def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = Users(username,password)
    return new_user

def save_user(users):
    '''
    Function to save a new user
    '''
    users.save_users()


def create_new_credential(account,username,password):
    """
    Function that creates new credentials
    """
    new_credential = Credentials(account,username,password)
    return new_credential

def login_users(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credentials.verify_users(username,password)
    return check_user

def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_credentials()
def display_accounts():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()

def find_credential(username):
    """
    Function that finds a Credentials by a username and returns the Credentials that belong to that username
    """
    return Credentials.find_by_username(username)
def check_credentials(username):
    """
    Function that check if a Credentials exists with that username and return true or false
    """
    return Credentials.if_credential_exist(username)

def random_Password():
    '''
    generates a random password for the user.
    '''
    new_password=Credentials.randompassword()
    return new_password

def main():
    print("Heyy, welcome to password locker. What is your name?")
    username = input()
    print(f"Hello {username}. what would you like to do?")
    print('\n')
    while True:
                print("Use these short codes : ca - create a new account, lo - LOGIN")
                short_code=input().lower()


                if short_code == "ca":
                      print("Create account")
                      print('*'*50)

                      username = input("username: ")
                      while True:
                       print(" OP - To type your own pasword:\n RP - To generate random Password")
                       password_Choice = input().lower().strip()
                       if password_Choice == 'op':
                          password = input("Enter Password\n")
                          break
                       elif password_Choice == 'rp':
                           password = random_Password()
                           break
                      save_user(create_new_user(username,password))
                      print("*"*75)
                      print(f"Hello {username}, You have successfully created an account! Password is: {password}")
                      print("*"*75)
                elif short_code == "lo":
                    print("*"*60)
                    print("Enter your User name and your Password to log in:")
                    print('*' * 60)
                    username = input("Username: ")
                    password = input("password: ")

                    login = login_users(username,password)
                    if login_users == login:
                      print("logged in successfully")
                      print('\n')
                while True:
                            print("Use the following short codes for credentials:cc-create credentials,dp-display credentials,dl-delete credentials,ex-exit")
                            short_code = input().lower().strip()
                            if short_code == "cc":
                                  print("Create new credential")
                                  print("."*30)
                                  print("Account.....")
                                  account = input().lower()
                                  print("Your Account username")
                                  username = input().lower()
                                  while True:
                                     print(" OP - To type your own pasword if you already have an account:\n RP - To generate random Password")
                                     password_Choice = input().lower().strip()
                                     if password_Choice == 'op':
                                       password = input("Enter Your Own Password\n")
                                       break
                                     elif password_Choice == 'rp':
                                        password = random_Password()
                                        break
                                     else:
                                       print("Invalid password please try again")
                                  save_credentials(create_new_credential(account,username,password))
                                  print('\n')
                                  print(f"Account details for: {account} - Username: {username} - Password:{password} created")
                                  print('\n')    
                            elif short_code == "dp":
                                if display_accounts():
                                    print("Here's your list of accounts: ")
                                    
                                    print('*' * 30)
                                    print('_'* 30)
                                    for account in display_accounts():
                                        print(f" Account:{account.account} \n User Name:{account.username}\n Password:{account.password}")
                                        print('_'* 30)
                                    print('*' * 30)
                                else:
                                    print("You don't have any credentials saved yet..........")
                            elif short_code == "dl":
                                print("Enter the username of the Credentials you want to delete")
                                search_name = input().lower()
                                if find_credential(search_name):
                                    search_credential = find_credential(search_name)
                                    print("_"*60)
                                    search_credential.delete_credentials()
                                    print('\n')
                                    print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                                    print('\n')
                                else:
                                    print("The Credential does not exist in your store yet")
                            elif short_code == 'ex':
                                print("Thanks for using password locker.. !")
                                break
                            else:
                              print("Invalid entry, repeat the process")

                else:
                      print("Invalid short codes.Try again!")
if __name__ == '__main__':
    main()