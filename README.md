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

--------------------------------------------------------------------------------------
Étapes du projet :
--------------------------------------------------------------------------------------

Acquisition de l'image du reçu :

    Utiliser une image prise par appareil photo ou scanner du reçu.
    Charger cette image en utilisant OpenCV pour les traitements d'image suivants.

Prétraitement de l'image :

    Convertir l'image en niveaux de gris (grayscale) pour simplifier l'extraction du texte.
    Appliquer des filtres comme le flou gaussien pour réduire le bruit et améliorer la qualité visuelle du texte.
    Binariser l'image si nécessaire, c'est-à-dire convertir l'image en noir et blanc pour maximiser le contraste entre le texte et l'arrière-plan.

Extraction du texte avec Tesseract :

    Utiliser Pytesseract pour appeler le moteur Tesseract OCR et extraire le texte de l'image prétraitée.
    Obtenir une chaîne de texte contenant les produits, leurs prix unitaires, et le total de l'achat.

Traitement et filtrage du texte :

    Utiliser les expressions régulières (regex) pour extraire les prix et d'autres informations utiles comme le "Total" ou la "Taxe" du texte récupéré.
    Par exemple, rechercher les montants sous forme de nombres décimaux (comme "9.99", "12.50").

Organisation des données :

    Stocker les informations extraites dans un DataFrame de Pandas pour faciliter l'analyse et les opérations de calcul.
    Organiser les produits et les prix dans une structure claire pour des calculs futurs.

Calcul du prix total :

    Utiliser les données organisées dans Pandas pour calculer automatiquement la somme des prix.
    Si nécessaire, identifier le "Total" ou les taxes dans le texte extrait pour une confirmation précise.

Affichage des résultats :

    Afficher ou renvoyer les résultats finaux : le montant total de l'achat, les prix des produits individuels, et éventuellement les taxes.

Améliorations (optionnel) :

    Ajouter des fonctionnalités avancées, comme l'analyse du texte avec NLTK ou SpaCy pour mieux comprendre les étiquettes comme "Total", "Taxe", etc.
    Utiliser des techniques de traitement d'image supplémentaires pour améliorer encore plus la qualité de l'extraction du texte dans des environnements difficiles (par exemple, si le reçu est froissé ou mal éclairé).