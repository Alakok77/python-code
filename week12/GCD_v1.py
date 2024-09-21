"""mod doc"""
def main():
    """doc"""
    num1 = int(input())
    num2 = int(input())
    if not num1 or not num2:
        print(max(num1, num2))
    else:
        while num1 and num2:
            if num1 > num2:
                num1, num2 = num2, num1
            num2 %= num1
        print(num1)
main()
