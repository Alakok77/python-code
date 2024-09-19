"""Second converter"""
def main():
    """Main Function"""
    k = int(input())
    s = int(input())
    m = int(input())
    h = int(input())
    second = k % s
    minutes = (k//s)%m
    hour = ((k//s)//m)%h
    print(f"{hour}:{minutes}:{second}")
main()
