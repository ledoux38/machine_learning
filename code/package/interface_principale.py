#!usr/bin/python3.5
#-*-coding:UTF-8 -*


from log import *
from tkinter import *
from interface_journal import*



from tkinter import *
class Interface_principale(Tk):
	def __init__(self,parent):
		Tk.__init__(self,parent)

		self.initialize()

	def initialize(self):
		self.grid()

		canvas = Canvas(self,background = 'yellow').grid(row=0,column=0,columnspan=4,sticky='NSEW')

		bp_generer = Button(self, text = "Generer").grid(row=1,column=0,sticky='EW')

		bp_recommencer = Button(self, text = "Recommencer").grid(row=1,column=1,sticky='EW')

		bp_journal = Button(self, text = "journal",command = self.ouvrir_journal).grid(row=1,column=2,sticky='EW')

		bp_quit = Button(self, text = "Fermer",command = self.quitter_interface).grid(row=1,column=3,sticky='EW')


		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)
		self.grid_columnconfigure(3,weight=1)

		self.grid_rowconfigure(0,weight=10)
		self.grid_rowconfigure(1,weight=0)

	def quitter_interface(self):
		self.quit()

	def ouvrir_journal(self):
		inter_journal = Interface_journal(None)

if __name__ == "__main__":
	app = Interface_principale(None)
	app.title("MNIST")
	app.resizable(False,False)
	app.mainloop()