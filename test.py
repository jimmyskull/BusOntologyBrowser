
import rdflib
import rdfextras
# from rdflib import sparql


rdfextras.registerplugins()


g = rdflib.Graph()
g.parse("bus_ontology.rdf")

# results = g.query("""PREFIX a:<http://ontokem.egc.ufsc.br/ontologia#> 
#                      SELECT ?linhas
#                      WHERE {?linhas rdf:type a:Linhas} """)
results = g.query("""PREFIX a:<http://ontokem.egc.ufsc.br/ontologia#> 
                     SELECT DISTINCT ?linhas
                     WHERE {
                     	?linhas rdf:type ?type
                     	{?linhas rdf:type "Linhas"}
                     UNION
                     	{?linhas rdf:type a:Linhas}
                     } """)
# processUpdate(g, """PREFIX a:<http://ontokem.egc.ufsc.br/ontologia#> 
#                      DELETE ?linhas
#                      WHERE {
#                      	a:Linhas a:temNome "llllll"
#                      } """)


for r in results:
	print r[0]


