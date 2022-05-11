# def book(name, character, setting, plot):
     # print(name + character + setting + plot)

 #print(book("Harry Potter", "Harry", "Azkaban", "Wizard dying"))

 # print(book("Builder", "Mark", "USA", "mark built a house" ))

def my_function(x):
    return x + 1

print(my_function(3))

def build_a_computer(cpu, gpu):
    if(cpu=="ready" and gpu=="ready"):
        print("Computer is ready to be built.")
    else:
        print("you do not have the parts to build a computer!")

y = build_a_computer("ready", "ready")
print(y)

z = build_a_computer("Not ready", "ready")
print(z)


def lots_of_math(a, b, c, d):
  first = a + b
  second = c - d
  third = first * second
  fourth = third % a
  print(first)
  print(second)
  print(third)
  return fourth

lots_of_math(1, 2, 3, 4)

