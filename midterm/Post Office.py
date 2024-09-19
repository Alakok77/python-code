"""mod doc"""
def main():
    """doc"""
    envolop = int(input())
    package = int(input())
    price = (envolop * 13) + (package * 15)
    weight = 0
    for _ in range(envolop):
        weight = float(input())
        if weight <= 10:
            price += 16
        elif 10 < weight <= 20:
            price += 18
        elif 20 < weight <= 100:
            price += 23
        elif 100 < weight <= 250:
            price += 28
        elif 250 < weight <= 500:
            price += 33
        elif 500 < weight <= 1000:
            price += 48
        else:
            price += 68

    for _ in range(package):
        weight = float(input())
        if weight <= 500:
            price += 45
        elif 500 < weight <= 1000:
            price += 55
        else:
            price += 70
    print(f"{price}")
main()
