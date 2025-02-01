import cv2
import pytesseract
import re

cuadro = 100
doc = 0
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 740)

def texto(imagen):
    global doc
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    umbral = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 55, 25)
    config = '--psm 1'
    texto = pytesseract.image_to_string(umbral, config=config)
    sececol = r'COLOMBIA'
    sececol2 = r'IDENTIFICACIÓN'
    busquedacol = re.findall(sececol, texto)
    busquedacol2 = re.findall(sececol2, texto)
    print(busquedacol, busquedacol2)

    if len(busquedacol) != 0 and len(busquedacol2) != 0:
        doc = 1
    print(texto)

while True:
    ret, frame = cap.read()
    cv2.putText(frame, 'Ubique el documento de identificacion', (458, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (0, 255, 0), 2)
    cv2.rectangle(frame, (cuadro, cuadro), (1280 - cuadro, 720 - cuadro), (0, 255, 0), 2)

    if doc == 0:
        cv2.putText(frame, 'PRESIONE S PARA IDENTIFICAR', (470, 750 - cuadro), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (0, 255, 0), 2)
    elif doc == 1:
        cv2.putText(frame, 'IDENTIDICACIÓN COLOMBIANA', (470, 750 - cuadro), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (0, 255, 255), 2)
        print('Cedula de Ciudadania Colombiana')
    else:
        cv2.putText(frame, 'LA IDENTIDICACIÓN NO ES COLOMBIANA', (470, 750 - cuadro), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (0, 255, 255), 2)
        print('La Cedula de Ciudadania no Colombiana')
        


    t = cv2.waitKey(5)
    cv2.imshow('ID INTELIGENTE', frame)

    if t == 27:
        break
    elif t == 83 or 115:
        texto(frame)

cap.release()
cv2.destroyAllWindows()
