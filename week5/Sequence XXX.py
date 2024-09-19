"""mod doc"""
def main():
    """doc"""
    size = int(input())
    number = int(input())
    for i in range(size):
        for _ in range(number):
            for j in range(size):
                if i == j or i + j == size - 1:
                    print("*", end = "")
                elif i in (0, size - 1) or j in (0, size - 1):
                    print("*", end = "")
                else:
                    print(" ", end = "")
            print(" ", end ="")
        print(" ")
main()
