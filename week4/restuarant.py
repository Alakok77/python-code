"""mod doc"""
def main():
    """doc"""
    price = float(input())
    stand = float(input())
    discount = float(input())
    add = float(input())
    new_price = 0
    if price >= stand:
        price -= price * (discount/100)
        new_price = price
    elif price + add < stand:
        new_price += add + price
    else:
        new_price = (price + add) * ((100 - discount)/100)


    if new_price > price:
        print(f"No {new_price - price:.3f}")
    elif price > new_price:
        print(f"Yes {price - new_price:.3f}")
    else:
        print("Yes")
main()
