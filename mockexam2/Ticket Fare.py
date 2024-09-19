"""mod doc"""
def main():
    """doc"""
    last_station = int(input())
    first_station = int(input())
    price_first = int(input())
    second_station = int(input())
    second_price = int(input())
    last_price = int(input())
    start = int(input())
    goal = int(input())
    distant =  abs(goal - start)
    total = price_first
    if 0 < start <= last_station and 0 < goal <= last_station:
        if not distant:
            print(price_first)
        elif distant > last_station:
            print("Error")
        else:
            if distant - first_station <= second_station:
                total += (distant - first_station) * second_price
            else:
                total += second_price * second_station
                total += (distant - (first_station + second_station)) * last_price
            print(total)
    else:
        print("Error")
main()
