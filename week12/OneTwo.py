"""mod doc"""
def one_two(number):
    """doc"""
    if number in (1, 2):
        return str(number)
    return one_two(number - 1) + one_two(number - 2)
print(one_two(int(input())))
