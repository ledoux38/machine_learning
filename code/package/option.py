#!usr/bin/python3.5c 
#-*-coding:UTF-8 -*



from tkinter import *
from interface_journal import*
#import tkinter.messagebox
import pickle
import os
from functools import partial

class Options:
	def __init__(self):
		self.param = self.chargement_opt()
		self.interface = False

	def sauvegarde_opt(self, option):
		"""
		methode de class qui permet la sauvegarde des données
		"""
		if not isinstance(option, dict):
			raise TypeError("erreur option = {} n'est pas de type dict ".format(type(option)))
		
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
		dic = {"ch_img":"./img", "ch_log":"./log/activity.log", "h_canvas":18, "l_canvas":18, "e_t_canvas":1}
		return dic


	def interface_option(self,object_tk):
		"""
		methode de class qui creer l'interface graphique
		"""
		self.interface = True

		frame_principal = Frame(object_tk)
		frame_principal.grid(row = 0, column = 0)

		frame_ch_accees = LabelFrame(frame_principal, text = "gestion des chemins d'accées", padx = 5, pady = 5)

		label_ch_sauv_image = Label(frame_ch_accees, text = "Chemin d'accès image: ")
		entry_ch_accees_image = Entry(frame_ch_accees)
		entry_ch_accees_image.insert(0, self.param["ch_img"])

		label_ch_sauv_image.grid(row = 0, column = 0)
		entry_ch_accees_image.grid(row = 0, column = 1, sticky = 'EW')

		label_ch_log = Label(frame_ch_accees, text = "Chemin d'accès log: ")
		entry_ch_log = Entry(frame_ch_accees)
		entry_ch_log.insert(0, self.param["ch_log"])

		label_ch_log.grid(row = 1, column = 0, sticky = 'E')		
		entry_ch_log.grid(row = 1, column = 1, sticky = 'EW')		

		frame_ch_accees.grid(row = 0, column = 0, sticky = "EW")


		frame_opt_canvas = LabelFrame(frame_principal, text = "gestion de la table de dessin", padx = 5, pady = 5)

		value_long = IntVar(frame_opt_canvas)
		value_long.set(self.param["h_canvas"])
		scale_long = Scale(frame_opt_canvas,from_= 18, to = 50, showvalue = False, variable = value_long, orient = 'h')
		entry_long = Entry(frame_opt_canvas, textvariable = value_long, width = 10)
		label_long = Label(frame_opt_canvas, text = "longueur canvas: ")

		label_long.grid(row = 0, column = 0, sticky = 'E')
		scale_long.grid(row = 0, column = 1)
		entry_long.grid(row = 0, column = 2)

		value_hot = IntVar(frame_opt_canvas)
		value_hot.set(self.param["l_canvas"])
		scale_hot = Scale(frame_opt_canvas,from_= 18, to = 50, showvalue = False, variable = value_hot, orient = 'h')
		entry_hot = Entry(frame_opt_canvas, textvariable = value_hot, width = 10)		
		label_hot = Label(frame_opt_canvas, text = "hauteur canvas: ")

		label_hot.grid(row = 1, column = 0, sticky = 'E')
		scale_hot.grid(row = 1, column = 1)
		entry_hot.grid(row = 1, column = 2)

		value_epais = IntVar(frame_opt_canvas)
		value_epais.set(self.param["e_t_canvas"])
		scale_epais = Scale(frame_opt_canvas,from_= 1, to = 5, showvalue = False, variable = value_epais, orient = 'h')
		entry_epais = Entry(frame_opt_canvas, textvariable = value_epais, width = 10)		
		label_epais = Label(frame_opt_canvas, text = "épaisseur canvas: ")
		
		label_epais.grid(row = 2, column = 0, sticky = 'E')
		scale_epais.grid(row = 2, column = 1)
		entry_epais.grid(row = 2, column = 2)


		frame_opt_canvas.grid(row = 1, column = 0, sticky = 'EW')





		frame_bp_opt = Frame(frame_principal)

		bp_journal = Button(frame_bp_opt, text = "journal",command = partial(self.ouvrir_journal, object_tk))
		bp_journal.grid(row=0,column=0,sticky='W')

		frame_bp_opt.grid(row = 2, column = 0, sticky = "EW")



		frame_bp_command_inter = Frame(frame_principal)

		bp_appliquer = Button(frame_bp_command_inter, text = "Appliquer", command = partial(self.sauv_configuration, entry_ch_accees_image, entry_ch_log, value_long, value_hot, value_epais))
		bp_appliquer.grid(row=0,column=0,sticky='EW')

		bp_quit = Button(frame_bp_command_inter, text = "Fermer",command = partial(self.quitter_interface, object_tk))
		bp_quit.grid(row=0,column=1,sticky='EW')
		
		frame_bp_command_inter.grid(row = 3, column = 0, sticky = "EW")

		frame_principal.grid_columnconfigure(0,weight=1)
		frame_principal.grid_rowconfigure(0,weight=0)
		frame_principal.grid_rowconfigure(2,weight=1)



	def sauv_configuration(self, ch_img, ch_log, value_long, value_hot, value_epais):
		"""
		methode de class qui sauvegarde la nouvelle configuration
		"""
		if not isinstance(ch_img, Entry):
			raise TypeError("erreur option = {} n'est pas de type Entry ".format(type(ch_img)))
		
		if not isinstance(ch_log, Entry):
			raise TypeError("erreur option = {} n'est pas de type Entry ".format(type(ch_log)))		
		
		if not isinstance(value_long, IntVar):
			raise TypeError("erreur option = {} n'est pas de type IntVar ".format(type(value_long)))
		
		if not isinstance(value_hot, IntVar):
			raise TypeError("erreur option = {} n'est pas de type IntVar ".format(type(value_hot)))
		
		if not isinstance(value_epais, IntVar):
			raise TypeError("erreur option = {} n'est pas de type IntVar ".format(type(value_epais)))


		self.param["ch_img"] = ch_img.get()
		self.param["ch_log"] = ch_log.get()
		self.param["h_canvas"] = value_hot.get()
		self.param["l_canvas"] = value_long.get()
		self.param["e_t_canvas"] = value_epais.get()

		self.sauvegarde_opt(self.param)

	def quitter_interface(self, fenetre):
		"""
		methode de class qui permet de quitter
		"""
		#if not isinstance(fenetre, Tk):
		#	raise TypeError("erreur option = {} n'est pas de type Tk ".format(type(fenetre)))
		self.interface = False
		fenetre.destroy()

	def ouvrir_journal(self, fenetre):		
		"""
		methode de class qui ouvre l'interface graphique
		"""
		#if not isinstance(fenetre, Tk):
		#	raise TypeError("erreur option = {} n'est pas de type Tk ".format(type(fenetre)))

		inter_journ = journal(options = self.param)
		top = Toplevel(fenetre)
		top.title("Journal")
		inter_journ.interface_journal(top)
		

		#inter_journal = Interface_journal(None)





if __name__ == "__main__":

	a = Options()
	app = Tk()
	a.interface_option(app)
	app.title("Options")
	app.resizable(False,False)
	app.mainloop()



	
