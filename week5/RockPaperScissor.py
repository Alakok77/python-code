"""mod doc"""
def main():
    """doc"""
    text = input()
    a = 0
    b = 0
    for i in range(0,len(text),2):
        check = f"{text[i]}{text[i+1]}"
        if check == "RP":
            b += 1
        elif check == "PR":
            a += 1
        elif check == "SP":
            a += 1
        elif check == "PS":
            b += 1
        elif check == "SR":
            b += 1
        elif check == "RS":
            a += 1
    if a == b:
        print(f"DRAW {a}")
    elif a > b:
        print(f"A win {a}-{b}")
    else:
        print(f"B win {b}-{a}")
main()
