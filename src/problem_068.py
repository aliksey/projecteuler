# -------------------------------------------------------------------------------
# Name:        Problem 68
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------


def main():
    variants = []

    numbers = set(range(1, 11))
    for a in range(1, 11):
        numbers.remove(a)

        for b in numbers:
            numbers.remove(b)

            for c in numbers:
                numbers.remove(c)

                for d in numbers:
                    numbers.remove(d)

                    for e in numbers:
                        numbers.remove(e)

                        for v in numbers:
                            numbers.remove(v)

                            sum = a + b + v
                            w = sum - b - c

                            if w in numbers:
                                numbers.remove(w)
                                x = sum - c - d

                                if x in numbers:
                                    numbers.remove(x)
                                    y = sum - d - e

                                    if y in numbers:
                                        numbers.remove(y)
                                        z = sum - e - a

                                        if z in numbers:
                                            variants.append([a, b, c, d, e, v, w, x, y, z])

                                        numbers.add(y)
                                    numbers.add(x)
                                numbers.add(w)
                            numbers.add(v)
                        numbers.add(e)
                    numbers.add(d)
                numbers.add(c)
            numbers.add(b)
        numbers.add(a)

    n = []

    for variant in variants:
        index = variant.index(min(variant[5:])) - 5
        strn = str(variant[index]) + str(variant[(index - 5) % 10]) + str(variant[(index - 4) % 10]) + str(
            variant[(index + 1) % 10]) + str(variant[(index + 1 - 5) % 10]) + str(variant[(index + 1 - 4) % 10]) + str(
            variant[(index + 2) % 10]) + str(variant[(index + 2 - 5) % 10]) + str(variant[(index + 2 - 4) % 10]) + str(
            variant[(index + 3) % 10]) + str(variant[(index + 3 - 5) % 10]) + str(variant[(index + 3 - 4) % 10]) + str(
            variant[(index + 4) % 10]) + str(variant[(index + 4 - 5) % 10]) + str(variant[(index + 4 - 4) % 10])
        sn = [variant[5 + (index % 5)], variant[index % 5], variant[(index + 1) % 5],
              variant[5 + ((index + 1) % 5)], variant[(index + 1) % 5], variant[(index + 1 + 1) % 5],
              variant[5 + ((index + 2) % 5)], variant[(index + 2) % 5], variant[(index + 2 + 1) % 5],
              variant[5 + ((index + 3) % 5)], variant[(index + 3) % 5], variant[(index + 3 + 1) % 5],
              variant[5 + ((index + 4) % 5)], variant[(index + 4) % 5], variant[(index + 4 + 1) % 5]]

        k = int("".join(map(str, sn)))
        if k < 10000000000000000:
            n.append(k)

    print "Solution:", max(n)


if __name__ == '__main__':
    main()
