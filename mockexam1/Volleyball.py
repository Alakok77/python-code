"""mod doc"""
def main():
    """doc"""
    point = input()
    a_point = 0
    b_point = 0
    a_set = 0
    b_set = 0
    seter = ""
    counting = 1
    for i, j in enumerate(point):
        if j == "A":
            a_point += 1
        elif j == "B":
            b_point += 1
        if ((a_point >= 25 or b_point >= 25) and (abs(a_point-b_point) >= 2)) or i == len(point)-1:
            seter += f"Set {counting}: A ({str(a_point)}) | B ({str(b_point)})\n"
            counting += 1
            if a_point > b_point:
                a_set += 1
            elif b_point > a_point:
                b_set += 1
            a_point = 0
            b_point = 0
    if a_set == 3 or b_set == 3:
        print(seter[0:-1])
        if a_set > b_set:
            print(f"A won {a_set}:{b_set} set")
        elif b_set > a_set:
            print(f"B won {b_set}:{a_set} set")
    else:
        print(seter[0:-1])
        print("The game has not finished yet.")
main()
