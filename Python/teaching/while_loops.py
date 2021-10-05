n = False
while n == False:
    answer = input("Please enter your age.")
    try:
        answer = int(answer)
        n = True
    except:
        print("Invalid answer. Please retry.")
print("Your age is:", str(answer))