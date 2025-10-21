import cv2
import albumentations as A
import os

# Pasta de saída (onde as imagens transformadas serão salvas)
pasta_saida = "imagens_transformadas"

# Cria a pasta de saída se não existir
os.makedirs(pasta_saida, exist_ok=True)

# Define uma transformação do Albumentation
transformacao = A.Compose([
    A.RandomBrightnessContrast(p=0.5),
    A.RandomRotate90(p=0.5),
    A.MotionBlur(p=0.3),
    A.GaussNoise(p=0.3),
    A.Perspective(p=0.3)
])

# Pasta de entrada (onde você colocou suas imagens)
pasta_entrada = "imagens_geradas"

# Lista todas as imagens da pasta de entrada
arquivos = os.listdir(pasta_entrada)


# Itera sobre cada imagem da pasta
for arquivo in arquivos:
    caminho_arquivo = os.path.join(pasta_entrada, arquivo)
    imagem = cv2.imread(caminho_arquivo)
    
    # Aplica a transformação
    imagem_aumentada = transformacao(image=imagem)["image"]
    
    # Salva a imagem transformada
    caminho_saida = os.path.join(pasta_saida, "aug_" + arquivo)
    cv2.imwrite(caminho_saida, imagem_aumentada)
    
