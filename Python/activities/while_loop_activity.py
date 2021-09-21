"""
Activity: Write a script which asks for the user’s full name and gender. If gender is female, 
ask for marital status of user. If user is male, print “Hello Mr {name}”. If user is female and married, 
print “Hello Mrs {name}”. If user is female and unmarried, print “Hello Ms {name}”. 
Make sure the script asks again for the gender or marital status if an unsuitable answer is provided 
(e.g: the question is “Please enter your gender [M/F]”, and the answer was “123”, print(“invalid response”) before asking again)
"""
name = input("Please enter your full name.")
gendervalid = False #variable which becomes True if a valid response for gender is recorded
maritalvalid = False #variable which becomes True if a valid response for maritalstatus is recorded
while gendervalid == False: #while loop ensures that the questions are asked again if responses are still invalid
    gender = input("Please enter your gender [M/F]")
    gender = gender.upper() #.upper() method changes the string content to uppercase to accept lowercase responses
    if gender == "M":
        print("Hello Mr. " + name)
        gendervalid = True #changes variable to True in order to stop the while loop
    elif gender == "F":
        while maritalvalid == False:
            maritalstat = input("Are you married? [Y/N]")
            maritalstat = maritalstat.upper()
            if maritalstat == "Y":
                print("Hello Mrs. " + name)
                maritalvalid = True
            elif maritalstat == "N":
                print("Hello Ms. " + name)
                maritalvalid = True
            else:
                print("Invalid response")
                #If invalid response is received, maritalvalid variable remains False and while loop repeats
        gendervalid = True
    else:
        print("Invalid response")
        #If invalid response is received, gendervalid variable remains False and while loop repeats