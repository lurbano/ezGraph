

# conventional
def residual(lst1, lst2):
    n = len(lst1)
    s = 0
    for i in range(n):
        d = lst1[i] - lst2[i]
        s += d
        #print(i, lst1[i], lst2[i], d, s)
    return s


x1 = [2, 5, 7]
x2 = [3, 1, 1]

r = residual(x1, x2)
print(f'residual= {r}')
