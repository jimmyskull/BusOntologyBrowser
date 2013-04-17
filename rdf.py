# -*- encoding: utf-8 -*-
#!/usr/bin/python2
import rdflib
import rdfextras

rdfextras.registerplugins()

g = rdflib.Graph()
g.parse("ontology.rdf")

results = g.query("""
prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
SELECT ?itinerario
WHERE { a:local_Banco_do_Brasil a:temPontoMaisProximo ?ponto.
	?linha a:temPontos ?ponto.
	?itinerario a:temLinhas ?linha}
""")

for r in results:
	print r[0]
