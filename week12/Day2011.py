"""mod doc"""
def main():
    """doc"""
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = int(input())
    month = int(input())
    check = (sum(days[:month-1]) + day)%7
    dct = {0:"Friday", 1:"Saturday", 2:"Sunday",3:"Monday",
           4:"Tuesday", 5:"Wednesday", 6:"Thursday"}
    print(dct[check])
main()
