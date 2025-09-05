from .Eleitor import Eleitor

class Urna:
    def __init__(self, cidade, zona, secao):
        self.cidade = cidade
        self.zona = zona
        self.secao = secao

    def pode_receber(self, eleitor: Eleitor):
        """Verifica se o eleitor vota nesta urna e se está apto"""
        if not eleitor.apto_a_votar():
            return False
        # verifica se o eleitor está na zona/secao correta
        return (self.zona == eleitor.titulo.zona) and (self.secao == eleitor.titulo.secao)
