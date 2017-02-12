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
		text = Text(self,background = 'white').grid(row=0,column=0,columnspan=2,sticky='NSEW')
        
		bp_button_ok = Button(self, text = "Ok",command= self.fermeture_interface()).grid(row=1,column=0,sticky='EW')

		bp_button_RAZ = Button(self, text = "RAZ").grid(row=1,column=1,sticky='EW')

		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)

		self.grid_rowconfigure(0,weight=10)
		self.grid_rowconfigure(1,weight=0)

	def fermeture_interface(self):
		self.quit()

	def raz_journal(self):
		pass

if __name__ == "__main__":
	app = Interface_journal(None)
	app.mainloop()
