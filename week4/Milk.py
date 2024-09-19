"""mod doc"""
def main():
    """mod"""
    price = float(input())
    promotion = int(input())
    free = int(input())
    money = float(input())
    milk_recieve = money//price
    total = 0
    if not promotion:
        print(int(milk_recieve))
    else:
        remain = milk_recieve % promotion
        extra_box = (milk_recieve//promotion)*free
        check = extra_box + remain
        if check >= promotion:
            while check >= promotion:
                check -= promotion
                check += free
                total += 1
            milk_all = milk_recieve + extra_box + total*free
            print(int(milk_all))
        else:
            milk_all = milk_recieve + extra_box
            print(int(milk_all))
main()
