"""
Activity: Count the number of times each word appears in a given text input,
then print the two most common words and how many times they each appear.
Make sure to remove punctuation from the ends of the words
    Only remove punctuation from the ends of the words
        E.g: remove "." in "end." but leave "-" in "well-being"
Make sure to convert all letters to lowercase
    E.g: Convert "Hello" to "hello" before counting it in the dictionary
Print the resulting dictionary and the two most common words:
    E.g: text input is "The big bad boy hit the big red barn."
    Should print:
    {'the': 2, 'big': 2, 'bad': 1, 'boy': 1, 'hit': 1, 'red': 1, 'barn': 1}
    Most common word is 'the', mentioned 2 times
    Second most common word is 'big', mentioned 2 times
"""
import string #A module which can give us a list of all the punctuations, so we can remove those punctuation
text = input("Please enter the text\n") #Ask for the text to be input
counter = {} #Initialize dictionary variable
textlst = text.split() #Split the str input into a list, separating the string based on the " " character
for word in textlst: #Iterate through the list, manipulating the dictionary accordingly
    word = word.strip(string.punctuation) #Removes punctuation from both ends of the string. Leaves punctuation in the middle such as "I'm"
    word = word.lower() #Converts to lowercase
    counter[word] = counter.get(word,0) + 1 #Increments the value for the key by +1. If key doesn't exist, creates key default 0
print(counter) #Prints the dictionary

#This next block of code is to find the 2 most common words
commonword = "" #Initialize a string type variable to store the most common word
secondcommon = "" #Initialize a string type variable to store the second most common word
commoncount = 0 #Initialize an integer type variable to store the number of times the most common word appears
secondcommoncount = 0 #Initialize an integer type variable to store the number of times the second most common word appears
for key in counter: #Iterates through the dictionary
    if counter[key] > secondcommoncount: #Checks if the value of that key is larger than the second most common word
        if counter[key] > commoncount: #Checks if the value of that key is larger than the most common word
            commonword = key #If value is larger, then the most common word becomes the key
            commoncount = counter[key] #The most common count becomes the value of that key
        else: #Occurs if value of key is larger than second most common but smaller than most common
            secondcommon = key
            secondcommoncount = counter[key]
print("Most common word is '{}', mentioned {} times".format(commonword,commoncount))
print("Second most common word is '{}', mentioned {} times".format(secondcommon,secondcommoncount))