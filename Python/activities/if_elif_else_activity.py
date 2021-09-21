height = int(input("Please enter your height in cm"))
#int() function changes datatype from string to integer, allowing mathematical comparisons
if height < 160:
    print("Short")
elif height > 175:
    print("Tall")
else:
    print("Average")