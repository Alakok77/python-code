"""mod doc"""
def main():
    """doc"""
    number = input()
    press = 0
    for i in range(1, int(number) + 1):
        press += len(str(i)) + 1
    if number in ("0","1"):
        print("1")
    else:
        print(f"{press}")
main()