"""mod doc"""
import json
def main():
    """doc"""
    lst_a = list(json.loads(input()))
    lst_b = list(json.loads(input()))
    diff = {}
    for i in lst_a:
        if lst_a.count(i) != lst_b.count(i) and i not in diff:
            diff[i] = abs(lst_a.count(i) - lst_b.count(i))
    for i in lst_b:
        if lst_b.count(i) != lst_a.count(i) and i not in diff:
            diff[i] = abs(lst_a.count(i) - lst_b.count(i))

    if not diff:
        print("ONAJI DAYO!")
    else:
        for i in sorted(diff.keys(), key= str):
            print(f"{i} {diff[i]}")
main()
