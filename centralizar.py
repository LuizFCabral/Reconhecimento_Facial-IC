import face_recognition
import cv2

# Carregue a imagem
imagem = face_recognition.load_image_file("./images/andrew3.jpg")

# Detecte todos os rostos na imagem
faces = face_recognition.face_locations(imagem)

# Se nenhum rosto for detectado, você pode tratar esse caso como quiser
if len(faces) == 0:
    print("Nenhum rosto detectado na imagem.")
else:
    # Suponha que estamos interessados apenas no primeiro rosto detectado
    face = faces[0]

    # Calcule as coordenadas do centro do rosto
    top, right, bottom, left = face
    altura_rosto = bottom - top
    largura_rosto = right - left
    centro_x = left + largura_rosto // 2
    centro_y = top + altura_rosto // 2

    # Calcule as dimensões da imagem
    altura_imagem, largura_imagem, _ = imagem.shape

    # Calcule as coordenadas para centralizar o rosto na imagem
    x_inicial = max(0, centro_x - largura_imagem // 2)
    x_final = min(largura_imagem, centro_x + largura_imagem // 2)
    y_inicial = max(0, centro_y - altura_imagem // 2)
    y_final = min(altura_imagem, centro_y + altura_imagem // 2)

    # Recorte a imagem para centralizar o rosto
    imagem_centralizada = imagem[y_inicial:y_final, x_inicial:x_final]

    # Exiba a imagem centralizada
    cv2.imshow("Rosto Centralizado", imagem_centralizada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()