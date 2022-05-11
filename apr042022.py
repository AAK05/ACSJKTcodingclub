# Dictionaries

exam = {"q1": "Math", "q2": "English", "q3": "Science"} # key: value
print(exam) 

students = {
    "Warren": True, # keys can only be strings, numbers and tuples (not important) 
    "Darryl": 1,
    True: "Warren"
}

print(students)

# dictionary key-value methods

# .keys(), .values(), .items()

alphabet_animals = {
    "a": "antelope",
    "b": "bear",
    "c": "chameleon",
}

print(alphabet_animals.keys()) # prints out keys of the dictionary
print(alphabet_animals.values()) # prints out values of the dictionary
print(alphabet_animals.items()) # prints out items of the dictionary

# get() method

liquid_solid = {
    "water": "wood",
    "lava": "marble",
    "juice": "cloth"
}

return_wood = liquid_solid.get("water", "water is not available")
print(return_wood)

return_glass = liquid_solid.get("glass")
print(return_glass)

return_brick = liquid_solid.get("brick", "brick is not available")
print(return_brick)

# .pop() method

liquid_solid = {
    "water": "wood",
    "lava": "marble",
    "juice": "cloth"
}

liquid_solid.pop("water")
print(liquid_solid)

# .update() method

dictionary1 = {"color": "blue", "shape": "circle"}
dictionary2 = {"color": "red", "number": 42}

updating = dictionary1.update(dictionary2)
print(updating)




