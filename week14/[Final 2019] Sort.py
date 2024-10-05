"""mod doc"""
def main():
    """doc"""
    numbers = []
    while True:
        number = input()
        if number == "END":
            break
        numbers.append(int(number))
    swap = True
    cnt = 0
    while swap:
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                cnt += 1
        if not cnt:
            swap = False
        cnt = 0
    for i in numbers:
        print(i)
main()
