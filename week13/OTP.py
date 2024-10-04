""""mod doc"""
def main():
    """doc"""
    number = ""
    cnt = {}
    while True:
        number = input()
        if number == "0":
            break
        for i in number:
            if i not in cnt:
                cnt[i] = 1
            else:
                cnt[i] += 1
        if max(cnt, key= cnt.values()) > 
main()
