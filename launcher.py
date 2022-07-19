from utils.custom_print.custom_print import center, div
from utils.pyorn.yorn import question

from utils.database.database import new_acc, get_usr

import os
import time

SPECIAL_CHARS = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + '"'

class Start():
    def __init__(self):
        self.done = False
        return self.launch()

    def launch(self):
        if self.done:
            return self.user
        else:
            os.system('clear')
            div()
            center("Python Adventures 2")
            center("O inimigo agora é outro")
            div()
            center("Account Login")
            self.verify_user()
        
    def verify_user(self):
        user = input("Insert your username\n-> ")
        if any(c in SPECIAL_CHARS for c in user):
            print("Invalid username!")
            self.verify_user()
        elif not user:
            print("Username cannot be blank")
            self.verify_user()
        elif len(user)<3:
            print("Username is too short!")
            self.verify_user()
        elif len(user)>50:
            print("Username is too long!")
            self.verify_user()
        else:
            self.search_user_db(user)


    def search_user_db(self, user):
        acc = get_usr()
        self.all_users = []
        self.all_passwords = []
        for a in acc:
            self.all_users.append(a[1])
            self.all_passwords.append(a[2])
        if user in self.all_users:
            print("User found!")
            if question(f"Do you want to login using {user}?"):
                self._user_login(user)
            else:
                self.launch()
        else:
            print("User not found!")
            if question(f"Do you want to create a new account with the name: {user}?"):
                self.user = user
                self._create_user()
            else:
                self.launch()


    def _user_login(self, user, _try=1):
        _ten = _try
        idx = self.all_users.index(user)
        pwd = input("Insert your password\n-> ")
        
        if pwd == self.all_passwords[idx]:
            self.user = user
            div()
            center(f"WELCOME {self.user.upper()}")
            self.done = True
            self.launch()
        elif _ten == 4:
            print("You tried loggin in a lot of times.\nRedirecting...")
            time.sleep(2)
            self.launch()
        else:
            print(f"Wrong password! ({_ten}/3)")
            self._user_login(user,_ten+1)


    def _create_user(self):
        pwd1 = input("Insert your password\n-> ")
        if any(c in SPECIAL_CHARS for c in pwd1):
            print("Invalid password!")
            self._create_user()
        elif not pwd1:
            print("Password cannot be blank")
            self._create_user()
        elif len(pwd1)<6:
            print("Password is too short!")
            self._create_user()
        elif len(pwd1)>50:
            print("Password is too long!")
            self._create_user()
        else:
            pwd2 = input("Insert your password again\n-> ")
            if pwd2 == pwd1:
                print("Creating account...")
                new_acc(self.user, pwd2)
                time.sleep(2)
                print("Loggin in...")
                time.sleep(2)
                div()
                center(f"WELCOME {self.user.upper()}")
                self.done = True
                self.launch()
            else:
                print("Passwords don't match!")
                self._create_user()