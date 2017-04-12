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



class machine_learning_avancer:

	def __init__ (self, option = {"ch_mnist": "./MNIST_data", "ch_model_avancer": "modeles/avancer/model_avancer.ckpt"}):
		if not isinstance(option, dict):
			raise TypeError("erreur option = {} n'est pas de type dict ".format(type(option)))

		self.option = option
		self.session = None
		self.x = None
		self.y_conv = None
		self.mnist = None
		self.keep_prob = None

		self.init_machine_learning()



	def init_machine_learning(self):
		"""
		methode de class qui initialise la creation du modele et sont entrainement 
		"""
		try:
			print("debut du chargement! ")

			self.x = tf.placeholder(tf.float32, [None, 784])

			self.session = tf.Session()
			new_saver = tf.train.import_meta_graph("./modeles/avancer/model_avancer.meta")
			new_saver.restore(self.session, tf.train.latest_checkpoint('./'))
			all_vars = tf.get_collection('vars')

			#self.y_conv = all_vars[3]
			#self.keep_prob = all_vars[4]

			#for v in all_vars:
			#	v_ = self.session.run(v)
			#	print(v_)

			print("chargement terminer")
			
		except:
			
			print("le chargement a echouer ! \n creation d'un nouveau modele !")
			self.mnist  = input_data.read_data_sets(self.option["ch_mnist"], one_hot=True)

			self.session = tf.InteractiveSession()
			#creation des variables
			W_conv1 = self.weight_variable([5, 5, 1, 32])
			b_conv1 = self.bias_variable([32])

			# Placeholder
			self.x = tf.placeholder(tf.float32, [None, 784])
			y_ = tf.placeholder(tf.float32, [None, 10])

			# Reshape
			x_image = tf.reshape(self.x , [-1,28,28,1])

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
			
			self.keep_prob = tf.placeholder(tf.float32)
			h_fc1_drop = tf.nn.dropout(h_fc1, self.keep_prob)

			W_fc2 = self.weight_variable([1024, 10])
			b_fc2 = self.bias_variable([10])

			self.y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2


					
			cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(self.y_conv, y_))
			train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
			correct_prediction = tf.equal(tf.argmax(self.y_conv,1), tf.argmax(y_ ,1))
			accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
			self.session.run(tf.global_variables_initializer())

			print("sauvegarde variable")
			tf.add_to_collection("vars", h_fc1_drop)
			tf.add_to_collection("vars", W_fc2)
			tf.add_to_collection("vars", b_fc2)
			tf.add_to_collection("vars", self.y_conv)
			tf.add_to_collection("vars", self.keep_prob)

			print("lancement antrainement modele")
			
			for i in range(1000):
				batch = self.mnist.train.next_batch(50)
				if i%100 == 0:
					train_accuracy = accuracy.eval(feed_dict={self.x : batch[0], y_ : batch[1],  self.keep_prob : 1.0})
					print("step %d, training accuracy %g"%(i, train_accuracy))
				train_step.run(feed_dict={self.x : batch[0], y_ : batch[1],  self.keep_prob: 0.5})

			batchSize = 5000
			for i in range(len(self.mnist.train.labels) // batchSize):
				bat = self.mnist.test.next_batch(100)
				print("test accuracy %g" % accuracy.eval(feed_dict={self.x : bat[0], y_: bat[1],  self.keep_prob: 1.0}))
			
			#sauvegarde des données
			saver = tf.train.Saver()
			save_path = saver.save(self.session, "./modeles/avancer/model_avancer")
			print("Model saved in file: %s" % save_path)
			


	def test_modele(self, data):
		"""
		methode de classe qui permet de tester le modele
		"""
		if not isinstance(data, ndarray):
			raise TypeError("erreur data = {} n'est pas de type numpy.ndarray ".format(type(data)))			

		#result = self.session.run(tf.argmax(self.variable_mnsit["y_conv"],1), feed_dict={self.variable_mnsit["x"]: [data]})
		[tableau_pourcent, result] = self.session.run([self.y_conv, tf.argmax(self.y_conv, 1)], feed_dict={self.x : [data], self.keep_prob: 1.0})
		print ("l'ordinateur voit un ... {}", result)
		print ("tableaux:  {}".format(tableau_pourcent))


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









if __name__ == "__main__":
	import scipy.ndimage
	from PIL import Image
	version = 2

	#creation et sauvegarde du modele
	if version == 0:

		sess, x, y = restauration_modele()
		mnist = input_data.read_data_sets("./MNIST_data", one_hot=True)
		ud.print_array(mnist.test.images[0])

		result2 = sess.run(tf.argmax(y,1), feed_dict={x: [mnist.test.images[0]]})
		print ('resultat ', result2)


	if version == 1:
		sess, x, y = mlb("./MNIST_data")

		chiffre = Image.open("test/0v1.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		ud.print_array_convert(data)
		result2 = sess.run(tf.argmax(y,1), feed_dict={x: [data]})
		print ('resultat ', result2)

		
		chiffre = Image.open("test/0v2.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		ud.print_array_convert(data)
		result2 = sess.run(tf.argmax(y,1), feed_dict={x: [data]})
		print ('resultat ', result2)

		chiffre = Image.open("test/0v3.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		ud.print_array_convert(data)
		result2 = sess.run(tf.argmax(y,1), feed_dict={x: [data]})
		print ('resultat ', result2)

		chiffre = Image.open("test/0v4.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		ud.print_array_convert(data)
		result2 = sess.run(tf.argmax(y,1), feed_dict={x: [data]})
		print ('resultat ', result2)

		chiffre = Image.open("test/0v5.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		ud.print_array_convert(data)
		result2 = sess.run(tf.argmax(y,1), feed_dict={x: [data]})
		print ('resultat ', result2)

	if version == 2:

		a = machine_learning_avancer()
		
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
		
		"""
		
		chiffre = Image.open("test/1v1.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/1v2.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/1v3.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/1v4.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/1v5.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)



		chiffre = Image.open("test/2v1.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/2v2.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/2v3.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/2v4.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/2v5.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)



		chiffre = Image.open("test/3v1.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/3v2.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/3v3.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/3v4.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/3v5.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)


		chiffre = Image.open("test/4v1.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/4v2.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/4v3.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/4v4.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/4v5.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)


		chiffre = Image.open("test/5v1.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/5v2.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/5v3.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/5v4.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/5v5.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)


		print("procedure de test epaisseur 10")

		chiffre = Image.open("test/0v10.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/1v10.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)	

		
		chiffre = Image.open("test/2v10.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)	

		chiffre = Image.open("test/3v10.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)	

		chiffre = Image.open("test/4v10.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)
		
		chiffre = Image.open("test/5v10.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)	

		chiffre = Image.open("test/6v10.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)	

		
		chiffre = Image.open("test/7v10.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/8v10.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)

		chiffre = Image.open("test/9v10.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data)
		"""

