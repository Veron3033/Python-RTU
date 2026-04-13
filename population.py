p0 = 1000
per = 2
c = 50
t = 1200
def nb_year(p0, per, c, t):
    rate = per / 100
    n = 0
    p = p0
    while p < t:
        p = p + rate * p + c
        n += 1
    return n

print(nb_year(1500000, 2.5, 10000, 2000000))