from mpmath import *
mp.dps=40
def scalar(v):
    return mpf(pow(sum(multiplication(v, v)), .5))
def multiplication(v1, v2):
    return [mpf(v1[i])*mpf(v2[i]) for i in range(len(v1))]
def sum_v(v1,v2):
    return [v1[i]+v2[i] for i in range(len(v1))]

def cos(v1, v2):
    denominator = mpf(scalar(v1) * scalar(v2))
    numerator = mpf(sum(multiplication(v1, v2)))
    return mpf(0) if (numerator==mpf(0) ) else min(mpf(numerator / denominator),mpf(1))

def divide(v,k):
    k =  mpf(k)
    for i in range(len(v)):
        if v[i]!=0:
            v[i] /= k
    return v[:]