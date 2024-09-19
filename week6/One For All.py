"""mod doc"""
def main():
    """doc"""
    element = int(input())
    result = ""
    star = "*"
    minus = "-"
    for i in range(1, element + 1):
        name = input()
        if i == element:
            result += f"{name}_{i}"
        elif i % 2:
            result += f"{name}{star * i}"
        else:
            result += f"{name}{minus * i}"
    print(result)
main()
