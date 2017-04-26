#!usr/bin/python3.5
#-*-coding:UTF-8 -*

import tkinter.ttk as ttk 
import tkinter as Tk
import threading
import time

class barre_progression:
	def __init__(self):
		self.t = threading.Thread(target = self.initiatiation_barre_progression)
		self.t.start()


	def initiatiation_barre_progression(self):
		self.fenetre = Tk.Tk()
		label = Tk.Label(self.fenetre, text = "veuillez patienter!")
		label.grid(row = 0, column = 0, sticky = "EW")

		barre_proression=ttk.Progressbar(self.fenetre, mode="indeterminate")
		barre_proression.grid(row = 1, column = 0, sticky = "EW")
		barre_proression.start()

		self.text = Tk.Text(self.fenetre, height = 10, width = 60, bg = "white")
		self.text.grid(row = 2, column = 0, sticky = "EW")

		self.fenetre.mainloop()


	def inserer_texte(self, texte = None):
		"""
		methode de class qui permet d'inserer le text dans l'entry
		"""
		#je verifie que text et de type str
		if not isinstance(texte, str):
			#si text different de str j'affiche une erreur
			raise TypeError("erreur option = {} n'est pas de type str ".format(type(texte)))
			#sinon j'insert le texte dans self.text
		self.text.insert(Tk.END, texte)


	def fermer_barre_progression(self):
		self.fenetre.quit()
		self.t.join()



class barre_progression_top_level:
	def __init__(self, parent):
		#self.t = threading.Thread(target = self.initiatiation_barre_progression(parent))
		#self.t.start()
		self.initiatiation_barre_progression(parent)

	def initiatiation_barre_progression(self, parent):
		self.top = Tk.Toplevel(parent)
		#les parametres de la fenetre chargement image
		self.top.title("veuillez patienter!")
		#je fais apparaître la fenetre enfant sur la fenetre parent
		self.top.transient(parent)
		#la fenêtre principale est bloquée par grab_set rend la fenêtre "modale"
		self.top.grab_set()
		#focus_set permet d'attraper les évènements sur la fenêtre principale
		self.top.focus_set()
		#j'empeche la fenetre d'etre redimenssionner
		self.top.resizable(False, False)
		# je fais toutes les modifications dont j'ai besoins

		label = Tk.Label(self.top, text = "veuillez patienter!")
		label.grid(row = 0, column = 0, sticky = "EW")

		barre_proression=ttk.Progressbar(self.top, mode="indeterminate")
		barre_proression.grid(row = 1, column = 0, sticky = "EW")
		barre_proression.start()

		self.text = Tk.Text(self.top, height = 10, width = 60, bg = "white")
		self.text.grid(row = 2, column = 0, sticky = "EW")



	def inserer_texte(self, texte = None):
		"""
		methode de class qui permet d'inserer le text dans l'entry
		"""
		#je verifie que text et de type str
		if not isinstance(texte, str):
			#si text different de str j'affiche une erreur
			raise TypeError("erreur option = {} n'est pas de type str ".format(type(texte)))
			#sinon j'insert le texte dans self.text
		self.text.insert(Tk.END, texte)


	def fermer_barre_progression(self):
		self.top.quit()



class basique_barre_progression:
	def __init__(self):
		self.fenetre = Tk.Tk()
		barre_proression=ttk.Progressbar(self.fenetre, mode="indeterminate")
		barre_proression.pack(side='bottom')
		barre_proression.start()
		self.fenetre.mainloop()

	def fermer_barre_progression(self):
		self.top.quit()


if __name__ == "__main__":

	version = 4

	if version == 0:
		app2 = tk.Tk()

		label = tk.Label(app2,text = "coucou")
		label.grid(row = 0, column = 0, sticky = "EW")

		a = barre_progression()

		top = tk.Tk(app2)
		#les parametres de la fenetre des options
		top.title("Options")
		#je fais apparaître la fenetre enfant sur la fenetre parent

		top.resizable(False, False)


		a.affichage_barre_progression(top)

		a.inserer_texte(texte = "initialisation de la procedure \n")
		a.inserer_texte(texte = "recherche donnée enregistrer \n")
		a.inserer_texte(texte = "recuperation en cours.")

		a.inserer_texte(texte = "\n")
		a.inserer_texte(texte = "recuperation terminer.")
		a.fermer_barre_progression(top)

		app2.mainloop()

	if version == 1:

		app2 = tk.Tk()

		a = barre_progression()

		top = tk.Tk(app2)
		#les parametres de la fenetre des options
		top.title("Options")
		#je fais apparaître la fenetre enfant sur la fenetre parent

		top.resizable(False, False)


		a.affichage_barre_progression(top)

		a.inserer_texte(texte = "initialisation de la procedure \n")
		a.inserer_texte(texte = "recherche donnée enregistrer \n")
		a.inserer_texte(texte = "recuperation en cours.")

		a.inserer_texte(texte = "\n")
		a.inserer_texte(texte = "recuperation terminer.")
		a.fermer_barre_progression(top)

		app2.mainloop()

	if version == 2:

		app2 = tk.Tk()
		progress=ttk.Progressbar(app2, mode="indeterminate")
		progress.grid(row = 1, column = 0, sticky = "EW")
		progress.start()
		app2.mainloop()

	if version == 3:


		app2 = Tk.Tk()

		progress=barre_progression_top_level(app2)
		time.sleep(2)
		print("coucou")
		progress.fermer_barre_progression()

		app2.mainloop()

	if version == 4:
		app2 = Tk.Tk()
		progress=barre_progression()
		time.sleep(2)
		print("coucou")
		del progress
		#print("coucou")
		
		labelText=Tk.Label(app2,text="MonText")
		labelText.pack()
		app2.mainloop()



