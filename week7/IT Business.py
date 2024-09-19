"""mod doc"""
def main():
    """doc"""
    account = float(input())
    my_money = float(input())
    statement = ""
    error = 0
    while True:
        error = max(0, error)
        if error == 3:
            break
        statement = input()
        if statement == "end":
            break
        if statement[0] == "D" and my_money - float(statement[2:]) >= 0:
            account += float(statement[2:])
            my_money -= float(statement[2:])
            error -= 1
        elif statement[0] == "W" and account - float(statement[2:]) >= 0:
            account -= float(statement[2:])
            my_money += float(statement[2:])
            error -= 1
        else:
            error += 1
            continue
    print(f"{account:.2f}")
    print(f"{my_money:.2f}")
main()
