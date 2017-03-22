#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import logging

from logging.handlers import RotatingFileHandler

class log:
	def __init__(self):

		if not isinstance(chemin_log, str) or not isinstance(str_formatter, str):
			raise TypeError("erreur chemin_log = {} ou str_formatter = {} n'est pas de type str ".format(type(chemin_log), type(str_formatter)))

		#recuperation ch fichier
		self.ch_log = ("log/activity.log")

		#recuperation str_formatter
		self.format_log = ("%(asctime)s :: %(levelname)s :: %(message)s")

		# création de l'objet logger servir à écrire les logs
		self.logger = logging.getLogger()

		# on met le niveau du logger à DEBUG, comme ça il écrit tout
		self.logger.setLevel(logging.DEBUG)
 
		# création d'un formateur 
		formatter = logging.Formatter(self.format_log)

		# création d'un handler qui va rediriger une écriture du log vers un fichier en mode 'append'
		file_handler = RotatingFileHandler(self.ch_log, 'a', 1000000, 1)

		# on lui met le niveau sur DEBUG
		file_handler.setLevel(logging.DEBUG)
		file_handler.setFormatter(formatter)
		self.logger.addHandler(file_handler)
		 
		# création d'un second handler qui redirige l'écriture de log sur la console
		steam_handler = logging.StreamHandler()
		steam_handler.setLevel(logging.DEBUG)
		self.logger.addHandler(steam_handler)
		
	def ecriture_log(self, type_message, message):
		"""
		methode de classe qui permet d'ecrire dans le fichier log'
		"""
		if not isinstance(type_message, str) or not isinstance(message, str):
			raise TypeError("erreur type_message = {} ou message = {} n'est pas de type str ".format(type(type_message), type(message)))
			

		if type_message is "critical":
			self.logger.critical(message)

		elif type_message is "error":
			self.logger.error(message)

		elif type_message is "warning":
			self.logger.warning(message)

		elif type_message is "info":
			self.logger.info(message)

		elif type_message is "debug":
			self.logger.debug(message)
		
		else:
			raise ValueError("erreur dans le type de message les posibilités sont: (info|warn|debug|error|critical)")

	def lecture_log(self):
		"""
		methode de classe qui permet de recuperer le fichier txt du log
		"""
		with open(self.ch_log, 'rb') as fichier:
			mon_fichier = pickle.Unpickler(fichier)
			parametre = mon_fichier.load()
			return parametre




if __name__ == "__main__":
	a = log()
	a.ecriture_log('info', 'message1')
	

