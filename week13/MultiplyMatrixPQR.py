"""mod doc"""
import numpy
def main():
    """doc"""
    a_lst = []
    b_lst = []
    p = int(input())
    q = int(input())
    r = int(input())
    pull = []
    for _ in range(p):
        for _ in range(q):
            num = int(input())
            pull.append(num)
        a_lst.append(pull)
        pull = []
    for _ in range(q):
        for _ in range(r):
            num = int(input())
            pull.append(num)
        b_lst.append(pull)
        pull = []
    a_lst = numpy.array(a_lst)
    b_lst = numpy.array(b_lst)
    result = a_lst @ b_lst
    for i in result:
        print(*i)
main()
