# -*- coding: utf-8 -*-

from math import *

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
    #for i in range(0, T):
    #    print (a[i][0], ' ', a[i][1])

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







 #  Ax       By              C
#(y2-y1)*x | -y*(x2-x1) | +y1*(x2-x1)-(y2-y1)*x1 = 0 #уравнение прямой

#  первые два числа в инпуте - координаты центра окружности - Mx и My
#  math.fabs - модуль
#  math.sqrt - корень
#  d = (math.fabs (A*Mx+B*My+C))/(math.sqrt(A*A+B*B))
#  если d < R, то инкреминируем
