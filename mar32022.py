def write_book(character, setting, skills):
    print(character + " is in " + setting + " has " + skills)


write_book("Darryl", "Cambodia", "coding")
print(write_book)

def volumerectangle(length, width, height):
    print(length*width*height)


volumerectangle(2, 6, 8)
print(volumerectangle)

volumerectangle(20, 21, 22)
print(volumerectangle)

def function(x):
    return x + 1

print(function(9))
print(function(10))

def getSmaller(num1, num2):
    if num1<num2:
        smaller = num1
    else:
        smaller = num2
    return smaller

def main():
    userInput1 = int(input("Enter a number: "))
    userInput2 = int(input("Enter a second number: "))
    
    smallerNumber = getSmaller(userInput1,userInput2)
    print("The smaller of the two numbers is", smallerNumber)


