# -*- encoding: utf-8 -*-
from Model import Model

import rdflib
import rdfextras


class BusModel(Model):
	def __init__(self, filename):
		Model.__init__(self, filename)

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
			SELECT ?nome
			WHERE {{ a:{0} a:temPontoMaisProximo ?ponto.
			?linha a:temPontos ?ponto.
			?itinerario a:temLinhas ?linha.
			?itinerario a:temNome ?nome.}}
			""".format(local))
		return results

	def buscar_ponto_proximo_local(self, local):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?nome
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

if __name__ == '__main__':
	bm = BusModel("../bus_ontology_browser.rdf")
	print "\n"
	for r in bm.buscar_horarios_para_local("local_CEDETEG"):
		print r[0]
	print "\n"
	for r in bm.buscar_linhas_em_um_ponto("terminal_Fonte"):
		print r[0]
	print "\n"
	for r in bm.buscar_horarios_linha("linha_Karpinsky"):
		print r[0]
	print "\n"
	for r in bm.buscar_itinerario_para_local("local_Banco_do_Brasil"):
		print r[0]
	print "\n"
	for r in bm.buscar_ponto_proximo_local("local_CEDETEG"):
		print r[0]
	print "\n"
	for r in bm.buscar_horarios_ponto_proximo_para_outro_local("local_Superpao_Hiper", "local_CEDETEG"):
		print r[0]
	print "\n"