#Defining a function
"""
def count(m):
    n = 0
    while n < m+1:
        print(n)
        n+=1

count(8)
"""
def area_square(length):
    area = length**2
    return area

#Importing a function
from circles import circle_area

#Calling a function
areaofcircle = circle_area(2)
areaofsquare = area_square(2)
print(areaofcircle)
print(areaofsquare)
