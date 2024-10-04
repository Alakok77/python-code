"""mod doc"""
def main():
    """doc"""
    time, before, cnt = 0, 0, 0
    state, cool, first = False, False, True
    while True:
        time = input()
        if time == "End":
            break
        state = not state
        if state and first:
            cool, first = True, False
        elif state and float(time) - before <= 6 and cool:
            cnt += 1
            cool = not cool
        elif state and float(time) - before <= 6:
            cool = not cool
        elif state and float(time) - before > 6:
            cool = True
        before = float(time)
    print(cnt)
main()
