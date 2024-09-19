"""mod doc"""
def main():
    """doc"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    price = a * b
    group = b + c
    wanted = d//group
    remain = d%group
    if remain >= b:
        result = (wanted + 1) * price
        donut = (wanted + 1) * group
        print(f"{result} {donut}")
    else:
        result = (wanted * price) + ((d % group) * a)
        donut =  (wanted * group) + (d % group)
        print(f"{result} {donut}")
main()
