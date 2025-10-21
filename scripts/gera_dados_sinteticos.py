import csv
import random
from faker import Faker

def gerar_csv(qtd_itens, nome_arquivo="dados_fakes.csv"):
    fake = Faker('pt_BR')
    tipos_curso = ["Graduação", "Mestrado", "Doutorado"]

    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["nome_completo", "tipo_curso"])
        for _ in range(qtd_itens):
            nome = fake.name()
            tipo = random.choice(tipos_curso)

    print(f"{qtd_itens} registros salvos em '{nome_arquivo}'")

if __name__ == "__main__":
    qtd = int(input("Quantos registros deseja gerar? "))
    gerar_csv(qtd)
