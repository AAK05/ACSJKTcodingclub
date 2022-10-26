import numpy as np
import random
import time

choices = [i for i in range(10)]
data = random.choices(choices,k=10000000)
data1 = random.choices(choices,k=10000000)

def regular(data,data1):
    newlst = []
    for i in range(len(data)):
        newlst.append(data[i]*data1[i])
    return newlst

def numpyver(data,data1):
    nparray = np.array(data)
    nparray1 = np.array(data1)
    newarray = np.multiply(nparray,nparray1)
    newlist = newarray.tolist()
    return newlist

nparray = np.array(data)
nparray1 = np.array(data1)
t1 = time.time()
store = regular(data,data1)
t2 = time.time()
store = numpyver(nparray,nparray1)
t3 = time.time()
print("regular:",t2-t1)
print("numpyver:",t3-t2)