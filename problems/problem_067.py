# -------------------------------------------------------------------------------
# Name:        Problem 67
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------


def main():
    fin = open("../input/067_triangle.txt", 'r')
    lines = fin.readlines()
    elements = []
    
    for line in lines:
        elements.append(map(int,line.split()))
    fin.close()
    
    for i in range(len(elements)-2,-1,-1):
        for j in range(len(elements[i])):
            elements[i][j] += max(elements[i+1][j], elements[i+1][j+1])
            
    print "Solution:", elements[0][0]

if __name__ == '__main__':
    main()