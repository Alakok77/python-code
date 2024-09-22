"""mod doc"""
def main():
    """doc"""
    txt = input()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    my_dict = {}
    for i in alpha:
        if i in txt:
            my_dict[i] = txt.count(i)
    values_lst = list(my_dict.values())
    key_lst = list(my_dict.keys())
    for i in range(max(list(my_dict.values())), -1, -1):
        for j in range(len(my_dict)):
            if not j and not i:
                print("  ", end = "  ")
            elif not j:
                print(str(i).rjust(2), end = "  ")
            if not i:
                print(key_lst[j], end = " ")
            elif values_lst[j] >= i:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print("")
main()
