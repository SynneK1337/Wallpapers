import hashlib
import os

path = os.getcwd()
filenames = os.listdir(os.getcwd())
hashes = []
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
           hash_md5.update(chunk)
        if hash_md5.hexdigest() in hashes:
            print(fname, " Removed.")
            os.remove(fname)
        hashes.append(hash_md5.hexdigest())

for filename in filenames:
    md5(filename)
