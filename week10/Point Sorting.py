"""mod doc"""
def main():
    """doc"""
    t_var = int(input())
    n_var = 0
    point = ""
    lst = []
    for _ in range(t_var):
        n_var  = int(input())
        for _ in range(n_var):
            point = input().split()
            lst.append(point)
        lst.sort(key= lambda x: (int(x[0])+int(x[1]), int(x[1])))
        for i in lst:
            print(f"{i[0]} {i[1]}")
        lst.clear()
main()
