import face_recognition
import cv2
import os
import datetime
import subprocess
import platform



# Pasta onde as imagens conhecidas estão localizadas
pasta_imagens_conhecidas = "./images/conhecidos/"

# Crie uma lista de imagens conhecidas e seus respectivos nomes
imagens_conhecidas = []

for imagem_conhecida_nome in os.listdir(pasta_imagens_conhecidas):
    imagem_conhecida_path = os.path.join(pasta_imagens_conhecidas, imagem_conhecida_nome)

    # Use o nome do arquivo como o nome da pessoa
    nome_pessoa = os.path.splitext(imagem_conhecida_nome)[0]

    imagens_conhecidas.append({"imagem": imagem_conhecida_path, "nome": nome_pessoa})

# Carregue as codificações dos rostos conhecidos
codificacoes_conhecidas = []
nomes_conhecidos = []

for pessoa in imagens_conhecidas:
    imagem_conhecida = face_recognition.load_image_file(pessoa["imagem"])
    codificacao_conhecida = face_recognition.face_encodings(imagem_conhecida)[0]
    codificacoes_conhecidas.append(codificacao_conhecida)
    nomes_conhecidos.append(pessoa["nome"])

# Carregue a imagem desconhecida que você deseja comparar
imagem_desconhecida = face_recognition.load_image_file("./images/desconhecidos/Willian2.jpg")

# Encontre todos os rostos na imagem desconhecida
faces_desconhecidas = face_recognition.face_locations(imagem_desconhecida)
codificacoes_desconhecidas = face_recognition.face_encodings(imagem_desconhecida, faces_desconhecidas)

# Inicialize uma lista para armazenar os nomes correspondentes aos rostos
nomes_correspondentes = []

# Compare os rostos desconhecidos com os rostos conhecidos
for codificacao_desconhecida in codificacoes_desconhecidas:
    correspondencias = face_recognition.compare_faces(codificacoes_conhecidas, codificacao_desconhecida)

    nome_correspondente = "Desconhecido"  # Defina um nome padrão caso o rosto não seja reconhecido

    for i, correspondencia in enumerate(correspondencias):
        if correspondencia:
            nome_correspondente = nomes_conhecidos[i]
            print("Reconheceu!")
            break  # Pare de procurar assim que encontrar uma correspondência

    nomes_correspondentes.append(nome_correspondente)

# Desenhe retângulos ao redor dos rostos na imagem desconhecida e coloque os nomes
#for (top, right, bottom, left), nome in zip(faces_desconhecidas, nomes_correspondentes):
#   cv2.rectangle(imagem_desconhecida, (left, top), (right, bottom), (0, 0, 255), 2)
#    fonte = cv2.FONT_HERSHEY_DUPLEX
#    cv2.putText(imagem_desconhecida, nome, (left + 6, bottom - 6), fonte, 0.5, (255, 255, 255), 1)

# Registra os logs
with open("log_entrada.txt", "a") as arquivo_txt:
    for nome in nomes_correspondentes:
        arquivo_txt.write(nome + "  " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n")

# Exiba a imagem com os rostos reconhecidos
# cv2.imshow("Reconhecimento Facial", imagem_desconhecida)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

