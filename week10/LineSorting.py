"""mod doc"""
def main():
    """doc"""
    time = int(input())
    text = ""
    lst = []
    for _ in range(time):
        text = input()
        lst.append(text)
    lst.sort(key=len)
    for i in lst:
        print(i)
main()
