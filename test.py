import rdflib
import rdfextras
from rdflib import URIRef

rdfextras.registerplugins()



g = rdflib.Graph()
g.parse("http://dbpedia.org/resource/Elvis_Presley")


name = g.subject_objects(URIRef("http://dbpedia.org/property/name"))
birth = g.subject_objects(URIRef("http://dbpedia.org/ontology/birthDate"))

print "bla"

for b in birth:
     print "Data de nascimento: {}".format(b[1])
for n in name:
     print "Nome de nascimento: ", str(n[1])

