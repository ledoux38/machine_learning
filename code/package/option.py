#!usr/bin/python3.5c 
#-*-coding:UTF-8 -*



import tkinter as Tk
import pickle
import os
from functools import partial


try:
	import package.journal as Ij
except:
	import journal as Ij


class Options:
	def __init__(self):
		self.param = self.chargement_opt()






	def interface_option(self,object_tk):
		"""
		methode de class qui creer l'interface graphique
		"""

		frame_principal = Tk.Frame(object_tk)
		frame_principal.grid(row = 0, column = 0)

		frame_ch_accees = Tk.LabelFrame(frame_principal, text = "gestion des chemins d'accées", padx = 5, pady = 5)

		label_ch_sauv_image = Tk.Label(frame_ch_accees, text = "Chemin d'accès image: ")
		self.entry_ch_accees_image = Tk.Entry(frame_ch_accees)
		self.entry_ch_accees_image.insert(0, self.param["ch_img"])

		label_ch_sauv_image.grid(row = 0, column = 0)
		self.entry_ch_accees_image.grid(row = 0, column = 1, sticky = 'EW')

		label_ch_log = Tk.Label(frame_ch_accees, text = "Chemin d'accès log: ")
		self.entry_ch_log = Tk.Entry(frame_ch_accees)
		self.entry_ch_log.insert(0, self.param["ch_log"])

		label_ch_log.grid(row = 1, column = 0, sticky = 'E')		
		self.entry_ch_log.grid(row = 1, column = 1, sticky = 'EW')		


		label_ch_mnist = Tk.Label(frame_ch_accees, text = "Chemin d'accès base Mnist: ")
		self.entry_ch_mnist = Tk.Entry(frame_ch_accees)
		self.entry_ch_mnist.insert(0, self.param["ch_mnist"])

		label_ch_mnist.grid(row = 2, column = 0, sticky = 'E')		
		self.entry_ch_mnist.grid(row = 2, column = 1, sticky = 'EW')	


		frame_ch_accees.grid(row = 0, column = 0, sticky = "EW")


		frame_opt_canvas = Tk.LabelFrame(frame_principal, text = "gestion de la table de dessin", padx = 5, pady = 5)

		self.value_long = Tk.IntVar(frame_opt_canvas)
		self.value_long.set(self.param["h_canvas"])
		scale_long = Tk.Scale(frame_opt_canvas,from_= 18, to = 150, showvalue = False, variable = self.value_long, orient = 'h')
		entry_long = Tk.Entry(frame_opt_canvas, textvariable = self.value_long, width = 10)
		label_long = Tk.Label(frame_opt_canvas, text = "longueur canvas: ")

		label_long.grid(row = 0, column = 0, sticky = 'E')
		scale_long.grid(row = 0, column = 1)
		entry_long.grid(row = 0, column = 2)

		self.value_hot = Tk.IntVar(frame_opt_canvas)
		self.value_hot.set(self.param["l_canvas"])
		scale_hot = Tk.Scale(frame_opt_canvas,from_= 18, to = 150, showvalue = False, variable = self.value_hot, orient = 'h')
		entry_hot = Tk.Entry(frame_opt_canvas, textvariable = self.value_hot, width = 10)		
		label_hot = Tk.Label(frame_opt_canvas, text = "hauteur canvas: ")

		label_hot.grid(row = 1, column = 0, sticky = 'E')
		scale_hot.grid(row = 1, column = 1)
		entry_hot.grid(row = 1, column = 2)

		self.value_epais = Tk.IntVar(frame_opt_canvas)
		self.value_epais.set(self.param["e_t_canvas"])
		scale_epais = Tk.Scale(frame_opt_canvas,from_= 1, to = 10, showvalue = False, variable = self.value_epais, orient = 'h')
		entry_epais = Tk.Entry(frame_opt_canvas, textvariable = self.value_epais, width = 10)		
		label_epais = Tk.Label(frame_opt_canvas, text = "épaisseur canvas: ")
		
		label_epais.grid(row = 2, column = 0, sticky = 'E')
		scale_epais.grid(row = 2, column = 1)
		entry_epais.grid(row = 2, column = 2)

		frame_opt_canvas.grid(row = 1, column = 0, sticky = 'EW')


		frame_choix_tensorflow = Tk.Frame(frame_principal)

		choix = Tk.Variable(frame_choix_tensorflow, ('machine learning basique', 'machine learning avancée'))
		self.lb_choix_tensorflow = Tk.Listbox(frame_choix_tensorflow, listvariable = choix, selectmode = "single",  exportselection=0)
		self.lb_choix_tensorflow.grid(row=0,column=0,sticky='WE')
		self.lb_choix_tensorflow.selection_set(self.param["index_tensorflow"])
		frame_choix_tensorflow.grid(row = 2, column = 0, sticky = "EW")



		frame_bp_opt = Tk.Frame(frame_principal)

		bp_journal = Tk.Button(frame_bp_opt, text = "journal",command = partial(self.ouvrir_journal, object_tk))
		bp_journal.grid(row=0,column=0,sticky='W')


		bp_defaut = Tk.Button(frame_bp_opt, text = "Defaut",command = partial(self.opt_par_def))
		bp_defaut.grid(row=0,column=1,sticky='W')

		frame_bp_opt.grid(row = 3, column = 0, sticky = "EW")



		frame_bp_command_inter = Tk.Frame(frame_principal)

		bp_appliquer = Tk.Button(frame_bp_command_inter, text = "Appliquer", command = self.sauv_configuration)
		bp_appliquer.grid(row=0,column=0,sticky='EW')

		bp_quit = Tk.Button(frame_bp_command_inter, text = "Fermer",command = partial(self.fermeture_interface, object_tk))
		bp_quit.grid(row=0,column=1,sticky='EW')
		
		frame_bp_command_inter.grid(row = 4, column = 0, sticky = "EW")

		frame_principal.grid_columnconfigure(0,weight=1)
		frame_principal.grid_rowconfigure(0,weight=0)
		frame_principal.grid_rowconfigure(2,weight=1)



	def sauvegarde_opt(self, option):
		"""
		methode de class qui permet la sauvegarde des données
		"""

		if not isinstance(option, dict):
			raise TypeError("erreur option = {} n'est pas de type dict ".format(type(option)))
		
		with open("parametre/param", 'wb') as fichier:
			mon_fichier = pickle.Pickler(fichier)
			mon_fichier.dump(option)



	def chargement_opt(self):
		"""
		methode de class qui verifie l'existance du chemin du dossier param
			si le chemin n'existe pas un dossier sera créée par defaut
			et un fichier param par defaut sera crée
		"""

		try:
			with open("parametre/param", 'rb') as fichier:
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

		dic = {"ch_img": "./img",
				 "ch_log": "./log/activity.log", 
				 "ch_mnist": "./MNIST_data",
				 "h_canvas": 18, 
				 "l_canvas": 18, 
				 "e_t_canvas": 1, 
				 "tensorflow": "machine learning basique", 
				 "index_tensorflow": 0,
				 "ch_model_basique": "modeles/basique/model_basique.ckpt",
				 "ch_model_avancer": "modeles/avancer/model_avancer.ckpt"
				 }

		return dic



	def opt_par_def(self):
		"""
		methode de class qui reset les variable par defaut
		"""
		self.param = self.get_param_defaut()
		self.sauvegarde_opt(self.param)
		self.set_items(self.param)



	def set_items(self, option):
		"""
		fonction qui modifie les items de l'interface graphique
		"""

		if not isinstance(option, dict):
			raise TypeError("erreur option = {} n'est pas de type dict ".format(type(option)))

		self.value_long.set(self.param["h_canvas"])

		self.value_hot.set(self.param["l_canvas"])

		self.value_epais.set(self.param["e_t_canvas"])		

		self.entry_ch_accees_image.delete(0,Tk.END)
		self.entry_ch_accees_image.insert(0, self.param["ch_img"])

		self.entry_ch_log.delete(0,Tk.END)
		self.entry_ch_log.insert(0, self.param["ch_log"])

		self.entry_ch_mnist.delete(0,Tk.END)
		self.entry_ch_mnist.insert(0, self.param["ch_mnist"])

		self.lb_choix_tensorflow.selection_set(self.param["index_tensorflow"])

	def sauv_configuration(self):
		"""
		methode de class qui sauvegarde la nouvelle configuration
		"""
		#sauvegarde des chemin de fichier
		self.save_ch_accees()
		#sauvegarde des attribut principaux du canvas
		self.save_canvas()
		#sauvegarde du choix de tensorflow
		self.save_choix_tensorflow()
		#enregistrement des nouvelles obtions dans le fichiers param
		self.sauvegarde_opt(self.param)




	def save_ch_accees(self):
		"""
		methode de class qui sauvegarde la nouvelle configuration des chemin d'accees
		"""
				
		self.param["ch_img"] = self.entry_ch_accees_image.get()
		self.param["ch_log"] = self.entry_ch_log.get()
		self.param["ch_mnist"] = self.entry_ch_mnist.get()
		self.param["ch_model_basique"] = "modeles/basique/model_basique.ckpt"
		self.param["ch_model_avancer"] = "modeles/avancer/model_avancer.ckpt"

	def save_canvas(self):
		"""
		methode de class qui sauvegarde la nouvelle configuration attributs du canvas
		"""

		self.param["h_canvas"] = self.value_hot.get()
		self.param["l_canvas"] = self.value_long.get()
		self.param["e_t_canvas"] = self.value_epais.get()




	def save_choix_tensorflow(self):
		"""
		methode de class qui sauvegarde la nouvelle selection de tensorflow
		"""

		index = self.lb_choix_tensorflow.curselection()
		index = index[0]
		self.param["tensorflow"] = self.lb_choix_tensorflow.get(index)
		self.param["index_tensorflow"] = index



	def fermeture_interface(self, fenetre):
		"""
		methode de class qui permet de fermer les options
		"""

		#je supprime la fenetre
		fenetre.destroy()



	def ouvrir_journal(self, fenetre):		
		"""
		methode de class qui ouvre l'interface graphique
		"""

		# j'instancie la class journal
		inter_journ = Ij.journal(options = self.param)
		#je creer une fenetre 
		top = Tk.Toplevel(fenetre)
		#j'integre des options 
		top.title("Journal")
		#j'empeche la fenetre d'etre redimenssionner
		top.resizable(False, False)
		#j'integre dans la la fenetre la frame de journal
		inter_journ.interface_journal(top)





if __name__ == "__main__":
	choix_version = 0
	if choix_version == 0:

		a = Options()
		app = Tk.Tk()
		a.interface_option(app)
		app.title("Options")
		app.resizable(False,False)
		app.mainloop()


	elif choix_version == 1:

		root = Tk()
	 
		lb = Listbox(root, selectmode=SINGLE, exportselection=0)
		lb.pack(padx=5, pady=5)
		 
		for item in ['un', 'deux', 'trois', 'quatre', 'cinq']:
		    lb.insert(END, item)
		 
		l = Label(root, bg='white')
		l.pack(padx=5, pady=5, fill=BOTH, expand=1)
		 
		def isselect(event=None):
		    if lb.curselection():
		        l.config(text='Selection actuelle : '+lb.get(lb.curselection()))
		    else:
		        l.config(text='Pas de selection')
		 
		e = Entry(root)
		e.pack(padx=5, pady=5)
		e.bind('<Button-1>' , isselect)
		 
		root.mainloop()

	elif choix_version == 2:
		a = Options()
		print(a.get_param_defaut())
			
