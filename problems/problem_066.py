# -------------------------------------------------------------------------------
# Name:        Problem 66
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------


import math
from fractions import gcd


def chainSqrt(m):
    a = []
    b = []
    c = []
    
    b.append(math.sqrt(m))
    a.append(int(math.floor(b[-1])))
    c.append(round(b[-1],8))
    
    while True:
        b.append(1. / (b[-1] - float(a[-1])))
        a.append(int(math.floor(b[-1])))
        c.append(round(b[-1],8))
        
#         print b
        if c[-1] in c[:-1]:
            k = c.index(c[-1])
            n = len(c) - k - 1
#             print c[-1],"in",c[:-1]
            break
            
    return a,n


def guessChain(m):
    a = [int(math.floor(math.sqrt(m)))]
    PQ_ = a[0]
    Z = math.sqrt(m)
    
    for i in range(5):
        A = 1
        P,Q = getFraction(a + [A])
        PQ_ = float(P)/float(Q)
            
        while True:
            P,Q = getFraction(a + [A+1])
            PQ = float(P)/float(Q)
            
            if (float(PQ_) - Z) * (float(PQ) - Z) < 0.0:
                a.append(A)
                break
            
            A += 1
            PQ_ = PQ

    return a


def getPeriod(a):
    n = 1
    
    while True:
        if len(a) <= 5*n:
            return 0
        for i in range(n):
            if a[-1-i] != a[-1-n-i]:
                break
            return n
        n += 1
        
    
def getFraction(a,n=False):
    if not n:
        n = len(a)
    
#     print a
    p = []
    p.append(a[0])
    p.append(a[0]*a[1]+1)
    
    q = []
    q.append(1)
    q.append(a[1])
    
    if n==1:
#         print "1:",p[-1],"/",q[-1]
        return p[-1], q[-1]

    
    for i in range(2,n):
        p.append(p[-1]*a[i] + p[-2])
        q.append(q[-1]*a[i] + q[-2])
#         print str(i)+":",p[-1],"/",q[-1]
    
    m = gcd(p[-1],q[-1])
    if m>1:
        print "Reducible fraction"
    
    return p[-1]/m, q[-1]/m


def nose(n):
    a = []
    ex = [1]
    ey = [1]
    p = []
    q = [1]
    
    while True:
        
        a = int(math.floor(math.sqrt(m) / e1))
    

def main():

    x = 0
    y = 0
    result = []

    for D in range(2,8):
        if int((round(math.sqrt(D)))**2) != D:
           a,n = chainSqrt(D)
#             print a
#             print n
           X,Y = getFraction(a,n)
           print D,"->",X,Y
           if X > x:
               d = D
               x = X
               y = Y
    print "Solution:",d,"->",x,y

    print guessChain(5)

#     for i in range
#     a,n = chainSqrt(2)
#     print a
#     print n
#     print getFraction(a[:-1])
    
    
if __name__ == '__main__':
    main()