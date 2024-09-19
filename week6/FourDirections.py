"""mod doc"""
def top(i, j):
    """Show on top of this direction"""
    if i == "U":
        print(" " * (2-j), "*" * (2*(j+1) -1)," " * (2-j), sep = "", end = " ")
    elif i == "D":
        print("  *  ", end = " ")
    elif i == "L":
        print(" " * (2 - j), "*"," " * (j + 2), sep = "", end = " ")
    else:
        print(" " * (j + 2), "*"," " * (2 - j), sep = "", end = " ")


def buttom(i, j):
    """Show on top of this direction"""
    if i == "U":
        print("  *  ", end = " ")
    elif i == "D":
        print(" " * (j - 2), "*" * (2 * (5 - j) - 1)," " * (j - 2), sep = "", end = " ")
    elif i == "L":
        print(" " * (j - 2), "*", " " * (6 - j), sep = "", end = " ")
    else:
        print(" " * (6 - j), "*"," " * (j - 2), sep = "", end = " ")


def main():
    """doc"""
    direct = input()
    for j in range(5):
        for i in direct:
            if j < 2:
                top(i, j)
            elif j == 2:
                if i in ("U", "D"):
                    print("* * *", end = " ")
                else:
                    print("*****", end = " ")
            else:
                buttom(i, j)
        print("")
main()
