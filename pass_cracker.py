import hashlib

user_hash_dict = {}

with open('passwords.txt', 'r') as f:
    passwords = f.read().splitlines()

with open('user_hash.txt', 'r') as f:
    txt = f.read().splitlines()
    for userHash in txt:
        username = userHash.split(":")[0]
        hash = userHash.split(":")[1]
        user_hash_dict[username] = hash

for password in passwords:
    hashedPass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for username, hash in user_hash_dict.items():
        if hashedPass == hash:
            print(f'Hash has been found\n{username}:{password}')

