"""mod doc"""
def main():
    """doc"""
    num = int(input())
    lenght = num + (num - 1)
    for i in range(lenght//2 + 1):
        one = lenght//2 - i + 1
        two = lenght//2
        for j in range(i):
            print(f"{one:02d}", end = " ")
            one += 1
        for j in range(lenght//2 + 1, i, -1):
            print(f"{j:02d}", end = " ")
        for j in range(lenght//2, i, -1):
            print(f"{ lenght//2 + i - j + 2:02d}", end = " ")
        for j in range(i):
            print(f"{two:02d}", end = " ")
            two -= 1
        print("")
    for i in range(lenght//2):
        one = i
        two = lenght//2 + 1
        tree = lenght//2 + 1
        forth = lenght//2
        for j in range(lenght//2 - i - 1):
            print(f"{one+2:02d}", end = " ")
            one += 1
        for j in range(i+2):
            print(f"{two:02d}", end = " ")
            two -= 1
        for j in range(i+1):
            print(f"{tree - i:02d}", end = " ")
            tree += 1
        for j in range(lenght//2 - 1, i, -1):
            print(f"{forth:02d}", end = " ")
            forth -= 1
        print("")
main()
