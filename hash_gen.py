import hashlib

password = "advait16"
hash = hashlib.sha256(password.encode('utf-8'))
print(hash.hexdigest())