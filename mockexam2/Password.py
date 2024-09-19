"""mod doc"""
import math
def entropy_cal():
    """doc"""
    password = input()
    pool = 0
    long = len(password)
    upper_first = True
    lower_first = True
    num_first = True
    iden_first = True
    iden = "!\"#$%&'()*+,-./:;<=>?@[\r]^_`{|}~"
    for i in password:
        if i.isupper() and upper_first:
            pool += 26
            upper_first = False
        if i.islower() and lower_first:
            pool += 26
            lower_first = False
        if i.isnumeric() and num_first:
            pool += 10
            num_first = False
        if i in iden and iden_first:
            pool += 32
            iden_first = False
    entropy = math.floor(math.log(pool**long, 2))
    return entropy

def main(entropry):
    """mod doc"""
    print(entropry)
    if entropry < 28:
        print("Very Weak")
    elif 28 <= entropry <= 35:
        print("Weak")
    elif 36 <= entropry <= 59:
        print("Reasonable")
    elif 60 <= entropry <= 127:
        print("Strong")
    else:
        print("Very Strong")

main(entropy_cal())
