"""
Activity: Create a script which prints only the first n odd numbers in a fibonacci sequence
    'n' is defined by user input, so you ask the user how many they want
The script should use at least two functions: one to generate the fibonacci sequence, and the other to remove even numbers from the sequence
The function to generate the fibonacci sequence should be imported from another file
    Note: you can use our for_loops_activity2.py as a basis for this function to save time
The function to remove even numbers should be defined in the same file
"""
from definitions import fibonacci

def remove_even(sequence): #Defines a function to remove even numbers from a sequence
    newsequence = [] #Creates a new list where we store the odd numbers
    for i in sequence: #Iterates through the old list
        if i%2!=0: #If not even, then append to new list
            newsequence.append(i)
    return newsequence #return new list

def main(): #Defines a main function where the main tasks will be executed
    validans = False
    while validans == False:
        try:
            n = int(input("How many odd number terms of the Fibonacci sequence do you want?"))
            if n >= 0:
                validans = True
            else:
                print("Please enter a positive integer")
        except:
            print("Please enter a positive integer")
    #Above code is to obtain user input and ensure correct input is given
    original_fibonacci = fibonacci(3*n) #Generates first 3n terms, generating more than needed just in case
    modified_fibonacci = remove_even(original_fibonacci) #Removes even numbers from original sequence to create modified sequence
    print(modified_fibonacci[0:n]) #prints the first n terms from modified sequence

main() #executes main