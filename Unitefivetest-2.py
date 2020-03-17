import numpy as np 
import math
x=[64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]
y=[62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]
sumx=0
sumy=0
i=0
while i<10:
    sumx+=x[i]
    sumy+=y[i]
    i+=1
avgx=sumx/10
avgy=sumy/10
print(avgx,avgy)
top=0
bottom=0
j=0
while j<10:
    top+=((x[j]-avgx)*(y[j]-avgy))
    bottom+=((x[j]-avgx)*(x[j]-avgx))
    j+=1
w=top/bottom
print("w=",w)
b=avgy-w*avgx
print("b=",b)