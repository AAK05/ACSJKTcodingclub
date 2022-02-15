"""
Activity: Create a script which prints only the first n odd numbers in a fibonacci sequence
    'n' is defined by user input, so you ask the user how many they want
The script should use at least two functions: one to generate the fibonacci sequence, and the other to remove even numbers from the sequence
The function to generate the fibonacci sequence should be imported from another file
    Note: you can use our for_loops_activity2.py as a basis for this function to save time
The function to remove even numbers should be defined in the same file
"""
from definitions import fibonacci

def remove_even(sequence):
    newsequence = []
    for i in sequence:
        if i%2!=0:
            newsequence.append(i)
    return newsequence

def main():
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
    original_fibonacci = fibonacci(3*n)
    print(original_fibonacci)
    modified_fibonacci = remove_even(original_fibonacci)
    print(modified_fibonacci[0:n])

main()