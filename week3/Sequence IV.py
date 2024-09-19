"""mod doc"""
def main():
    """doc"""
    result = 0
    num = int(input())
    for i in range(num):
        i += 1
        for j in range(num):
            j += 1
            result += 1
            print(result, end = " ")
        print("")
main()
