#!usr/bin/python3.5
#-*-coding:UTF-8 -*
 
import tkinter as Tk
import tkinter.filedialog as fd
import numpy as np 
from functools import partial
import PIL.Image
import PIL.ImageFont
import PIL.ImageDraw
import PIL.ImageTk
#from PIL import Image, ImageFont, ImageDraw, ImageTk
import scipy.ndimage


try:
	import package.journal as Ij
except:
	import journal as Ij

try:
	import package.machine_learning_basique as Mgb
except:
	import machine_learning_basique as Mgb

try:
	import package.machine_learning_avancer as Mga	
except:
	import machine_learning_avancer as Mga	

try:
	import package.utilitaire_debug as ud	
except:
	import utilitaire_debug as ud	




class load_image:
	"""
	cette classe chargent des images
	"""
 
 
	def __init__(self, option = {"ch_img":"./test", "tensorflow" :"machine_learning"}):
		if not isinstance(option, dict):
			raise TypeError("erreur option = {} n'est pas de type list ".format(type(option)))

		#liste les options
		self.option = option
		#ce tableau est rempli lors du chargement de l'image
		self.tableau = None
		self.journal = Ij.journal()
		#self.machine_learning = machine_learning
		#self.machine_learning_avancer = machine_learning_avancer



	def interface_load_image(self,object_tk):
		"""
		methode de class qui creer l'interface graphique
		"""

		frame_principal = Tk.Frame(object_tk)
		frame_principal.grid(row = 0, column = 0, sticky='NSEW')
		label = Tk.Label(frame_principal)
		label.grid(row = 0, column = 0)
 
		frame_bp = Tk.Frame(frame_principal)
		frame_bp.grid(row = 1, column = 0, sticky='NSEW')
 
		bp_charger = Tk.Button(frame_bp, text = "Charger",command = partial(self.Charger, label))
		bp_charger.grid(row = 2,column = 0, sticky='EW')
 
		bp_generer = Tk.Button(frame_bp, text = "Generer",command = partial(self.generer, object_tk))
		bp_generer.grid(row = 3,column = 0, sticky='EW')
		
		bp_annuler = Tk.Button(frame_bp, text = "Fermer",command = partial(self.quitter_interface, object_tk))
		bp_annuler.grid(row = 4,column = 0, sticky='EW')




		#frame_principal.grid_columnconfigure(0,weight=1)
		#frame_principal.grid_rowconfigure(0,weight=0)
		#frame_principal.grid_rowconfigure(1,weight=1)



	def quitter_interface(self, object_tk):
		"""
		methode de class qui permet de quitter le programme
		"""

		object_tk.destroy()



	def Charger(self, object_label):
		"""
		methode de class qui permet de reset le canevas
		"""

		load = fd.askopenfilename(defaultextension = ".JPG", initialdir = self.option["ch_img"])

		if not load:
			return None
			print("annuler")
		else:
			self.create_data(file_img = load)
			image = PIL.Image.open(load)
			image = image.resize((70, 70))
			self.img_convert = PIL.ImageTk.PhotoImage(image)
			object_label.configure(image = self.img_convert)



	def afficher_donnee(self, object_tk):
		"""
		methode de class qui permet d'afficher les donnees
		"""
		top = Tk.Toplevel(object_tk)
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
		if self.option["tensorflow"] == 'machine learning basique':
			#lancement de la recherche
			self.machine_learning.test_modele(object_tk = object_tk, data = self.tableau )

		elif self.option["tensorflow"] == 'machine learning avancée':
			self.machine_learning_avancer.test_modele(object_tk = object_tk, data = self.tableau)




	def create_data(self, file_img):
		"""
		recupere les donnée de l'image
		"""

		#recupation des données
		chiffre = PIL.Image.open(file_img).convert("L")
		self.tableau = (255 - np.array(chiffre.getdata()))/255



		"""
		self.tableau = scipy.ndimage.imread(file_img, flatten=True)
		#si les dimentions des données sont differente de (28,28)
		#je redimentionne le tableau
		if not np.shape(self.tableau) == (28, 28):
			self.tableau = resize(self.tableau, (28, 28))
		#conversion d'un tableau en une dimension
		self.tableau  = np.ndarray.flatten(self.tableau)
		self.tableau = np.vectorize(lambda x: 255 - x)(self.tableau)
		"""


if __name__ == "__main__":

	limg = load_image()
	app = Tk.Tk()
	limg.interface_load_image(app)
	app.mainloop()