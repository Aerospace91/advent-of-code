import hashlib

def computeMD5hash(the_string):
    m = hashlib.md5()
    m.update(the_string.encode('utf-8'))
    return m.hexdigest()

user_input = 'ckczppom'
#user_input = 'pqrstuv'

hash_not_found = True
i = 0
while hash_not_found:
    hashify = user_input + str(i)
    hashed_string = computeMD5hash(hashify)
    if hashed_string[:5] == '00000':
        hash_not_found = False
    i += 1

print(i - 1)