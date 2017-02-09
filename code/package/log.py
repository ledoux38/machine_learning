#!usr/bin/python3.5
#-*-coding:UTF-8 -*
	
class Log:
	"""classe qui permet la recuperation de donnée ou de status des attributs"""
	@staticmethod
	def set_log(text):
		if not isinstance(text,str):
			raise TypeError("erreur parametre n'est pas de type str")
		text += "\n"
		with open('./journal/fichier.txt', 'a') as mon_fichier:
			mon_fichier.write(text)

	def get_log():
		with open('./journal/fichier.txt', 'r') as mon_fichier:
			texte = mon_fichier.read()
		return texte



"""

class Log:

	def __init__(self):

        @staticmethod
	def set_log(self,text):
		if not isinstance(text,str):
			raise TypeError("erreur parametre n'est pas de type str")
		text += "\n"
		with open('./journal/fichier.txt', 'a') as mon_fichier:
			mon_fichier.write(text)

	def get_log(self):
		with open('./journal/fichier.txt', 'r') as mon_fichier:
			texte = mon_fichier.read()
		return texte


Log.set_log("test")
print(Log.get_log())

"""
