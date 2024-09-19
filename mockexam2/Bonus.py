"""mod doc"""
def main():
    """doc"""
    income = int(input())
    year = int(input())
    month = int(input())
    multi = year + (month//10)
    bonus = income * min(multi, 20)
    last = max(5000, bonus)
    print(min(last, 1000000))
main()
