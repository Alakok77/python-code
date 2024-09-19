"""mod doc"""
def main():
    """doc"""
    top = input()
    middle = input()
    buttom = input()
    finger = int(input())
    space = finger
    all_potato = middle.count(")")
    potato = 0
    for i in middle:
        if not finger:
            break
        if i == ")":
            potato += 1
            all_potato -= 1
        finger -= 1
    print(potato)
    if all_potato > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(top)
    if space >= len(middle):
        print(" "* (len(middle) - 1), "|", sep = "")
    else:
        print(" "*space, middle[space:-1], "|", sep = "")
    print(buttom)
main()
