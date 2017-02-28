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

	def __init__ (self, parent, hauteur = 48, longueur = 48, outline = "black"):
		"""
		initialise la class:
		"""

		Canvas.__init__(self, parent, height = hauteur, width = longueur)

		self.bind("<B1-Motion>", self.creation_forme)
		self.bind("<ButtonRelease>", self.reset_position)
		self.old_position = (0,0)

	def creation_forme(self, event):
		"""
		methode de classe qui creer des lignes dans le canevas
		"""

		if self.old_position == (0,0):
			self.old_position = (event.x, event.y)

		else:
			self.create_line(self.old_position, (event.x,event.y))
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



if __name__ == "__main__":
	app = Tk()
	canvas = interface_canvas(app, 100, 100)
	canvas.pack()

	app.mainloop()
