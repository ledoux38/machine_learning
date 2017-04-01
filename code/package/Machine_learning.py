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

class machine_learning_basique:

	def __init__ (self, option = {"ch_mnist": "./MNIST_data"}):
		if not isinstance(option, dict):
			raise TypeError("erreur option = {} n'est pas de type dict ".format(type(option)))

		self.option = option
		self.session = None
		self.donnee_mnist = None
		self.variable_mnsit = {}



	def recuperation_donnee_mnist(self):
		"""
		methode de class qui charge les données mnist
		"""

		self.mnist = input_data.read_data_sets(self.option["ch_mnist"], one_hot=True)



	def creation_modele(self):
		"""
		methode de classe qui permet de créer le modele'
		"""
		
		self.variable_mnsit = {"x": tf.placeholder(tf.float32, [None, 784]),
								"W": tf.Variable(tf.zeros([784, 10])), 
								"b": tf.Variable(tf.zeros([10])),
								"y_": tf.placeholder(tf.float32, [None, 10])}
		
		self.variable_mnsit["y"] = tf.matmul(self.variable_mnsit["x"], self.variable_mnsit["W"]) + self.variable_mnsit["b"] 
		
		cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=self.variable_mnsit["y_"], logits=self.variable_mnsit["y"]))
		
		self.variable_mnsit["train_step"] = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

		self.session = tf.InteractiveSession()

		tf.global_variables_initializer().run()




	def entrainement(self):
		"""
		methode de classe qui permet d'entrainer le modele'
		"""

		for _ in range(1000):
			batch_xs, batch_ys = self.mnist.train.next_batch(100)
			self.session.run(self.variable_mnsit["train_step"], feed_dict={self.variable_mnsit["x"]: batch_xs, 
																			self.variable_mnsit["y_"]: batch_ys})

		correct_prediction = tf.equal(tf.argmax(self.variable_mnsit["y"], 1), tf.argmax(self.variable_mnsit["y_"], 1))

		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

		print(self.session.run(accuracy, feed_dict={self.variable_mnsit["x"]: self.mnist.test.images, 
											self.variable_mnsit["y_"]: self.mnist.test.labels}))



	def test_modele(self, data):
		"""
		methode de classe qui permet de tester le modele
		"""
		if not isinstance(data, numpy.ndarray):
			raise TypeError("erreur data = {} n'est pas de type numpy.ndarray ".format(type(data)))			

		result = self.session.run(tf.argmax(self.variable_mnsit["y"],1), feed_dict={self.variable_mnsit["x"]: [data]})
		print ('resultat ', result)



"""
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

  cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

  sess = tf.InteractiveSession()

  tf.global_variables_initializer().run()
  # Train
  for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

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
"""



if __name__ == "__main__":


  a = machine_learning_basique()
  print(a.variable_mnsit)

  a.recuperation_donnee_mnist()
  a.creation_modele()
  a.entrainement()


