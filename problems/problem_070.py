# -------------------------------------------------------------------------------
# Name:        Problem 70
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------


def getPrimes(n = None):
    prime = []
    
    for k in range(2,n+1):
        ok = True
        for m in prime:
            if k % m == 0:
                ok = False
                break
        if ok:
            prime.append(k)
    
    return prime


def isPrime(n,prime):
    for p in prime:
        if p**2 > n:
            return True
        if n % p == 0:
            return False
        

def isPalindrom(a,b):
    A = sorted(map(int,list(str(a))))
    B = sorted(map(int,list(str(b))))
    return A == B


def getCombinations(n,k):
    N = len(n)
    mult = list(n)
    factors = []

    a = [mult[i] for i in range(k)]
    factors.append(reduce(lambda x,y: x*y,a))
    
    while True:
        for j in range(k):
            if a[j] == mult[N-1] and j == k-1:
                return factors
            if j < k-1 and mult.index(a[j]) + 1 == mult.index(a[j+1]):
                continue
            a[j] = mult[mult.index(a[j])+1]
            for i in range(j):
                a[i] = mult[i]
                
#             print a
            factors.append(reduce(lambda x,y: x*y,a))


def main():
    prime = getPrimes(5000)
    Q = 10
    P = 0

    for n in range(2,10000000):
        N = n-1
        rem = n
        
        divs = set([])
        
        # find all prime divisors
        for p in prime:
            if p >= n:
                break
            if n % p == 0:
                while rem % p == 0:
                    rem = rem / p
                divs.add(p)
        
        if rem > 1:
            if isPrime(rem,prime):
                divs.add(rem)
            else:
                print("Should not happen. rem =", rem)
                
        for d in divs:
            N -= (N/d - 1)
            if n % d == 0:
                N -= 1
        
        if len(divs) > 1:
            for m in range(2,len(divs)+1):
                factors = getCombinations(divs,m)
#                 print factors
                for f in factors:
                    if m % 2 == 0:
                        N -= N / f
                    else:
                        N += N / f
                        
        q = float(n) / float(N)
        
        if isPalindrom(n,N):
            if q < Q:
                Q = q
                P = n
                # print "Candidate:",
        
            # print n,"->",N,divs,"->",q
        
    print("Solution:", P)


if __name__ == '__main__':
    main()