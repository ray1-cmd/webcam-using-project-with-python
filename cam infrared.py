#Camera thermique by RAY1
import cv2
import numpy as np

def vision_nocturne(image):
    # Convertir l'image en niveaux de gris.
    image_grise = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un filtre de flou pour réduire le bruit.
    image_floue = cv2.GaussianBlur(image_grise, (5, 5), 0)

    # Appliquer l'amplification de contraste pour améliorer la visibilité.
    image_amplifiee = cv2.equalizeHist(image_floue)

    # Réduire le bruit résiduel en utilisant un filtre de médiane.
    image_filtree = cv2.medianBlur(image_amplifiee, 3)

    # Appliquer la détection de contours pour améliorer les contours.
    contours = cv2.Canny(image_filtree, 30, 100)

    return contours

# Capturer une image de la webcam.
cap = cv2.VideoCapture(0)

while True:
    # Lire l'image
    ret, frame = cap.read()

    # Appeler la fonction de vision nocturne.
    image_vision_nocturne = vision_nocturne(frame)

    # Afficher l'image originale et l'image améliorée.
    cv2.imshow('Image originale', frame)
    cv2.imshow('Vision nocturne', image_vision_nocturne)

    # Quitter la boucle si la touche 'q' pour "quitter" est pressée.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la caméra et fermer les fenêtres.
cap.release()
cv2.destroyAllWindows()
