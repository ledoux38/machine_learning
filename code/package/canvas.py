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


	def image(self):
		"""
		methode de classe qui redessine le canvas dans une image vierge
		"""

		image = Image.new("RGB", (int(self.cget('height')), int(self.cget('width'))), "white")
		draw = ImageDraw.Draw(image)

		for x in self.find_all():
			draw.line((self.coords(x)), fill = "black")
		del draw
		return image


	def sauvegarder(self, obj_image):
		"""
		methode de classe qui sauvegarde le dessin
		"""

		save = asksaveasfilename(defaultextension = '.JPG', initialdir = '/home/ledoux/Images/')
		obj_image.save(save)

	def sauv_canvas_tmp(self, filename, type_img):
		"""
		methode de classe qui permet de sauvegarder temporairement les images
		"""

		pass

if __name__ == "__main__":
	app = Tk()
	canvas = interface_canvas(app, 100, 100)
	canvas.pack()

	app.mainloop()
