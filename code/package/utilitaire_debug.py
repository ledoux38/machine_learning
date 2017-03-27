#!usr/bin/python3.5
#-*-coding:UTF-8 -*
import numpy as np


def tableau(array):
	temp = str("")

	#si c'est une list ou un range
	if isinstance(array, list) or isinstance(array, range):
		redim = np.reshape(array, (28, 28))
		for i,u in enumerate(redim):
			for j,k in enumerate(redim[i]):
				temp += " {} ".format(redim[i,j])
			temp += "\n"

	#sinon si array et un tableau de numpy
	elif isinstance(array, np.ndarray):	
		for i,u in enumerate(array):
			for j,k in enumerate(array[i]):
				temp += " {} ".format(array[i,j])
			temp += "\n"
	return temp




def tableauv2(array):
	temp = str("")
	if isinstance(array, list):
		for i in range(28):
			for j in range(28):
				temp += " {} ".format(array[i,j])
				if j == 27:
					temp += "\n"

	else:
		#redim = reshape(data, (28, 28))
		for i,u in enumerate(array):
			temp += " {} ".format(array[i])
			temp += "\n"
	
	return temp



if __name__ == "__main__":
	i = np.eye(28)
	print (type(i))
	print(tableau(i))

	i = np.ones((28,28))
	print (type(i))
	print(tableau(i))

	i = range(784)
	print (type(i))
	print(tableau(i))

	i = list()
	temp = 0
	while temp < 784:
		i.append(temp)
		temp += 1

	print (type(i))
	print(tableau(i))