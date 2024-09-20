"""mod doc"""
def main():
    """doc"""
    most = int(input())
    station = int(input())
    wait = []
    buses = []
    info = []
    complete = 0
    for _ in range(station):
        wait = input().split()
        info.append(wait)
    info.sort(key= lambda x: int(x[0]))
    for human in info:
        while buses.count(human[0]) > 0:
            buses.remove(human[0])
            complete += 1
        for i in human[1:]:
            if int(i) > int(human[0]) and len(buses) < most:
                buses.append(i)
            if len(buses) == most:
                break
    print(complete)
main()
