"""mod doc"""
import math
def main():
    """doc"""
    amount = int(input())
    each_grade = 0.00
    for i in range(amount):
        i += 0
        point = float(input())
        if point >= 95:
            each_grade += 4.00
        elif point >= 90:
            each_grade += 3.50
        elif point >= 85:
            each_grade += 3.00
        elif point >= 80:
            each_grade += 2.50
        elif point >= 75:
            each_grade += 2.00
        elif point >= 70:
            each_grade += 1.50
        elif point >= 65:
            each_grade += 1.00
        elif point >= 60:
            each_grade += 0.50
        else:
            each_grade += 0.00
    gpax = math.floor((each_grade/amount) * 100)
    print(f"{gpax/100:.2f}")
main()
