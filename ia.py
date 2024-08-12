import cv2  #utilizar camera


from cvzone.HandTrackingModule import HandDetector


webcam = cv2.VideoCapture(0) # o numero zero captura a camera do computador
rastreador = HandDetector(detectionCon=0.8, maxHands=2) #rastreador de mãos

while True:
    sucesso, imagem = webcam.read()   #sucesso e imagem receberão 2 valores #"read" ler dados da webcam
    coordenadas, imagem_maos = rastreador.findHands(imagem)
    
    print(coordenadas)
    
    cv2.imshow("projeto 4 - IA", imagem) #mostrar a imagem da camera
    
    
    if cv2.waitKey(1) != -1: #funcionalidade teclado
        break
    
    
webcam.release()
cv2.destroyAllWindows()