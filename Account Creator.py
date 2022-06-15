from os import system
from tkinter import END, StringVar, Tk, Label, Text, Button, Frame
import re


class Account_Creator(): 
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.title("Password Checker")
        self.root.configure(bg="#134D0A")

        self.inputbox = Frame(self.root, bg="#4E9942", height=205, width=400)
        self.inputbox.place(x=60,y=30)

        self.usernamelabel = Label(self.root, text="Username", font=("Arial", 12, "bold"), bg="#4E9942")
        self.usernamelabel.place(x=90, y=50)

        self.passlabel = Label(self.root, text="Password", font=("Arial", 12, "bold"), bg="#4E9942")
        self.passlabel.place(x=90, y=100)

        self.emaillabel = Label(self.root, text="Email", font=("Arial", 12, "bold"), bg="#4E9942")
        self.emaillabel.place(x=90, y=150)

        self.usertext = Text(self.root, width=25, height=1, font=("Arial", 11, "bold"))
        self.usertext.place(x=200,y=50)

        self.passtext = Text(self.root, width=25, height=1, font=("Arial", 11, "bold"))
        self.passtext.place(x=200,y=100)

        self.emailtext = Text(self.root, width=25, height=1, font=("Arial", 11, "bold"))
        self.emailtext.place(x=200,y=150)

        self.button = Button(self.root, text="Create", height=1, border=0, command=lambda: self.create_account(self.usertext.get("1.0", END), self.passtext.get("1.0", END), self.emailtext.get("1.0",END)))
        self.button.place(x=350, y=195)


        self.errortext = ""
        self.errorframe = Frame(self.root, bg="#4E9942", height=90, width=320)
        self.errorlabel = Label(self.root, text=self.errortext, bg="#4E9942", border=0)
        

    def create_account(self, user, passw, email):
        self.username_checker(user)
        self.password_checker(passw)
        self.email_checker(email)

    
        self.errorlabel.place(x=120, y=250)
        self.errortext=""

    #Checks for intersections between two sets and returns whether or not the number of intersections is less than the required count(True or False).
    def req_check(self, set1, set2, count): 
        return len(set1.intersection(set2)) < count

    #Checks if a string meets the letter, numbrer, character, and symbol count requirements passed through the function. If not, it outputs what the error on the errortext string to be displayed by the error label.
    def password_checker(self, passw, letter_count=3, number_count=2, symbol_count=1, pass_length=7): #Arguements are the minimum requirement for each character type in password. Sets corresponding to these values are defined in the beginning of function.
        state = True
        letter_list = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        number_list = set("0124356789")
        symbol_list = set("!”#$%&'()*+,-./:;<=>?@[]^_`{|}~:")

        if len(passw) < pass_length:
            self.errortext+="\n"+f"You're password needs to be at least {pass_length} characters long"
            state =  False

        if self.req_check(letter_list, set(passw), letter_count):
            self.errortext+="\n"+f"You're password requires at least {letter_count} letters."
            state = False

        if self.req_check(number_list, set(passw), number_count):
            self.errortext+="\n"+f"You're password requires at least {number_count} numbers"
            state = False

        if self.req_check(symbol_list, set(passw), symbol_count):
            self.errortext+="\n"+f"You're password requires at least {symbol_count} symbol"
            state = False

        if(state):
            self.errortext+="You're password meets the requirements" 
            self.errorlabel.configure(text=self.errortext)
            return state 
        else:
            self.errorlabel.configure(text=self.errortext)
            return state
    
    #Checks if a string contains a space. If so, it appends the error to the errortext string that is later displayed by the error label.
    def username_checker(self, user):
        if(" " in user):
            self.errortext+="You're username cannot include any spaces"

    def email_checker(self, email):
        self.errortext+="\n"+"The email provided is invalid"
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat,email):
            return True
        self.errortext+="\n"+"The email provided is invalid"
        return False




#password_checker()
main = Tk()
Account_Creator(main)
main.mainloop()
