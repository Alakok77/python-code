"""mod doc"""
def main():
    """doc"""
    gen = input()
    wpm = int(input())
    if gen == "Kids" and wpm < 11:
        print("Very Slow")
    elif gen == "Kids" and 11 <= wpm <= 20:
        print("Slow")
    elif gen == "Kids" and 21 <= wpm <= 30:
        print("Average")
    elif gen == "Kids" and 31 <= wpm <= 40:
        print("Fast")
    elif gen == "Kids" and wpm > 40:
        print("Very Fast")
    elif wpm < 26:
        print("Very Slow")
    elif 26 <= wpm <= 35:
        print("Slow/Beginner")
    elif 36 <= wpm <= 45:
        print("Intermediate/Average")
    elif 46 <= wpm <= 65:
        print("Fast/Advanced")
    elif 66 <= wpm <= 80:
        print("Very Fast")
    else:
        print("Insane")
main()
