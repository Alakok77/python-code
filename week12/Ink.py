"""mod doc"""
import math as m
def main():
    """doc"""
    info = list(map(int, input().split()))
    area, people = info[0], info[1]
    point, time, radius = "", 0, 0
    for _ in range(people):
        point = list(map(int, input().split()))
        radius = (m.sqrt(int(point[0])**2 + int(point[1])**2))
        time = (3.1416 * (radius**2))/area
        print(m.ceil(time))
main()
