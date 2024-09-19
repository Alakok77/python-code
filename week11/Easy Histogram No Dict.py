"""mod doc"""
def main():
    """doc"""
    text = input()
    alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    for i in alpha:
        if i in text:
            print(f"{i} = {text.count(i)}")
main()
