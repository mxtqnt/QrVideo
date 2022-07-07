import cv2
captura = cv2.VideoCapture(0)

while (1):
    ret, frame = captura.read()
    cv2.imshow("Video", frame)

    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(frame)
    if vertices_array is not None:
        print("Conteúdo QRCode: ")
        print(data)
    else:
        print("Não encontrei")

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

captura.release()
cv2.destroyAllWindows()