#!usr/bin/python3.5c 
#-*-coding:UTF-8 -*

from tkinter import *
from numpy import *


class interface_canvas(Canvas):
	def __init__ (self, parent, hauteur = 48, longueur = 48, outline = "black"):
		Canvas.__init__(self, parent, height = hauteur, width = longueur)

		self.canvas_hauteur = hauteur
		self.canvas_longueur = longueur

		self.bind("<B1-Motion>", self.creation_forme)
		self.bind("<ButtonRelease>", self.reset_position)
		self.old_position = (0,0)
		
		self.nb_item = 0

	def creation_forme(self, event):
		if self.old_position == (0,0):
			self.old_position = (event.x, event.y)

		else:
			self.nb_item = self.create_line(self.old_position, (event.x,event.y), capstyle = 'round')
			self.old_position = (event.x, event.y)


	def reset_position(self, event):
		self.old_position = (0,0)

	def tout_supprimer(self):
		self.delete(ALL)
		self.nb_item = 0

	def get_tableau(self):
		tableau = zeros((int(self.cget('height')), int(self.cget('width'))), dtype = 'i')
		compteur = 1
		while compteur <= self.nb_item:
			variable_x = self.coords(compteur)
			variable_x = int(variable_x[0])

			variable_y = self.coords(compteur)
			variable_y = int(variable_y[1])

			tableau[variable_x][variable_y] = 1
			compteur += 1
		return tableau

	def sauvegarde_canvas(self, filename):

		if not isinstance(filename, str):
			raise TypeError("error file is not {} is this str ".format(type(filename)))

		self.postscript(file="fichier.ps")



if __name__ == "__main__":
	app = Tk()
	canvas = interface_canvas(app, 100, 100)
	canvas.pack()

	app.mainloop()
