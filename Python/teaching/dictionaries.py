"""
Syntax of dictionaries
    dict = {"key":"value","anotherkey":2,"yetanotherkey":[1,2,3]}
.get() method
iterating through dictionary
"""
var = {"key":"value","key2":3}
#print(var["key"])
#print(var["key2"])

print(var.get("key"))
print(var.get("key5",3))

#for key in var:
    #print(var.get(key))