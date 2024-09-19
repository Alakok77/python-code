"""mod doc"""
def main():
    """doc"""
    book = int(input())
    page = int(input())
    read = page
    x = int(input())
    y = int(input())
    days = 0
    for _ in range(book):
        page = read
        while page > 1:
            page -= (read * x) // y
            x += 1
            y += 1
            days += 1
    print(days)
main()
