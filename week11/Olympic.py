"""mod doc"""
def main():
    """doc"""
    athletes = int(input())
    info = []
    for _ in range(athletes):
        info.append(input().split())
    info.sort(key= lambda x: (x[1], x[2], x[3]), reverse= True)
    print(info)
main()
