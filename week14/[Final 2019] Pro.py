"""mod doc"""
def main():
    """doc"""
    pro = int(input())
    cnt = int(input())
    price = int(input())
    human = int(input())
    total = ((human % pro) * price) + (human // pro) * (price * cnt)
    print(total)
main()
