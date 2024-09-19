"""mod doc"""
def main():
    """doc"""
    diamond = int(input())
    counter = 1
    for i in range(diamond):
        if i == diamond//2:
            print("*" * diamond)
        else:
            if not i or i == diamond - 1:
                print(" " * abs((diamond//2 + 1) - i - 1), "*", sep = "")
            else:
                print(" " * abs((diamond//2 + 1) - i - 1), end ="")
                print("*", end = "")
                print(" " * counter, end = "")
                print("*")
                if i < diamond//2 - 1:
                    counter += 2
                elif i > diamond//2 - 1:
                    counter -= 2
main()
