#!/usr/bin/python2
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
