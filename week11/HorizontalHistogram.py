"""mod doc"""
def main():
    """doc"""
    txt = input()
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    my_dict = {}
    for i in alpha:
        if i in txt:
            my_dict[i] = txt.count(i)
    lst = my_dict.keys()
    result = ""
    for i in lst:
        result += f"{i} : "
        for j in range(1, my_dict[i]+my_dict[i]//5 + 1):
            if not j%6:
                result += "|"
            else:
                result += "-"
        if result[-1] == "|":
            print(result[0:-1])
        else:
            print(result)
        result = ""
main()
