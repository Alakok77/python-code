"""mod doc"""
def main():
    """doc"""
    text = input()
    result = ""
    multi = ""
    for i in text:
        if i.isnumeric():
            multi += i
        else:
            result += int(multi) * i
    print(result)
main()
