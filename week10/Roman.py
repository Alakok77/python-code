"""mod doc"""
def main():
    """doc"""
    roman = input()
    arabic = 0
    first = True
    roman_dict = {"I":1, "V":5, "X":10, "L":50,
                  "C":100, "D":500, "M":1000}
    for i,j in enumerate(roman):
        if first:
            arabic += roman_dict[j]
            first = False
        elif roman_dict[j] > roman_dict[roman[i-1]] and not first:
            arabic += roman_dict[j] - roman_dict[roman[i-1]] - roman_dict[roman[i-1]]
        else:
            arabic += roman_dict[j]
    print(arabic)
main()
