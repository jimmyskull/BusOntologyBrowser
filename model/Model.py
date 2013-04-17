# -*- encoding: utf-8 -*-

import rdflib
import rdfextras

class Model(object):
	def __init__(self, filename):
		self.filename = filename
		rdfextras.registerplugins()
		self.g = rdflib.Graph()
		self.g.parse(filename)