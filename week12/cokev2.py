"""mod doc"""
def coke(price, cap, discount, wanted, my_cap):
    """doc"""
    if wanted < 1:
        return 0
    if my_cap >= cap:
        return discount + coke(price, cap, discount, wanted - 1, my_cap - cap + 1)
    return price + coke(price, cap, discount, wanted - 1, my_cap + 1)

print(coke(int(input()), int(input()), int(input()), int(input()), 0))
