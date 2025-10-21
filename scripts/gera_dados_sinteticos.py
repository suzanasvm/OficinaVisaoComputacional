import csv
import random
from faker import Faker

def gerar_csv(qtd_itens, nome_arquivo="dados_fakes.csv"):
    fake = Faker('pt_BR')
    tipos_curso = ["Graduação", "Mestrado", "Doutorado"]
    nomes_curso = [
        "Engenharia Elétrica",
        "Análise e Desenvolvimento de Sistemas",
        "Medicina",
        "Direito",
        "Administração",
        "Ciência da Computação",
        "Engenharia Mecânica",
        "Psicologia"
    ]

    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Nome Completo", "Tipo de Curso", "Nome do Curso", "Data de Validade"])

        for _ in range(qtd_itens):
            nome = fake.name()
            tipo = random.choice(tipos_curso)
            curso = random.choice(nomes_curso)
            mes = random.randint(1, 12)
            ano = random.randint(24, 35)
            data_validade = f"{mes:02d}/{ano}"
            escritor.writerow([nome, tipo, curso, data_validade])

    print(f"{qtd_itens} registros salvos em '{nome_arquivo}'")

if __name__ == "__main__":
    qtd = int(input("Quantos registros deseja gerar? "))
    gerar_csv(qtd)
