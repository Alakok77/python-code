"""mod doc"""
import math
def main():
    """doc"""
    times = int(input())
    year = ""
    century = 0
    for _ in range(times):
        year =input()
        if year[0:4] == "B.E.":
            century = math.ceil((int(year[5:]) - 543)/100)
            print(century)
        elif year[0:4] == "A.D.":
            century = math.ceil(int(year[5:])/100)
            print(century)
        else:
            print("ERROR")
main()
