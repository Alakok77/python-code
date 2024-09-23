"""mod doc"""
def main():
    """doc"""
    info = []
    student = ""
    while True:
        student = input()
        if student == "END":
            break
        info.append(student)
    info.sort()
    cnt_dict = {}
    for i in info:
        if i[0:4] in cnt_dict:
            cnt_dict[i[0:4]] += 1
        else:
            cnt_dict[i[0:4]] = 1
    cnt = list(cnt_dict.items())
    for i, j in enumerate(cnt):
        if str(j[0])[0:2] == ((cnt[i - 1])[0])[0:2]:
            print(f"-- {int(str(j[0])[2:4])} {str(j[1])}")
        else:
            print(f"{str(j[0])[0:2]} {int(str(j[0])[2:4])} {str(j[1])}")
main()
