"""mod doc"""
def main():
    """doc"""
    txt = input()
    digit = 0
    two = ["ten", "eleven", "twelve"]
    if "thousand" in txt:
        digit = 4
    elif "hundred" in txt:
        digit = 3
    elif "ty" in txt or "teen" in txt or txt in two:
        digit = 2
    else:
        digit = 1
    print(digit)
main()
