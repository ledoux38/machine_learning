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
		self.bind("<ButtonRelease>",self.reset_position)
		self.old_position = (0,0)
		
		self.nb_item = 0

	def creation_forme(self,event):
		if self.old_position == (0,0):
			self.old_position = (event.x,event.y)

		else:
			self.nb_item = self.create_line(self.old_position,(event.x,event.y))
			self.old_position = (event.x,event.y)

	def creation_tableau(self):
		pass
		"""
		tableau = zeros((int(self.cget('height')), int(self.cget('width'))),dtype = 'i')
		compteur = 1
		while compteur <= self.nb_item:
			variable_x = self.coords(compteur)
			variable_x = int(variable_x[0])

			variable_y = self.coords(compteur)
			variable_y = int(variable_y[1])

			tableau[variable_x][variable_y] = 1
			#print("id: ", compteur, "x: ", variable_x, "y: ", variable_y, self.tableau[variable_x][variable_y])
			compteur += 1
		"""

	def reset_position(self,event):
		self.old_position = (0,0)

	def tout_supprimer(self):
		self.delete(ALL)
		self.nb_item = 0

	def get_tableau(self):
		tableau = zeros((int(self.cget('height')), int(self.cget('width'))),dtype = 'i')
		compteur = 1
		while compteur <= self.nb_item:
			variable_x = self.coords(compteur)
			variable_x = int(variable_x[0])

			variable_y = self.coords(compteur)
			variable_y = int(variable_y[1])

			tableau[variable_x][variable_y] = 1
			#print("id: ", compteur, "x: ", variable_x, "y: ", variable_y, self.tableau[variable_x][variable_y])
			compteur += 1
		return tableau





if __name__ == "__main__":
	app = Tk()
	canvas = interface_canvas(app, 100, 100)
	canvas.pack()

	app.mainloop()

"""
class interface_canvas(Canvas):
	def __init__ (self, parent, hauteur = 48, longueur = 48):
		Canvas.__init__(self, parent, height = hauteur, width = longueur)

		self.bind("<B1-Motion>", self.creation_forme)

	def creation_forme(self,event):
		i = self.create_rectangle((event.x,event.y),(event.x,event.y),fill = 'black')
		#print(i,self.index(i,0))

	def tout_supprimer(self):
		self.delete(ALL)

if __name__ == "__main__":
	app = Tk()
	canvas = interface_canvas(app, 100, 100)
	canvas.pack()

	app.mainloop()
"""