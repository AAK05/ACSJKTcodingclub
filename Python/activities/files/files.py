"""
Activity:
You are given a "raw-email.txt" file containing a list of emails, 1 email per line
Some emails end in @gmail.com, while others have @yahoo.com, @hotmail.com, etc

Instructions:
    Create a script to first read the .txt file
    Find all the emails ending in @gmail.com
    Write these emails ending in @gmail.com to a separate file, called "clean-email.txt"
    Write one email per line in this "clean-email.txt" file
    Bonus point:
        Write all the other emails, not ending in @gmail.com, to another file
        Name this file "legacy-email.txt"

Important tip:
    Make sure you run the script from the directory where the files are located
"""

clean = [] #Initializes list for @gmail.com emails
legacy = [] #Initializes list for legacy emails
with open("raw-email.txt","r") as raw_email: #opens file to read
    for line in raw_email: #Iterates line by line
        line = line.strip() #Removes whitespace such as newline
        if line.endswith("@gmail.com"): #Checks if email ends with @gmail.com
            clean.append(line) #Appends clean email to the list
        else:
            legacy.append(line) #Appends legacy email to the list

with open("clean_email.txt", "w") as clean_email: #Opens file to write clean emails
    for email in clean: #Iterates through list of clean emails
        clean_email.write(email + "\n") #Writes each clean email to file, adding newline

with open("legacy_email.txt", "w") as legacy_email: #Opens file to write legacy emails
    for email in legacy: #Iterates through list of legacy emails
        legacy_email.write(email + "\n") #Writes each legacy email to file, adding newline