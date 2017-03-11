#!usr/bin/python3.5
#-*-coding:UTF-8 -*


from tkinter import *
from functools import partial
import tkinter.messagebox

class journal:
	def __init__(self, options):
		self.options = options


	def interface_journal(self,object_tk):

		frame_principal = Frame(object_tk)
		frame_principal.grid(row = 0, column = 0)

		text = Text(frame_principal, background = 'white')
		text.grid(row=0,column=0, columnspan=2, sticky='NSEW')
		text.insert(END, self.insert_text())

		bp_button_ok = Button(frame_principal, text = "Ok", command = partial(self.fermeture_interface, object_tk))
		bp_button_ok.grid(row=1, column=0, sticky='EW')

		bp_button_RAZ = Button(frame_principal, text = "RAZ", command = partial(self.raz_journal, text))
		bp_button_RAZ.grid(row=1, column=1, sticky='EW')

		frame_principal.grid_columnconfigure(0, weight=1)
		frame_principal.grid_columnconfigure(1, weight=1)

		frame_principal.grid_rowconfigure(0, weight=10)
		frame_principal.grid_rowconfigure(1, weight=0)

	def fermeture_interface(self, object_tk):
		object_tk.destroy()

	def insert_text(self):
		log = ""
		try:

			with open(self.options["ch_log"], 'r') as mon_fichier:
				log = mon_fichier.read()

		except FileNotFoundError:
			log = "Erreur dans le chemin d'acces du fichier {}".format(self.options["ch_log"])
			return log
		else:
			return log

	def raz_journal(self, object_text):
		log =""
		with open(self.options["ch_log"], 'w') as mon_fichier:
			mon_fichier.write(log)
			object_text.delete(0.0, END)


if __name__ == "__main__":

	dic = {"ch_img":"./img", "ch_log":"./log/activity.log", "h_canvas":18, "l_canvas":18, "e_t_canvas":1}

	a = journal(options = dic)
	app = Tk()
	a.interface_journal(app)
	app.title("journal")
	app.resizable(False,False)
	app.mainloop()
