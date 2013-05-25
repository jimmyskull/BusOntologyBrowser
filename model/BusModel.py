# -*- encoding: utf-8 -*-
from Model import Model
from Insert import Insert

import rdflib
import rdfextras
from rdflib import ConjunctiveGraph, plugin, Namespace, Literal, URIRef, XSD, RDF
from rdflib.store import NO_STORE, VALID_STORE, Store



class BusModel(Model):
	def __init__(self, filename):
		Model.__init__(self, filename)

	# Retorna lista de "Nome do local/ponto" "Ponto mais proximo/Ponto"
	def buscar_pontos_ou_locais(self, filtro):
		pontos = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?nome ?ponto
			WHERE { ?ponto a:temNome ?nome }
			""")
		locais = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?nome ?ponto
			WHERE { ?local a:temNome ?nome .
				?local a:temPontoMaisProximo ?ponto }
			""")
		f = filtro.lower()
		result = list(pontos) + list(locais)
		return filter(lambda r: f in r[0].lower(), result), pontos, locais


	def buscar_horarios_para_local(self, local):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?horas
			WHERE {{ a:{0} a:temPontoMaisProximo ?ponto.
			?linha a:temPontos ?ponto.
			?linha a:temHorarios ?horarios.
			?horarios a:temHora ?horas}}
			""".format(local))
		return results


	def buscar_ponto(self, ponto):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?nome
			WHERE {{ a:{0} a:temNome ?nome.}}
			""".format(ponto))
		return [list(results)[0][0], 'http://ontokem.egc.ufsc.br/ontologia#' + ponto]
		
	def buscar_linhas_em_um_ponto(self, ponto):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?nome
			WHERE {{ ?linha a:temPontos a:{0}.
			?linha a:temNome ?nome.}}
			""".format(ponto))
		return results

	def buscar_horarios_linha(self, linha):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?horas
			WHERE {{ a:{0} a:temHorarios ?horarios.
			?horarios a:temHora ?horas.}}
			""".format(linha))
		return results

	def buscar_itinerario_para_local(self, local):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?itinerario
			WHERE {{ a:{0} a:temPontoMaisProximo ?ponto.
			?linha a:temPontos ?ponto.
			?itinerario a:temLinhas ?linha.
			?itinerario a:temNome ?nome.}}
			""".format(local))
		return results
		
	def buscar_itinerario_para_ponto(self, ponto):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?itinerario
			WHERE {{ 
			?linha a:temPontos a:{0}.
			?itinerario a:temLinhas ?linha.
			?itinerario rdf:type ?Itinerarios.}}
			""".format(ponto))
		return results
	
	def buscar_qual_linha_tem_ponto_de_um_itinerario(self, itinerario, ponto):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?nome
			WHERE {{ a:{0} a:temLinhas ?linhas.
					 ?linhas a:temPontos a:{1}.
					 ?linhas a:temNome ?nome.
			}}""".format(itinerario, ponto))
		return list(results)
	
	def buscar_linhas_do_itinerario(self, itinerario):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?linhas
			WHERE {{ 
				a:{0} a:temLinhas ?linhas.
			}}""".format(itinerario))
		return results
		
	# nome pode ser um ponto ou local
	def buscar_ponto_origem_itinerario(self, origem, destino):
		origem_eh_local = 'local_' in origem
		destino_eh_local = 'local_' in destino
		if destino_eh_local:
			iti = self.buscar_itinerario_para_local(destino)
		else:
			iti = self.buscar_itinerario_para_ponto(destino)
		itinerario = list(iti)[0][0][37:]

		print 'ITINERARIO: ', itinerario
		
		if origem_eh_local:
			ptorigem = list(self.buscar_ponto_proximo_local(origem))[0]
			print '** ORIGEM1', ptorigem
			ResultadoOrigem = ptorigem
		else:
			print '** ORIGEM2', list(self.buscar_ponto(origem))
			ResultadoOrigem = list(self.buscar_ponto(origem))

		if destino_eh_local:
			ptdestino = list(self.buscar_ponto_proximo_local(destino))[0]
			print '** DESTINO1', ptdestino
			ResultadoDestino = ptdestino
		else:
			print '** DESTINO2', list(self.buscar_ponto(destino))
			ResultadoDestino = list(self.buscar_ponto(destino))
			
		linhaOrigem = self.buscar_qual_linha_tem_ponto_de_um_itinerario(itinerario, ResultadoOrigem[1][37:])
		linhaDestino = self.buscar_qual_linha_tem_ponto_de_um_itinerario(itinerario, ResultadoDestino[1][37:])
		return [ResultadoOrigem, linhaOrigem, ResultadoDestino, linhaDestino]
		

	def buscar_ponto_proximo_local(self, local):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?nome ?ponto
			WHERE {{ a:{0} a:temPontoMaisProximo ?ponto.
			?ponto a:temNome ?nome.}}
			""".format(local))
		return results

	def buscar_horarios_ponto_proximo_para_outro_local(self, start_local, end_local):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT DISTINCT ?horas
			WHERE {{ a:{0} a:temPontoMaisProximo ?pontoInicio.
			a:{1} a:temPontoMaisProximo ?pontoChegada.
			?linhaChegada a:temPontos ?pontoChegada.
			?linhaInicio a:temPontos ?pontoInicio.
			?itinerario a:temLinhas ?linhaChegada.
			?itinerario a:temLinhas ?linhaInicio.
			?pontoInicio a:temHorarios ?horariosInicio.
			?linhaChegada a:temHorarios ?horariosLinha.
			?horariosInicio a:temHora ?horas. }}
			""".format(start_local, end_local))
		return results
	
	def inserir_linha(self, linha, nome):
		rdflib = Namespace('http://ontokem.egc.ufsc.br/ontologia#')
		self.g.add((rdflib[linha], RDF.type, Literal("Linhas")))
		self.g.add((rdflib[linha], rdflib['temNome'], Literal(nome, datatype=XSD.string)))
		self.g.commit()

	def inserir_horarios_linha(self, linha, horarios):
		pass

	def inserir_pontos_linha(self, linha, pontos):
		pass

if __name__ == '__main__':
	bm = BusModel("../bus_ontology.rdf")
	# bm = BusModel("../bus_ontology_browser.rdf")
	# print "\n"
	# for r in bm.buscar_horarios_para_local("local_CEDETEG"):
	# 	print r[0]
	# print "\n"
	# for r in bm.buscar_linhas_em_um_ponto("terminal_Fonte"):
	# 	print r[0]
	# print "\n"
	bm.inserir_linha("linha_UNICENTRO11", "UNICENTRO11")
	for r in bm.buscar_horarios_linha("linha_Karpinsky"):
		print r[0]
	print "\n"
	# for r in bm.buscar_itinerario_para_local("local_Banco_do_Brasil"):
	# 	print r[0]
	# for r in bm.buscar_linhas_do_itinerario('itinerario_karpinski-tancredo'):
	# 	print r[0]

	# print bm.buscar_ponto_origem_itinerario('local_CEDETEG', 'ponto_Colegio_Belem')
	# raise
	# print "\n"
	# for r in bm.buscar_ponto_proximo_local("local_CEDETEG"):
	# 	print r[0]
	# print "\n"
	# for r in bm.buscar_horarios_ponto_proximo_para_outro_local("local_Superpao_Hiper", "local_CEDETEG"):
	# 	print r[0]
	# print "\n"
	# for r in bm.buscar_pontos_ou_locais("co"):
	# 	print r[0].encode('iso-8859-1'), r[1]
