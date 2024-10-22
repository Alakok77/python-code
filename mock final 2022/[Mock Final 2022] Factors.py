"""mod doc"""
def main():
    """doc"""
    time = int(input())
    num = 0
    result = []
    pull = []
    for _ in range(time):
        num = int(input())
        for i in (2,3,5,7,11,13):
            while not num%i:
                pull.append(i)
                num /= i
        result.append(pull)
        pull = []
    stand = 0
    for lst in result:
        for i, j in enumerate(lst):
            if stand != j:
                if lst.count(j) == 1:
                    print(j, end = " ")
                else:
                    print(f"{j}**{lst.count(j)}", end = " ")
                if j != lst[-1]:
                    print("x", end = " ")
            stand = j
        print("")
main()
