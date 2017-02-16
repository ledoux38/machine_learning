#!usr/bin/python3.5
#-*-coding:UTF-8 -*


from log import *
from tkinter import *
from interface_journal import*
from canvas import *
import tkinter.messagebox

class Interface_principale(Tk):
	def __init__(self,parent):
		Tk.__init__(self,parent)

		self.initialize()

	def initialize(self):
		self.grid()

		menu_bar = Menu(self)
		menu_fichier = Menu(menu_bar, tearoff = 0)
		menu_fichier.add_command(label = "Generer", command = self.generer)
		menu_fichier.add_command(label = "Recommencer", command = self.recommencer_dessin)
		menu_fichier.add_command(label = "Option", command = self.ouvrir_option)
		menu_fichier.add_command(label = "Quitter", command = self.quitter_interface)
		menu_bar.add_cascade(label = "Fichier", menu = menu_fichier)
		self.config(menu = menu_bar)

		self.canvas = interface_canvas(self, longueur = 65, hauteur = 50)
		self.canvas.grid(row=0,column=0,columnspan = 2, rowspan = 4, sticky = "NSEW")

		self.bp_generer = Button(self, text = "Generer")
		self.bp_generer.grid(row=0,column=2,sticky='EW')

		self.bp_recommencer = Button(self, text = "Recommencer", command = self.recommencer_dessin)
		self.bp_recommencer.grid(row=1,column=2,sticky='EW')

		"""
		self.bp_journal = Button(self, text = "journal",command = self.ouvrir_journal)
		self.bp_journal.grid(row=1,column=2,sticky='EW')
		"""

		self.bp_quit = Button(self, text = "Fermer",command = self.quitter_interface)
		self.bp_quit.grid(row=2,column=2,sticky='EW')

		self.grid_columnconfigure(0,weight=1)
		self.grid_rowconfigure(0,weight=0)
		self.grid_rowconfigure(1,weight=0)

	def quitter_interface(self):
		self.quit()

	def ouvrir_journal(self):
		inter_journal = Interface_journal(None)

	def recommencer_dessin(self):
		self.canvas.tout_supprimer()

	def generer(self):
		tkinter.messagebox.showinfo("Information","Boutton <generer> non implémenté \n Prochainement!!")

	def ouvrir_option(self):
		tkinter.messagebox.showinfo("Information","menu <option> non implémenté \n Prochainement!!")



if __name__ == "__main__":
	app = Interface_principale(None)
	app.title("MNIST")
	#app.resizable(False,False)
	app.mainloop()

