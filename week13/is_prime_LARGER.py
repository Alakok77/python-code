"""mod doc"""
def is_prime(number):
    """check prime"""
    for i in range(3, int(number ** 0.5) + 1, 2):
        if not number % i:
            return "False"
    return "True"

def main():
    """doc"""
    number = int(input())
    if number == 1 and number != 2:
        print("False")
    else:
        print(is_prime(number))
main()
