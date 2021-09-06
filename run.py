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



