"""mod doc"""
def main():
    """doc"""
    kilo = float(input())
    city = {"InValid":58.855, "Chon Buri":52.900, "Chachoengsao":35.477,
            "Samut Prakarn":5.032, "Bangkok":-1}
    result = ""
    for i, j in city.items():
        if kilo > j:
            result = i
            break
    if kilo < 0:
        result = "InValid"
    print(result)
main()
