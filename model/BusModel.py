# -*- encoding: utf-8 -*-
from Model import Model

import rdflib
import rdfextras


class BusModel(Model):
	def __init__(self, filename):
		Model.__init__(self, filename)

	def busca_horarios_para_local(self, local):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?horas
			WHERE { a:local_Banco_do_Brasil a:temPontoMaisProximo ?ponto.
			?linha a:temPontos ?ponto.
			?linha a:temHorarios ?horarios.
			?horarios a:temHora ?horas}
			""".format(local=local))
		return results

	def buscar_linhas_em_um_ponto(self, ponto):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?nome
			WHERE {{ ?linha a:temPontos a:{ponto}.
			?linha a:temNome ?nome.}}
			""".format(ponto=ponto))
		return results

	def busca_horarios_linha(self, linha):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?horas
			WHERE { a:linha_Karpinsky a:temHorarios ?horarios.
			?horarios a:temHora ?horas.}
			""".format(ponto=ponto))
		return results

	def busca_itinerario_para_local(self, local):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?itinerario
			WHERE { a:local_Banco_do_Brasil a:temPontoMaisProximo ?ponto.
			?linha a:temPontos ?ponto.
			?itinerario a:temLinhas ?linha}
			""".format(ponto=ponto))
		return results

	def busca_ponto_proximo_local(self, local):
		results = self.g.query("""
			prefix a:<http://ontokem.egc.ufsc.br/ontologia#>
			SELECT ?itinerario
			WHERE { a:local_Banco_do_Brasil a:temPontoMaisProximo ?ponto.
			?linha a:temPontos ?ponto.
			?itinerario a:temLinhas ?linha}
			""".format(ponto=ponto))
		return results


if __name__ == '__main__':
	bm = BusModel("../ontology.rdf")
	bm.buscar_linhas_em_um_ponto("terminal_Fonte")