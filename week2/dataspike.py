"""dataspike"""
d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
d5 = int(input())
d6 = int(input())
d7 = int(input())
d8 = int(input())
def d1_2():
    """dataspike"""
    if d1 >= d2:
        c1 = d1
    else:
        c1 = d2
    return c1
def d3_4():
    """dataspike"""
    if d3 >= d4:
        c2 = d3
    else:
        c2 = d4
    return c2
def d5_6():
    """dataspike"""
    if d5 >= d6:
        c3 = d5
    else:
        c3 = d6
    return c3
def d7_8():
    """dataspike"""
    if d7 >= d8:
        c4 = d7
    else:
        c4 = d8
    return c4
def c1_2():
    """ds"""
    if d1_2() >= d3_4():
        g1 = d1_2()
    else:
        g1 = d3_4()
    return g1
def c3_4():
    """d"""
    if d5_6() >= d7_8():
        g2 = d5_6()
    else:
        g2 = d7_8()
    return g2
if c1_2() >= c3_4():
    print(c1_2())
else:
    print(c3_4())
