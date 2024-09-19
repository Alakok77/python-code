"""mod doc"""
def main():
    """doc"""
    result = 10
    number = 1
    while int(number):
        number = str(input())
        result = number
        while len(str(result)) != 1:
            result = 0
            for i in str(number):
                result += int(i)
            number = result
        if int(result):
            print(result)
main()
