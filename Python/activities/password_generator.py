#!/usr/bin/env python3
"""
Activity: Create a script to randomly generate a password

The core function is to just randomly ask the user for the length of the password, then generate a string of random characters
However, this is the sort of activity where you can be creative
Add as many of your own features to this generator for example:
    Automatic copy to clipboard
    Option to limit which characters are allowed in the generator (e.g: only letters, only digits, only punctuation, etc)
    etc

Tip: use the library called 'string', 'random', 'pyperclip'
    'string' library provides a collection of characters
        string.ascii_letters generates a string of all the lowercase and uppercase letters, 52 characters long
        There are others such as string.digits, string.punctuation, etc which you can use
    'random' library allows random generation
        random.choice() randomly selects a character from a string
    'pyperclip' library allows copying to clipboard
        To install, type "pip install pyperclip" for windows, or "pip3 install pyperclip" for mac
        pyperclip.copy() copies to clipboard
        pyperclip.paste() returns the item that was in the clipboard
"""

import random
import string
import pyperclip
def generate(length): #Creates function to generate passcode, taking length as parameter
    x=[] #Initialize a list to store every character of the passcode
    for i in range(length): #for loop used as a counter to see how many characters has been appended
        x.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
        #string.ascii_letters returns a string of all characters
        #string.digits and string.punctuation also return strings
        #random.choice() selects a random character from the concatenated string
        #Random choice is appended to list x
    return ''.join(x) #Joins all the elements of the list into a stringm, seperated by ""

lastclip = pyperclip.paste() #Stores the last copied item, just in case it was important
out = generate(int(input("Enter password length:"))) #Asks for password length and generates
if input("Copy password to clipboard? [y/n]") == "y": #Optional copy to clipboard
    pyperclip.copy(out) #Copies to clipboard
    print('Password successfully copied')
    if input("Print previous clipboard contents? [y/n]") == "y": #asks if we need to print the previous clipboard items
        print(lastclip)
if input("Print password to screen? [y/n]") == "y":
    print(out)