# PassCracker

PassCracker is a Python script designed to crack hashed passwords using brute force techniques. It utilizes the hashlib library to generate SHA-256 hashes and compares them against a dictionary of hashed passwords stored in a user_hash.txt file.

## Features

- **Password Cracking**: PassCracker reads a list of plaintext passwords from a passwords.txt file and generates their SHA-256 hashes. It then compares these hashes against a dictionary of username-password hashes stored in user_hash.txt to identify matches.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/AdvaitKhaire/pass-cracker.git
```

2. Navigate to the project directory:

```bash
cd pass-cracker
```

3. Run the PassCracker script:

```bash
python pass_cracker.py
```

## Usage

1. Ensure that the passwords.txt file contains a list of plaintext passwords you want to crack.
2. Update the user_hash.txt file with username-password hashes in the format `username:hash`.
3. Run the pass_cracker.py script to initiate the password cracking process.

## Example

Suppose we have the following entries in passwords.txt:

```
test123
password1
12345
```

And the user_hash.txt file contains the following entries:

```
user1:5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
user2:5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
user3:3b28fa7d63b6d6f3ef296b265c4e798d11461877b91db24b72cbd8ab11602beb
```

Running the PassCracker script will output:

```
Hash has been found
user1:test123
```
