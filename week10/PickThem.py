"""doc doc"""
import json
def main():
    """doc"""
    txt = json.loads(input())
    pair = False
    for i in txt:
        if not i%2:
            print(i)
            pair = True
    if not pair:
        print("Nope")
main()
