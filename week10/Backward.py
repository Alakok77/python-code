"""mod doc"""
def main():
    """doc"""
    text = ""
    lst = []
    while True:
        text = input()
        if text == "NULL":
            break
        lst.append(text)
    for i in lst[-1::-1]:
        print(i)
main()
