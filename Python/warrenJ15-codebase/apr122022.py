## -- Variables -- ##
abraham = 0
ada = 0
frieda = 0
moe = 0

     
## -- Instructions -- ##

print ("Which famous historical figure are you? Answer the questions below to find out!")
input ("Press Enter to Begin")
print ()

#### ---- QUESTIONS ---- ####

## -- Question 1 -- ##

print (" I would rather...")
print ("    a) Do something brand new")
print ("    b) Improve something that already exists")
answer = input (" Your answer: ")

## -- Scores 1 -- ##

if answer == "a" :
       ada += 1
       
elif answer == "b" :
       frieda += 1
       abraham += 1
       
else :
       moe += 1
       print ("That wasn't one of the available choices. Moving on.")
    
print ()






## -- Question 2 -- ##
print ("My idea of fun is...")
print ("    a) Spending time with friends")
print ("    b) Creating art ")
print ("    c) Learning something new")
answer2 = input ("Your answer: ")

## -- Scores 2 -- ##

if answer2 == "a" :
       abraham += 1
       
elif answer2 == "b" :
       frieda += 1
       
elif answer2 == "c" :
       ada += 1
       
else :
       moe += 1
       print ("That wasn't one of the available choices. Next question.")

print ()

## -- Question 3 -- ##

print ("Of the following, my favorite class is: ")
print ("    a) English")
print ("    b) Math")
print ("    c) Art")
answer3 = input ("Your answer: ")  

## -- Scores 3 -- ##

if answer3 == "a" :
       abraham += 1
       
elif answer3 == "b" :
       ada += 1
       
elif answer3 == "c" :
       frieda += 1
       
else :
       moe += 1
       print ("That wasn't one of the available choices. Ignoring your answer.")         
print ()

#### ---- FINAL SCORES ---- ####

## -- Label -- ##

print ("-- YOUR HISTORICAL FIGURE --")

## -- All scores -- ##
print()
print ("Your final scores were as follows: ")
print ("Abraham Lincoln = " + str(abraham) )
print ("Ada Lovelace = " + str(ada) )
print ("Frieda Kahlo = " + str(frieda) )

## -- Joke win -- ##
print()
if moe == 3 :
    print ("Alright wise guy, you're Moe Howard.")

## -- Majority win -- ##

elif abraham > ada and abraham > frieda :
    print ("You are Abraham Lincoln!")

elif ada > abraham and ada > frieda :
    print ("You are Ada Lovelace!")
    
elif frieda > abraham and frieda > ada :
    print ("You are Frieda Kahlo!")

## -- No majority -- ##
else :
    print ("You didn't get a majority score on any one person; looks like you're a true individual!")
