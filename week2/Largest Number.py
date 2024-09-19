"""mod doc"""
def main():
    """doc"""
    a = input()
    b = input()
    c = input()
    num1 = f"{a}{b}{c}"
    num2 = f"{a}{c}{b}"
    num3 = f"{b}{a}{c}"
    num4 = f"{b}{c}{a}"
    num5 = f"{c}{a}{b}"
    num6 = f"{c}{b}{a}"
    pair1 = num1 if num1 >= num2 else num2
    pair2 = num3 if num3 >= num4 else num4
    pair3 = num5 if num5 >= num6 else num6
    semi = pair1 if pair1 >= pair2 else pair2
    final = semi if semi >= pair3 else pair3
    print(int(final))
main()
