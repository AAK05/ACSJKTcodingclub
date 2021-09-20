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