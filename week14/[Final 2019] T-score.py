"""mod doc"""
def main():
    """doc"""
    student = int(input())
    most = int(input())
    most = most + 2
    point_lst = []
    for _ in range(student):
        point_lst.append(int(input()))
    average = sum(point_lst) / student
    sd_ = 0
    for i in point_lst:
        sd_ += (i - average)**2
    sd_ = (sd_ / (student - 1))**0.5
    z_score = []
    for i in point_lst:
        z_score.append((i - average) / sd_)
    for i in z_score:
        print(f"{50 + (10 * i):.2f}")
main()
