"""mod doc"""
def main():
    """doc"""
    number = input().replace("-", "")
    test = number[-1]
    if test == "X":
        test = 10
    total = 0
    for i, j in enumerate(number):
        if i == len(number) - 1:
            break
        total += int(j) * (10-i)
    total = (total * -1)%11
    if total == int(test):
        print("Yes")
    else:
        if total == 10:
            total = "X"
        print(f"No {total}")
main()
