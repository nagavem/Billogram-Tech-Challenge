#Service for generating the discount codes
import random
import string
import secrets

def discount_generator():
    num = 9
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for x in range(num))
    return str('{'+res+'}')


