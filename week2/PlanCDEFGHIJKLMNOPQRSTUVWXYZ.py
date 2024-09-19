"""mod doc"""
def main():
    """doc"""
    txt = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    a = 1.0
    b = 1.0
    c = 1.0
    if num1 >= num2:
        a = num1
        if num1 >= num3:
            if num2 >= num3:
                b = num2
                c = num3
            else:
                a = num1
                b = num3
                c = num2
        else:
            a = num3
            b = num1
            c = num2
    else:
        a = num2
        if num2 >= num3:
            if num3 >= num1:
                b = num3
                c = num1
            else:
                b = num1
                c = num3
        else:
            a = num3
            b = num2
            c = num1
    if txt == "Ascend":
    # น้อยไปมาก
        print(f"{c:.2f}, {b:.2f}, {a:.2f}")
    elif txt == "Descend":
    # มากไปน้อย
        print(f"{a:.2f}, {b:.2f}, {c:.2f}")
main()
