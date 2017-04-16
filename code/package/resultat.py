#!usr/bin/python3.5
#-*-coding:UTF-8 -*


import tkinter as Tk

from functools import partial

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class resultat:
	def __init__(self):
		pass






	def interface_resultat(self,object_tk):
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
		graph_mnsit.grid(row = 1, column = 0)

		graph_tensorflow = graph(frame_img)
		graph_tensorflow.grid(row = 1, column = 1)



		
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





class graph(Tk.Frame):

	def __init__(self, parent):
		Tk.Frame.__init__(self, parent)

		f = Figure(figsize=(2, 2), dpi=100)
		a = f.add_subplot(111)
		a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=True)

		#toolbar = NavigationToolbar2TkAgg(canvas, self)
		#toolbar.update()
		canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=True)


if __name__ == "__main__":
	choix_version = 0
	if choix_version == 0:

		a = resultat()
		app = Tk.Tk()
		a.interface_resultat(app)
		app.title("Resultat")
		#app.resizable(False,False)
		app.mainloop()

