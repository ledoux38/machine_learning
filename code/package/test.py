#!usr/bin/python3.5
#-*-coding:UTF-8 -*



"""
import tkinter
class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        label = tkinter.Label(self,anchor="center",bg="green")
        label.grid(column=0,row=0,sticky='EW')

        label2 = tkinter.Label(self,anchor="center",bg="black")
        label2.grid(column=1,row=0,sticky='EW')

        label3 = tkinter.Label(self,anchor="center",bg="red")
        label3.grid(column=2,row=0,sticky='EW')

        label4 = tkinter.Label(self,anchor="center",bg="purple")
        label4.grid(column=0,row=1,sticky='EW')

        label5 = tkinter.Label(self,anchor="center",bg="blue")
        label5.grid(column=1,row=1,sticky='EW')

        label6 = tkinter.Label(self,anchor="center",bg="yellow")
        label6.grid(column=2,row=1,sticky='EW')


        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)

        self.grid_columnconfigure(2,weight=1)
        #self.grid_rowconfigure(0,weight=1)
        #self.grid_rowconfigure(1,weight=1)
"""
#//////////////////////////////////////////////////////////////////////////////
"""

from tkinter import *
class simpleapp_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        

        self.initialize()

    def initialize(self):
        self.grid()

        canvas = Canvas(self,background = 'yellow').grid(row=0,column=0,columnspan=4,sticky='NSEW')

        bp_generer = Button(self, text = "Generer").grid(row=1,column=0,sticky='EW')

        bp_recommencer = Button(self, text = "Recommencer").grid(row=1,column=1,sticky='EW')

        bp_journal = Button(self, text = "journal").grid(row=1,column=2,sticky='EW')

        bp_quit = Button(self, text = "Fermer").grid(row=1,column=3,sticky='EW')


        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)

        self.grid_rowconfigure(0,weight=10)
        self.grid_rowconfigure(1,weight=0)


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title("MNIST")
    app.resizable(False,False)
    app.mainloop()
"""
"""
from tkinter import *
class simpleapp_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)

        self.initialize()

    def initialize(self):
        
        self.canvas = Canvas(self,background = 'yellow')
        self.canvas.grid(row=0,column=0,columnspan=1,sticky='NSEW')
        self.canvas.bind("<B1-Motion>", self.creation_ligne)
        self.canvas.bind("<ButtonPress-3>",self.tout_supprimer)

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def creation_ligne(self,event):
    	self.canvas.create_rectangle((event.x,event.y),(event.x,event.y),fill = 'red')

    def tout_supprimer(self,event):
    	self.canvas.delete(ALL)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title("MNIST")
    app.resizable(False,False)
    app.mainloop()
"""
"""
from tkinter import *
root = Tk()

def key(event):
    print ("pressed", repr(event.char))

def callback(event):
	canvas.create_rectangle((event.x,event.y),(event.x,event.y),fill = 'red')
	print ("clicked at", event.x, event.y)

canvas= Canvas(root, width=1000, height=1000)
canvas.bind("<Key>", key)
canvas.bind("<B1-Motion>", callback)
canvas.pack()

root.mainloop()
"""
"""
from tkinter import *

class interface_canvas(Canvas):
	def __init__ (self, parent, hauteur = 48, longueur = 48):
		Canvas.__init__(self, parent, height = hauteur, width = longueur)

		self.bind("<B1-Motion>", self.creation_forme)
		self.bind("<ButtonRelease>",self.reset_position)
		self.old_position = (0,0)

	def creation_forme(self,event):
		if self.old_position == (0,0):
			self.old_position = (event.x,event.y)

		else:
			self.create_line(self.old_position,(event.x,event.y),width = 10)
			self.old_position = (event.x,event.y)
			
		#print(i,self.index(i,0))

	def reset_position(self,event):
		self.old_position = (0,0)

	def tout_supprimer(self):
		self.delete(ALL)

if __name__ == "__main__":
	app = Tk()
	canvas = interface_canvas(app, 1000, 1000)
	canvas.pack()

	app.mainloop()

"""

