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
		self.bind("<ButtonRelease>", self.reset_position)
		self.old_position = (0,0)

	def creation_forme(self, event):
		if self.old_position == (0,0):
			self.old_position = (event.x, event.y)

		else:
			self.create_line(self.old_position, (event.x,event.y))
			self.old_position = (event.x, event.y)


	def reset_position(self, event):
		self.old_position = (0,0)

	def tout_supprimer(self):
		self.delete(ALL)


	def sauv_canvas(self, filename, type_img):

		if not isinstance(filename, str):
			raise TypeError("error file is not {} is this str ".format(type(filename)))

		image = Image.new("RGB", (int(self.cget('height')), int(self.cget('width'))), "white")
		draw = ImageDraw.Draw(image)

		for x in self.find_all():
			draw.line((self.coords(x)), fill = "black")
		del draw
		image.save(filename, type_img)

	def sauv_canvas_tmp(self, filename, type_img):


if __name__ == "__main__":
	app = Tk()
	canvas = interface_canvas(app, 100, 100)
	canvas.pack()

	app.mainloop()
