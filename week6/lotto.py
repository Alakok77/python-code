"""mod doc"""
def main():
    """doc"""
    first_prize = input()
    last_two_digits = input()
    first_three_digits1 = input()
    first_three_digits2 = input()
    last_three_digits1 = input()
    last_three_digits2 = input()
    my_lotto = input()
    reward = 0
    if my_lotto == first_prize:
        reward += 6000000
    else:
        if int(my_lotto) in (int(first_prize) + 1, int(first_prize) - 1):
            reward += 100000
        else:
            if first_prize == "000000":
                if my_lotto in ("000001","999999"):
                    reward += 100000
            if first_prize == "999999":
                if my_lotto in ("000000","999998"):
                    reward += 100000
    if my_lotto[-2:] == last_two_digits:
        reward += 2000
    if my_lotto[0:3] == first_three_digits1:
        reward += 4000
    if my_lotto[0:3] == first_three_digits2:
        reward += 4000
    if my_lotto[-3:] == last_three_digits1:
        reward += 4000
    if my_lotto[-3:] == last_three_digits2:
        reward += 4000
    print(reward)
main()
