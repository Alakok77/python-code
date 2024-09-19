"""mod doc"""
def main():
    """doc"""
    cup = float(input())
    pro = float(input())
    discount = float(input())
    stand = float(input())
    wanted = int(input())
    pro1 = cup + (wanted - 1) * (cup * (1 - (pro/100)))
    pro2 = cup * wanted
    if wanted * cup >= stand:
        pro2 = pro2 * (1 - discount/100)
    if pro2 <= pro1:
        print("2")
        print(f"{pro2:.2f}")
    else:
        print("1")
        print(f"{pro1:.2f}")
main()
