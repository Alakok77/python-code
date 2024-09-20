"""mod doc"""
def is_prime(i):
    """check prime"""
    if i <= 1:
        return 0
    for d in (2,3,5,7,11):
        if not i%d and i not in (2, 3, 5 ,7):
            return 0 + (is_prime(i - 1))
    return 1 + is_prime(i - 1)

def main():
    """doc"""
    number = int(input())
    print(is_prime(number))
main()
