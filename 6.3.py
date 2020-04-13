import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import scale
import tensorflow as tf

df = pd.read_csv("L:/boston.csv", header=0)  # 导入数据
ds = df.values  # 以np数组形式返回数据集的值
# boston_housing = tf.keras.datasets.boston_housing
# (x_data,y_data),(_,_) = boston_housing.load_data(test_split=0)
x_data = ds[:, :12]
y_data = ds[:, 12]  # 处理数据
for i in range(12):
    x_data[:, i] = (x_data[:, i] - x_data[:, i].min() / x_data[:, i].max() - x_data[:, i].min())

train_num = 300  # 训练集的数量
valid_num = 100  # 验证集的数量
test_num = len(x_data) - train_num - valid_num  # 测试集的数量

x_train = x_data[:train_num]
y_train = y_data[:train_num]  # 训练集划分
x_valid = x_data[train_num:train_num + valid_num]
y_valid = y_data[train_num:train_num + valid_num]  # 验证集划分
x_test = x_data[train_num + valid_num:train_num + valid_num + test_num]
y_test = y_data[train_num + valid_num:train_num + valid_num + test_num]  # 测试集划分

x_train = tf.cast(scale(x_train), dtype=tf.float32)
x_valid = tf.cast(scale(x_valid), dtype=tf.float32)
x_test = tf.cast(scale(x_test), dtype=tf.float32)


def model(x, w, b):  # 定义模型
    return tf.matmul(x, w) + b


W = tf.Variable(tf.random.normal([12, 1], mean=0.0, stddev=1.0, dtype=tf.float32))
B = tf.Variable(tf.zeros(1), dtype=tf.float32)

training_epochs = 100  # 迭代次数
learning_rate = 0.0015  # 学习率
batch_size = 10  # 训练一次的样本数


def loss(x, y, w, b):  # 定义损失函数
    err = model(x, w, b) - y
    squared_err = tf.square(err)
    return tf.reduce_mean(squared_err)


def grad(x, y, w, b):  # 定义梯度计算函数
    with tf.GradientTape() as tape:
        loss_ = loss(x, y, w, b)
    return tape.gradient(loss_, [w, b])


optimizer = tf.keras.optimizers.SGD(learning_rate)  # 创建优化器
loss_list_train = []  # 保存训练集loss值
loss_valid_train = []  # 保存验证集loss值
total_step = int(train_num / batch_size)
for epoch in range(training_epochs):
    for step in range(total_step):
        xs = x_train[step * batch_size:(step + 1) * batch_size, :]
        ys = y_train[step * batch_size:(step + 1) * batch_size]
        grads = grad(xs, ys, W, B)  # 计算梯度
        optimizer.apply_gradients(zip(grads, [W, B]))
    loss_train = loss(x_train, y_train, W, B).numpy()
    loss_valid = loss(x_valid, y_valid, W, B).numpy()
    loss_list_train.append(loss_train)
    loss_valid_train.append(loss_valid)
    print("epoch={:3d},train_loss={:.4f},valid_loss={:.4f}".format(epoch + 1, loss_train, loss_valid))

test_house_id = np.random.randint(0, test_num)
y = y_test[test_house_id]
y_pred = model(x_test, W, B)[test_house_id]
y_predit = tf.reshape(y_pred, ()).numpy()
print("房屋id：", test_house_id, "实际价格：", y, "预测价格：", y_predit)
