"""mod doc"""
def main():
    """doc"""
    a = int(input())
    b = int(input())
    wanted = input()
    ea = 1 / (1 + 10 **((b - a)/400))
    eb = 1 / (1 + 10 **((a - b)/400))
    if wanted == "A":
        print(f"{ea:.2f}")
    else:
        print(f"{eb:.2f}")
main()
