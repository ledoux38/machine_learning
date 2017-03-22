#!usr/bin/python3.5
#-*-coding:UTF-8 -* 

from tkinter import *
from tkinter.filedialog import *
from numpy import *
from functools import partial
from PIL import Image, ImageFont, ImageDraw, ImageTk 
import scipy.ndimage
from Machine_learning import *
from interface_journal import *

class load_image:
	
	#cette classe a pour but de charger des images, ainsi qu'un environement graphique


	def __init__(self, option = {"ch_img":"./test", "h_canvas":100, "l_canvas":100, }):
		
		if not isinstance(option, dict):
			raise TypeError("erreur option = {} n'est pas de type list ".format(type(option)))

		#liste les options
		self.option = option
		self.text = str()
		self.load = None
		self.journal =journal()


	def interface_load_image(self,object_tk):
		"""
		methode de class qui creer l'interface graphique
		"""

		frame_principal = Frame(object_tk)
		frame_principal.grid(row = 0, column = 0, sticky='NSEW')
		label = Label(frame_principal)
		label.grid(row = 0, column = 0)

		frame_bp = Frame(frame_principal)
		frame_bp.grid(row = 1, column = 0, sticky='NSEW')

		bp_charger = Button(frame_bp, text = "Charger",command = partial(self.Charger, label))
		bp_charger.grid(row=0,column=0,sticky='W')

		bp_generer = Button(frame_bp, text = "Generer",command = partial(self.generer))
		bp_generer.grid(row=0,column=1,sticky='W')

		bp_annuler = Button(frame_bp, text = "Fermer",command = partial(self.quitter_interface, object_tk))
		bp_annuler.grid(row=0,column=2,sticky='W')

		#frame_principal.grid_columnconfigure(0,weight=1)
		#frame_principal.grid_rowconfigure(0,weight=0)
		#frame_principal.grid_rowconfigure(1,weight=1)



	def quitter_interface(self, object_tk):
		"""
		methode de class qui permet de quitter le programme
		"""

		object_tk.quit()



	def Charger(self, object_label):
		"""
		methode de class qui permet de reset le canevas
		"""

		self.load = askopenfilename(defaultextension = ".JPG", initialdir = self.option["ch_img"])
		
		if not self.load:
			return None

		else:
			image = Image.open(self.load)  
			self.photo = ImageTk.PhotoImage(image)
			object_label.configure(width =  image.size[0])
			object_label.configure(height = image.size[1])
			object_label.configure(image = self.photo)




	def generer(self):
		self.text += "\n\n lancement \n\n"
		tableau_img = scipy.ndimage.imread(self.load, flatten=True)
		print(tableau_img, shape(tableau_img))
		self.text += "\n\n {} \n\n {} \n\n".format(tableau_img, shape(tableau_img))

		flatten  = ndarray.flatten(tableau_img)
		print(flatten, shape(flatten))
		self.text += "\n\n {} \n\n {} \n\n".format(flatten, shape(flatten))

		data = vectorize(lambda x: 255 - x)(flatten)
		#print("\n\n\n", data, shape(data), type(data))

		#self.text += "\n\n {} \n\n {} \n\n {} \n\n".format((data, shape(data), type(data)))

		machine_learning(donnee = data)

		top = Toplevel(object_tk)
		self.inter_option.interface_option(top)


if __name__ == "__main__":
	limg = load_image()
	app = Tk()
	limg.interface_load_image(app)
	app.mainloop()

