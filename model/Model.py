# -*- encoding: utf-8 -*-

import rdflib
import rdfextras

class Model(object):
	def __init__(self, filename):
		self.filename = filename
		rdfextras.registerplugins()
		self.g = rdflib.Graph()
		self.g.parse(filename)

	def finish(self):
		f = open('bus_ontology.rdf', 'w')
		f.write(str(self.g.serialize()))
		f.close()
		self.g.close()
