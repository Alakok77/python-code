"""mod doc"""
def fibo(number):
    """return fibonancci value"""
    if not number:
        return 0
    if number == 1:
        return 1
    return fibo(number - 1) + fibo(number - 2)
print(fibo(int(input())))
