#!usr/bin/python3.5
#-*-coding:UTF-8 -*



from tkinter import *
from numpy import *

class interface_canvas(Canvas):
	def __init__ (self, parent, hauteur = 48, longueur = 48, outline = "black"):
		Canvas.__init__(self, parent, height = hauteur, width = longueur)

		self.bind("<B1-Motion>", self.creation_forme)
		self.bind("<ButtonRelease>",self.reset_position)
		self.bind("<ButtonPress-3>",self.tableau_numpy)
		self.old_position = (0,0)
		self.tableau = zeros((hauteur,longueur),dtype = 'i')
		self.nb_item = 0

	def creation_forme(self,event):
		if self.old_position == (0,0):
			self.old_position = (event.x,event.y)

		else:
			self.nb_item = self.create_line(self.old_position,(event.x,event.y))
			self.old_position = (event.x,event.y)
		print(self.nb_item,self.coords(self.nb_item))

	def reset_position(self,event):
		self.old_position = (0,0)

	def tout_supprimer(self):
		self.delete(ALL)

	def creation_tableau(self):

		tableau = zeros((int(self.cget('height')), int(self.cget('width'))),dtype = 'i')
		compteur = 1
		while compteur <= self.nb_item:
			variable_x = self.coords(compteur)
			variable_x = int(variable_x[0])

			variable_y = self.coords(compteur)
			variable_y = int(variable_y[1])

			tableau[variable_x][variable_y] = 1
			print("id: ", compteur, "x: ", variable_x, "y: ", variable_y, tableau[variable_x][variable_y])
			compteur += 1

	def tableau_numpy(self,event):
		set_printoptions(threshold = nan)
		self.creation_tableau()
		print(self.tableau)
#		save("numpy_array.npy",self.tableau)
#		print(load("numpy_array.npy"))
	
			
                
if __name__ == "__main__":
	app = Tk()
	canvas = interface_canvas(app, 50, 50)
	canvas.pack()

	app.mainloop()

"""
from tkinter import *
from numpy import *
i = [5.0, 5.0, 22.0, 20.0]
variable_x = i
variable_x = int(variable_x[0])
variable_y = i
variable_y = int(variable_y[1])


tableau = zeros((10,10),dtype = 'f')
tableau[variable_x][variable_y] = 1

print(tableau)
"""
