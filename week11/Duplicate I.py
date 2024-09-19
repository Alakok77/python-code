"""mod doc"""
def main():
    """doc"""
    group_a = int(input())
    group_b = int(input())
    a_set = set()
    b_set = set()
    a_var = ""
    b_var = ""
    for i in range(group_a):
        a_var = input()
        a_set.add(a_var)
    for i in range(group_b):
        b_var = input()
        b_set.add(b_var)
    z = sorted(a_set & b_set, reverse=True)
    if len(z):
        for i in z:
            print(i)
    else:
        print("Nope")
main()
