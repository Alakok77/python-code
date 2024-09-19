"""mod doc"""
def main():
    """doc"""
    num = int(input())
    lenght = num + (num-1)
    show = lenght//2
    for i in range((lenght//2)+1):
        for j in range(i):
            print(f"{j+1:02d}", end = " ")
        for j in range(lenght - (i*2)):
            print(f"{i+1:02d}", end = " ")
        for j in range(i):
            print(f"{i - j:02d}", end = " ")
        print("")
    for i in range(lenght//2):
        counter = i+3
        show_up = (lenght - (i + lenght - (lenght//2))) - 1
        for j in range((lenght//2)-1, i, -1):
            print(f"{(lenght//2) - j:02d}", end = " ")
        for j in range(i + counter):
            print( f"{show:02d}", end = " ")
            counter += 1
        for j in range((lenght//2)-1, i, -1):
            print(f"{show_up:02d}",end = " ")
            show_up -= 1
        show -= 1
        print("")
main()
