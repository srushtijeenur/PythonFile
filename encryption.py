# import hashlib

# def encrypt_data(data):
#     return hashlib.sha256(data.encode()).hexdigest()

# def hash_keyword(keyword):
#     return hashlib.sha256(keyword.encode()).hexdigest()

# def generate_trapdoor(keyword):
#     return hashlib.sha256(("trap" + keyword).encode()).hexdigest()

import hashlib

def encrypt_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

def hash_keyword(keyword):
    return hashlib.sha256(keyword.encode()).hexdigest()
