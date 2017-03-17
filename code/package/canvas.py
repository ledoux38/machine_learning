#!usr/bin/python3.5
#-*-coding:UTF-8 -*

from tkinter.filedialog import *
from tkinter import *
from numpy import *
from PIL import Image
from PIL import ImageDraw



class interface_canvas(Canvas):
	"""
	canvas personaliser pour dessiner des lignes
	"""

	def __init__ (self, parent, outline = "black", option = {"ch_img":"./img", "ch_log":"./log/activity.log", "h_canvas":18, "l_canvas":18, "e_t_canvas":1}):
		"""
		initialise la class:
		"""
		self.option = option

		# je creer un canvas et je lui donne en parametre  les valeurs des options
		Canvas.__init__(self, parent, height = self.option["h_canvas"], width = self.option["l_canvas"])

		
		self.bind("<B1-Motion>", self.creation_forme)
		self.bind("<ButtonRelease>", self.reset_position)
		self.old_position = (0,0)



	def __repr__(self):
		"""
		methode de classe qui permet l'affichage dans l'interpréteur
		"""
		items = str()
		for x in self.find_all():
			items += "{}: {} \n".format(x,self.coords(x))

		return items



	def __str__(self):
		"""
		methode de classe qui permet l'affichage via le print
		"""

		items = str()
		for x in self.find_all():
			items += "{}: {} \n".format(x,self.coords(x))

		return 	items



	def creation_forme(self, event):
		"""
		methode de classe qui creer des lignes dans le canevas
		"""

		if self.old_position == (0,0):
			self.old_position = (event.x, event.y)

		else:
			self.create_line(self.old_position, (event.x,event.y), width = self.option["e_t_canvas"], capstyle = "round",  joinstyle = "round" )
			self.old_position = (event.x, event.y)



	def reset_position(self, event):
		"""
		methode de classe qui reset la derniere position de la souris lors du tracage de la ligne
		"""

		self.old_position = (0,0)



	def tout_supprimer(self):
		"""
		methode de classe qui supprime tout les items
		"""

		self.delete(ALL)



	def set_canvas(self, nouv_option):
		"""
		modifie les attributs du canvas
		"""

		if not isinstance(nouv_option, dict):
			raise TypeError("erreur option = {} n'est pas de type dict ".format(type(nouv_option)))

		self.configure(height = nouv_option['h_canvas'])
		self.configure(width = nouv_option['l_canvas'])




if __name__ == "__main__":
	
	option = dict()
	option["h_canvas"] = 35
	option["l_canvas"] = 35
	option["e_t_canvas"] = 1

	app = Tk()
	canvas = interface_canvas(app, option = option)
	canvas.create_line(0,0,30,30)

	option = dict()
	option["h_canvas"] = 100
	option["l_canvas"] = 100
	option["e_t_canvas"] = 1

	canvas.set_canvas(option)

	canvas.pack()
	print(canvas)
	app.mainloop()
