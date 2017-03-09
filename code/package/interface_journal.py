#!usr/bin/python3.5
#-*-coding:UTF-8 -*


from tkinter import *
from functools import partial

class journal:
	def __init__(self):
		pass

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
		with open('./log/activity.log', 'r') as mon_fichier:
			log = mon_fichier.read()
			return log

	def raz_journal(self, object_text):
		log =""
		with open('./log/activity.log', 'w') as mon_fichier:
			mon_fichier.write(log)
			object_text.delete(0.0, END)


if __name__ == "__main__":
	a = journal()
	app = Tk()
	a.interface_journal(app)
	app.title("Options")
	app.resizable(False,False)
	app.mainloop()
