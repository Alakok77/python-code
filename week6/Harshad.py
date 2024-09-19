"""Harshad Number"""
def harshad_check():
    """checking Harshad Number"""
    number = 0
    for _ in range(10):
        number = abs(int(input()))
        total = 0
        for i in str(number):
            total += int(i)
        if not int(number):
            print("No")
        elif int(number) % total:
            print("No")
        else:
            print("Yes")
harshad_check()
