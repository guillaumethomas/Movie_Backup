import os
import hashlib
# https://docs.python.org/3.7/library/filecmp.html
import filecmp

start_path = '/Volumes/Films'  # current directory
print(os.listdir(start_path))
'''
for path, dirs, files in os.walk(start_path):
    for filename in files:
        print(os.path.join(path, filename))
        print(os.stat(os.path.join(path, filename)))
'''
'''
with open("/Volumes/Films/pi/Pagnol/Manon of the Spring.m4v", "rb") as f:
    file_hash = hashlib.md5()
    chunk = f.read(8192)
    i = 0
    while chunk is not None:
        file_hash.update(chunk)
        chunk = f.read(8192)
        print(i)
        i += 1
'''
file1 = "/Volumes/Films/pi/Pagnol/Manon of the Spring.m4v"
a = filecmp.cmp(file1, file1)
print(a)

# print(file_hash.digest())
# print(file_hash.hexdigest())  # to get a printable str instead of bytes