"""mod doc"""
def main():
    """doc"""
    x = int(input())
    y = int(input())
    result = "pass :"
    total = 0
    if x <= y:
        for i in range(x, y+1):
            if not i % 2 :
                total += i
                result += " " + str(i)
            elif x == y:
                result = y
                total += y
    else:
        for i in range(x, y-1 ,-1):
            if not i % 2 :
                total += i
                result += " " + str(i)
    print(result)
    print(f"Sum : {total}")
main()
