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
import pickle

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
		#creation des variables
		self.variable_mnsit = {"x": tf.placeholder(tf.float32, [None, 784]),
								"W": tf.Variable(tf.zeros([784, 10])), 
								"b": tf.Variable(tf.zeros([10])),
								"y_": tf.placeholder(tf.float32, [None, 10])}
		#remplissage des variables
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

		#self.variable_mnsit["accuracy"] = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

		print(self.session.run(accuracy, feed_dict={self.variable_mnsit["x"]: self.mnist.test.images, self.variable_mnsit["y_"]: self.mnist.test.labels}))



	def test_modele(self, data):
		"""
		methode de classe qui permet de tester le modele
		"""
		if not isinstance(data, ndarray):
			raise TypeError("erreur data = {} n'est pas de type numpy.ndarray ".format(type(data)))			

		result = self.session.run(tf.argmax(self.variable_mnsit["y"],1), feed_dict={self.variable_mnsit["x"]: [data]})
		print ('resultat ', result)



	def sauve_modele(self):
		"""
		methode de class qui permet la sauvegarde des données
		"""
		saver = tf.train.Saver()
		save_path = saver.save(self.session, "modeles/basique/model_basique.ckpt")
		print("Model saved in file: %s" % save_path)



	def chargement_modele(self):
		saver = tf.train.Saver()
		with tf.Session() as self.session:
			# Restore variables from disk.
			saver.restore(self.session, "modeles/basique/model_basique.ckpt")
			print("Model restored.")












