"""mod doc"""
num_dict = {0:0, 1:1}
def fibo(number):
    """return fibonancci value"""
    if number in num_dict:
        return num_dict[number]
    result = fibo(number - 1) + fibo(number - 2)
    num_dict[number] = result
    return result
print(fibo(int(input())))
