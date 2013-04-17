#!/usr/bin/python2
# Desinstalar futuramente:
#	python2-rdflib 
# 	python2-pyparsing
# 	python2-rdfextras
# 	extra/libtracker-sparql 
# 	aur/python2-sparqlwrapper
# 	python2-isodate
# 	python2-pyparsing
import rdflib
import rdfextras
rdfextras.registerplugins()

filename = "ontology.rdf"

g = rdflib.Graph()
g.parse(filename)

results = g.query("""
SELECT 
	?p ?o
WHERE {
	?s ?p ?o.
}
""")

for r in results:
	print r
