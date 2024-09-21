"""mod doc"""
def main():
    """doc"""
    num1 = int(input())
    num2 = int(input())
    if not num1 or not num2:
        num1 = max(num1, num2)
    else:
        while num1 and num2:
            if num1 > num2:
                num1, num2 = num2, num1
            num2 %= num1
    if num1 != 1:
        print(f"NO\n{num1}")
    else:
        print("YES\n1")
main()
