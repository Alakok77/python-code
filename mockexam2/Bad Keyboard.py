"""mod doc"""
def main():
    """doc"""
    text = input()
    result = ""
    for i in text:
        if i == "o":
            result += "i"
        elif i == "O":
            result += "I"
        elif i == "i":
            result += "o"
        elif i == "I":
            result += "O"
        else:
            result += i
    print(result)
main()
