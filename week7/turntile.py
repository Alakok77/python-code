"""mod doc"""
def main():
    """doc"""
    state = ""
    locked = True
    unlocked = False
    human = 0
    while state != "END":
        state = input()
        if locked and state == "C":
            locked = False
            unlocked = True
        elif unlocked and state == "P":
            locked = True
            unlocked = False
            human += 1
    print(human)
main()
