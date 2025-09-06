import csv
import os

# Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade, email, contato):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.contato = contato

    def to_list(self):
        return [self.nome, self.idade, self.email, self.contato]

# Classe CRUD
class CadastroPessoas:
    ARQUIVO = "pessoas.csv"

    def __init__(self):
        # Se não existir o arquivo, cria com cabeçalho
        if not os.path.exists(self.ARQUIVO):
            with open(self.ARQUIVO, mode="w", newline="") as f:
                escritor = csv.writer(f)
                escritor.writerow(["Nome", "Idade", "Email", "Contato"])

    def adicionar(self, pessoa: Pessoa):
        with open(self.ARQUIVO, mode="a", newline="") as f:
            escritor = csv.writer(f)
            escritor.writerow(pessoa.to_list())
        print("✅ Pessoa cadastrada com sucesso!")

    def listar(self):
        with open(self.ARQUIVO, mode="r") as f:
            leitor = csv.reader(f)
            for i, linha in enumerate(leitor):
                if i == 0:
                    continue  # pula cabeçalho
                print(linha)

    def atualizar(self, email, novo_nome, nova_idade, nova_contato):
        linhas = []
        atualizado = False
        with open(self.ARQUIVO, mode="r") as f:
            leitor = csv.reader(f)
            for linha in leitor:
                if linha and linha[2] == email:
                    linha[0] = novo_nome
                    linha[1] = nova_idade
                    linha[3] = nova_contato
                    atualizado = True
                linhas.append(linha)
        with open(self.ARQUIVO, mode="w", newline="") as f:
            escritor = csv.writer(f)
            escritor.writerows(linhas)
        if atualizado:
            print("✅ Cadastro atualizado com sucesso!")
        else:
            print("⚠️ Pessoa não encontrada.")

    def excluir(self, email):
        linhas = []
        excluido = False
        with open(self.ARQUIVO, mode="r") as f:
            leitor = csv.reader(f)
            for linha in leitor:
                if linha and linha[2] != email:
                    print("log ", linha, linha[2], email)
                    linhas.append(linha)
                else:
                    print("log else ", linha, linha[2], email)
                    excluido = True
        with open(self.ARQUIVO, mode="w", newline="") as f:
            escritor = csv.writer(f)
            escritor.writerows(linhas)
        if excluido:
            print("🗑️ Pessoa excluída com sucesso!")
        else:
            print("⚠️ Pessoa não encontrada.")

def menu():
    cadastro = CadastroPessoas()

    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Atualizar Pessoa")
        print("4 - Excluir Pessoa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            idade = input("Idade: ")
            email = input("Email: ")
            contato = input("Contato: ")
            pessoa = Pessoa(nome, idade, email, contato)
            cadastro.adicionar(pessoa)

        elif opcao == "2":
            cadastro.listar()

        elif opcao == "3":
            email = input("Digite o email da pessoa que deseja atualizar: ")
            novo_nome = input("Novo nome: ")
            nova_idade = input("Nova idade: ")
            nova_contato = input("Novo Contato: ")
            cadastro.atualizar(email, novo_nome, nova_idade, nova_contato)

        elif opcao == "4":
            email = input("Digite o email da pessoa que deseja excluir: ")
            confirmacao = input(" Deseja realmente excluir esta pessoa? (s/n): ").strip().lower()
            if confirmacao == 's':
                cadastro.excluir(email)
            else:
                print("Excluição de Pessoa Cancelada!!!")

        elif opcao == "5":
            print("👋 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
