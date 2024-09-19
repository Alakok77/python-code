"""mod doc """
def main():
    """doc"""
    text =input()
    total = 0
    for i in text:
        total += int(i)
    last = int(text[-3:]) * 10
    result = total + last
    if len(str(result)) > 4:
        print(str(result)[-4:])
    elif len(str(result)) < 4:
        print(result+1000)
    else:
        print(result)
main()
