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

g = rdflib.Graph()
g.parse("ontology.rdf")

results = g.query("""
SELECT 
	?s ?p ?o
WHERE {
	?s ?p ?o.
}
""")

for r in results:
	print r
