import random
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import scipy.ndimage

mnist = input_data.read_data_sets('/tmp/tensorflow/mnist/input_data', one_hot=True)


x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(1000)
    sess.run(train_step, feed_dict= {x: batch_xs, y_: batch_ys})

print ("done with training")

tableau_img = scipy.ndimage.imread("test/_v3_5_t5.JPG", flatten=True)
print(tableau_img, np.shape(tableau_img))

flatten  = np.ndarray.flatten(tableau_img)
print(flatten, np.shape(flatten))

data = np.vectorize(lambda x: 255 - x)(flatten)
print(data, np.shape(data))

result = sess.run(tf.argmax(y,1), feed_dict={x: [data]})

print (' '.join(map(str, result))) 




"""
import random
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import scipy.ndimage
def machine_learning(donnee):

  mnist = input_data.read_data_sets("/home/ledoux/Documents/Programmation/python/python-le-on/proj/machine_learning/code/tensorflow/mnist/input_data/", one_hot=True)


  x = tf.placeholder(tf.float32, [None, 784])
  W = tf.Variable(tf.zeros([784, 10]))
  b = tf.Variable(tf.zeros([10]))

  y = tf.nn.softmax(tf.matmul(x, W) + b)
  y_ = tf.placeholder(tf.float32, [None, 10])

  cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

  init = tf.initialize_all_variables()

  sess = tf.Session()
  sess.run(init)

  for i in range(1000):
      batch_xs, batch_ys = mnist.train.next_batch(1000)
      sess.run(train_step, feed_dict= {x: batch_xs, y_: batch_ys})

  print ("done with training")


  data = donnee
  result = sess.run(tf.argmax(y,1), feed_dict={x: [data]})

  print (' '.join(map(str, result))) 

if __name__ == "__main__":

  tableau = scipy.ndimage.imread("test/_v3_5_t5.JPG", flatten=True)
  print("\n\n\n",tableau, np.shape(tableau))
  tableau2 = np.ndarray.flatten(tableau)
  print("\n\n\n",tableau2, np.shape(tableau2))
  data = np.vectorize(lambda x: 255 - x)(tableau2)
  print("\n\n\n",data, np.shape(data))
"""