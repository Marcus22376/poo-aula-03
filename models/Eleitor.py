from .TituloEleitor import TituloEleitor

class Eleitor:
    def __init__(self, nome, idade, titulo: TituloEleitor):
        self.nome = nome
        self.idade = idade
        self.titulo = titulo

    def apto_a_votar(self):
        """Retorna True se o eleitor pode votar, False caso contrário"""
        return self.idade >= 16

    def tipo_voto(self):
        """Define se o voto é obrigatório ou facultativo"""
        if self.idade < 16:
            return "Não pode votar"
        elif 16 <= self.idade < 18 or self.idade > 70:
            return "Voto facultativo"
        else:
            return "Voto obrigatório"
