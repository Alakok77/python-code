"""mod doc"""
def main():
    """doc"""
    result = ""
    num = int(input())
    for i in range(num):
        if num - i > 1:
            result += str(i+1) + "_"
        else:
            result += str(i+1)
    print(result)
main()
