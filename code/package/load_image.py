#!usr/bin/python3.5
#-*-coding:UTF-8 -*
 
 
from tkinter import *
from tkinter.filedialog import *
import numpy as np 
from functools import partial
import PIL.Image
import PIL.ImageFont
import PIL.ImageDraw
import PIL.ImageTk
#from PIL import Image, ImageFont, ImageDraw, ImageTk
import scipy.ndimage
from interface_journal import *
from Machine_learning import *

class load_image:
	"""
	cette classe chargent des images
	"""
 
 
	def __init__(self, option = {"ch_img":"./test"}):
		if not isinstance(option, dict):
			raise TypeError("erreur option = {} n'est pas de type list ".format(type(option)))

		#liste les options
		self.option = option
		#ce tableau est rempli lors du chargement de l'image
		self.tableau = None
		self.journal = journal()



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
 
		bp_generer = Button(frame_bp, text = "Generer",command = partial(self.generer, object_tk))
		bp_generer.grid(row=0,column=1,sticky='W')
		
		bp_journal = Button(frame_bp, text = "Journal",command = partial(self.afficher_donnee, object_tk))
		bp_journal.grid(row=0,column=2,sticky='W')
		
		bp_annuler = Button(frame_bp, text = "Fermer",command = partial(self.quitter_interface, object_tk))
		bp_annuler.grid(row=0,column=3,sticky='W')




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

		load = askopenfilename(defaultextension = ".JPG", initialdir = self.option["ch_img"])

		if not load:
			return None
			print("annuler")
		else:
			self.create_data(file_img = load)
			image = PIL.Image.open(load)
			self.img_convert = PIL.ImageTk.PhotoImage(image)
			object_label.configure(image = self.img_convert)



	def afficher_donnee(self, object_tk):
		"""
		methode de class qui permet d'afficher les donnees
		"""
		top = Toplevel(object_tk)
		#les parametres de la fenetre des options
		top.title("journal")
		#j'empeche la fenetre d'etre redimenssionner
		#top.resizable(False, False)
		# affiche le journal
		self.journal.interface_journal(top)

	def generer(self, object_tk):
		"""
		generer tensorflow
		"""
		#self.afficher_donnee(object_tk)
		#self.journal.insert_text("{}".format(self.tableau))
		machine_learning_v3(self.tableau)
		pass

	def create_data(self, file_img):
		"""
		recupere les donnée de l'image
		"""

		#recupation des données
		self.tableau = scipy.ndimage.imread(file_img, flatten=True)
		#si les dimentions des données sont differente de (28,28)
		#je redimentionne le tableau
		print(self.tableau, type(self.tableau), shape(self.tableau))
		if not shape(self.tableau) == (28, 28):
			self.tableau = resize(self.tableau, (28, 28))

		self.tableau  = np.ndarray.flatten(self.tableau)
		print(self.tableau, np.shape(self.tableau))
		
		self.tableau = np.vectorize(lambda x: 255 - x)(self.tableau)
		#affichage des données
		print(self.tableau, type(self.tableau), shape(self.tableau))


if __name__ == "__main__":

	limg = load_image()
	app = Tk()
	limg.interface_load_image(app)
	app.mainloop()