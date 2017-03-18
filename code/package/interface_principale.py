#!usr/bin/python3.5
#-*-coding:UTF-8 -*


from log import *
from tkinter import *
from option import *
from canvas import *
import tkinter.messagebox
from numpy import *
from img import*
from functools import partial
from Machine_learning import *

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
		self.inter_option = Options()
		self.opt = self.inter_option.param
		self.image = img(option = self.opt)



	def interface_principale(self, object_tk):
		"""
		methode de class qui permet d'initialiser les bouttons pour les autre fonctions
		"""

		frame_principal = Frame(object_tk)
		frame_principal.grid(row = 0, column = 0)

		menu_bar = Menu(object_tk)
		menu_fichier = Menu(menu_bar, tearoff = 0)
		menu_fichier.add_command(label = "Generer", command = self.generer)
		menu_fichier.add_command(label = "Recommencer", command = self.recommencer_dessin)
		menu_fichier.add_command(label = "Option", command = partial(self.ouvrir_option, object_tk))
		menu_fichier.add_command(label = "Sauver image", command = self.sauv_img)
		menu_fichier.add_command(label = "Quitter", command = partial(self.quitter_interface, object_tk))
		menu_bar.add_cascade(label = "Fichier", menu = menu_fichier)
		object_tk.config(menu = menu_bar)

		self.canvas = interface_canvas(frame_principal, option = self.opt)
		self.canvas.grid(row = 0, column = 0, rowspan = 3, sticky = "NW")

		frame = Frame(frame_principal)
		bp_generer = Button(frame, text = "Generer", command = self.generer)
		bp_generer.grid(row = 0, column = 0, sticky = 'EW')

		bp_recommencer = Button(frame, text = "Recommencer", command = self.recommencer_dessin)
		bp_recommencer.grid(row = 1, column = 0, sticky = 'EW')

		frame.grid(row = 2, column = 2, sticky = "EW")
		
		bp_quit = Button(frame_principal, text = "Quitter", command =partial(self.quitter_interface, object_tk))
		bp_quit.grid(row = 4, column = 2, sticky = 'EW')

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
		


	def generer(self):
		"""
		methode de class qui permet d'initialiser la recuperation du tableau
		"""

		self.image._set_image(self.canvas)
		#creation du tableau numpy et recuperation de la list de l'image
		liste = self.image.get_data( resize = (28, 28))
		print(len(liste))
		#print(liste[783])
		
		arr = zeros((28, 28))
		print(shape(arr),"  :  ",size(arr))

		#arr.reshape(28,28)
		
		#print( list(self._image.getdata()))


		#je prepare les parametres de tensorflow
		#machine_learning(donnee = arr)
		
		


	def ouvrir_option(self, object_tk):
		"""
		methode de class qui permet d'acceder au option
		"""

		#je creer une fenetre pour inserer la frame de options
		top = Toplevel(object_tk)
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



	def sauv_img(self):
		"""
		methode de class qui permet de sauvegarder l'image à un endroit donné par la class options
		"""

		#modification de l'image dans la fenetre 
		self.image._set_image(self.canvas)
		#enregistrement de l'image
		self.image.sauv_img()
	


if __name__ == "__main__":

	liste = [(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255),(255, 255, 255)]
	print(len(liste))

	#arr = zeros((3,3))

	arr = array(liste[0],dtype = tuple)
	append(arr,liste[1])
	append(arr,liste[2])
	append(arr,liste[3])
	append(arr,liste[4])

	print(shape(arr),"  :  ",size(arr), "\n", arr)

	"""
	x= 0
	y= 0
	num = 0
	while y < 3:
		while x <3:
			arr[x][y] = liste[num]
			x+=1
			y+=1
			num +=1
	#arr = array(liste)
	print(shape(arr),"  :  ",size(arr))
	"""

	"""
	a = Interface_principale()

	app = Tk()
	a.interface_principale(app)
	app.title("MNIST")
	app.resizable(False, False)
	app.mainloop()
	"""
