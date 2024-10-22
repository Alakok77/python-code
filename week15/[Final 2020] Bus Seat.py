"""mod doc"""
def main():
    """doc"""
    column = int(input())
    row = int(input())
    seat = int(input())
    gap = int(column/2) - 1
    step = column
    for i in range(1, column + gap + 1):
        if not i%3:
            print("")
            continue
        for j in range(row):
            if step+(column*j) == seat:
                print("XX", end = " ")
            else:
                print(f"{step+(column*j):02d}", end = " ")
        step -= 1
        print("")
main()
