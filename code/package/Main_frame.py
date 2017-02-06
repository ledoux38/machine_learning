#!usr/bin/python3.5
#-*-coding:UTF-8 -*

from Main_class import *
from tkinter import *


class Main_frame(Main_class):
	def __init__(self):
		Main_class.__init__(self)
		self._set_log("initialisation de l'application")
		self.fenetre = Tk()
		self.panel_principal = PanedWindow(self.fenetre, orient=VERTICAL)
		self.panel_principal.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
		self.canvas = Canvas(self.panel_principal,width = 150, height = 120,background = 'yellow')

		self.panel_principal.add(self.canvas)

		self.panel_button = PanedWindow(self.fenetre,orient = HORIZONTAL)

		self.button_fermer = Button(self.panel_button, text = "Fermer", command = self.fenetre.quit)
		self.button_generer = Button(self.panel_button, text = "Generer")
		self.button_recommencer = Button(self.panel_button, text = "Recommencer")
		self.button_option = Button(self.panel_button, text = "Option")

		self.panel_button.add(self.button_option)
		self.panel_button.add(self.button_recommencer)
		self.panel_button.add(self.button_generer)
		self.panel_button.add(self.button_fermer)

		self.panel_principal.add(self.panel_button)

		self.panel_principal.pack()

		self.fenetre.mainloop()









a = Main_frame()
