"""mod doc"""
def main():
    """doc"""
    num = int(input())
    second = num%60
    minute = (num//60)%60
    hours = (num//3600)%24
    day = (num//3600)//24
    count = len(str(day))
    if count < 5:
        print(f"{day:04}:{hours:02}:{minute:02}:{second:02}")
    else:
        print("ERR_:__:__:__")
main()
