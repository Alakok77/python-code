"""mod doc"""
def main():
    """doc"""
    most = int(input())
    station = int(input())
    wait = []
    buses = []
    complete = 0
    for _ in range(station):
        wait = input().split()
        while buses.count(wait[0]) > 0:
            buses.remove(wait[0])
            complete += 1
        for i in wait[1:]:
            if int(i) > int(wait[0]) and len(buses) < most:
                buses.append(i)
            if len(buses) == most:
                break
    print(complete)
main()
