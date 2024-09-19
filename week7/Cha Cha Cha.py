"""mod doc"""
import math
def main():
    """doc"""
    day = int(input())
    hour = 0
    total = 0
    for _ in range(day):
        hour = math.ceil(float(input()))
        total += hour*8720
    print(total)
main()
