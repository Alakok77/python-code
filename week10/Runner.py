"""mod doc"""
def main():
    """doc"""
    finish = int(input())
    people = int(input())
    info = []
    total = []
    lst = []
    equal = ""
    indexer = ""
    for _ in range(people):
        info = input().split()
        total.append(info[0])
        cal = (finish - int(info[1]))/int(info[0])
        lst.append(cal)
    if lst.count(min(lst)) > 1:
        equal = min(lst)
        for _ in range(lst.count(min(lst))):
            indexer += str(lst.index(equal))
            lst.remove(equal)
        result = max(total[int(indexer[0])], total[int(indexer[1]) + 1])
        print(total.index(result) + 1)
    else:
        print(lst.index(min(lst)) + 1)
main()
