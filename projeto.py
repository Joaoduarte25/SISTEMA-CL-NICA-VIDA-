class Paciente:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Telefone: {self.telefone}"

class Clinica:
    def __init__(self):
        self.pacientes = []

    def cadastrar_paciente(self):
        nome = input("Nome do paciente: ")
        try:
            idade = int(input("Idade: "))
        except ValueError:
            print("Idade inválida.")
            return
        telefone = input("Telefone: ")
        paciente = Paciente(nome, idade, telefone)
        self.pacientes.append(paciente)
        print("Paciente cadastrado com sucesso!")

    def ver_estatisticas(self):
        if not self.pacientes:
            print("Nenhum paciente cadastrado.")
            return
        total_pacientes = len(self.pacientes)
        idade_media = sum(p.idade for p in self.pacientes) / total_pacientes
        paciente_mais_novo = min(self.pacientes, key=lambda p: p.idade)
        paciente_mais_velho = max(self.pacientes, key=lambda p: p.idade)
        print(f"Total de pacientes: {total_pacientes}")
        print(f"Idade média: {idade_media:.2f}")
        print(f"Paciente mais novo: {paciente_mais_novo.nome} ({paciente_mais_novo.idade} anos)")
        print(f"Paciente mais velho: {paciente_mais_velho.nome} ({paciente_mais_velho.idade} anos)")

    def buscar_paciente(self):
        nome = input("Nome do paciente: ")
        for p in self.pacientes:
            if p.nome == nome:
                print(p)
                return
        print("Paciente não encontrado.")

    def listar_pacientes(self):
        if not self.pacientes:
            print("Nenhum paciente cadastrado.")
            return
        for p in self.pacientes:
            print(p)

class Fila:
    def __init__(self):
        self.pacientes = []

    def adicionar(self, paciente):
        self.pacientes.append(paciente)

    def remover(self):
        if not self.pacientes:
            return None
        return self.pacientes.pop(0)

    def imprimir(self):
        for p in self.pacientes:
            print(p)

def main():
    clinica = Clinica()
    fila = Fila()
    while True:
        print("=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Adicionar paciente à fila")
        print("6. Remover paciente da fila")
        print("7. Imprimir fila")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            clinica.cadastrar_paciente()
        elif opcao == "2":
            clinica.ver_estatisticas()
        elif opcao == "3":
            clinica.buscar_paciente()
        elif opcao == "4":
            clinica.listar_pacientes()
        elif opcao == "5":
            nome = input("Nome do paciente: ")
            for p in clinica.pacientes:
                if p.nome == nome:
                    fila.adicionar(p)
                    print("Paciente adicionado à fila.")
                    break
            else:
                print("Paciente não encontrado.")
        elif opcao == "6":
            paciente = fila.remover()
            if paciente:
                print(f"Paciente atendido: {paciente.nome}")
            else:
                print("Fila vazia.")
        elif opcao == "7":
            fila.imprimir()
        elif opcao == "8":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()