"""mod doc"""
def main():
    """doc"""
    time = int(input())
    number = 0
    lst = []
    for _ in range(time):
        number = int(input())
        lst.append(number)
    lst.sort()
    for i in lst:
        print(i)
main()
