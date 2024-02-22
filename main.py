import face_recognition
import cv2

# Carregue uma imagem com os rostos que você deseja reconhecer
imagem_conhecida = face_recognition.load_image_file("./images/conhecidos/andrew.jpg")

# Codifique o rosto na imagem conhecida
codificacao_conhecida = face_recognition.face_encodings(imagem_conhecida)[0]

# Carregue a imagem na qual você deseja realizar o reconhecimento facial
imagem_desconhecida = face_recognition.load_image_file("./images/desconhecidos/Alipio.jpg")

# Encontre todos os rostos na imagem desconhecida
faces_desconhecidas = face_recognition.face_locations(imagem_desconhecida)
codificacoes_desconhecidas = face_recognition.face_encodings(imagem_desconhecida, faces_desconhecidas)

# Inicialize uma lista para armazenar os nomes correspondentes aos rostos
nomes_correspondentes = []

# Compare os rostos desconhecidos com o rosto conhecido
for codificacao_desconhecida in codificacoes_desconhecidas:
    # Compare a codificação do rosto desconhecido com o rosto conhecido
    correspondencias = face_recognition.compare_faces([codificacao_conhecida], codificacao_desconhecida)

    nome_correspondente = "Desconhecido"  # Defina um nome padrão caso o rosto não seja reconhecido

    if correspondencias[0]:  # Se houver uma correspondência
        nome_correspondente = "Andrew"  # Defina o nome da pessoa conhecida
        print("Reconheceu!")

    nomes_correspondentes.append(nome_correspondente)

# Desenhe retângulos ao redor dos rostos na imagem desconhecida e coloque os nomes
for (top, right, bottom, left), nome in zip(faces_desconhecidas, nomes_correspondentes):
    cv2.rectangle(imagem_desconhecida, (left, top), (right, bottom), (0, 0, 255), 2)
    fonte = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(imagem_desconhecida, nome, (left + 6, bottom - 6), fonte, 0.5, (255, 255, 255), 1)

# Exiba a imagem com os rostos reconhecidos
cv2.imshow("Reconhecimento Facial", imagem_desconhecida)
cv2.waitKey(0)
cv2.destroyAllWindows()