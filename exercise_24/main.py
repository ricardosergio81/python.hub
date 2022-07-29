import hashlib

file1 = 'file1.txt'
file2 = 'file2.txt'

#print(hashlib.algorithms_available)

hash1 = hashlib.md5()
hash1.update(open(file1, 'rb').read())

hash2 = hashlib.md5()
hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print("Files are different")
    print(f"Hash file 1 {hash1.hexdigest()}")
    print(f"Hash file 2 {hash2.hexdigest()}")
else:
    print("Files are equals")
