"""mod doc"""
def main():
    """doc"""
    parity_bit = input()
    wanted = input()
    check = 0
    for i in parity_bit:
        if i == "1":
            check += 1
    if wanted == "Even":
        if check % 2:
            print(f"{parity_bit}1")
        else:
            print(f"{parity_bit}0")
    elif wanted == "Odd":
        if not check % 2:
            print(f"{parity_bit}1")
        else:
            print(f"{parity_bit}0")
main()
