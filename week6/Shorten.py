"""doc"""
def main() :
    """func"""
    number = int(input())
    result = ""
    gap = 1
    first = True
    next_up = False
    one = number
    if number != -1:
        while number != -1:
            if number - one != gap and not first:
                if next_up:
                    result += f"{one}-{one + gap - 1}, "
                    next_up = False
                else:
                    result += f"{one}, "
                gap = 1
                one = number
                number = int(input())
            if number - one == gap and not first:
                next_up = True
                gap += 1
                number = int(input())
            if first:
                number = int(input())
                first = False
        if next_up:
            result += f"{one}-{one + gap - 1}"
        else:
            result += f"{one}"
    print(result)
main()
