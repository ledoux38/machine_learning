#!usr/bin/python3.5
#-*-coding:UTF-8 -*


from log import *
from tkinter import *
from option import *
from canvas import *
import tkinter.messagebox
from numpy import *
from img import*

class Interface_principale(Tk):
	"""
	interface principale du programme
	la classe manage toute le programme:-les options
										-initialisation
										-quitter_interface
										-generer
										-ouvrir_option

	"""

	def __init__(self,parent):
		Tk.__init__(self,parent)
		self.initialize()


	def initialize(self):
		"""
		methode de class qui permet d'initialiser les bouttons pour les autre fonctions
		"""
		# instanciation de la class Options
		self.inter_option = Options()
		opt = self.inter_option.param


		self.image = img()

		self.grid()

		menu_bar = Menu(self)
		menu_fichier = Menu(menu_bar, tearoff = 0)
		menu_fichier.add_command(label = "Generer", command = self.generer)
		menu_fichier.add_command(label = "Recommencer", command = self.recommencer_dessin)
		menu_fichier.add_command(label = "Option", command = self.ouvrir_option)
		menu_fichier.add_command(label = "Sauver image", command = self.sauv_img)
		menu_fichier.add_command(label = "Quitter", command = self.quitter_interface)
		menu_bar.add_cascade(label = "Fichier", menu = menu_fichier)
		self.config(menu = menu_bar)

		self.canvas = interface_canvas(self, option_canvas = opt)
		self.canvas.grid(row = 0, column = 0, rowspan = 3, sticky = "NSEW")

		frame = Frame(self)
		self.bp_generer = Button(frame, text = "Generer", command = self.generer)
		self.bp_generer.grid(row = 0, column = 0, sticky = 'EW')

		self.bp_recommencer = Button(frame, text = "Recommencer", command = self.recommencer_dessin)
		self.bp_recommencer.grid(row = 1, column = 0, sticky = 'EW')

		frame.grid(row = 2, column = 2, sticky = "EW")
		
		self.bp_quit = Button(self, text = "Fermer", command = self.quitter_interface)
		self.bp_quit.grid(row = 4, column = 2, sticky = 'EW')

		

		

		self.grid_columnconfigure(0, weight = 1)
		self.grid_rowconfigure(0, weight = 0)
		self.grid_rowconfigure(2, weight = 1)
		

	def quitter_interface(self):
		"""
		methode de class qui permet de quitter le programme
		"""

		self.quit()

	def recommencer_dessin(self):
		"""
		methode de class qui permet de reset le canevas
		"""

		self.canvas.tout_supprimer()
		


	def generer(self):
		"""
		methode de class qui permet d'initialiser la recuperation du tableau
		"""

		self.image._set_image(self.canvas)
		#creation du tableau numpy et recuperation de la list de l'image
		arr = array(self.image.get_data())
		print(arr)
		tkinter.messagebox.showinfo("Information","programme en cours de realisation \n Prochainement!!")

	def ouvrir_option(self):
		"""
		methode de class qui permet d'acceder au option
		"""

		# je fais toutes les modifications dont j'ai besoins
		

		top = Toplevel(self)
		top.title("Options")
		self.inter_option.interface_option(top)

		#quand le programme s'arrete je recharge les données
		self.canvas.set_canvas(nouv_option = self.inter_option.param)

	def sauv_img(self):
		self.image._set_image(self.canvas)
		self.image.sauv_img()
	


if __name__ == "__main__":
	app = Interface_principale(None)
	app.title("MNIST")
	app.resizable(True,True)
	app.mainloop()

