Introduction du projet :

    ---- Création d'un projet qui permet d'extraire le prix total d'un achat à partir d'un ticket de reçu pris en photo. L'objectif est de développer un système automatisé capable de lire une image de ticket, d'en extraire les informations textuelles telles que les produits achetés et leurs prix unitaires, et enfin d'identifier le prix total de l'achat.

Langage utilisé :

    ---- Python 3.11

Librairies utilisées :

    OpenCV : Permettra de manipuler nos images en appliquant des filtres, les convertir en niveaux de gris, les binariser, et les améliorer pour une lecture optimale.

    Tesseract OCR : Servira à extraire du texte à partir des images de reçus. Il lira les caractères imprimés et nous retournera une chaîne de texte comprenant les produits et les prix.

    Pandas : Pour organiser les données extraites de manière structurée dans des tableaux et faciliter les opérations de calcul, comme la somme des prix ou l'analyse des taxes.

    Pytesseract : Nous permettra d'utiliser le moteur Tesseract OCR directement dans notre code Python pour l'intégration avec OpenCV.

    re (Expressions régulières) : Pour rechercher et extraire des motifs spécifiques dans le texte, comme les montants (prix) ou des informations importantes.

    NLTK ou SpaCy (optionnel) : Ces bibliothèques de traitement du langage naturel pourront être utilisées pour améliorer l'analyse textuelle, comme l'identification des mots-clés ("Total", "Taxes", etc.).