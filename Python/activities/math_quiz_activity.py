"""
Activity: Write a script that quizzes the user with basic arithmetic questions
Questions should follow the format "a + b", "a - b", "a * b", or "a / b"
    Operators (+,-,*,/) should be generated randomly
    Value "a" should be generated randomly for 0<=a<=10
    Value "b" should be generated randomly for 1<=b<=10
        "b" should not be 0 because it may cause division by zero errors
    Round off answers to 2 decimal points
Ask 10 questions, check how many answers are correct, then present the final score out of 10
Hints:
    Search up "random.randint()"
    Search up "eval()"
"""
import random #Python module which generates pseudo-random numbers

print("Math Quiz: 10 marks\nRound off your answers to 2 decimal points where necessary")

#Generate the questions and answers:
questions = {} #Initialize dictionary to store questions
answers = {} #Initialize dictionary to store corresponding answers
operator_translate = {0:"+", 1:"-", 2:"*", 3:"/"} #Dictionary table to convert integers to operator symbols
for qn in range(1,11): #Iterates through questions number 1-10
    a = str(random.randint(0,10)) #Generates and stores random integer "a"
    b = str(random.randint(1,10)) #Generates and stores random integer "b"
    operator = random.randint(0,3) #Genetrates and stores random integer to determine operator symbol
    equation = a + " " + operator_translate[operator] + " " + b 
    """
    Creates a string out of the randomly generated integers.
    operator_translate[operator] provides the value to the key, 
    where the keys are the integers and the values are the operator symbols
    """
    questions[qn] = equation #Stores question in the dictionary
    answers[qn] = round(eval(equation),2) #Calculates, rounds off to 2 dp, then stores answer in dictionary
#print(questions) #Debug print statemet
#print(answers) #Debug print statement

#Ask the questions:
score = 0 #Variable to store score count
for key in questions: #Iterates through questions number 1-10
    formattedqn = str(key) + ". " + questions[key] + " =" #Generates a formatted string out of the question number and question
    validans = False #Variable which becomes True when a valid answer is received
    while not validans: #While loop to ensure question is continuously asked until valid answer is received
        ans = input(formattedqn)
        try:
            ans = float(ans)
            validans = True
        except:
            print("Invalid response")
    if ans == answers[key]: #Compares user answer to previously generated answer
        score += 1 #Increments score +1 if answer is correct
print("Score: " + str(score) + "/10") #Print final score