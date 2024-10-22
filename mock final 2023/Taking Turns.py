"""mod doc"""
import json
def main():
    """doc"""
    txt = json.loads(input())
    txt.insert(0, txt[-1])
    txt.pop()
    txt.insert(3, txt[-1])
    txt.pop()
    txt.insert(4, txt[-1])
    txt.pop()
    txt.insert(-2, txt[-1])
    txt.pop()
    print(txt)
main()
