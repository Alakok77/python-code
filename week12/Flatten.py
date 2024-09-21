"""mod doc"""
import json
def flatter():
    """return new list"""
    txt = json.loads(input())
    result = []
    for i in txt:
        if isinstance(i, int):
            result.append(i)
        elif isinstance(i, list):
            txt.extend(i)
    print(sorted(result, reverse= True))
flatter()
