#!usr/bin/python3.5
#-*-coding:UTF-8 -*
import numpy as np


def tableau(array):
	temp = str("")
	if isinstance(array, list) or isinstance(array, range):
		print("if")	
		for i in range(28):
			for j in range(28):
				temp += " {} ".format(array[i,j])
				if j == 27:
					temp += "\n"
	else:
		print("else")		
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
	#print(tableauv2(i))

	i = np.ones((28,28))
	print (type(i))
	print(tableau(i))
	#print(tableauv2(i))

	i = range(784)
	print (type(i))
	print(tableau(i))