# -------------------------------------------------------------------------------
# Name:        Problem 61
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------


import sys


def get3erSeries():
    return [int(n * (n + 1) / 2) for n in range(40, 141) if n * (n + 1) >= 2000 and n * (n + 1) < 20000]


def get4erSeries():
    return [n ** 2 for n in range(30, 101) if n ** 2 >= 1000 and n ** 2 < 10000]


def get5erSeries():
    return [int(n * (3 * n - 1) / 2) for n in range(90) if n * (3 * n - 1) >= 2000 and n * (3 * n - 1) < 20000]


def get6erSeries():
    return [int(n * (2 * n - 1)) for n in range(75) if n * (2 * n - 1) >= 1000 and n * (2 * n - 1) < 10000]


def get7erSeries():
    return [int(n * (5 * n - 3) / 2) for n in range(65) if n * (5 * n - 3) >= 2000 and n * (5 * n - 3) < 20000]


def get8erSeries():
    return [int(n * (3 * n - 2)) for n in range(60) if n * (3 * n - 2) >= 1000 and n * (3 * n - 2) < 10000]


def getNextNumbers(number, series):
    return [series[i] for i in range(len(series)) if number % 100 == series[i] // 100]


def main():
    series = [get3erSeries(), get4erSeries(), get5erSeries(), get6erSeries(), get7erSeries(), get8erSeries()]
    series1 = series[5]

    for n1 in series1:
        index1 = set(range(5))
        for j1 in range(5):
            if j1 not in index1:
                continue
            index2 = index1.copy()
            index2.remove(j1)
            series2 = getNextNumbers(n1, series[j1])

            if len(series2) > 0:
                for n2 in series2:
                    for j2 in range(5):
                        if j2 not in index2:
                            continue
                        index3 = index2.copy()
                        index3.remove(j2)
                        series3 = getNextNumbers(n2, series[j2])

                        if len(series3) > 0:
                            for n3 in series3:
                                for j3 in range(5):
                                    if j3 not in index3:
                                        continue
                                    index4 = index3.copy()
                                    index4.remove(j3)
                                    series4 = getNextNumbers(n3, series[j3])

                                    if len(series4) > 0:
                                        for n4 in series4:
                                            for j4 in range(5):
                                                if j4 not in index4:
                                                    continue
                                                index5 = index4.copy()
                                                index5.remove(j4)
                                                series5 = getNextNumbers(n4, series[j4])

                                                if len(series5) > 0:
                                                    for n5 in series5:
                                                        for j5 in range(5):
                                                            if j5 not in index5:
                                                                continue
                                                            index6 = index5.copy()
                                                            index6.remove(j5)
                                                            series6 = getNextNumbers(n5, series[j5])

                                                            if len(series6) > 0:
                                                                for n6 in series6:
                                                                    if n6 % 100 == n1 // 100:
                                                                        print 'Found:', n1, n2, n3, n4, n5, n6, ':', n1 + n2 + n3 + n4 + n5 + n6
                                                                        sys.exit()


if __name__ == '__main__':
    main()
