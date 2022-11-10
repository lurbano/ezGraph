def findAvg(lst): 
    # Finds the average of a list
    t = 0
    n = 0
    for x in lst:
        t += x 
        n += 1 
    avg = t/n
    return avg

def resSq(lst1, lst2):
    # Finds the sum of the residuals squared 
    t = 0
    for i in range(len(lst1)):
        t += (lst1[i]-lst2[i])**2
    return t

def meanDif(lst):
    t = 0
    avg = findAvg(lst)
    for x in lst:
        t += (x - avg)**2
    return t

def rSquared(measured, modeled):
    rSq = 1 - (resSq(measured, modeled) / meanDif(measured))
    return rSq