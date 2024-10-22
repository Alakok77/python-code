"""mod doc"""
def main():
    """doc"""
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0]
    day1 = int(input())
    month1 = int(input())
    day2 = int(input())
    month2 = int(input())
    if day1 > days[month1-1] or day2 > days[month2-1]:
        print("Impossible")
    else:
        gap = abs((sum(days[:month1-1]) + day1) - (sum(days[:month2-1]) + day2))
        print(gap)
main()
