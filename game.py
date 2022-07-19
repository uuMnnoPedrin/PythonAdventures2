from utils.custom_print.custom_print import center, div
from utils.print_ascii_art.print_ascii_art import art

import os

import launcher



class Game():
    def __init__(self, user):
        self.user = user
        self.Save().menu()

    class Save():
        def menu(self):
            try:
                self.get_save_data()
            except FileNotFoundError:
                self.create_save_data()
            pass

        def get_save_data(self):
            with open(f"data/{self.user}.txt", "r") as s:
                    last_save = s.readlines()
                    last_save = last_save[len(last_save)-1]
                    print(f"Last save file")
                    print(last_save)

        def create_save_data(self):
            with open(f"data/{self.user}.txt","w") as s:
                    div()
                    center("Select your class")
                    div()
                    print("1 - Warrior\n2 - Wizard\n3 - Rogue\n4 - Demon Hunter\n")
                    char = self.create_character()
                    if char == "1":
                        char = "Warrior"
                    elif char == "2":
                        char = "Wizard"
                    elif char == "3":
                        char = "Rogue"
                    elif char == "4":
                        char = "Demon Hunter"
                    s.write(f"1//{char}//1//Tutorial Grounds//Inventory")
                    print("New Save File Created!")

        def create_character(self):
            c = input("-> ")
            if c in ("1","2","3","4"):
                return c
            else:
                return self.create_character()
                

Game("hector")