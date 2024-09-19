"""mod doc"""
import math
def main():
    """doc"""
    money = float(input())
    year = int(input())
    if not year:
        last = money
    else:
        result = money + money*0.0381
        for _ in range(year-1):
            result += (int((result*0.0381)*100))/100
        last = (math.floor(result*100))/100
    print(last)
main()
