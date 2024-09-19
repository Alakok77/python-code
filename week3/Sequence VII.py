"""mod doc"""
def main():
    """doc"""
    num = int(input())
    for i in range(num):
        for j in range(i+1):
            print(j+1, end = " ")
        print("")
    for i in range(num-1):
        for j in range(num-1, i, -1):
            print(num - j, end = " ")
        print("")
main()
