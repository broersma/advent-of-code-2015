import hashlib

key = b"ckczppom"
for i in range(104897000):
    md5 = hashlib.md5()
    md5.update(key + bytes(str(i), encoding='utf8'))
    if md5.hexdigest().startswith("0"*6):
        print(i)
        break