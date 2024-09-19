"""Quadrant"""
def main():
    """Quadrant"""
    x = int(input())
    y = int(input())
    if x>0 :
        if y>0:
            print("Q1")
        elif not y:
            print("X")
        else:
            print("Q4")
    elif x<0:
        if y>0:
            print("Q2")
        elif not y:
            print("X")
        else:
            print("Q3")
    elif not x:
        if y>0:
            print("Y")
        elif y<0:
            print("Y")
        else:
            print("O")
main()
