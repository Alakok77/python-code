"""mod doc"""
def my_func(x):
    """doc"""
    if x.isupper():
        return x
    return x.upper()
def main():
    """doc"""
    txt = input()
    alpha = []
    num = []
    for i in txt:
        if not i in alpha and i.isalpha():
            alpha.append(i)
            num.append(1)
        elif i.isalpha():
            num.insert(alpha.index(i), num[alpha.index(i)] + 1)
            num.pop(alpha.index(i) + 1)
    lst = list(zip(alpha, num))
    result = []
    for i in lst:
        result.append(f"{i[0]}{i[1]}")
    result.sort(key= my_func(i))
    print(result)
main()
