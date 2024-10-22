"""mod doc"""
def main():
    """doc"""
    txt = input()
    total = 0
    numbers = {"one":1, "two":2, "three":3, "four":4, "five":5,
               "six":6, "seven":7, "eight":8, "nine":9, "ten":10,
               "eleven":11, "twelve":12, "thirteen":13, "fourteen":14,
               "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18,
               "nineteen":19, "twenty":20, "thirty":30, "forty":40, "fifty":50,
               "sixty":60, "seventy":70, "eighty":80, "ninety":90,
               }
    more = {"hundred":100, "thousand":1000}
    for i in txt.split():
        if i in more:
            total *= more[i]
        else:
            total += numbers[i]
    print(total)
main()
