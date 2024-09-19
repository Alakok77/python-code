"""mod doc"""
def main():
    """doc"""
    weight = float(input())
    divi = int(input())
    weight_safe = float(input())
    shoot = 0
    counting = 0
    while weight >= weight_safe:
        weight /= divi
        shoot += divi**counting
        counting += 1
    print(shoot)
main()
