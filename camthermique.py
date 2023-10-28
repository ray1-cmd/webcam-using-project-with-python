#Camera thermique by RAY1
import cv2
import numpy as np

def apply_heatmap(image):
    # Convertir l'image en niveaux de gris.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer une fausse couleur à l'image.
    heatmap = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    return heatmap

def main():
    # Ouvrir le flux vidéo de la caméra thermique.
    cap = cv2.VideoCapture(0)

    while True:
        # Lire la prochaine frame du flux vidéo.
        ret, frame = cap.read()

        # Vérifier si la lecture de la frame a réussi.
        if not ret:
            break

        # Appliquer la fausse couleur à l'image.
        heatmap = apply_heatmap(frame)

        # Afficher l'image avec la fausse couleur.
        cv2.imshow('Camera thermique by RAY1', heatmap)

        # Attendre la touche 'q' pour quitter.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libérer la caméra
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
