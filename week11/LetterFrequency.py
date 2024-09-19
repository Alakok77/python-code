"""mod doc"""
def main():
    """doc"""
    text = input().lower()
    count_dict = {}
    for i in text:
        if not i in count_dict and not i.isspace():
            count_dict[i] = 1
        elif not    i.isspace():
            count_dict[i] += 1
    lst_key = list(count_dict.keys())
    lst_values = list(count_dict.values())
    print(f"{lst_key[lst_values.index(max(lst_values))]}")
main()
