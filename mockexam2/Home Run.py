"""mod doc"""
def main():
    """doc"""
    feild = int(input())
    player = float(input())
    distant = 0
    home_run = 0
    for _ in range(feild):
        distant = float(input())
        if player > distant:
            home_run += 1
    print(home_run)
main()
