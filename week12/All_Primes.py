"""mod doc"""
def is_prime(number):
    """doc"""
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            return False
    return True

def main():
    """doc"""
    number = int(input())
    cnt = 0
    for i in range(1, number + 1):
        if is_prime(i):
            cnt += 1
    print(cnt)
main()
