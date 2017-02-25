#!usr/bin/python3.5
#-*-coding:UTF-8 -*


from tkinter import *
from numpy import *
from PIL import Image
from PIL import ImageDraw



class interface_canvas(Canvas):
	def __init__ (self, parent, hauteur = 48, longueur = 48, outline = "black"):
		Canvas.__init__(self, parent, height = hauteur, width = longueur)

		self.bind("<B1-Motion>", self.creation_forme)
		self.bind("<ButtonRelease>",self.reset_position)
		self.bind("<ButtonPress-3>",self.sauvegarde_image)
		self.old_position = (0,0)
		self.tableau = zeros((hauteur,longueur),dtype = 'i')
		self.nb_item = 0

	def creation_forme(self,event):
		if self.old_position == (0,0):
			self.old_position = (event.x,event.y)

		else:
			self.nb_item = self.create_line(self.old_position,(event.x,event.y), capstyle = 'round')
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

	def sauvegarde_image(self,event):
		image = Image.new("RGB", (int(self.cget('height')), int(self.cget('width'))), "white")
		draw = ImageDraw.Draw(image)

		for x in self.find_all():
			draw.line((self.coords(x)), fill = "black")
			print(x, " : ", self.coords(x))
		del draw
		image.save("trace.png", "PNG")
			
if __name__ == "__main__":

	app = Tk()
	canvas = interface_canvas(app)
	canvas.pack()
	app.mainloop()
