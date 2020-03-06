#solvingtest.py 
'''完成一元二次方程的求解，要求程序输入任意a,b,c的值后，
程序能判断出有解或无解，有解的话，输出x的解为多少。
'''

import math
def quadratic(a,b,c):
    p=b*b-4*a*c
    if p>=0 and a!=0:#一元二次方程有解的条件
        x1=(-b+math.sqrt(p))/(2*a)
        x2=(-b-math.sqrt(p))/(2*a)
        return x1,x2
    elif a==0:#a=0的情况下为一元一次方程
    	x1=x2=-c/b
    	return x1
    else:
        return('Wrong Number！')
 
a=float(input('Please input a='))
b=float(input('Please input b='))
c=float(input('Please input c='))
print(quadratic(a,b,c))
