"""mod doc"""
def main():
    """doc"""   
    a = int(input())
    b = int(input())
    goal = int(input())
    big = goal//5
    small = goal%5
    if big <= b and a + (big*5) >= goal:
        print(small)
    elif b <= big and a + (b*5) >= goal :
        print(goal - (b*5))
    elif b <= big and a + (b*5) <= goal:
        print(-1)
    elif big <= b and a + (big*5) <= goal:
        print(-1)
    else:
        print(-1)
main()
