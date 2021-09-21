"""
Activity: Historical Figures Personality test
"""
Ada = 0
Frieda = 0
Lincoln = 0
Moe = 0
print("Which famous historical figure are you?")
input("Press enter to begin the quiz")

#Question1

print("Would you rather:")
print("a) Do something brand new")
print("b) Improve something that already exists")
qn1 = input()
if qn1 == "a":
    Ada = Ada + 1
elif qn1 == "b":
    Frieda = Frieda + 1
    Lincoln = Lincoln + 1
else:
    print("Invalid answer")
    Moe += 1

#Question2

print("My idea of fun is:")
print("a) Spending time with friends")
print("b) Creating art")
print("c) Learning new things")
qn2 = input()
if qn2 == "a":
    Lincoln += 1
elif qn2 == "b":
    Frieda += 1
elif qn2 == "c":
    Ada += 1
else:
    print("Invalid answer")
    Moe += 1

#Question3

print("My favourite subject is:")
print("a) English")
print("b) Math")
print("c) Art")
qn3 = input()
if qn3 == "a":
    Lincoln += 1
elif qn3 == "b":
    Ada += 1
elif qn3 == "c":
    Frieda += 1
else:
    print("Invalid answer")
    Moe += 1

print("-- YOUR HISTORICAL FIGURE --")
print("Abraham Lincoln:",Lincoln)
print("Ada Lovelace:",Ada)
print("Frieda Kahlo:",Frieda)
print("-"*15)

if Frieda > Lincoln and Frieda > Ada:
    print("You are Frieda Kahlo")
elif Lincoln > Frieda and Lincoln > Ada:
    print("You are Abraham Lincold")
elif Ada > Lincoln and Ada > Frieda:
    print("You are Ada Lovelace")
else:
    print("Congrats wise guy, you're Moe Howard")