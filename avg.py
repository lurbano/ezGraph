def avg1(lst):
    return sum(lst)/len(lst)


def myAvg(lst):
    # sum 
    s = 0
    n = 0
    for i in lst:
        s = s + i
        n += 1
    return s/n



x = [ 3, 5, 22, 11, 7]
y = [ 1,2, 3, 4, 5, 6]

avg = myAvg(y)
print ("AVG1:", avg)




