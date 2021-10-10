"""
Activity: Create a script that asks for the names of people in a group one after another.
Keep asking for names until the user inputs the string "DONE". At this point, print the list,
sorted in alphabetical order. Make sure this script still works if inputs have differing upper and lowercases.
Eg: if "tOkyO" is input, make sure the list prints out "Tokyo"
"""
names = [] #Initialises a list to store the names
stop = False #Variable to determine whether to stop or continue asking for names
while stop == False:
    name = input("Please enter a name, or input DONE if done.")
    if name == "DONE":
        stop = True #if the special keyword "DONE" is input, the script stops asking for names
    else:
        name = name.lower() #Converts entire string to lowercase first
        name = name.capitalize() #Capitalizes the first letter of the string
        names.append(name) #Adds the name to the list of names
names.sort() #Sorts the list of names
print(names)