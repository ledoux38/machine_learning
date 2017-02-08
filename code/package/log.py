#!usr/bin/python3.5
#-*-coding:UTF-8 -*

class Main_class:
	"""classe qui permet la recuperation de donnée ou de status des attributs"""
	def __init__(self):
		"""constructeur de la classe"""

	def _set_log(self,text):
		if not isinstance(text,str):
			raise TypeError("erreur parametre n'est pas de type str")
		text += "\n"
		with open('./journal/fichier.txt', 'a') as mon_fichier:
			mon_fichier.write(text)

	def _get_log(self):
		with open('./journal/fichier.txt', 'r') as mon_fichier:
			texte = mon_fichier.read()
		return texte

	donnee = property(_get_log,_set_log)



"""
class Test(Main_class):
	def __init__(self):
		Main_class.__init__(self)
		self.text = str()

	def ecriture(self):
		i = 0

		while(i<10):
			text = input()
			self._set_log(text)
			i += 1


a = Test()
a.ecriture()
print(a._get_log())
"""