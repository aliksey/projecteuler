# -------------------------------------------------------------------------------
# Name:        Problem 65
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------


class ratio:
    def __init__(self, _a, _b):
        self.a = long(_a)
        self.b = long(_b)
        self.simplify()

    def simplify(self):
        c = NOD(self.a, self.b)
        if c > 1:
            self.a = self.a / c
            self.b = self.b / c

    def inverse(self):
        c = self.a
        self.a = self.b
        self.b = c

    def add(self, c):
        self.a += c * self.b
        self.simplify()


def NOD(a, b):
    while a != b:
        if a < b:
            b = b - a
        else:
            a = a - b
    return a


def makeSeries(c):
    d = ratio(c[-1], 1)
    for n in reversed(c[:-1]):
        d.inverse()
        d.add(n)
    return d


def sumDigits(c):
    s = 0
    while c > 0:
        s += c % 10
        c /= 10
    return s


def main():
    c = [2]
    for i in range(33):
        c = c + [1, 2 * (i + 1), 1]
    d = makeSeries(c)
    print sumDigits(d.a)


if __name__ == '__main__':
    main()
