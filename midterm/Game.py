"""mod doc"""
def main():
    """doc"""
    a_point = int(input())
    b_point = int(input())
    if a_point%3 == b_point%3:
        print(f"{a_point%3}")
    else:
        print("Error")
main()
