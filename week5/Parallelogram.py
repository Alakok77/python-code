"""Parallelogram"""
def main():
    """Parallelogram"""
    text = input()
    for i in range(1,len(text) + 1):
        print(" "*(len(text) - i), end = "")
        print(text[0:i])
    for i in range(1,len(text)):
        print(text[i-len(text):])
main()
