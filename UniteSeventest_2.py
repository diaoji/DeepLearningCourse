import tensorflow as tf 
import numpy as np
import matplotlib.pyplot as plt

minst=tf.keras.datasets.mnist
(train_x,train_y),(test_x,test_y)=minst.load_data()

for i in range(16):
    num=np.random.randint(1,5000)

    plt.subplot(4,4,i+1)
    plt.axis("off")
    plt.imshow(train_x[num],cmap="gray")
    plt.title(train_y[num],fontsize=14)

plt.suptitle("MINST Test set sample",fontsize=20,color="red")
plt.show()

