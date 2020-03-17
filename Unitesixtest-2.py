import tensorflow as tf 
import matplotlib.pyplot as plt
import numpy as np 

plt.rcParams["font.sans-serif"]="SimHei" 
plt.rcParams["axes.unicode_minus"]=False 

boston_housing=tf.keras.datasets.boston_housing
(train_x,train_y),(_,_)=boston_housing.load_data(test_split=0)

plt.rcParams["font.sans-serif"]="SimHei"
plt.rcParams["axes.unicode_minus"]=False

titles=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B-1000","LSTAT","MEDV"]

plt.figure(figsize=(12,12))

for i in range(13):
    plt.subplot(4,4,(i+1))
    plt.scatter(train_x[:,i],train_y)
    plt.xlabel(titles[i])
    plt.ylabel("Prices($1000's)")
    plt.title(str(i+1)+"."+titles[i]+"-Prices")

plt.tight_layout()
#plt.tight_layout()
plt.suptitle("各个属性与房价的关系",x=0.5,y=1.02,fontsize=14)
plt.show()

print("请选择你要打印的属性：")
for i in range(13):
    print(str(i+1)+" -- "+titles[i])
intuser=int(input())
#print(intuser)

plt.subplot(111)
plt.scatter(train_x[:,intuser-1],train_y)
plt.xlabel(titles[intuser])
plt.ylabel("Prices($1000's)")
plt.title(str(intuser)+"."+titles[intuser-1]+"-Prices")

plt.show()