"""
from tkinter import *
import tkinter.messagebox

class Interface_principale(Tk):
	def __init__(self,parent):
		Tk.__init__(self,parent)

		self.initialize()

	def initialize(self):
		self.grid()

		menu_bar = Menu(self)
		menu_fichier = Menu(menu_bar, tearoff = 0)
		menu_fichier.add_command(label = "Generer", command = self.generer)
		menu_fichier.add_command(label = "Recommencer", command = self.recommencer_dessin)
		menu_fichier.add_command(label = "Option", command = self.ouvrir_option)
		menu_fichier.add_command(label = "Quitter", command = self.quitter_interface)
		menu_bar.add_cascade(label = "Fichier", menu = menu_fichier)
		
		
		self.config(menu = menu_bar)

		self.canvas = Canvas(self, width = 100, height = 100)
		self.canvas.grid(row=0,column=0,columnspan = 2, rowspan = 4, sticky = "NWSE")

		self.bp_generer = Button(self, text = "Generer", command = self.generer)
		self.bp_generer.grid(row=0,column=2,sticky='EW')

		self.bp_recommencer = Button(self, text = "Recommencer", command = self.recommencer_dessin)
		self.bp_recommencer.grid(row=1,column=2,sticky='EW')

		
		#self.bp_journal = Button(self, text = "journal",command = self.ouvrir_journal)
		#self.bp_journal.grid(row=1,column=2,sticky='EW')
		

		self.bp_quit = Button(self, text = "Quitter",command = self.quitter_interface)
		self.bp_quit.grid(row=2,column=2,sticky='EW')

		self.grid_columnconfigure(0,weight=1)
		self.grid_rowconfigure(0,weight=0)
		self.grid_rowconfigure(1,weight=0)

	def quitter_interface(self):
		self.quit()

	def ouvrir_journal(self):
		inter_journal = Interface_journal(None)

	def recommencer_dessin(self):
		self.canvas.tout_supprimer()

	def generer(self):
		tkinter.messagebox.showinfo("Information","Boutton <generer> non implémenté \n Prochainement!!")

	def ouvrir_option(self):
		tkinter.messagebox.showinfo("Information","Boutton <option> non implémenté \n Prochainement!!")


if __name__ == "__main__":
	app = Interface_principale(None)
	app.title("MNIST")
	#app.resizable(False,False)
	app.mainloop()

"""
"""
from tkinter import *
import tkinter.messagebox

class Interface_principale(Tk):
	def __init__(self,parent):
		Tk.__init__(self,parent)

		self.initialize()

	def initialize(self):
		self.grid()

		menu_bar = Menu(self)
		menu_fichier = Menu(menu_bar, tearoff = 0)
		menu_fichier.add_command(label = "Generer", command = self.generer)
		menu_fichier.add_command(label = "Recommencer", command = self.recommencer_dessin)
		menu_fichier.add_command(label = "Option", command = self.ouvrir_option)
		menu_fichier.add_command(label = "Quitter", command = self.quitter_interface)
		menu_bar.add_cascade(label = "Fichier", menu = menu_fichier)
		
		
		self.config(menu = menu_bar)

		self.canvas = Canvas(self, width = 100, height = 100)
		self.canvas.grid(row=0,column=0, rowspan = 3, sticky = "NWSE")

		self.bp_generer = Button(self, text = "Generer", command = self.generer)
		self.bp_generer.grid(row=0,column=2,sticky='EW')

		self.bp_recommencer = Button(self, text = "Recommencer", command = self.recommencer_dessin)
		self.bp_recommencer.grid(row=1,column=2,sticky='EW')

		
		#self.bp_journal = Button(self, text = "journal",command = self.ouvrir_journal)
		#self.bp_journal.grid(row=1,column=2,sticky='EW')
		

		self.bp_quit = Button(self, text = "Quitter",command = self.quitter_interface)
		self.bp_quit.grid(row=4,column=2,sticky='EW')

		self.grid_columnconfigure(0,weight=1)
		self.grid_rowconfigure(0,weight=0)
		self.grid_rowconfigure(2,weight=1)

	def quitter_interface(self):
		self.quit()

	def ouvrir_journal(self):
		inter_journal = Interface_journal(None)

	def recommencer_dessin(self):
		self.canvas.tout_supprimer()

	def generer(self):
		tkinter.messagebox.showinfo("Information","Boutton <generer> non implémenté \n Prochainement!!")

	def ouvrir_option(self):
		tkinter.messagebox.showinfo("Information","Boutton <option> non implémenté \n Prochainement!!")


if __name__ == "__main__":
	app = Interface_principale(None)
	app.title("MNIST")
	#app.resizable(False,False)
	app.mainloop()

"""

