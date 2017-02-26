#!usr/bin/python3.5
#-*-coding:UTF-8 -*
from 
from PIL import Image
from PIL import ImageDraw

class save_img:
	"""
	cette classe a pour but de sauvegarder le dessin du canevas de Tkinter
	la classe propose deux solutions de sauvegarde: - Sauvegarde du dessin dans un dossier specifique
													- Sauvegarde dans un fichier temporaire 
	"""
	
	def __init__(default_filename, default_type_img):

		if not isinstance(filename, str):
			raise TypeError("error file is not {} it must be string type ".format(type(filename)))

		if not isinstance(default_type_img, str):
			raise TypeError("error default_type_img is not {} it must be string type ".format(type(default_type_img)))

		"""
		attibut filename qui est le chemin par defaut à afficher
		"""	
		self.filename = default_filename

		"""
		attibut type_img qui est le typage à donner par defaut
		"""			
		self.type_img = default_type_img

	@staticmethod
	def sauv_canvas(canvas, self.filename, self.type_img):

		"""
		verification que l'objet donnée en parametre et bien un canevas
		"""
		if not isinstance(canvas, Canvas):
			raise TypeError("error file is not {} is this str ".format(type(filename)))

		image = Image.new("RGB", (int(self.cget('height')), int(self.cget('width'))), "white")
		draw = ImageDraw.Draw(image)

		for x in self.find_all():
			draw.line((self.coords(x)), fill = "black")
		del draw
		image.save(filename, type_img)

	def sauv_canvas_tmp(type_img):
		pass


if __name__ == "__main__":

	app = Tk()
	canvas = interface_canvas(app)
	canvas.pack()
	app.mainloop()