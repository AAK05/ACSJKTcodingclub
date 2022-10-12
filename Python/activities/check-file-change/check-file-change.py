import os
import hashlib
import json

def hashfile(fobj):
    sha = hashlib.sha1()
    sha.update(fobj)
    return sha.hexdigest()

def openfile(fname):
    with open(fname,"rb") as f:
        return f.read()

def diriter(dir):
    digests = []
    for (root,subdirs,files) in os.walk(dir,topdown=True):
        for file in files:
            name = os.path.join(root,file)
            digests.append(hashfile(openfile(name)))
    return digests

def readjson(fname="ACSJKTcodingclub\\Python\\activities\\check-file-change\\state.json"):
    with open(fname,"r") as f:
        obj = json.load(f)
    return obj

def writejson(obj,fname="ACSJKTcodingclub\\Python\\activities\\check-file-change\\state.json"):
    with open(fname,"w") as f:
        json.dump(obj,f)

def main(dir="ACSJKTcodingclub\\Python\\activities\\check-file-change\\sample-folder"):
    try:
        prevstate = readjson()
    except:
        prevstate = []
    newstate = diriter(dir)
    if prevstate != newstate:
        print("Folder has been edited since last check")
        writejson(newstate)
    else:
        print("Folder has not been edited since last check")

if __name__ == "__main__":
    main()

#print(diriter("ACSJKTcodingclub\\Python\\activities\\check-file-change\\sample-folder"))
#print(hashfile(openfile("ACSJKTcodingclub\\Python\\activities\\check-file-change\\sample-folder\\subdirectory\\Test2.txt")))