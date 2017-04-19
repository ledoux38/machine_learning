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
import tkinter as Tk

try:
	import package.utilitaire_debug as ud
except:
	import utilitaire_debug as ud

try:
	import package.resultat as rt
except:
	import resultat as rt

class machine_learning_avancer:

	def __init__ (self, option = {"ch_mnist": "./MNIST_data"}):
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
		self.mnist  = input_data.read_data_sets(self.option["ch_mnist"], one_hot=True)


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


		self.session = tf.InteractiveSession()
		saver = tf.train.Saver()
		print("debut du chargement! ")

		try:

			saver.restore(self.session, "./modeles/avancer/model_avancer.ckpt")
		except:
			
			print("le chargement a echouer ! \n creation d'un nouveau modele !")

			print("initialisation entrainement modele")
			self.session.run(tf.global_variables_initializer())

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
			

			save_path = saver.save(self.session, "./modeles/avancer/model_avancer.ckpt") #sauvegarde des données
			print("Model saved in file: %s" % save_path)

		print("chargement terminer")



	def test_modele(self, data, object_tk):
		"""
		methode de classe qui permet de tester le modele
		"""
		if not isinstance(data, ndarray):
			raise TypeError("erreur data = {} n'est pas de type numpy.ndarray ".format(type(data)))			

		#result = self.session.run(tf.argmax(self.variable_mnsit["y_conv"],1), feed_dict={self.variable_mnsit["x"]: [data]})
		[tableau_pourcent, result] = self.session.run([self.y_conv, tf.argmax(self.y_conv, 1)], feed_dict={self.x : [data], self.keep_prob: 1.0})

		texte = "Le resultat vue par l'ordinateur: {} \n tableau recapitulatif: \n".format(result)
		for i , y in enumerate(tableau_pourcent[0]):
			texte += "[{}] -----> {}% \n".format(i,y*10)

		self.ouvrir_affichage_resultat(object_tk, data, texte, tableau = tableau_pourcent[0])


	def ouvrir_affichage_resultat(self, object_tk, data, texte, tableau):
		"""
		methode de class qui permet d'afficher les resultats
		"""
		a = rt.resultat()

		if object_tk == None:
			
			app = Tk.Tk()
			a.interface_resultat(object_tk = app, data = data, tableau = tableau)
			a.insert_text(str(texte))
			app.title("Resultat")
			app.resizable(False, False)
			app.mainloop()
		else:

			#je creer une fenetre pour inserer la frame de options
			top = Tk.Toplevel(object_tk)
			#les parametres de la fenetre des options
			top.title("Resultat")
			#je fais apparaître la fenetre enfant sur la fenetre parent
			top.transient(object_tk)
			#la fenêtre principale est bloquée par grab_set rend la fenêtre "modale"
			top.grab_set()
			#focus_set permet d'attraper les évènements sur la fenêtre principale
			top.focus_set()
			#j'empeche la fenetre d'etre redimenssionner
			top.resizable(False, False)
			# je fais toutes les modifications dont j'ai besoins
			a.interface_resultat(object_tk = top, data = data, tableau = tableau)
			a.insert_text(str(texte))
			#pandant ce temps interface_principale et mit en pause
			object_tk.wait_window(top)
			#quand j'en n'ai fini avec les options je charge les nouvelles données



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
	version = 3

	if version == 1:
		a = machine_learning_avancer()
		a.creation_modele()
		a.chargement_modele()
		
		#tableau_img = scipy.ndimage.imread("test/0v0.bmp", flatten=True)
		chiffre = Image.open("test/1v0.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		plt.matshow(tf.reshape(data,(28, 28)).eval())
		plt.show()

		a.test_modele(data = data)
		

	if version == 2:
		a = machine_learning_avancer()
		a.init_machine_learning()
		
		#tableau_img = scipy.ndimage.imread("test/0v0.bmp", flatten=True)

		chiffre = Image.open("test/0v1.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data = data)

		chiffre = Image.open("test/0v2.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data = data)

		chiffre = Image.open("test/0v3.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data = data)

		chiffre = Image.open("test/0v4.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data = data)

		chiffre = Image.open("test/0v5.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data = data)




		chiffre = Image.open("test/1v1.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data = data)

		chiffre = Image.open("test/1v2.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data = data)

		chiffre = Image.open("test/1v3.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data = data)

		chiffre = Image.open("test/1v4.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data = data)

		chiffre = Image.open("test/1v5.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255
		a.test_modele(data = data)

		#plt.matshow(tf.reshape(data,(28, 28)).eval())
		#plt.show()


	if version == 3:
		u = [[-2.63639092,  2.91137624,  0.58372426,  3.49859715,  4.58603239, -4.23958731
  -4.01916981,  1.08883286,  0.56773269,  2.38709688]]
		texte = "Le resultat vue par l'ordinateur:  \n tableau recapitulatif: \n"
		print(u)
		for i , y in enumerate(u[0]):
			print("coucou")
			texte += "[{}] -----> {}% \n".format(i,y)

	print(texte)