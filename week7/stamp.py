"""mod doc"""
def main():
    """doc"""
    times = int(input())
    promotion = int(input())
    stamp = int(input())
    change = int(input())
    discount = int(input())
    price = 0
    total = 0
    my_stamp = 0
    price_result = 0
    for _ in range(times):
        price = int(input())
        if my_stamp >= change:
            price -= (my_stamp//change)*discount
            my_stamp -= (my_stamp//change)*change
        if price >= promotion:
            my_stamp += (total//promotion) * stamp
            total -= (price//promotion) * promotion
        price_result    
        total += price
        price_result += price
    print(price_result)
    print(my_stamp)
main()
