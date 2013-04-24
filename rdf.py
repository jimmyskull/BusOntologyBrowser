# -*- encoding: utf-8 -*-
#!/usr/bin/python2
import rdfextras
import rdflib
rdfextras.registerplugins()


g = rdflib.Graph()
g.parse("bus_ontology_browser.rdf")

results = g.query("""PREFIX a:<http://ontokem.egc.ufsc.br/ontologia#> 
                     SELECT ?linhas
                     WHERE {?linhas rdf:type a:Linhas } """)


for r in results:
	print r[0]


g.add((rdflib["novaLinha"],"rdf:type","Linhas"))
g.commit()

results = g.query("""PREFIX a:<http://ontokem.egc.ufsc.br/ontologia#> 
                     SELECT ?linhas
                     WHERE {?linhas rdf:type a:Linhas } """)


for r in results:
	print r[0]
