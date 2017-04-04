#!usr/bin/python3.5
#-*-coding:UTF-8 -*
import tkinter as Tk
import package.interface_principale as Ip

#instanciation de la classe 
a = Ip.Interface_principale()

#creation de la fenetre principale
app = Tk.Tk()

#integration de la fenetre principale dans la fenetre principale
a.interface_principale(app)

#modification des options
app.title("MNIST")
app.resizable(False, False)

#affichage de la fenetre
app.mainloop()

