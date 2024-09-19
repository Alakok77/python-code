"""mod doc"""
import math
def main():
    """doc"""
    size = int(input())
    align = input()
    text = input()
    left = math.ceil((size - len(text))/2)
    right = math.floor((size - len(text))/2)
    size = size - len(text)
    if align == "left":
        print(text, " "*size, sep = "")
    elif align == "right":
        print(" "*size, text, sep = "")
    else:
        print(" "*left, text, " "*right, sep = "")
main()
