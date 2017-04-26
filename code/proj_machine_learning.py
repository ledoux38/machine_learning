#!usr/bin/python3.5
#-*-coding:UTF-8 -*

import tkinter as Tk
import tkinter.ttk as ttk
from functools import partial
import threading

import package.interface_principale as ip

try:
	import package.progress_bar as pb
except:
	import progress_bar as pb

try:
	import package.load_image as li	
except:
	import load_image as li


def affichage_choix(parent):
	frame_principal = Tk.Frame(parent)
	frame_principal.grid(row = 0, column = 0)

	bp_interface_mnist = Tk.Button(frame_principal, text = "Interface mnist", command = partial(interface_mnist, parent, frame_principal))
	bp_interface_mnist.grid(row = 1, column = 0, sticky = 'EW')

	bp_etude_image = Tk.Button(frame_principal, text = "Chargement image", command = partial(interface_etude_image, parent))
	bp_etude_image.grid(row = 2, column = 0, sticky = 'EW')

	bp_quitter = Tk.Button(frame_principal, text = "Quitter", command = partial(quitter, parent))
	bp_quitter.grid(row = 3, column = 0, sticky = 'EW')



def quitter(parent):
	parent.quit()


def interface_mnist(parent, frame):
	frame.destroy()

	frame_principal = Tk.Frame(parent)
	frame_principal.grid(row = 0, column = 0)

	barre_proression=ttk.Progressbar(frame_principal, mode="indeterminate")
	barre_proression.grid(row = 1, column = 0, sticky = 'EW')
	barre_proression.start(interval = 1)

	parent.update()

	interface_mnist = ip.Interface_principale()

	parent.update()

	interface_mnist.initialisation_machine_learning(parent)

	barre_proression.stop()

	if parent is not None:
		parent.destroy()

	#creation de l'instance interface_principale
	app = Tk.Tk()

	interface_mnist.interface_principale(app)
	app.mainloop()
	app.destroy()


def interface_etude_image(parent):
	if parent is not None:
		parent.destroy()

	#creation de l'instance load_image
	etude_image = li.load_image()
	etude_image.interface_load_image(parent)



if __name__ == "__main__":

	app = Tk.Tk()
	affichage_choix(parent = app)
	#affichage de la fenetre
	app.mainloop()




