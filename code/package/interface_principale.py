#!usr/bin/python3.5
#-*-coding:UTF-8 -*

from Main_class import *
from tkinter import *
from Frame_journal import*


class Interface_principale(Frame):
	def __init__(self,fenetre,**kwargs):
		Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
		self.pack(fill=BOTH)
		self.log = Main_class()
		self.log._set_log("initialisation de l'interface principale")

		self.panel_principal = PanedWindow(self, orient=VERTICAL)
		self.panel_principal.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
		self.canvas = Canvas(self.panel_principal,width = 150, height = 120,background = 'yellow')

		self.panel_principal.add(self.canvas)

		self.panel_button = PanedWindow(self,orient = HORIZONTAL)

		self.button_fermer = Button(self.panel_button, text = "Fermer", command = self.quitter_application)
		self.button_generer = Button(self.panel_button, text = "Generer")
		self.button_recommencer = Button(self.panel_button, text = "Recommencer")
		self.button_option = Button(self.panel_button, text = "journal",command = self.interface_journal)

		self.panel_button.add(self.button_option)
		self.panel_button.add(self.button_recommencer)
		self.panel_button.add(self.button_generer)
		self.panel_button.add(self.button_fermer)

		self.panel_principal.add(self.panel_button)

		self.panel_principal.pack()

	def quitter_application(self):
		self.log._set_log("arret de l'application")
		self.quit()

	def interface_journal(self):
		pass





fenetre = Tk()
interface = Interface_principale(fenetre)

interface.mainloop()
interface.destroy()



