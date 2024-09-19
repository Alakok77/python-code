"""mod doc"""
def main():
    """doc"""
    address = input().upper()
    sign = ""
    hex_count = 0
    stand = 0
    error = False
    first = True
    stand = 4
    if address.find("-") != -1 or address.find(":") != -1:
        stand = 2
    for i in address:
        if i.isnumeric() or i in ("ABCDEF"):
            hex_count += 1
        else:
            if i in ("-", ":", ".") and hex_count == stand:
                hex_count = 0
                if first:
                    sign += i
                    first = False
                elif sign != i:
                    error = True
            else:
                error = True
    if address.count("-") != 5 and address.count(":") != 5 and address.count(".") !=  2:
        error = True
    if error:
        print("ERROR")
    elif sign.find("-") != -1:
        print("VALID 1")
    elif sign.find(":") != -1:
        print("VALID 2")
    elif sign.find(".") != -1:
        print("VALID 3")
main()
