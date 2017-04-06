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

class machine_learning_basique:

	def __init__ (self, option = {"ch_mnist": "./MNIST_data", 
									"ch_model_basique": "modeles/basique/model_basique.ckpt"}):

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
		save_path = saver.save(self.session, self.option["ch_model_basique"])
		print("Model saved in file: %s" % save_path)



	def chargement_modele(self):
		saver = tf.train.Saver()
		# Restore variables from disk.
		saver.restore(self.session, self.option["ch_model_basique"])
		print("Model restored.")





if __name__ == "__main__":
	import scipy.ndimage
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
