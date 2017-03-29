#!usr/bin/python3.5
#-*-coding:UTF-8 -*

# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""A very simple MNIST classifier.
See extensive documentation at
http://tensorflow.org/tutorials/mnist/beginners/index.md
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data
from numpy import *

import tensorflow as tf

FLAGS = None

#tensorflow de base
def machine_learning(donnee):
  # importation des données
  mnist = input_data.read_data_sets("/home/ledoux/Documents/Programmation/python/python-le-on/proj/machine_learning/code/tensorflow/mnist/input_data/", one_hot=True)

  # creation du modele
  #x = images
  #y = etiquettes
  x = tf.placeholder(tf.float32, [None, 784])
  W = tf.Variable(tf.zeros([784, 10]))
  b = tf.Variable(tf.zeros([10]))
  y = tf.matmul(x, W) + b

  # Define loss and optimizer
  y_ = tf.placeholder(tf.float32, [None, 10])

  # The raw formulation of cross-entropy,
  #
  #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
  #                                 reduction_indices=[1]))
  #
  # can be numerically unstable.
  #
  # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
  # outputs of 'y', and then average across the batch.
  cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

  sess = tf.InteractiveSession()
  tf.global_variables_initializer().run()
  # Train
  for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    #print(FLAGS.donnee)
  # Test trained model
  correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
  print(tf.cast(tf.argmax(y, 1), tf.float32), tf.argmax(y_, 1))
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

  print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
  print("test ", x,y_)
  print("sortie:{}".format(tf.cast(correct_prediction, tf.float32)))

  data = mnist.test.images[0]
  print("solution: {}".format(mnist.test.labels[0]))

  redim = reshape(data, (28, 28))
  for i in range(28):
    for j in range(28):
      print("#" if redim[i,j] >= 0.5 else " ", end= "")
    print("")

  print(mnist.test.images[0])



  #result = sess.run(tf.argmax(y,1), feed_dict={x: [donnee]})
  result = sess.run(y, feed_dict={x: [donnee]})
  print ('resultat'.join(map(str, result))) 



#tensorflow de base modifier
def machine_learning_v2(donnee):
  # importation des données
  mnist = input_data.read_data_sets("/home/ledoux/Documents/Programmation/python/python-le-on/proj/machine_learning/code/tensorflow/mnist/input_data/", one_hot=True)

  # creation du modele
  #x = images
  #y = etiquettes
  x = tf.placeholder(tf.float32, [None, 784])
  W = tf.Variable(tf.zeros([784, 10]))
  b = tf.Variable(tf.zeros([10]))
  y = tf.matmul(x, W) + b

  # Define loss and optimizer
  y_ = tf.placeholder(tf.float32, [None, 10])

  # The raw formulation of cross-entropy,
  #
  #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
  #                                 reduction_indices=[1]))
  #
  # can be numerically unstable.
  #
  # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
  # outputs of 'y', and then average across the batch.
  cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

  sess = tf.InteractiveSession()
  tf.global_variables_initializer().run()
  # Train
  for _ in range(1000):
    donnee, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: donnee, y_: batch_ys})
    #print(FLAGS.donnee)
  # Test trained model
  correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

  print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
  print("test ", x,y_)
  print("sortie:{}".format(tf.cast(correct_prediction, tf.float32)))

#tensorflow alternative
def machine_learning_v3(donnee):
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

  redim = reshape(donnee, (28, 28))
  for i in range(28):
    for j in range(28):
      print("#" if redim[i,j] >= 0.5 else " ", end= "")
    print("")

  result = sess.run(tf.argmax(y,1), feed_dict={x: [donnee]})

  print (' '.join(map(str, result))) 



if __name__ == '__main__':

  arr = array([(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)])

  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')

  parser.add_argument('--donnee', type=array, default=arr,
                      help='Directory for storing input data')

  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
