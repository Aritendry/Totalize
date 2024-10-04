import cv2 as cv
import pytesseract
import pandas as pd
import re
from pytesseract import Output
import numpy as np

# Etape 1 : application de filtre gris sur l'image

chemin = str(input("Entrer le chemin de la photo : "))

#E1.a Charger l'image

img = cv.imread(chemin)
grayscale = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

#E1.b Afficher l'image en gris

cv.imshow("Gris" , grayscale)
cv.waitKey(10000)


