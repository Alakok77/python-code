"""mod doc"""
import json
def main():
    """doc"""
    info = json.loads(input())
    stand = float(input())
    id_lst = []
    for i in info.items():
        if int(i[1]) >= stand:
            id_lst.append(i[0])
    id_lst.sort()
    if len(id_lst) > 0:
        for i in id_lst:
            print(f"{i}\t{info[i]:.2f}")
    else:
        print("Nope")
main()
