import tensorflow as tf

x = tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y = tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])

n = tf.cast(tf.size(x),tf.float32)
sum11 = tf.reduce_sum(x*y)
sum22 = tf.reduce_sum(x)
sum33 = tf.reduce_sum(y)

sum44 = tf.reduce_sum(pow(x,2))
sum55 = pow(tf.reduce_sum(x),2)

w = (n*sum11-sum22*sum33)/(n*sum44-sum55)

sum66 = tf.reduce_sum(y)
sum77 = w*tf.reduce_sum(x)
b = (sum66 - sum77)/n
print("w=",w.numpy())
print("b=",b.numpy())