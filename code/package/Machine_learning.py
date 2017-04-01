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
import matplotlib.pyplot as plt

FLAGS = None

#tensorflow de base
def machine_learning(donnee, option):
  # importation des données
  mnist = input_data.read_data_sets(option["ch_mnist"], one_hot=True)

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

  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

  print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

  #for i in range(1):
    #plt.matshow(tf.reshape(mnist.test.images[i], (28,28)).eval())
  #plt.show()


  #data = mnist.test.images[25]
  data = donnee

  redim = reshape(data, (28, 28))
  for i in range(28):
    for j in range(28):
      print("@" if redim[i,j] >= 0.5 else " ", end= "")
    print("")



  result = sess.run(tf.argmax(y,1), feed_dict={x: [data]})
  #result = sess.run(y, feed_dict={x: [donnee]})
  print ('resultat ', result)


