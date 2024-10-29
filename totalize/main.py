import cv2 as cv
import re
import pytesseract
import pandas as pd

# Étape 1 : Lire l'image
img = cv.imread("image/ticket_02.png")

# Étape 2 : Application d'un filtre gris à l'image pour la transformer en niveaux de gris
gray_filter = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Étape 3 : Application du seuil binaire
_, thresholded_img = cv.threshold(gray_filter, 155, 255, cv.THRESH_BINARY)
# _ indique qu'on ignore la valeur de retour correspondant au seuil utilisé
# cv.THRESH_BINARY applique un seuil binaire : les pixels > 155 deviennent blancs (255), les autres deviennent noirs (0)

# Étape 4 : Récupération des dimensions de l'image (hauteur et largeur)
height, width = thresholded_img.shape[:2]
# [:2] permet d'obtenir uniquement la hauteur et la largeur

# Étape 5 : Découpage de l'image en trois colonnes de largeur égale
noms_img = thresholded_img[0:height, 0:int(width/3)]  # Première colonne (nom)
prix_img = thresholded_img[0:height, int(width/3):int(2*width/3)]  # Deuxième colonne (prix)
quantites_img = thresholded_img[0:height, int(2*width/3):width]  # Troisième colonne (quantité)
# Les colonnes sont divisées en trois parties égales, chacune représentant environ 1/3 de la largeur totale

# Étape 6 : Affichage des images découpées pour vérification
cv.imshow("Nom", noms_img)
cv.imshow("Prix", prix_img)
cv.imshow("Quantité", quantites_img)
cv.waitKey(0)
cv.destroyAllWindows()
