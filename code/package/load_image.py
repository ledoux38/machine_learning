#!usr/bin/python3.5
#-*-coding:UTF-8 -*
 
 
from tkinter import *
from tkinter.filedialog import *
from numpy import *
from functools import partial
from PIL import Image, ImageFont, ImageDraw, ImageTk
import scipy.ndimage

class load_image:
	#cette classe chargent des images
 
 
	def __init__(self, option = {"ch_img":"./test", "h_canvas":100, "l_canvas":100, }):
		if not isinstance(option, dict):
			raise TypeError("erreur option = {} n'est pas de type list ".format(type(option)))

		#liste les options
		self.option = option
		self.img_convert = None
		self.tableau = None



	def interface_load_image(self,object_tk):
		#methode de class qui creer l'interface graphique

		frame_principal = Frame(object_tk)
		frame_principal.grid(row = 0, column = 0, sticky='NSEW')
		label = Label(frame_principal)
		label.grid(row = 0, column = 0)
 
		frame_bp = Frame(frame_principal)
		frame_bp.grid(row = 1, column = 0, sticky='NSEW')
 
		bp_charger = Button(frame_bp, text = "Charger",command = partial(self.Charger, label))
		bp_charger.grid(row=0,column=0,sticky='W')
 
		bp_generer = Button(frame_bp, text = "Generer",command = partial(self.generer))
		bp_generer.grid(row=0,column=1,sticky='W')
 
		bp_annuler = Button(frame_bp, text = "Fermer",command = partial(self.quitter_interface, object_tk))
		bp_annuler.grid(row=0,column=2,sticky='W')
 
		#frame_principal.grid_columnconfigure(0,weight=1)
		#frame_principal.grid_rowconfigure(0,weight=0)
		#frame_principal.grid_rowconfigure(1,weight=1)



	def quitter_interface(self, object_tk):
		#methode de class qui permet de quitter le programme
		object_tk.quit()



	def Charger(self, object_label):
		#methode de class qui permet de reset le canevas

		load = askopenfilename(defaultextension = ".JPG", initialdir = self.option["ch_img"])

		if not load:
			return None
			print("annuler")
		else:
			self.create_data(file_img = load)
			image = Image.open(load)
			self.img_convert = ImageTk.PhotoImage(image)
			object_label.configure(image = self.img_convert)



	def generer(self):
		pass

	def create_data(self, file_img):
		self.tableau = scipy.ndimage.imread(file_img, flatten=True)



if __name__ == "__main__":

	limg = load_image()
	app = Tk()
	limg.interface_load_image(app)
	app.mainloop()