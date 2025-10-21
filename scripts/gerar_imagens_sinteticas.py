import cv2
import csv
import json
import os
import sys

def gerar_imagens(quantidade_imagens, imagem_base, csv_arquivo, json_arquivo, pasta_saida):
    tamanho_fonte = 1
    cor_fonte = (0, 0, 255)
    os.makedirs(pasta_saida, exist_ok=True)
    # Lê os dados do CSV
    dados_csv = []
    with open(csv_arquivo, newline='', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            dados_csv.append(linha)

    # Lê o JSON com posições de cada campo
    with open(json_arquivo, encoding='utf-8') as f:
        posicoes = json.load(f)
    # Garante que a quantidade não ultrapasse o total de registros disponíveis
    quantidade_imagens = min(quantidade_imagens, len(dados_csv))

    # Cada linha do CSV gera uma imagem (limitado pela quantidade escolhida)
    for id_item, dado in enumerate(dados_csv[:quantidade_imagens], start=1):
        imagem = cv2.imread(imagem_base)

        cv2.putText(imagem, dado['nome_completo'], tuple(posicoes['nome_completo']),
                    cv2.FONT_HERSHEY_SIMPLEX, tamanho_fonte, cor_fonte, 1, cv2.LINE_AA)

        cv2.putText(imagem, dado['tipo_curso'], tuple(posicoes['tipo_curso']),
                    cv2.FONT_HERSHEY_SIMPLEX, tamanho_fonte, cor_fonte, 1, cv2.LINE_AA)

        nome_saida = os.path.join(pasta_saida, f"imagem_{id_item}.jpg")
        cv2.imwrite(nome_saida, imagem)

    print(f"{quantidade_imagens} imagens geradas na pasta '{pasta_saida}'")

def main():
    quantidade_imagens = int(sys.argv[1])
    imagem_base = "imagem_exemplo.jpg"
    csv_arquivo = "dados_fakes.csv"
    json_arquivo = "posicoes.json"
    pasta_saida = "imagens_geradas"
    gerar_imagens(quantidade_imagens, imagem_base, csv_arquivo, json_arquivo, pasta_saida)


if __name__ == "__main__":
    main()
