#!usr/bin/python3.5
#-*-coding:UTF-8 -*

from tkinter import *

class interface_canvas(Canvas):
	def __init__ (self, parent, hauteur, longueur):
		Canvas.__init__(self, parent, height = hauteur, width = longueur)

		self.bind("<B1-Motion>", self.creation_forme)

	def creation_forme(self,event):
		self.create_rectangle((event.x,event.y),(event.x,event.y),fill = 'black')

	def tout_supprimer(self):
		pass

if __name__ == "__main__":
	app = Tk()
	canvas = interface_canvas(app, 100, 100)
	canvas.pack()

	app.mainloop()
