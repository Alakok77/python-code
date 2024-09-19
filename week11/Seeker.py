"""mod doc"""
def main():
    """doc"""
    code = input()
    total = 0
    number = ""
    for i in f"{code}#":
        if i.isnumeric():
            number += i
        elif len(number) > 0:
            total += int(number)
            number = ""
    print(total)
main()
