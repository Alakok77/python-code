"""mod doc"""
def main():
    """doc"""
    age = int(input())
    weight = int(input())
    time = int(input())
    book = ""
    cond1 = age < 17 or 70 < age
    cond2 = False
    if not time:
        cond1 = age < 17 or age > 55
    if age in (17,60,61,62,63,64,65,66,67,68,69,70):
        book = input()
        cond2 = book == "False"
    cond3 = weight < 45
    if cond1 or cond2 or cond3:
        print("No")
    else:
        print("Yes")
main()
