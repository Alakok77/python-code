"""ChristmasTree"""
def main():
    """Main Function"""
    n = int(input())
    k = int(input())
    count = n - 1
    star = 1
    for i in range(n):
        i += 0
        print(" " * count, "*" * star, sep="")
        star += 2
        count -= 1
    for i in range(k):
        print(" " * (n-2), "---", sep ="")
main()
