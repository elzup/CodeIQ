# -*- coding: utf-8 -*-
def kinoko(n):
    a=range(n,0,-1)
    while(len(a)>1):a=a[::-2]
    return a[0]

for i in range(1, 2048):
    print(kinoko(i))
