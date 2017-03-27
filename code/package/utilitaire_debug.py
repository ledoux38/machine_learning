#!usr/bin/python3.5
#-*-coding:UTF-8 -*
import numpy as np


def print_array(array):
	"""
	fonction qui permet de creer un print du tableau modifié sans retour a la ligne
	"""
	try:

		temp = str("")

		#si c'est une list ou un range
		if isinstance(array, list) or isinstance(array, range):
			#je le redimensionne en tableau 2D
			array = np.reshape(array, (28, 28))
			#apres j'enregistre les données
			for i,u in enumerate(array):
				for j,k in enumerate(array[i]):
					if array[i,j] < 10:
						temp += "   {} ".format(array[i,j])
					elif array[i,j] > 10 and array[i,j] <100:
						temp += "  {} ".format(array[i,j])
					else:
						temp += " {} ".format(array[i,j])
				temp += "\n"
			return temp

		#sinon si array et un tableau de numpy
		if isinstance(array, np.ndarray):
			if not np.shape(array) == (28,28):
				print("non")
				array = np.reshape(array, (28, 28))
			for i,u in enumerate(array):
				for j,k in enumerate(array[i]):
					temp += " {} ".format(array[i,j])
				temp += "\n"
		return temp

	except:
		print("erreur!! affichage standard", type(array))
		print(array)

def print_array_convert(array, valeur1 = "#", valeur2 = " "):
	array = np.reshape(array, (28, 28))
	for i in range(28):
		for j in range(28):
			print(valeur1 if array[i,j] == 1 else valeur2, end= "")
		print("")



if __name__ == "__main__":
	i = np.eye(28, dtype = np.float64)
	print (type(i))
	print(print_array(i))

	i = np.ones((28,28), dtype = np.float64)
	print (type(i))
	print(print_array(i))

	i = range(784)
	print (type(i))
	print(print_array(i))

	i = list()
	temp = 0
	while temp < 784:
		i.append(temp)
		temp += 1

	print (type(i))
	print(print_array(i))


	i = np.ones((784), dtype = np.float64)
	print (type(i))
	print(print_array(i))
