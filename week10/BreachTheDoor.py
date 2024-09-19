"""mod doc"""
def main():
    """doc"""
    text = input()
    buffer = ""
    result = ""
    for i in text:
        if i.isalpha() or i.isspace():
            buffer += i
    buffer = buffer.split()
    for i in buffer:
        if len(i) > 6:
            result += f"{i} "
    print(result.strip())
main()
