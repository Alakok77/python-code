"""mod doc"""
import json
def main():
    """doc"""
    text = json.loads(input())
    for i in text:
        print(str(i)[-1])
main()
