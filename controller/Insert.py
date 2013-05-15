import rdflib
from rdflib import ConjunctiveGraph, plugin, Namespace, Literal, URIRef
from rdflib.store import NO_STORE, VALID_STORE, Store

from tempfile import mkdtemp

default_graph_uri = "http://ontokem.egc.ufsc.br/ontologia#"
configString = "/var/tmp/rdfstore"

graph = rdflib.Graph()
graph.parse("bus_ontology.rdf")
rt = graph.open("bus_ontology.rdf", create=False)
rdflib = Namespace('http://ontokem.egc.ufsc.br/ontologia#')
graph.bind("base", "http://ontokem.egc.ufsc.br/ontologia#")

graph.add((rdflib['linha_Santa_Cruz'], rdflib['name'], Literal('Santa Cruz')))

graph.commit()

f = open('bus_ontology.rdf', 'w+')
f.write(graph.serialize())
f.close()

graph.close()
