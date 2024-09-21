"""mod doc"""
def is_prime(number):
    """check prime"""
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            return "NO"
    return "YES"

def main():
    """doc"""
    number = int(input())
    if number == 1:
        print("NO")
    else:
        print(is_prime(number))
main()
