"""mod doc"""
def main():
    """doc"""
    price = int(input())
    twenfive = price//25
    ten_bath = (price%25)//10
    five_bath = (price%25%10) // 5
    one_bath = price%25%10%5
    coint = twenfive + ten_bath + five_bath + one_bath
    print(coint)
main()
