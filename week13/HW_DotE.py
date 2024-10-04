"""mod doc"""
import math
def main():
    """doc"""
    number = int(input())
    first = number//2
    second = number//2 + 1
    result = math.factorial(number) / (math.factorial(first) * math.factorial(number - first))
    if number%2:
        cal1 = math.factorial(number) / (math.factorial(first) * math.factorial(number - first))
        cal2 = math.factorial(number) / (math.factorial(second) * math.factorial(number - second))
        result  = cal1 + cal2
    print(int(result))
main()