"""
from tkinter import *
import tkinter.messagebox

class Interface_option(Tk):
	def __init__(self,parent):
		Tk.__init__(self,parent)
		self.title("Options")
		self.initialize()
		self.resizable(False,False)

	def initialize(self):
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

		#self.bp_journal = Button(self, text = "journal",command = self.ouvrir_journal)
		#self.bp_journal.grid(row=1,column=2,sticky='EW')


		frame_bp_command_inter = Frame(self)

		self.bp_appliquer = Button(frame_bp_command_inter, text = "Appliquer", command = self.sauv_configuration)
		self.bp_appliquer.grid(row=0,column=0,sticky='EW')

		self.bp_quit = Button(frame_bp_command_inter, text = "Quitter",command = self.quitter_interface)
		self.bp_quit.grid(row=0,column=1,sticky='EW')
		
		frame_bp_command_inter.grid(row = 2, column = 0, sticky = "EW")

		self.grid_columnconfigure(0,weight=1)
		self.grid_rowconfigure(0,weight=0)
		self.grid_rowconfigure(2,weight=1)

	def sauv_configuration(self):
		tkinter.messagebox.showinfo("Information","Boutton <Appliquer> non implémenté \n Prochainement!!")

	def quitter_interface(self):
		self.destroy()

	def ouvrir_journal(self):
		inter_journal = Interface_journal(None)

	def get_value_adress_picture(self):
		pass

	def get_value_adress_log(self):
		pass

	def get_value_longueur_canvas(self):
		pass

	def get_value_hauteur_canvas(self):
		pass

	def get_value_epaisseur(self):
		pass

	def set_value_adress_picture(self, value):
		pass

	def set_value_adress_log(self, value):
		pass

	def set_value_longueur_canvas(self, value):
		pass

	def set_value_hauteur_canvas(self, value):
		pass

	def set_value_epaisseur(self, value):
		pass

if __name__ == "__main__":
	app = Interface_option(None)
	app.mainloop()

"""

"""
from tkinter import *
from numpy import *

class interface_canvas(Canvas):
	def __init__ (self, parent, hauteur = 48, longueur = 48, outline = "black"):
		Canvas.__init__(self, parent, height = hauteur, width = longueur)

		self.bind("<B1-Motion>", self.creation_forme)
		self.bind("<ButtonRelease>",self.reset_position)
		self.bind("<ButtonPress-3>",self.tableau_numpy)
		self.old_position = (0,0)
		self.tableau = zeros((hauteur,longueur),dtype = 'i')

	def creation_forme(self,event):
		if self.old_position == (0,0):
			self.old_position = (event.x,event.y)

		else:
			i = self.create_line(self.old_position,(event.x,event.y))
			self.old_position = (event.x,event.y)
		print(i,self.coords(i))
		variable_x = self.coords(i)
		variable_x = variable_x[0]
		variable_y = self.coords(i)
		variable_y = variable_y[1]
		self.tableau[variable_x][variable_y] = 1

		print(variable_x,"  :  ",variable_y)

	def reset_position(self,event):
		self.old_position = (0,0)

	def tout_supprimer(self):
		self.delete(ALL)

	def tableau_numpy(self,event):
		print(self.tableau)

if __name__ == "__main__":
	app = Tk()
	canvas = interface_canvas(app, 50, 50)
	canvas.pack()

	app.mainloop()
"""

from tkinter import *
from numpy import *

tableau = zeros((50,50),dtype = 'i')
tableau[40][40] = 5
print(tableau)
