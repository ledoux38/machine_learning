#!usr/bin/python3.5
#-*-coding:UTF-8 -*


from tkinter import *
class Interface_journal(Tk):
	def __init__(self,parent):
		Tk.__init__(self,parent)
		self.title("MNIST")
		self.resizable(False,False)
		self.initialize()

	def initialize(self):
		self.grid()
		self.text = Text(self,background = 'white')
		self.text.grid(row=0,column=0,columnspan=2,sticky='NSEW')
		self.insert_text()
        
		bp_button_ok = Button(self, text = "Ok",command= self.fermeture_interface)
		bp_button_ok.grid(row=1,column=0,sticky='EW')

		bp_button_RAZ = Button(self, text = "RAZ",command= self.raz_journal)
		bp_button_RAZ.grid(row=1,column=1,sticky='EW')

		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)

		self.grid_rowconfigure(0,weight=10)
		self.grid_rowconfigure(1,weight=0)

	def fermeture_interface(self):
		self.destroy()

	def insert_text(self):
		with open('./journal/fichier.txt', 'r') as mon_fichier:
			log = mon_fichier.read()
		self.text.insert(END,log)

	def raz_journal(self):
		log =""
		with open('./journal/fichier.txt', 'w') as mon_fichier:
			mon_fichier.write(log)

if __name__ == "__main__":
	app = Interface_journal(None)
	app.mainloop()
