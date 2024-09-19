"""mod doc"""
def main():
    """doc"""
    text = input()
    deter = ""
    for i in text:
        if i.isalpha() or i.isspace():
            deter += i
    deter = deter.split()
    result = []
    vowel = 0
    for i in deter:
        vowel += i.count("a")
        vowel += i.count("e")
        vowel += i.count("i")
        vowel += i.count("o")
        vowel += i.count("u")
        if vowel >= 2:
            result.append(i)
        vowel = 0
    result.sort(key= str.lower)
    if len(result) > 0:
        for i in result:
            print(i)
    else:
        print("Nope")
main()
