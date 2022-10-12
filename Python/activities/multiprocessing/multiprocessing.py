"""
Create a script to hash via sha-512 the 10 million strings in the strings.json file
Use multiprocessing to speed up the process, and compare between multiprocessed and single time
Use time module to measure time of each
Make sure that the multiprocessing does NOT change the order of the output list
"""
import json
import concurrent.futures
import hashlib
import time

"""def generatejsonfile(filename):
    import random
    import string
    lst = []
    for n in range(10000000):
        x = []
        if n%1000000==0:
            print(n)
        for i in range(5):
            x.append(random.choice(string.ascii_letters))
        lst.append("".join(x))
    with open(filename,"w") as f:
        json.dump(lst,f)"""

def readjsonfile(filename):
    #Function that reads the json file filled with a list of 10million strings
    with open(filename,"r") as f:
        return json.load(f)

def hashSHA512(string):
    #Function to hash a single string in SHA512
    #Make it yourself

if __name__ == "__main__":
    #Combine all the functions and use multiprocessing on them
    #Make sure all the orders are the same (Tip: use enumerate)