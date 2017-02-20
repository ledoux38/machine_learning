#!usr/bin/python3.5c 
#-*-coding:UTF-8 -*

from tkinter import *

class interface_canvas(Canvas):
	def __init__ (self, parent, hauteur = 48, longueur = 48, outline = "black"):
		Canvas.__init__(self, parent, height = hauteur, width = longueur)

		self.bind("<B1-Motion>", self.creation_forme)
		self.bind("<ButtonRelease>",self.reset_position)
		self.old_position = (0,0)

	def creation_forme(self,event):
		if self.old_position == (0,0):
			self.old_position = (event.x,event.y)

		else:
			self.create_line(self.old_position,(event.x,event.y))
			self.old_position = (event.x,event.y)
		#print(i,self.index(i,0))

	def reset_position(self,event):
		self.old_position = (0,0)

	def tout_supprimer(self):
		self.delete(ALL)

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