#!usr/bin/python3.5
#-*-coding:UTF-8 -*


import tkinter as Tk 
from functools import partial
import tkinter.messagebox
import tkinter.font as tkFont

class journal:
	def __init__(self, options = {"ch_img":"./img", "ch_log":"./log/activity.log"}):
		self.options = options
		self.text = None


	def interface_journal(self,object_tk):
		"""
		methode de class qui creer l'interface graphique
		"""

		frame_principal = Tk.Frame(object_tk)
		frame_principal.grid(row = 0, column = 0)

		helv36 = tkFont.Font(family='Helvetica', size=6, weight='bold')
		self.text = Tk.Text(frame_principal, background = 'white', font = helv36)
		self.text.grid(row=0,column=0, columnspan=2, sticky='NSEW')
		#self.text.insert(END, self.insert_text(text_data))

		bp_button_ok = Tk.Button(frame_principal, text = "Ok", command = partial(self.fermeture_interface, object_tk))
		bp_button_ok.grid(row=1, column=0, sticky='EW')

		bp_button_RAZ = Tk.Button(frame_principal, text = "RAZ", command = partial(self.raz_journal))
		bp_button_RAZ.grid(row=1, column=1, sticky='EW')

		frame_principal.grid_columnconfigure(0, weight=1)
		frame_principal.grid_columnconfigure(1, weight=1)

		frame_principal.grid_rowconfigure(0, weight=10)
		frame_principal.grid_rowconfigure(1, weight=0)



	def fermeture_interface(self, object_tk):
		"""
		methode de class qui permet de fermer les options
		"""

		#je supprime la fenetre
		object_tk.destroy()



	def insert_text(self, text = None):
		"""
		methode de class qui permet d'inserer le text dans l'entry
		"""
		#je verifie que la fonction interface_journal est bien instancier correctement
		if isinstance(self.text, Text):
			#si j'envoi du text via la variable text, le parametre sera different	
			if not text == None:
				#je verifie que text et de type str
				if not isinstance(text, str):
					#si text different de str j'affiche une erreur
					raise TypeError("erreur option = {} n'est pas de type str ".format(type(text)))
				#sinon j'insert le texte dans self.text
				self.text.insert(END, text)
			#si variable text different de None j'affiche une erreur
		else:
			raise NameError("erreur pour charger du texte dans Text il faut instancier la fonction <<interface_journal>>")



	def charger_text(self, file = "ch_log"):
		if isinstance(self.text, Tk.Text):
			try:
				with open(self.options["ch_log"], 'r') as mon_fichier:
					log = mon_fichier.read()
					self.text.insert(Tk.END, log)
			except FileNotFoundError:
				log = "Erreur dans le chemin d'acces du fichier {}".format(self.options["ch_log"])
		else:
			raise NameError("erreur pour charger du texte dans Text il faut instancier la fonction <<interface_journal>>")


	def raz_journal(self):
		"""
		methode de class qui permet de supprimer integralement le contenu du fichier
		"""
		if isinstance(self.text, Tk.Text):
			#j'ecrase les données dans l'entry
			self.text.delete(0.0, Tk.END)
		else:
			raise NameError("erreur pour charger du texte dans Text il faut instancier la fonction <<interface_journal>>")

	def raz_fichier_journal(self):
		"""
		methode de class qui permet de supprimer integralement le contenu du fichier
		"""

		#j'instancie une chaine de caractere
		log =""

		#j'ouvre le fichier a l'adresse indiquer et j'ecrase les données 
		with open(self.options["ch_log"], 'w') as mon_fichier:
			mon_fichier.write(log)


if __name__ == "__main__":

	dic = {"ch_img":"./img", "ch_log":"./log/activity.log", "h_canvas":18, "l_canvas":18, "e_t_canvas":1}

	a = journal(options = dic)
	app = Tk.Tk()
	a.interface_journal(app)
	a.charger_text()
	app.title("journal")
	app.resizable(False,False)
	app.mainloop()
