#!usr/bin/python3.5
#-*-coding:UTF-8 -*

import Main_class
from tkinter import *

class Main_frame():
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

a = Main_frame()