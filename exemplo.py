from models.Eleitor import Eleitor
from models.Urna import Urna
from models.TituloEleitor import TituloEleitor


titulo = TituloEleitor("123456", "101", "12")
eleitor = Eleitor("Maria", 19, titulo)
urna = Urna("Cidade X", "101", "12")

print(eleitor.tipo_voto())
print("Pode votar nesta urna?", urna.pode_receber(eleitor))

