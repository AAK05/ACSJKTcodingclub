"""
Activity: Create a fibonacci sequence calculator which creates a list containing the 
first n terms in the fibonacci sequence. n is determined by user input.

Fibonacci sequence:
    1,1,2,3,5,8,13,21,34,55,89,...
    U(1)=1, U(2)=1, U(n+1)=U(n)+U(n-1)
    The first two numbers in the fibanacci sequence are both 1
    The next number in the fibonacci sequence is the sum of the previous two numbers

Example: User enters the number 10:
    Calculate and print out the first 10 numbers in the sequence: [1,1,2,3,5,8,13,21,34,55]
Example: User enters the number 200:
    Calculate and print the first 200 terms in the sequence: [1,1,2,3,5,...,280571172992510140037611932413038677189525]
"""
#First, ask for the number of terms, reject if not n>=0 or if float or string is input
while True:
    terms = input("Please enter the number of terms of the fibonacci sequence you want to have printed:")
    try:
        terms = int(terms)
        if terms >= 0:
            break
        else:
            print("Invalid response, must not be negative")
    except:
        print("Invalid response, must be integer ")

sequence = [1,1] #Initialize first 2 terms in the sequence, which are default
if terms == 0: #Special case if n=0, print empty list
    print([])
elif terms == 1: #Special case if n=1, print [1]
    print([1])
else:
    for i in range(terms - 2):
        sequence.append(sequence[i] + sequence[i+1])
    """
    Used range(terms - 2) because if terms=5, then we only need to append the next 3 values because first 2 already default
    Iterates through the values of i, starting from i=0, i=1, ..., i=(terms-2)-1
    .append(sequence[i] + sequence[i+1]) adds together the last 2 values in the list and then appends it to the end of the list
        When i=0: sequence=[1,1], sequence[i]=1, sequence[i+1]=1, sequence[i]+sequence[i+1]=2
        When i=1: sequence=[1,1,2], sequence[i]=1, sequence[i+1]=2, sequence[i]+sequence[i+1]=3
        When i=2: sequence=[1,1,2,3], sequence[i]=2, sequence[i+1]=3, sequence[i]+sequence[i+1]=5
        When i=3: sequence=[1,1,2,3,5], sequence[i]=3, sequence[i+1]=5, sequence[i]+sequence[i+1]=8
        When i=4: sequence=[1,1,2,3,5,8], sequence[i]=5, sequence[i+1]=8, sequence[i]+sequence[i+1]=13
        When i=5: sequence=[1,1,2,3,5,8,13], sequence[i]=8, sequence[i+1]=13, sequence[i]+sequence[i+1]=21
        Etc...
    """
    print(sequence) #prints resulting sequence