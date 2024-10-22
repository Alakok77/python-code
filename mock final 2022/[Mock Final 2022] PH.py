"""mod doc"""
def main():
    """doc"""
    value = float(input())
    if 0 <= value < 7:
        print("acidic")
    elif value == 7:
        print("neutral")
    elif 7 < value <= 14:
        print("akaline")
    else:
        print("error")
main()
