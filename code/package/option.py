#!usr/bin/python3.5c 
#-*-coding:UTF-8 -*



from tkinter import *
from interface_journal import*
import tkinter.messagebox

class Options:
	def __init__(self,parent):
		self.app = Tk()
		self.interface_option()


	def interface_option(self):

		self.app.title("Options")
		self.app.resizable(False,False)

		self.app.grid()

		frame_ch_accees = LabelFrame(self.app, text = "gestion des chemins d'accées", padx = 5, pady = 5)

		label_ch_sauv_image = Label(frame_ch_accees, text = "Chemin d'accès image: ")
		self.app.entry_ch_accees_image = Entry(frame_ch_accees)

		label_ch_sauv_image.grid(row = 0, column = 0)
		self.app.entry_ch_accees_image.grid(row = 0, column = 1, sticky = 'EW')

		label_ch_log = Label(frame_ch_accees, text = "Chemin d'accès log: ")
		self.app.entry_ch_log = Entry(frame_ch_accees)

		label_ch_log.grid(row = 1, column = 0, sticky = 'E')		
		self.app.entry_ch_log.grid(row = 1, column = 1, sticky = 'EW')		

		frame_ch_accees.grid(row = 0, column = 0, sticky = "EW")


		frame_opt_canvas = LabelFrame(self.app, text = "gestion de la table de dessin", padx = 5, pady = 5)

		self.app.value_long = IntVar(frame_opt_canvas)
		scale_long = Scale(frame_opt_canvas,from_= 18, to = 50, showvalue = False, variable = self.app.value_long, orient = 'h')
		entry_long = Entry(frame_opt_canvas, textvariable = self.app.value_long, width = 10)
		label_long = Label(frame_opt_canvas, text = "longueur canvas: ")

		label_long.grid(row = 0, column = 0, sticky = 'E')
		scale_long.grid(row = 0, column = 1)
		entry_long.grid(row = 0, column = 2)

		self.app.value_hot = IntVar(frame_opt_canvas)
		scale_hot = Scale(frame_opt_canvas,from_= 18, to = 50, showvalue = False, variable = self.app.value_hot, orient = 'h')
		entry_hot = Entry(frame_opt_canvas, textvariable = self.app.value_hot, width = 10)		
		label_hot = Label(frame_opt_canvas, text = "hauteur canvas: ")

		label_hot.grid(row = 1, column = 0, sticky = 'E')
		scale_hot.grid(row = 1, column = 1)
		entry_hot.grid(row = 1, column = 2)

		self.app.value_epais = IntVar(frame_opt_canvas)
		scale_epais = Scale(frame_opt_canvas,from_= 1, to = 5, showvalue = False, variable = self.app.value_epais, orient = 'h')
		entry_epais = Entry(frame_opt_canvas, textvariable = self.app.value_epais, width = 10)		
		label_epais = Label(frame_opt_canvas, text = "épaisseur canvas: ")
		
		label_epais.grid(row = 2, column = 0, sticky = 'E')
		scale_epais.grid(row = 2, column = 1)
		entry_epais.grid(row = 2, column = 2)


		frame_opt_canvas.grid(row = 1, column = 0, sticky = 'EW')

		frame_bp_opt = Frame(self.app)

		self.app.bp_journal = Button(frame_bp_opt, text = "journal",command = self.ouvrir_journal)
		self.app.bp_journal.grid(row=0,column=0,sticky='W')

		frame_bp_opt.grid(row = 2, column = 0, sticky = "EW")

		frame_bp_command_inter = Frame(self.app)

		self.app.bp_appliquer = Button(frame_bp_command_inter, text = "Appliquer", command = self.sauv_configuration)
		self.app.bp_appliquer.grid(row=0,column=0,sticky='EW')

		self.app.bp_quit = Button(frame_bp_command_inter, text = "Quitter",command = self.quitter_interface)
		self.app.bp_quit.grid(row=0,column=1,sticky='EW')
		
		frame_bp_command_inter.grid(row = 3, column = 0, sticky = "EW")

		self.app.grid_columnconfigure(0,weight=1)
		self.app.grid_rowconfigure(0,weight=0)
		self.app.grid_rowconfigure(2,weight=1)
		self.app.mainloop()

	def initialize(self):
		"""
		self.grid()

		frame_ch_accees = LabelFrame(self, text = "gestion des chemins d'accées", padx = 5, pady = 5)

		label_ch_sauv_image = Label(frame_ch_accees, text = "Chemin d'accès image: ")
		self.entry_ch_accees_image = Entry(frame_ch_accees)

		label_ch_sauv_image.grid(row = 0, column = 0)
		self.entry_ch_accees_image.grid(row = 0, column = 1, sticky = 'EW')

		label_ch_log = Label(frame_ch_accees, text = "Chemin d'accès log: ")
		self.entry_ch_log = Entry(frame_ch_accees)

		label_ch_log.grid(row = 1, column = 0, sticky = 'E')		
		self.entry_ch_log.grid(row = 1, column = 1, sticky = 'EW')		

		frame_ch_accees.grid(row = 0, column = 0, sticky = "EW")


		frame_opt_canvas = LabelFrame(self, text = "gestion de la table de dessin", padx = 5, pady = 5)

		self.value_long = IntVar(frame_opt_canvas)
		scale_long = Scale(frame_opt_canvas,from_= 18, to = 50, showvalue = False, variable = self.value_long, orient = 'h')
		entry_long = Entry(frame_opt_canvas, textvariable = self.value_long, width = 10)
		label_long = Label(frame_opt_canvas, text = "longueur canvas: ")

		label_long.grid(row = 0, column = 0, sticky = 'E')
		scale_long.grid(row = 0, column = 1)
		entry_long.grid(row = 0, column = 2)

		self.value_hot = IntVar(frame_opt_canvas)
		scale_hot = Scale(frame_opt_canvas,from_= 18, to = 50, showvalue = False, variable = self.value_hot, orient = 'h')
		entry_hot = Entry(frame_opt_canvas, textvariable = self.value_hot, width = 10)		
		label_hot = Label(frame_opt_canvas, text = "hauteur canvas: ")

		label_hot.grid(row = 1, column = 0, sticky = 'E')
		scale_hot.grid(row = 1, column = 1)
		entry_hot.grid(row = 1, column = 2)

		self.value_epais = IntVar(frame_opt_canvas)
		scale_epais = Scale(frame_opt_canvas,from_= 1, to = 5, showvalue = False, variable = self.value_epais, orient = 'h')
		entry_epais = Entry(frame_opt_canvas, textvariable = self.value_epais, width = 10)		
		label_epais = Label(frame_opt_canvas, text = "épaisseur canvas: ")
		
		label_epais.grid(row = 2, column = 0, sticky = 'E')
		scale_epais.grid(row = 2, column = 1)
		entry_epais.grid(row = 2, column = 2)


		frame_opt_canvas.grid(row = 1, column = 0, sticky = 'EW')

		frame_bp_opt = Frame(self)

		self.bp_journal = Button(frame_bp_opt, text = "journal",command = self.ouvrir_journal)
		self.bp_journal.grid(row=0,column=0,sticky='W')

		frame_bp_opt.grid(row = 2, column = 0, sticky = "EW")

		frame_bp_command_inter = Frame(self)

		self.bp_appliquer = Button(frame_bp_command_inter, text = "Appliquer", command = self.sauv_configuration)
		self.bp_appliquer.grid(row=0,column=0,sticky='EW')

		self.bp_quit = Button(frame_bp_command_inter, text = "Quitter",command = self.quitter_interface)
		self.bp_quit.grid(row=0,column=1,sticky='EW')
		
		frame_bp_command_inter.grid(row = 3, column = 0, sticky = "EW")

		self.grid_columnconfigure(0,weight=1)
		self.grid_rowconfigure(0,weight=0)
		self.grid_rowconfigure(2,weight=1)
		"""
		pass

	def sauv_configuration(self):
		tkinter.messagebox.showinfo("Information","Boutton <Appliquer> non implémenté \n Prochainement!!")

	def quitter_interface(self):
		self.app.quit()

	def ouvrir_journal(self):
		inter_journal = Interface_journal(None)

	def get_param(self):
		print("canvas longueur:", self.value_long.get(), "canvas hauteur:", self.value_hot.get(), "canvas epaisseur:", self.value_epais.get())

if __name__ == "__main__":
	app = Options(None)


