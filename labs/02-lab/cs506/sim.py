from math import sqrt
def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    return sum(abs(val1-val2) for val1, val2 in zip(x,y))

def jaccard_dist(x, y):
    nominator = x.symmetric_difference(y)
    denominator = x.union(y)
    distance = len(nominator)/len(denominator)
    
    return distance

def cosine_sim(x, y):
    return dot(x,y) / ( (dot(x,x) **.5) * (dot(y,y) ** .5) )
    # raise NotImplementedError()
def dot(x,y): 
    return (sum(a*b for a,b in zip(x,y)))
    # Feel free to add more
