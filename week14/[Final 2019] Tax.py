"""mod doc"""
def main():
    """doc"""
    age = int(input())
    motor = int(input())
    price = 0
    if motor <= 600:
        price += motor * 0.5
    elif 600 < motor <= 1800:
        price += 300 + min(motor - 600, 1200) * 1.50
    else:
        price += 2100 + (motor - 1800) * 4.00
    if age >= 6:
        price *= 1 - min(50, (age - 5) * 10)/100
    print(f"{price:.2f}")
main()
