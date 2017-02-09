# -*- coding: utf-8 -*-

import math

n = 0
a = []
b = []

with open("input.txt", "rt") as file1:

    for line in file1:                      #  cчитали количество точек и окружностей
        for number in line.split():
            T = int(number)
        break;
    for line in file1:
        for number in line.split():
            O = int(number)
        break;
    i = int(0)
    a = [[0] * 2 for i in range(T)]
    b = [[0] * 3 for i in range(O)]

    i = int (0)      #координаты точек
    j = int (0)
    f = True
    for line in file1:
        for number in line.split():
            a[i][j] = int(number)
            j = 1
        j=0
        i+=1
        if i > T-1:
            f = False
            break


    i = int(0)  # координаты окружностей
    j = int(0)
    f = True
    for line in file1:
        if not f:
            break
        for number in line.split():
            b[i][j] = int(number)
            j+=1
        j = 0
        i+=1
        if i > O - 1:
            f = False
            break

max = int(0)
per = int(0)
for i in range (0, T-1):
    for j in range (i+1, T):
        per = int(0)
        Ax = (a[j][1])-(a[i][1])
        By = -((a[j][0])-(a[i][0]))
        C = (a[i][1])*((a[j][0])-(a[i][0]))-((a[j][1])-(a[i][1]))*(a[i][0])
        for k in range (0,O):
            d = (math.fabs(Ax * (b[k][0]) + By * (b[k][1]) + C)) / (math.sqrt(Ax * Ax + By * By))
            if (d < (b[k][2])) or (d == (b[k][2])):
                per+=1
        if per > max:
            max = per
            x1 = int(a[i][0])
            x2 = int(a[j][0])
            y1 = int(a[i][1])
            y2 = int(a[j][1])

print (max)
print (x1, ' ', y1)
print (x2, ' ', y2)




