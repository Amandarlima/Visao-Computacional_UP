import cv2

# declaração da imagem utilizada no execício
imagem = cv2.imread("boi.jpg")
cv2.imshow("muuu", imagem)
cv2.waitKey(0) # aguarda alguma tecla ser pressionada para fechar a imagem
cv2.destroyAllWindows()

# Altera o tamanho da imagem para 300px x 300px
img_resize = cv2.resize(imagem, (300, 300))
cv2.imshow("TAMANHO", img_resize)
cv2.waitKey(0) # aguarda alguma tecla ser pressionada para fechar a imagem
cv2.destroyAllWindows()

# Rotaciona a imagem com tamanho alterado 49 graus a partir do ponto 200px x 100px
matRot = cv2.getRotationMatrix2D((200,100), 49, 1.0)
imgRot = cv2.warpAffine(img_resize, matRot, img_resize.shape[:2])
cv2.imshow("Rotacionar", imgRot)
cv2.waitKey(0) # aguarda alguma tecla ser pressionada para fechar a imagem
cv2.destroyAllWindows()

# Adiciona um desfoque leve na imagem original
imgBlur = cv2.GaussianBlur(imagem, (5, 5), 10)
cv2.imshow("Desfoque", imgBlur)
cv2.waitKey(0) # aguarda alguma tecla ser pressionada para fechar a imagem
cv2.destroyAllWindows()

# Corta a imagem
imgCrop = imagem[0:400, 0:250]
cv2.imshow("Corta", imgCrop)
cv2.waitKey(0) # aguarda alguma tecla ser pressionada para fechar a imagem
cv2.destroyAllWindows()