#!/usr/bin/env python3
#By FabriNvs
#GNU/GPL License
#My first secuence

#sumar los primeros 10 números enteros

N=10
a=1
b=1
print(a)
print(b)
#c=a+b
vec=[1,1]

suma=0
for x in range(N+1):
    c=a+b
    vec.append(c)
    b1=b
    a=b1
    b=c

print(vec)
    
    
    
