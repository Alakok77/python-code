"""mod doc"""
def show_output(wet):
    """Show output"""
    if 16 >= wet > 0:
        print(f"Still Wet (Wet Level: {wet:.2f})")
    elif wet <= 0:
        print("Dry")
    else:
        print("Lost")


def condition(i, hour):
    """return minis value"""
    minus = 0
    if i in ("C", "c"):
        if 6 <= hour < 18:
            minus = 0.50
        else:
            minus = 0.25
    elif i in ("N", "n"):
        if 6 <= hour < 18:
            minus = 1.00
        else:
            minus = 0.50
    elif i in ("W", "w"):
        if 6 <= hour < 18:
            minus = 1.50
        else:
            minus = 0.75
    return minus

def main():
    """doc"""
    hour = int(input())
    wheather = input()
    wet = 8
    for i in wheather:
        wet = min(16, wet)
        if wet <= 0:
            break
        if hour > 24:
            hour = 1

        wet -= condition(i, hour)

        if i in ("R", "r"):
            wet += 2.00
        elif i in ("S", "s"):
            wet += 3.00
        elif i in ("H", "h"):
            wet = 77
            break
        hour += 1
    show_output(wet)
main()
