"""mod doc"""
def main():
    """doc"""
    animal = int(input())
    leg = int(input())
    rabbit = (leg - 2 * animal) / 2
    bird = animal - rabbit
    cond1 = rabbit != int(rabbit) or bird != int(bird)
    cond2 = rabbit < 0 or bird < 0
    if cond1 or cond2:
        print("Impossible")
    else:
        print(f"{int(rabbit)} {int(bird)}")
main()
