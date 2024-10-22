"""mod doc"""
def main():
    """doc"""
    park = " ".join(input()).split()
    cnt = 0
    for i, j in enumerate(park):
        if len(park) == 1:
            if j == "0":
                cnt += 1
        elif not i and len(park):
            if j == "0" and park[i+1] == "0":
                cnt += 1
                park.insert(i, "1")
                park.pop(i+1)
        elif i == len(park) - 1:
            if j == "0" and park[i-1] == "0":
                cnt += 1
                park.insert(i, "1")
                park.pop(i+1)
        else:
            if j == "0" and park[i-1] == "0" and park[i+1] == "0":
                cnt += 1
                park.insert(i, "1")
                park.pop(i+1)
    print(cnt)
main()
