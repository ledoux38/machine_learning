#!usr/bin/python3.5
#-*-coding:UTF-8 -*

class Main_class:
	"""classe qui permet la recuperation de donnée ou de status des attributs"""
	def __init__(self):
		"""constructeur de la classe"""
		self._donnee = str()

	def _set_log(self,text):
		if not isinstance(text,str):
			raise TypeError("erreur parametre n'est pas de type str")
		self._donnee += text + "\n"

	def _get_log(self):
		return self._donnee

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