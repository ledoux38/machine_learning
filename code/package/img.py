#!usr/bin/python3.5
#-*-coding:UTF-8 -*
from tkinter.filedialog import *
from tkinter import Canvas
from PIL import Image
from PIL import ImageDraw


class img:
	"""
	cette classe a pour but de sauvegarder le dessin du canevas de Tkinter
	la classe propose via les methodes : - cree un dessin via les item du canevas ( init )
										 - Sauvegarde du dessin dans un dossier specifique
										 - Sauvegarde dans un fichier temporaire 
	"""
	
	def __init__(self, obj_canvas = None, list_option = ['/home/ledoux/Images/', '.JPG']):
		"""
		if not isinstance(obj_canvas, Canvas):
			raise TypeError("erreur obj_canvas = {} n'est pas de type Canvas ".format(type(obj_canvas)))
		"""
		if not isinstance(list_option, list):
			raise TypeError("erreur option = {} n'est pas de type list ".format(type(list_option)))


		self.option = list_option
		"""
		liste les options données: [0] chemin par defauts
								   [1] type par defauts
		"""
		if obj_canvas is None:
			self._image = None
		else:
			self._image = self.creation_image(obj_canvas)
		"""
		creation d'une image pillow vierge
		"""
	
	def creation_image(self, obj_canvas):
		"""
		creer une image via pillow
		"""

		if not isinstance(obj_canvas, Canvas):
			raise TypeError("erreur obj_canvas = {} n'est pas de type Canvas ".format(type(obj_canvas)))

		"""
		creation d'une image pillow vierge
		"""
		image = Image.new("RGB", (int(obj_canvas.cget('height')), int(obj_canvas.cget('width'))), "white")
		draw = ImageDraw.Draw(image)
		
		""" 
		ecriture sur l'image pillow
		"""
		for x in obj_canvas.find_all():
			draw.line((obj_canvas.coords(x)), fill = "black")

		del draw
		return image
	
	def _get_image(self):
		"""
		retourne l'image 
		"""
		return self._image

	def _set_image(self, obj_canvas):
		"""
		modification de l'image 
		"""
		if not isinstance(obj_canvas, Canvas):
			raise TypeError("erreur obj_canvas = {} n'est pas de type Canvas ".format(type(obj_canvas)))

		self._image = self.creation_image(obj_canvas)

	def sauv_img(self):
		"""
		proposition a l'utilisateur de sauvegarder sont image
		"""
		
		save = asksaveasfilename(defaultextension = self.option[1], initialdir = self.option[0])
		"""
		si sauvegarde annuler alors return sinon sauvegarde
		"""

		if not save:
			return None
		else:
			self.image.save(save)
			return save



	def get_data(self):
		"""
		methode de classe qui retourne une list de l'image
		"""

		return list(self._image.getdata())

	image = property(_get_image, _set_image)

from canvas import *
if __name__ == "__main__":

	
	app = Tk()
	appcanvas = interface_canvas(app, hauteur = 5, longueur = 5)
	appcanvas.create_line(0, 0, 4, 4)
	im = img(appcanvas)
	i = im.get_data()
	print(i)
	appcanvas.pack()
	app.mainloop()
	

	"""
	image = Image.new("RGB", (10,10), "white")
	draw = ImageDraw.Draw(image)
	draw.line((0,0,9,9), fill = "black")
	del draw
	print(image)
	i = list(image.getdata())
	print(i)
	"""
