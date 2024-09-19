"""mod doc"""
def main():
    """doc"""
    price = int(input())
    cap = int(input())
    promotion = int(input())
    buy = int(input())
    total_price = 0
    my_cap = 0
    for _ in range(buy):
        if my_cap == cap and my_cap:
            total_price += promotion
            my_cap -= cap
            my_cap += 1
        else:
            total_price += price
            my_cap += 1
    print(total_price)
main()
