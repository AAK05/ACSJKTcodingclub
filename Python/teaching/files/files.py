#Opening and closing files
#file = open("sample.txt")
#file.close()

#Opening as r,w,a,x,
#file = open("sample.txt", "r") #only read

#File object read methods: .read(), .readlines(), .readline()
file = open("sample.txt", "r")
contents = file.readline()
#print(contents)
file.close()

#File object write methods: .write()
#file = open("sample.txt","w")
#texts = ["apple","pear","mouse","keyboard"]
#for item in texts:
#    file.write(item + "\n")
#file.close()

#File object iteration
file = open("sample.txt","r")
#for a in file:
#    print(a,end="")
#file.close()

#"with open(filename,mode) as file_object:" syntax
with open("sample.txt","r") as file:
    text=file.readlines()
    print(text)

