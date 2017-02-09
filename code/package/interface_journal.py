#!usr/bin/python3.5
#-*-coding:UTF-8 -*

from log import *
from tkinter import *

class Interface_journal(Frame):
	def __init__(self,Frame):
		Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
		self.pack(fill=BOTH)
		self.panel_principal = PanedWindow(self.fenetre, orient=VERTICAL)
		self.panel_principal.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
		self.text = Text(self.panel_principal,background = 'white')
		self.panel_principal.add(self.text)

		self.panel_boutton = PanedWindow(self.fenetre, orient = HORIZONTAL)
		self.bp_button_ok = Button(self.panel_boutton, text = "Ok")
		self.bp_button_RAZ = Button(self.panel_boutton, text = "RAZ")

		self.panel_boutton.add(self.bp_button_ok)
		self.panel_boutton.add(self.bp_button_RAZ)

		self.panel_principal.add(self.panel_boutton)

		self.panel_principal.pack()


#a = Frame_journal()

"""
class Frame_journal():
	def __init__(self):

		self.fenetre = Tk()
		self.panel_principal = PanedWindow(self.fenetre, orient=VERTICAL)
		self.panel_principal.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
		self.text = Text(self.panel_principal,background = 'white')
		self.panel_principal.add(self.text)

		self.panel_boutton = PanedWindow(self.fenetre, orient = HORIZONTAL)
		self.bp_button_ok = Button(self.panel_boutton, text = "Ok")
		self.bp_button_RAZ = Button(self.panel_boutton, text = "RAZ")

		self.panel_boutton.add(self.bp_button_ok)
		self.panel_boutton.add(self.bp_button_RAZ)

		self.panel_principal.add(self.panel_boutton)

		self.panel_principal.pack()
		self.fenetre.mainloop()
"""