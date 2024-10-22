"""mod doc"""
def main():
    """doc"""
    m_var = int(input())
    n_var = int(input())
    num =[float(input()) for _ in range(m_var*n_var)]
    gap = max(num) - min(num)
    num = [(abs(min(num)) + i)/gap for i in num]
    cnt = 0
    for _ in range(m_var):
        for _ in range(n_var):
            print(f"{num[cnt]:.2f}", end = " ")
            cnt += 1
        print("")
main()
