
import rdflib 

from StringIO import StringIO
from rdflib import Graph, URIRef

contents = '''\
subject1\tpredicate1\tobject1
subject2\tpredicate2\tobject2'''  
tabfile = StringIO(contents)

graph = rdflib.Graph()

for line in tabfile:
    triple = line.split()                # triple is now a list of 3 strings
    triple = (URIRef(t) for t in triple) # we have to wrap them in URIRef
    graph.add(triple)                    # and add to the graph


print graph.serialize(format='nt')
