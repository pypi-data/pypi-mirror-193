import secrets
import string

def random_passwd(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    password = ''.join(secrets.choice(all) for i in range(length))  
    return password