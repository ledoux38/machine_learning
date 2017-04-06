#!usr/bin/python3.5
#-*-coding:UTF-8 -*

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


class machine_learning_avancer:

	def __init__ (self, option = {"ch_mnist": "./MNIST_data", "ch_model_avancer": "modeles/avancer/model_avancer.ckpt"}):
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

		#result = self.session.run(tf.argmax(self.variable_mnsit["y_conv"],1), feed_dict={self.variable_mnsit["x"]: [data]})
		[tableau_pourcent, result] = self.session.run([self.variable_mnsit["y_conv"], tf.argmax(self.variable_mnsit["y_conv"],1)], feed_dict={self.variable_mnsit["x"]: [data], self.variable_mnsit["keep_prob"]: 1.0})
		print ("l'ordinateur voit un ... {}", result)
		print ("tableaux:  {}".format(tableau_pourcent))



	def sauve_modele(self):
		"""
		methode de class qui permet la sauvegarde des données
		"""
		saver = tf.train.Saver()
		save_path = saver.save(self.session, self.option["ch_model_avancer"])
		print("Model saved in file: %s" % save_path)



	def chargement_modele(self):
		saver = tf.train.Saver()
		# Restore variables from disk.
		saver.restore(self.session, self.option["ch_model_avancer"])
		print("Model restored.")




if __name__ == "__main__":
	import scipy.ndimage
	from PIL import Image
	version = 2

	#creation et sauvegarde modele evoluer
	if version == 1:
		a = machine_learning_avancer()
		a.recuperation_donnee_mnist()
		a.creation_modele()
		a.entrainement()
		a.sauve_modele()
		#a.entrainement()

	if version == 2:
		a = machine_learning_avancer()
		a.creation_modele()
		a.chargement_modele()
		
		#tableau_img = scipy.ndimage.imread("test/0v0.bmp", flatten=True)
		chiffre = Image.open("test/0v0.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		plt.matshow(tf.reshape(data,(28, 28)).eval())
		plt.show()

		a.test_modele(data = data)
		
