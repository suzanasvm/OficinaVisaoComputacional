import cv2

# Carregar classificadores pré-treinados
classificador_face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
classificador_sorriso = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# Inicializar a câmera
camera = cv2.VideoCapture(0)

while True:
    # Captura frame a frame
    ret, frame = camera.read()
    if not ret:
        break

    # Converter para escala de cinza
    imagem_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar faces
    faces = classificador_face.detectMultiScale(
        imagem_gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(50, 50)
    )

    for (x, y, w, h) in faces:
        # Desenhar retângulo na face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

        # Regiões de interesse
        face_gray = imagem_gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]

        # Detectar sorrisos dentro da face
        smiles = classificador_sorriso.detectMultiScale(
            face_gray,
            scaleFactor=1.7,
            minNeighbors=22,
            minSize=(25, 25)
        )

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(face_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)

    # Mostrar o resultado
    cv2.imshow("Detector de Sorrisos e Rostos", frame)

    # Tecla ESC (27
