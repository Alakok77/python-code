"""mod doc"""
def main():
    """doc"""
    text = input()
    text = text.replace("13", "B")
    text = text.replace("12", "R")
    text = text.replace("1", "I")
    text = text.replace("3", "E")
    text = text.replace("4", "A")
    text = text.replace("5", "S")
    text = text.replace("0", "O")
    for i in text:
        if i in ("26789"):
            text = text.replace(i,"")
    print(text.upper())
main()
