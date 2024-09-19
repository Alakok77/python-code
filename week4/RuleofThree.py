"""mod doc"""
def main():
    """doc"""
    price_list = []
    weight_list = []
    compare_list = []
    check = []
    count = 0
    piece = int(input())
    for i in range(piece):
        price_list.append(float(input()))
        weight_list.append(float(input()))
        compare_list.append(price_list[i]/weight_list[i])
    result = compare_list.index(min(compare_list))
    for i in range(piece):
        if min(compare_list) == compare_list[i]:
            check.append(price_list[i])
            count += 1
    if count > 1:
        equal = min(check)
        print(f"{equal:.2f} {weight_list[price_list.index(equal)]:.2f}")
    else:
        print(f"{price_list[result]:.2f} {weight_list[result]:.2f}")
main()
