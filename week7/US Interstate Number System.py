"""mod doc"""
def main():
    """doc"""
    road = int(input())
    if not road % 5 and road:
        if len(str(road)) < 3:
            if not int(str(road)[-1]):
                print("Horizontal Major Interstate")
                print(f"I-{road}")
            elif str(road)[-1] == "5":
                print("Vertical Major Interstate")
                print(f"I-{road}")
            else:
                print("Others")
        elif int(str(road)[1:]) >= 10:
            if int(str(road)[0]) % 2:
                print("Odd Minor Interstate")
                print(f"I-{int(str(road)[1:])}")
            elif not int(str(road)[0]) % 2:
                print("Even Minor Interstate")
                print(f"I-{int(str(road)[1:])}")
        else:
            print("Others")
    else:
        print("Others")
main()
