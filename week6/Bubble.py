"""mod doc"""
def main():
    """doc"""
    route = input()
    jump = 0
    i = 0
    result = 0
    while i < len(route) - 1:
        point = route[i]
        if point in  ("o", "^"):
            jump += 1
            i += 1
        elif point == "O":
            if route[i + 1] == "|":
                jump += 1
                i += 1
            else:
                if len(route) - i - 1 >= 3:
                    jump += 1
                    i += 3
                else:
                    jump += 1
                    i += len(route) - i - 1
            if route[i] == " ":
                i -= 1
                if route[i] == " ":
                    i -= 1
                    if route[i] == " ":
                        result = len(route) - i 
                        break
        elif point == " ":
            result = len(route) - i
            break
    if not result:
        print("POSSIBLE")
        print(jump)
    else:
        print("IMPOSSIBLE")
        print(result)
main()
