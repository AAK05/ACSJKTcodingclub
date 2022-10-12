import os

filepaths = []

dir = "ACSJKTcodingclub\\Python\\teaching\\oswalk\\test-folder"
for (root,subdirs,files) in os.walk(dir,topdown=True):
    for file in files:
        name = os.path.join(root,file)
        filepaths.append(name)

print(filepaths)