class machine_learning_avancer:

	def __init__ (self, option = {"ch_mnist": "./MNIST_data"}):
		if not isinstance(option, dict):
			raise TypeError("erreur option = {} n'est pas de type dict ".format(type(option)))

		self.option = option
		self.session = None
		self.donnee_mnist = None
		self.variable_mnsit = {}
		self.correct_prediction = None



	def recuperation_donnee_mnist(self):


		self.mnist = input_data.read_data_sets(self.option["ch_mnist"], one_hot=True)



	def weight_variable(self, shape):

		initial = tf.truncated_normal(shape, stddev=0.1)
		return tf.Variable(initial)



	def bias_variable(self, shape):
		initial = tf.constant(0.1, shape=shape)
		return tf.Variable(initial)		


	def conv2d(self, x, W):
		return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')




	def max_pool_2x2(self, x):
		return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')



	def creation_modele(self):

		self.session = tf.InteractiveSession()
		#creation des variables
		W_conv1 = self.weight_variable([5, 5, 1, 32])
		b_conv1 = self.bias_variable([32])

		# Placeholder
		self.variable_mnsit["x"] = tf.placeholder(tf.float32, [None, 784])
		self.variable_mnsit["y_"] = tf.placeholder(tf.float32, [None, 10])

		# Reshape
		x_image = tf.reshape(self.variable_mnsit["x"], [-1,28,28,1])

		h_conv1 = tf.nn.relu(self.conv2d(x_image, W_conv1) + b_conv1)
		h_pool1 = self.max_pool_2x2(h_conv1)

		W_conv2 = self.weight_variable([5, 5, 32, 64])
		b_conv2 = self.bias_variable([64])

		h_conv2 = tf.nn.relu(self.conv2d(h_pool1, W_conv2) + b_conv2)
		h_pool2 = self.max_pool_2x2(h_conv2)

		W_fc1 = self.weight_variable([7 * 7 * 64, 1024])
		b_fc1 = self.bias_variable([1024])

		h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
		h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
		
		self.variable_mnsit["keep_prob"] = tf.placeholder(tf.float32)
		h_fc1_drop = tf.nn.dropout(h_fc1, self.variable_mnsit["keep_prob"])

		W_fc2 = self.weight_variable([1024, 10])
		b_fc2 = self.bias_variable([10])

		self.variable_mnsit["y_conv"] = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
				
		cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(self.variable_mnsit["y_conv"], self.variable_mnsit["y_"]))
		self.variable_mnsit["train_step"] = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
		self.correct_prediction = tf.equal(tf.argmax(self.variable_mnsit["y_conv"],1), tf.argmax(self.variable_mnsit["y_"] ,1))
		self.variable_mnsit["accuracy"] = tf.reduce_mean(tf.cast(self.correct_prediction, tf.float32))
		self.session.run(tf.global_variables_initializer())


	def entrainement(self):
		# Setup loss & Train

		for i in range(1000):
			batch = self.mnist.train.next_batch(50)
			if i%100 == 0:
				train_accuracy = self.variable_mnsit["accuracy"].eval(feed_dict={self.variable_mnsit["x"]:batch[0], self.variable_mnsit["y_"] : batch[1], self.variable_mnsit["keep_prob"] : 1.0})
				print("step %d, training accuracy %g"%(i, train_accuracy))
			self.variable_mnsit["train_step"].run(feed_dict={self.variable_mnsit["x"] : batch[0], self.variable_mnsit["y_"]: batch[1], self.variable_mnsit["keep_prob"]: 0.5})

		batchSize = 5000
		for i in range(len(self.mnist.train.labels) // batchSize):
			bat = self.mnist.test.next_batch(100)
			print("test accuracy %g" % self.variable_mnsit["accuracy"].eval(feed_dict={self.variable_mnsit["x"] : bat[0],  self.variable_mnsit["y_"]: bat[1], self.variable_mnsit["keep_prob"]: 1.0}))




	def test_modele(self, data):
		"""
		methode de classe qui permet de tester le modele
		"""
		if not isinstance(data, ndarray):
			raise TypeError("erreur data = {} n'est pas de type numpy.ndarray ".format(type(data)))			

		result = self.session.run(tf.argmax(self.variable_mnsit["y_conv"],1), feed_dict={self.variable_mnsit["x"]: [data]})
		print ('resultat ', result)



	def sauve_modele(self):
		"""
		methode de class qui permet la sauvegarde des données
		"""
		saver = tf.train.Saver()
		save_path = saver.save(self.session, "modeles/avancer/model_avancer.ckpt")
		print("Model saved in file: %s" % save_path)



	def chargement_modele(self):
		saver = tf.train.Saver()
		with tf.Session() as self.session:
			# Restore variables from disk.
			saver.restore(self.session, "modeles/avancer/model_avancer.ckpt")
			print("Model restored.")

import scipy.ndimage

if __name__ == "__main__":
	version = 1

	#creation et sauvegarde du modele
	if version == 0:
		a = machine_learning_basique()
		print(a.variable_mnsit)
		a.recuperation_donnee_mnist()
		a.creation_modele()
		a.entrainement()
		a.sauve_modele()

		tableau_img = scipy.ndimage.imread("test/0v0.bmp", flatten=True)
		print(tableau_img, shape(tableau_img))

		flatten  = ndarray.flatten(tableau_img)
		print(flatten, shape(flatten))

		data = vectorize(lambda x: 255 - x)(flatten)
		print(data, shape(data))
		a.test_modele(data = data)

	# chargement du modele
	if version == 1:
		a = machine_learning_basique()
		a.creation_modele()
		a.chargement_modele()

		tableau_img = scipy.ndimage.imread("test/0v0.bmp", flatten=True)
		print(tableau_img, shape(tableau_img))

		flatten  = ndarray.flatten(tableau_img)
		print(flatten, shape(flatten))

		data = vectorize(lambda x: 255 - x)(flatten)
		print(data, shape(data))
		a.test_modele(data = data)

	#creation et sauvegarde modele evoluer
	if version == 2:
		a = machine_learning_avancer()
		a.recuperation_donnee_mnist()
		a.creation_modele()
		a.entrainement()
		a.sauve_modele()
		#a.entrainement()

	if version == 3:
		a = machine_learning_avancer()
		a.creation_modele()
		a.chargement_modele()

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

