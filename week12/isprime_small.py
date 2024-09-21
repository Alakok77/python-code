"""mod doc"""
def is_prime(i):
    """check prime"""
    for d in "23456789":
        if not i%int(d) and str(i) not in "2357" or i == 1:
            return "NO"
    return "YES"

def main():
    """doc"""
    number = int(input())
    print(is_prime(number))
main()
