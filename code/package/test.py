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

	def creation_forme(self,event):
		if self.old_position == (0,0):
			self.old_position = (event.x,event.y)

		else:
			i = self.create_line(self.old_position,(event.x,event.y))
			self.old_position = (event.x,event.y)
		print(i,self.coords(i))

		variable_x = self.coords(i)
		variable_x = int(variable_x[0])

		variable_y = self.coords(i)
		variable_y = int(variable_y[1])

		self.tableau[variable_x][variable_y] = 1

		print(variable_x,"  :  ",variable_y)

	def reset_position(self,event):
		self.old_position = (0,0)

	def tout_supprimer(self):
		self.delete(ALL)

	def tableau_numpy(self,event):
		print(self.tableau)
		save("numpy_array.npy",self.tableau)
		print(load("numpy_array.npy"))
			
                
if __name__ == "__main__":
	app = Tk()
	canvas = interface_canvas(app, 10, 10)
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
