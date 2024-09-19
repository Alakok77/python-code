"""mod doc"""
def main():
    """doc"""
    num = int(input())
    for i in range(num):
        for j in range(i+1):
            print(j+1, end = " ")
        print("")
main()
