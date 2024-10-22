"""mod doc"""
def main():
    """doc"""
    lst = []
    total = []
    goal = ""
    first = True
    distant = 0
    error = False
    old = 0
    while True:
        txt = input()
        lst = txt.split(", ")
        total.append(lst[0])
        if lst[0] == "Done" or lst[0] == goal:
            if total.count(goal) <= 0:
                error = True
            elif total.count(goal) > 0 and lst[0] == goal:
                distant += abs(float(lst[1]) - old)
            break
        if not first and old:
            distant += abs(float(lst[1]) - old)
            old = float(lst[1])
        if not first and not old:
            old = float(lst[1])
        if first:
            goal = lst[1]
            first = False
    if error:
        print("Error")
    else:
        print(f"{distant:.2f}")
main()
