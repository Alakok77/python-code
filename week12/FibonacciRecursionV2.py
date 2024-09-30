"""mod doc"""
num_dict = {0:0, 1:1}
def fibo(numbers):
    """return fibonancci value"""
    if numbers in num_dict:
        return num_dict[numbers]
    result = fibo(numbers - 1) + fibo(numbers - 2)
    num_dict[numbers] = result
    return result
print(fibo(int(input())))
