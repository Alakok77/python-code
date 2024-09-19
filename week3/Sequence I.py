"""mod doc"""
def main():
    """doc"""
    num = int(input())
    for i in range(num):
        for j in range(num):
            print(j+1+i-i, end = " ")
        print("")
main()
