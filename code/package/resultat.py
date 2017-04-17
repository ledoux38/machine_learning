#!usr/bin/python3.5
#-*-coding:UTF-8 -*


import tkinter as Tk

from functools import partial

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import pylab as plt

import scipy.ndimage
from PIL import Image
from numpy import *

class resultat:
	def __init__(self):
		pass






	def interface_resultat(self,object_tk, data):
		"""
		methode de class qui creer l'interface graphique
		"""

		frame_principal = Tk.Frame(object_tk)
		frame_principal.grid(row = 0, column = 0)

		frame_img = Tk.Frame(frame_principal)
		frame_img.grid(row = 1, column = 0, sticky='EW')

		label_image_numpy = Tk.Label(frame_img, text = "image numpy ")
		label_image_numpy.grid(row = 0, column = 0)

		label_vue_tensorflow = Tk.Label(frame_img, text = "vue tensorflow ")
		label_vue_tensorflow.grid(row = 0, column = 1)

		graph_mnsit = graph(frame_img)
		graph_mnsit.grid(row = 1, column = 0, sticky='EW')

		graph_tensorflow = graphv3(frame_img, data)
		graph_tensorflow.grid(row = 1, column = 1, sticky='EW')



		
		frame_resultat = Tk.Frame(frame_principal)
		frame_resultat.grid(row = 2, column = 0)

		label_resultat = Tk.Label(frame_resultat, text = "Resultat ")
		label_resultat.grid(row = 0, column = 0)

		self.text_resultat = Tk.Text(frame_resultat)
		self.text_resultat.grid(row = 1, column = 0)
		

		frame_bp_command_inter = Tk.Frame(frame_principal)

		bp_quit = Tk.Button(frame_bp_command_inter, text = "Fermer",command = partial(self.fermeture_interface, object_tk))
		bp_quit.grid(row=0, column=0, sticky='EW')
		
		frame_bp_command_inter.grid(row = 3, column = 0, sticky = "EW")

		#frame_principal.grid_columnconfigure(0,weight=1)
		#frame_principal.grid_rowconfigure(0,weight=0)
		#frame_principal.grid_rowconfigure(2,weight=1)




	def fermeture_interface(self, fenetre):
		"""
		methode de class qui permet de fermer les options
		"""

		#je supprime la fenetre
		fenetre.destroy()




	def insert_text(self, text = None):
		"""
		methode de class qui permet d'inserer le text dans l'entry
		"""
		#si j'envoi du text via la variable text, le parametre sera different	
		if not text == None:
			#je verifie que text et de type str
			if not isinstance(text, str):
				#si text different de str j'affiche une erreur
				raise TypeError("erreur option = {} n'est pas de type str ".format(type(text)))
				#sinon j'insert le texte dans self.text
			self.text_resultat.insert(Tk.END, text)
			#si variable text different de None j'affiche une erreur
		else:
			raise NameError("erreur pour charger du texte dans Text il faut instancier la fonction <<interface_journal>>")


class graph(Tk.Frame):

	def __init__(self, parent):
		Tk.Frame.__init__(self, parent)

		f = Figure(figsize=(3, 3), dpi=100)
		a = f.add_subplot(111)
		a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=True)

		#toolbar = NavigationToolbar2TkAgg(canvas, self)
		#toolbar.update()
		canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=True)



class graphv2(Tk.Frame):

	def __init__(self, parent):
		Tk.Frame.__init__(self, parent)

		image = plt.imread("test/4v5.bmp")
		f = Figure(figsize=(3, 3), dpi=100)
		a = f.add_subplot(111)
		im = a.imshow(image) # later use a.set_data(new_data)

		# a tk.DrawingArea
		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
		canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=True)

class graphv3(Tk.Frame):

	def __init__(self, parent, data):
		Tk.Frame.__init__(self, parent)

		f = Figure(figsize=(3, 3), dpi=100)
		a = f.add_subplot(111)
		im = a.matshow(reshape(data, (28,28))) # later use a.set_data(new_data)

		# a tk.DrawingArea
		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
		canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=True) 



if __name__ == "__main__":
	choix_version = 0
	if choix_version == 0:

		chiffre = Image.open("test/4v1.bmp").convert("L")
		data = (255 - array(chiffre.getdata()))/255

		a = resultat()
		app = Tk.Tk()
		a.interface_resultat(app, data)
		app.title("Resultat")
		a.insert_text(text = "[0] ------> 1.245645 \n")
		a.insert_text(text = "[1] ------> 4.245645 \n")
		a.insert_text(text = "[2] ------> 9.245645 \n")
		a.insert_text(text = "[3] ------> 4.245645 \n")
		a.insert_text(text = "[4] ------> 2.245645 \n")
		a.insert_text(text = "[5] ------> 7.245645 \n")
		a.insert_text(text = "[6] ------> 6.245645 \n")
		a.insert_text(text = "[7] ------> 8.245645 \n")
		a.insert_text(text = "[8] ------> 9.245645 \n")
		a.insert_text(text = "[9] ------> 10.245645 \n")
		#app.resizable(False,False)
		app.mainloop()

	if choix_version == 1:
		fig, ax = plt.subplots()

		# Example data
		people = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
		y_pos = arange(len(people))
		performance = 3 + 10 * random.rand(len(people))
		error = random.rand(len(people))

		ax.barh(y_pos, performance, xerr=error, align='center',
		        color='green', ecolor='black')
		ax.set_yticks(y_pos)
		ax.set_yticklabels(people)
		ax.invert_yaxis()  # labels read top-to-bottom
		ax.set_xlabel('Performance')
		ax.set_title('How fast do you want to go today?')

		plt.show()