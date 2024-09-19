"""mod doc"""
def main ():
    """doc"""
    num = int(input())
    for i in range(num):
        counter = 1
        for j in range(num-i-1):
            j += 0
            print(" ", end = "  ")
        for j in range(i + 1):
            print(f"{counter:02d}", end = " ")
            counter += 1
        print("")
main()
