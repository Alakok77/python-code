"""mod doc"""
def calculate(i):
    """doc"""
    if i == 0:
        return 0
    return len(str(i)) + 1 + calculate(i - 1)
number = int(input())
if number == 1:
    print("1")
else:
    print(calculate(number))
