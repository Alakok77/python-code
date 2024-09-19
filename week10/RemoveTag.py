"""mod doc"""
def main():
    """doc"""
    tag = input()
    text = ""
    start =  False
    if not ">" in tag and not "<" in tag:
        print(tag.split())
    else:
        for i in tag:
            if i == ">":
                start = True
                continue
            if i == "<":
                start = False
                text += " "
            if start:
                text += i
        print(text.split())
main()
