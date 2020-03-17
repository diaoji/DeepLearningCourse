import numpy as np 
import random
np.random.seed(612)
arr=np.random.rand(1,1000)
ureceptnum=int(input("请输入一个1~100之间的整数："))
i=0
while i<1000:
    if(i%ureceptnum==0):
        print(arr[0,i])
    i+=1
