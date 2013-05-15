# -*- encoding: utf-8 -*-
#!/usr/bin/python2
import rdfextras
import rdflib 
from rdflib.graph import ConjunctiveGraph
from rdflib import plugin, BNode, Literal, RDF, Namespace
from StringIO import StringIO
from rdflib import Graph, URIRef

rdfextras.registerplugins()


g = rdflib.Graph()
g.parse("bus_ontology_browser.rdf")

results = g.query("""PREFIX a:<http://ontokem.egc.ufsc.br/ontologia#> 
                     SELECT ?linhas
                     WHERE {?linhas rdf:type a:Linhas } """)


for r in results:
	print r[0]


contents = '''\
subject1\tpredicate1\tobject1
subject2\tpredicate2\tobject2'''  
tabfile = StringIO(contents)


for line in tabfile:
    triple = line.split()                # triple is now a list of 3 strings
    triple = (URIRef(t) for t in triple) # we have to wrap them in URIRef
    g.add(triple)                    # and add to the graph

g.commit()
g.

results = g.query("""PREFIX a:<http://ontokem.egc.ufsc.br/ontologia#> 
                     SELECT ?p ?o
                     WHERE {a:subject1 ?p ?o } """)





for r in results:
	print r[0]

