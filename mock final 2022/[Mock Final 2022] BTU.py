"""mod doc"""
def main():
    """doc"""
    room_area = [(100, 151), (151, 251), (251, 301), (301, 351), (351, 401),
                 (401, 451,), (451, 551), (551, 701), (701, 1001), (1001, 1201),
                 (1201, 1401), (1401, 1501), (1501, 2001), (2001, 2501)]
    btu = [5000, 6000, 7000, 8000, 9000, 10000, 12000, 14000,
           18000, 21000, 23000, 24000, 30000, 34000]
    area = int(input())
    height = int(input())
    human = int(input())
    room = input()
    sunshine = input()
    total = 0
    for i, j in enumerate(room_area):
        if j[0] <= area < j[1]:
            total = btu[i] + max(0, height-8)*1000 + max(0, human-2)*600
    if room == "kitchen":
        total += 4000
    if sunshine == "facing the sun":
        total += total * 0.1
    elif sunshine == "shaded":
        total -= total * 0.1
    print(int(total))
main()
