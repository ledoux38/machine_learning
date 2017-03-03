#!usr/bin/python3.5c 
#-*-coding:UTF-8 -*



from tkinter import *
from interface_journal import*
import tkinter.messagebox
import pickle
import os

class Options:
	def __init__(self):

		self.initialize()
		self.set_param(self.chargement_opt())


	def sauvegarde_opt(self, option):
		
		with open("param", 'wb') as fichier:
			mon_fichier = pickle.Pickler(fichier)
			mon_fichier.dump(option)

	def chargement_opt(self):
		"""
		methode de class qui verifie l'existance du chemin du dossier param
			si le chemin n'existe pas un dossier sera créée par defaut
			et un fichier param par defaut sera crée
		"""
		try:
			with open("param", 'rb') as fichier:
				mon_fichier = pickle.Unpickler(fichier)
				parametre = mon_fichier.load()
				return parametre

		except FileNotFoundError:

			self.sauvegarde_opt(self.get_param_defaut())
			return self.get_param_defaut()

	def get_param_defaut(self):
		"""
		methode de class qui renvoi les attributs par defauts
		"""
		dic = {"ch_img":"/img", "ch_log":"/journal", "h_canvas":18, "l_canvas":18, "e_t_canvas":1}
		return dic

	def get_param(self):
		"""
		methode de class qui renvoi les attributs des objet principaux de la classe
		"""		
		dic = {"ch_img":self.app.entry_ch_accees_image.get(), "ch_log":self.app.entry_ch_log.get(), "h_canvas":self.app.value_hot.get(), "l_canvas":self.app.value_long.get(), "e_t_canvas":self.app.value_epais.get()}
		return dic

	def set_param(self, option):
		"""
		methode de class qui modifie directement les attributs de la class
		"""

		self.app.entry_ch_accees_image.insert(0, option["ch_img"])
		self.app.entry_ch_log.insert(0, option["ch_log"])
		self.app.value_hot.set(option["h_canvas"])
		self.app.value_long.set(option["l_canvas"])
		self.app.value_epais.set(option["e_t_canvas"])

	def afficher(self):
		"""
		methode de class qui affiche la fenetre
		"""

		self.app.mainloop()

	def initialize(self):
		"""
		methode de class qui creer l'interface graphique
		"""

		self.app = Tk()
		self.app.title("Options")
		self.app.resizable(False,False)

		self.app.grid()

		frame_ch_accees = LabelFrame(self.app, text = "gestion des chemins d'accées", padx = 5, pady = 5)

		label_ch_sauv_image = Label(frame_ch_accees, text = "Chemin d'accès image: ")
		self.app.entry_ch_accees_image = Entry(frame_ch_accees)

		label_ch_sauv_image.grid(row = 0, column = 0)
		self.app.entry_ch_accees_image.grid(row = 0, column = 1, sticky = 'EW')

		label_ch_log = Label(frame_ch_accees, text = "Chemin d'accès log: ")
		self.app.entry_ch_log = Entry(frame_ch_accees)

		label_ch_log.grid(row = 1, column = 0, sticky = 'E')		
		self.app.entry_ch_log.grid(row = 1, column = 1, sticky = 'EW')		

		frame_ch_accees.grid(row = 0, column = 0, sticky = "EW")


		frame_opt_canvas = LabelFrame(self.app, text = "gestion de la table de dessin", padx = 5, pady = 5)

		self.app.value_long = IntVar(frame_opt_canvas)
		scale_long = Scale(frame_opt_canvas,from_= 18, to = 50, showvalue = False, variable = self.app.value_long, orient = 'h')
		entry_long = Entry(frame_opt_canvas, textvariable = self.app.value_long, width = 10)
		label_long = Label(frame_opt_canvas, text = "longueur canvas: ")

		label_long.grid(row = 0, column = 0, sticky = 'E')
		scale_long.grid(row = 0, column = 1)
		entry_long.grid(row = 0, column = 2)

		self.app.value_hot = IntVar(frame_opt_canvas)
		scale_hot = Scale(frame_opt_canvas,from_= 18, to = 50, showvalue = False, variable = self.app.value_hot, orient = 'h')
		entry_hot = Entry(frame_opt_canvas, textvariable = self.app.value_hot, width = 10)		
		label_hot = Label(frame_opt_canvas, text = "hauteur canvas: ")

		label_hot.grid(row = 1, column = 0, sticky = 'E')
		scale_hot.grid(row = 1, column = 1)
		entry_hot.grid(row = 1, column = 2)

		self.app.value_epais = IntVar(frame_opt_canvas)
		scale_epais = Scale(frame_opt_canvas,from_= 1, to = 5, showvalue = False, variable = self.app.value_epais, orient = 'h')
		entry_epais = Entry(frame_opt_canvas, textvariable = self.app.value_epais, width = 10)		
		label_epais = Label(frame_opt_canvas, text = "épaisseur canvas: ")
		
		label_epais.grid(row = 2, column = 0, sticky = 'E')
		scale_epais.grid(row = 2, column = 1)
		entry_epais.grid(row = 2, column = 2)


		frame_opt_canvas.grid(row = 1, column = 0, sticky = 'EW')

		frame_bp_opt = Frame(self.app)

		self.app.bp_journal = Button(frame_bp_opt, text = "journal",command = self.ouvrir_journal)
		self.app.bp_journal.grid(row=0,column=0,sticky='W')

		frame_bp_opt.grid(row = 2, column = 0, sticky = "EW")

		frame_bp_command_inter = Frame(self.app)

		self.app.bp_appliquer = Button(frame_bp_command_inter, text = "Appliquer", command = self.sauv_configuration)
		self.app.bp_appliquer.grid(row=0,column=0,sticky='EW')

		self.app.bp_quit = Button(frame_bp_command_inter, text = "Quitter",command = self.quitter_interface)
		self.app.bp_quit.grid(row=0,column=1,sticky='EW')
		
		frame_bp_command_inter.grid(row = 3, column = 0, sticky = "EW")

		self.app.grid_columnconfigure(0,weight=1)
		self.app.grid_rowconfigure(0,weight=0)
		self.app.grid_rowconfigure(2,weight=1)

	def sauv_configuration(self):
		"""
		methode de class qui sauvegarde la nouvelle configuration
		"""

		self.sauvegarde_opt(self.get_param())

	def quitter_interface(self):
		"""
		methode de class qui permet de quitter
		"""

		self.app.destroy()

	def ouvrir_journal(self):		
		"""
		methode de class qui ouvre l'interface graphique
		"""

		inter_journal = Interface_journal(None)





if __name__ == "__main__":
	app = Options()
	app.afficher()