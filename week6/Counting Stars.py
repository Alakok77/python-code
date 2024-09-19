"""mod doc"""
def main():
    """doc"""
    star = input()
    check = ""
    constellation = 0
    comet = 0
    shooting_star = 0
    for i in star:
        if i.isspace():
            check = ""
        else:
            check += i
            if check in ("*~", "~*"):
                comet += 1
            elif check == "*/":
                shooting_star += 1
            elif check == "**":
                constellation += 1
        if len(check) == 2:
            check = ""
    all_star = comet + constellation + shooting_star
    if all_star > 0:
        print(f"constellation: {constellation}")
        print(f"comet: {comet}")
        print(f"shooting star: {shooting_star}")
    else:
        print("Tonight is a quiet night.")
main()
