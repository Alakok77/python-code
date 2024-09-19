"""mod doc"""
def main():
    """doc"""
    num = int(input())
    def f_function (num):
        result = 2 * num
        return result
    def g_function(num):
        result = (num/2) + 1
        return result
    total1 = f_function(g_function(num))
    total2 = g_function(f_function(num))
    print(f"{total1:.2f}")
    print(f"{total2:.2f}")
main()
