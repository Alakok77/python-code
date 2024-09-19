"""mod doc"""
def main():
    """doc"""
    text = input()
    alpha = {}
    for i in text:
        if not i in alpha and i.isalpha():
            alpha[i] = 1
        elif i.isalpha():
            alpha[i] += 1
    for i in sorted(alpha.keys(), key = lambda x: x.lower() + x if x.isupper() else x):
        print(f"{i} = {alpha[i]}")
main()
