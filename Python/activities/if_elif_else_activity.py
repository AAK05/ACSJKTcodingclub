"""
Activity: Write a script which asks for the user’s height in cm. 
If the user’s height is less than 160, print “short”. 
If user’s height is above 175, print “tall”. If user’s height is in between, print “average”.
"""
height = int(input("Please enter your height in cm"))
#int() function changes datatype from string to integer, allowing mathematical comparisons
if height < 160:
    print("Short")
elif height > 175:
    print("Tall")
else:
    print("Average")