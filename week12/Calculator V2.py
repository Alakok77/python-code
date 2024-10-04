"""mod doc"""
def calculate(number):
    """doc"""
    if not number:
        return 1
    if number == 1:
        return 1
    return len(str(number)) + 1 + calculate(number - 1)
print(calculate(int(input())))
