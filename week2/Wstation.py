"""mod doc"""
def main():
    """doc"""
    average = float(input())
    roller1 = float(input())
    roller2 = float(input())
    roller3 = float(input())
    gain = average/2
    roller4 = (average*4) - (roller1 + roller2 + roller3)
    total_roller = (roller1/1000) + (roller2/1000) + (roller3/1000) + (roller4/1000)
    a = abs(average - roller1) < gain
    b = abs(average - roller2) < gain
    c = abs(average - roller3) < gain
    d = abs(average - roller4) < gain
    if total_roller <= 15:
        if a and b and c and d:
            print(f"Pass {roller4:.2f}")
        else:
            print("Unbalance")
    else:
        print("Overweight")
main()
