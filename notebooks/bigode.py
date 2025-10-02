import cv2
import dlib
import numpy as np

# Carregar detector de faces e shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_5_face_landmarks.dat")

# Carregar bigode PNG com transparência
bigode = cv2.imread("bigode.png", cv2.IMREAD_UNCHANGED)

def aplicar_bigode(imagem_rgb, faces):
    for face in faces:
        landmarks = predictor(imagem_rgb, face)

        # Usando o landmark 4 (nariz/boca dir dependendo do modelo 5 pontos)
        x_ref = landmarks.part(4).x
        y_ref = landmarks.part(4).y

        # Calcular largura do bigode proporcional à largura da face
        face_width = face.right() - face.left()
        bigode_width = int(face_width * 0.6)
        scale = bigode_width / bigode.shape[1]
        bigode_height = int(bigode.shape[0] * scale)

        # Redimensionar bigode
        bigode_resized = cv2.resize(bigode, (bigode_width, bigode_height))

        # Posicionar bigode centralizado
        x1 = x_ref - bigode_width // 2
        y1 = y_ref - int(bigode_height * 0.4)
        x2 = x1 + bigode_width
        y2 = y1 + bigode_height

        # Ajustar para não sair da imagem
        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(imagem_rgb.shape[1], x2)
        y2 = min(imagem_rgb.shape[0], y2)

        # Ajustar bigode ao ROI
        roi_width = x2 - x1
        roi_height = y2 - y1
        if roi_width <= 0 or roi_height <= 0:
            continue
        bigode_resized = cv2.resize(bigode_resized, (roi_width, roi_height))

        # Aplicar bigode com alpha
        if bigode_resized.shape[2] == 4:
            alpha = bigode_resized[:, :, 3] / 255.0
            for c in range(3):
                imagem_rgb[y1:y2, x1:x2, c] = (
                    alpha * bigode_resized[:, :, c] + (1 - alpha) * imagem_rgb[y1:y2, x1:x2, c]
                )
    return imagem_rgb


# ----------- MODO VÍDEO (CAMERA) -------------
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = detector(frame_rgb)
    frame_com_bigode = aplicar_bigode(frame_rgb, faces)

    # Converter de volta para BGR para exibir no OpenCV
    frame_bgr = cv2.cvtColor(frame_com_bigode, cv2.COLOR_RGB2BGR)
    cv2.imshow("Bigode em tempo real", frame_bgr)

    # Tecla ESC para sair
    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()
