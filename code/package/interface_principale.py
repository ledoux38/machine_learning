#!usr/bin/python3.5
#-*-coding:UTF-8 -*

from functools import partial
import numpy as Np
import tkinter.messagebox
import tkinter as Tk

try:
	import package.option as Opt 
except:
	import option as Opt 
try:
	import package.canvas as Cv
except:
	import canvas as Cv

try:
	import package.log as Lg 
except:
	import log as Lg 

try:
	import package.img as Ig
except:
	import img as Ig

try:
	import package.machine_learning_basique as Mgb
except:
	import machine_learning_basique as Mgb

try:
	import package.machine_learning_avancer as Mga
except:
	import machine_learning_avancer as Mga

try:
	import package.load_image as limg
except:
	import load_image as limg

try:
	import package.utilitaire_debug as ud
except:
	import utilitaire_debug as ud


class Interface_principale:
	"""
	interface principale du programme
	la classe manage toute le programme:-les options
										-initialisation
										-quitter_interface
										-generer
										-ouvrir_option

	"""

	def __init__(self):

		# instanciation de la class Options
		self.inter_option = Opt.Options()
		# recuperation des donnée option
		self.opt = self.inter_option.param
		# instanciation de la class image
		self.image = Ig.img(option = self.opt)
		# instanciation de la class machine_learning_basique et initialisation
		self.machine_learning = Mgb.machine_learning_basique(option = self.opt)
		# instanciation de la class machine_learning_avancer
		self.machine_learning_avancer = Mga.machine_learning_avancer(option = self.opt)
		# initialisation de la machine_learning_avancer



	def interface_principale(self, object_tk):
		"""
		methode de class qui permet d'initialiser les bouttons pour les autre fonctions
		"""

		frame_principal = Tk.Frame(object_tk)
		frame_principal.grid(row = 0, column = 0)

		menu_bar = Tk.Menu(object_tk)
		menu_fichier = Tk.Menu(menu_bar, tearoff = 0)
		menu_fichier.add_command(label = "Generer", command = self.generer)
		menu_fichier.add_command(label = "Recommencer", command = self.recommencer_dessin)
		menu_fichier.add_command(label = "Option", command = partial(self.ouvrir_option, object_tk))
		menu_fichier.add_command(label = "Sauver image", command = self.sauv_img)
		menu_fichier.add_command(label = "Charger image", command = partial(self.ouvrir_inter_charge_img, object_tk))
		menu_fichier.add_command(label = "Quitter", command = partial(self.quitter_interface, object_tk))
		menu_bar.add_cascade(label = "Fichier", menu = menu_fichier)
		object_tk.config(menu = menu_bar)





		self.canvas = Cv.interface_canvas(frame_principal, option = self.opt)
		self.canvas.grid(row = 0, column = 0, sticky = "NW")


		bp_generer = Tk.Button(frame_principal, text = "Generer", command = partial(self.generer, object_tk))
		bp_generer.grid(row = 1, column = 0, sticky = 'EW')

		bp_recommencer = Tk.Button(frame_principal, text = "Recommencer", command = self.recommencer_dessin)
		bp_recommencer.grid(row = 2, column = 0, sticky = 'EW')

		

		bp_quit = Tk.Button(frame_principal, text = "Quitter", command =partial(self.quitter_interface, object_tk))
		bp_quit.grid(row = 3, column = 0, sticky = 'EW')

		frame_principal.grid_columnconfigure(0, weight = 1)
		frame_principal.grid_rowconfigure(0, weight = 0)
		frame_principal.grid_rowconfigure(2, weight = 1)




	def quitter_interface(self, object_tk):
		"""
		methode de class qui permet de quitter le programme
		"""

		object_tk.quit()



	def recommencer_dessin(self):
		"""
		methode de class qui permet de reset le canevas
		"""

		self.canvas.tout_supprimer()



	def generer(self, object_tk):
		"""
		methode de class qui permet d'initialiser la recuperation du tableau
		"""

		self.image._set_image(self.canvas)
		#recuperation de la list de l'image
		data = self.image.get_data(resize = (28, 28))
		#conversion de l'image en tableau
		data = (255 - Np.array(data))/255
		#ud.print_array_convert(data)

		if self.opt["tensorflow"] == 'machine learning basique':
			#lancement de la recherche
			self.machine_learning.test_modele(object_tk = object_tk, data = data )

		elif self.opt["tensorflow"] == 'machine learning avancée':
			self.machine_learning_avancer.test_modele(object_tk = object_tk, data = data)

			#tkinter.messagebox.showinfo("ATTENTION", "MACHINE LEARNING AVANCÉE PAS ENCORE IMPLEMENTÉ")
			#Mgb.machine_learning_v2(donnee = data, option = self.opt)



	def ouvrir_option(self, object_tk):
		"""
		methode de class qui permet d'acceder au option
		"""

		#je creer une fenetre pour inserer la frame de options
		top = Tk.Toplevel(object_tk)
		#les parametres de la fenetre des options
		top.title("Options")
		#je fais apparaître la fenetre enfant sur la fenetre parent
		top.transient(object_tk)
		#la fenêtre principale est bloquée par grab_set rend la fenêtre "modale"
		top.grab_set()
		#focus_set permet d'attraper les évènements sur la fenêtre principale
		top.focus_set()
		#j'empeche la fenetre d'etre redimenssionner
		top.resizable(False, False)
		# je fais toutes les modifications dont j'ai besoins
		self.inter_option.interface_option(top)
		#pandant ce temps interface_principale et mit en pause
		object_tk.wait_window(top)
		#quand j'en n'ai fini avec les options je charge les nouvelles données
		self.canvas.set_canvas(nouv_option = self.inter_option.param)




	def ouvrir_inter_charge_img(self, object_tk):
		"""
		methode de class qui permet d'acceder à l'interface chargement image
		"""
		inter_char_img = limg.load_image(self.machine_learning, self.machine_learning_avancer, self.opt)
		#je creer une fenetre pour inserer la frame de chargement image
		top = Tk.Toplevel(object_tk)
		#les parametres de la fenetre chargement image
		top.title("Interface chargement image")
		#je fais apparaître la fenetre enfant sur la fenetre parent
		top.transient(object_tk)
		#la fenêtre principale est bloquée par grab_set rend la fenêtre "modale"
		top.grab_set()
		#focus_set permet d'attraper les évènements sur la fenêtre principale
		top.focus_set()
		#j'empeche la fenetre d'etre redimenssionner
		top.resizable(False, False)
		# je fais toutes les modifications dont j'ai besoins
		inter_char_img.interface_load_image(top)



	def sauv_img(self):
		"""
		methode de class qui permet de sauvegarder l'image à un endroit donné par la class options
		"""

		#modification de l'image dans la fenetre 
		self.image._set_image(self.canvas)
		#enregistrement de l'image
		self.image.sauv_img()




if __name__ == "__main__":


	a = Interface_principale()

	app = Tk.Tk()
	a.interface_principale(app)
	app.title("MNIST")
	app.resizable(False, False)
	app.mainloop()

