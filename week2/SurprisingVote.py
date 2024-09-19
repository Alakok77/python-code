"""mod doc"""
def main():
    """doc"""
    total = float(input())
    most = float(input())
    remain = total - most
    if most - (remain//2) >= 2:
        point = (most, total%most, (remain - (total%most)))
        if max(point) -  min(point) > 2:
            print("Surprising")
        else:
            print("Not surprising")
    else:
        print("Not surprising")
main()
