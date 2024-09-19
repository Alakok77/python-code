"""mod doc"""
def main():
    """doc"""
    income = int(input())
    tax = 0
    if 0 < income <= 150000:
        tax = 0
    elif 150000 < income <= 300000:
        tax = (income - 150000) * 0.05
    elif 300000 < income <= 500000:
        tax = 7500 + ((income - 300000) * 0.10)
    elif 500000 < income <= 750000:
        tax = 27500 + ((income - 500000) * 0.15)
    elif 750000 < income <= 1000000:
        tax = 65000 + ((income - 750000) * 0.20)
    elif 1000000 < income <= 2000000:
        tax = 115000 + ((income - 1000000) * 0.25)
    elif 2000000 < income <= 4000000:
        tax = 365000 + ((income - 2000000) * 0.30)
    elif income > 4000000:
        tax = 965000 + ((income - 4000000) * 0.35)
    print(int(tax))
main()
