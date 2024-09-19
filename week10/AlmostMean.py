"""mdd doc"""
def main():
    """doc"""
    time = int(input())
    info = ""
    score = []
    number = []
    gap = 0
    gapper = []
    total = 0
    for _ in range(time):
        info = input()
        score.append(info[9:])
        number.append(info)
        total += float(info[9:])
    average = total/time
    for i in score:
        gap = average - float(i)
        if gap >= 0:
            gapper.append(gap)
        else:
            gapper.append(average + 1)
    print(number[gapper.index(min(gapper))])
main()
