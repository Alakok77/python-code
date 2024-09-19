counter = 1
num = int(input())
while counter <= num:
    if counter%15:
        print("FizzBuzz")
    elif counter%5:
        print("Buzz")
    elif counter%3:
        print("Fizz")
    else:
        print(counter)
    counter += 1