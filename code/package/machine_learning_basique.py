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

try:
	import package.utilitaire_debug as ud
except:
	import utilitaire_debug as ud

class machine_learning_basique:

	def __init__ (self, option = {"ch_mnist": "./MNIST_data"}):

		if not isinstance(option, dict):
			raise TypeError("erreur option = {} n'est pas de type dict ".format(type(option)))

		self.option = option
		self.session = None
		self.x = None
		self.y = None
		self.mnist = None

		self.init_machine_learning()


	def test_modele(self, data):
		"""
		methode de classe qui permet de tester le modele
		"""
		if not isinstance(data, ndarray):
			raise TypeError("erreur data = {} n'est pas de type numpy.ndarray ".format(type(data)))	

		ud.print_array_convert(data)
		result2 = self.session.run(tf.argmax(self.y,1), feed_dict={self.x: [data]})
		print ('resultat ', result2)


	def init_machine_learning(self):
		"""
		methode de class qui initialise la creation du modele et sont entrainement 
		"""
		self.mnist  = input_data.read_data_sets(self.option["ch_mnist"], one_hot=True)
		self.x = tf.placeholder(tf.float32, [None, 784], name="x")
		W = tf.Variable(tf.zeros([784, 10]), name="W")
		b = tf.Variable(tf.zeros([10]), name="b")
		self.y  = tf.matmul(self.x, W, name="y") + b
		y_ = tf.placeholder(tf.float32, [None, 10], name="y_")

		cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y_, logits = self.y ), name="cross_entropy")
		train_step = tf.train.GradientDescentOptimizer(0.5,  name="train_step").minimize(cross_entropy)

		saver = tf.train.Saver()
		self.session = tf.Session()

		print("debut du chargement! ")

		try:
			saver.restore(self.session, "./modeles/basique/model_basique.ckpt")

		except:
			#creation d'un nouveau fichier
			print("le chargement a echouer ! \n creation d'un nouveau modele !")

			init_op = tf.global_variables_initializer()
			self.session.run(init_op)

			#entrainement du modele
			for _ in range(1000):
				batch_xs, batch_ys = self.mnist .train.next_batch(100)
				self.session.run(train_step, feed_dict={self.x: batch_xs, y_: batch_ys})

			# verification de l'entrainement du modele
			correct_prediction = tf.equal(tf.argmax(self.y , 1), tf.argmax(y_, 1))
			accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
			print(self.session.run(accuracy, feed_dict={self.x: self.mnist .test.images, y_: self.mnist .test.labels}))		

			#sauvegarde des données
			save_path = saver.save(self.session, "./modeles/basique/model_basique.ckpt")
			print("Model saved in file: %s" % save_path)

		print("chargement terminer")



if __name__ == "__main__":
	import scipy.ndimage
	from PIL import Image
	version = 2

	#creation et sauvegarde du modele

	if version == 2:

		a = machine_learning_basique()
		
		chiffre = Image.open("test/0v1.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)


		
		chiffre = Image.open("test/0v2.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/0v3.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/0v4.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/0v5.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)