import hashlib

def hashstring(words):
    sha = hashlib.sha256()
    sha.update(words.encode("ascii"))
    return sha.hexdigest()

def hashfile(fname):
    sha = hashlib.sha256()
    with open(fname,"rb") as f:
        sha.update(f.read())
    return sha.hexdigest()

print(hashstring("Hello world"))
print(hashfile("Test0.txt"))