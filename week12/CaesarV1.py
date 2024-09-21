"""mod doc"""
def main():
    """doc"""
    direct = int(input())
    txt = input()
    alpha_a = "abcdefghijklmnopqrstuvwxyz"
    alpha_b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_txt = ""
    point = 0
    for i in txt:
        if not i.isalpha():
            new_txt += i
            continue
        if i.islower():
            point = (alpha_a.index(i) + direct) % len(alpha_a)
            new_txt += alpha_a[point]
        else:
            point = (alpha_b.index(i) + direct) % len(alpha_b)
            new_txt += alpha_b[point]
    print(new_txt)
main()
