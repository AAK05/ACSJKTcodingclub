"""
Activity: Write a script to encrypt a message using Caesar Shift
    E.g: "abcde" encrypted with shift 2 becomes "cdefg"

The script should ask the user what message and what caesar shift value they want

Ignore spaces and uppercase
    E.g: treat "Hi my name is Adrien" the same as "himynameisadrien"
    So make sure to remove spaces and convert uppercase to lowercase
    Also ignore punctuation, although you don't have to account for that in this activity

Steps and tips (Ignore if you want to challenge yourself):
    First remove spaces and convert to lowercase
        E.g: " X y Z  " becomes "xyz"
    Then convert the string into a list of numbers
        E.g: convert "xyz" into [24,25,26]
        Remember, you can iterate through a string's characters using for loops
        Use the ord() function to help you do this
    Then iterate through and add the shift value
        E.g: [24,25,26] with shift 2 becomes [26,27,28]
    Then use modulo by 26 to make numbers "wrap around" back to 0
        E.g: [26,27,28] becomes [0,1,2]
    Lastly, convert list of numbers back to string
        E.g: [0,1,2] becomes "zab"
        Remember, 0 becomes "z", 1 becomes "a"
        Use the chr() function to help you do this

Good luck :)
"""
#Function to convert string to list of numbers
def converttonum(str):
    lst = []
    str = str.lower()
    str = str.replace(" ","")
    for n in str:
        num = ord(n)-96
        lst.append(num)
    return lst

#Function to convert list of numbers to string
def converttostr(numlst):
    charlst = []
    for n in numlst:
        if n==0:
            charlst.append("z")
        else:
            n += 96
            a = chr(n)
            charlst.append(a)
    char = "".join(charlst)
    return char

#Function to add shifts and modulo the numbers
#Combined with conversions to numlst and back to str
def caesarshift(str,i):
    original = converttonum(str)
    final = []
    for n in original:
        n += i
        n = n % 26
        final.append(n)
    endchar = converttostr(final)
    return endchar

#Asking for input and calling our function
inputstr = input("Please enter the string of characters to encrypt with caesarshift")
shift_value = int(input("Please enter the caesar shift value"))
print(caesarshift(inputstr,shift_value))