import cv2
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import os

# Chemin d'accés au dossier contenant le dataset de formes
img_folder=r'F:\ETML-ES\POBJ\2135_AnalysePicture\soft\V2\Shapes-Dataset\output'

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-Th','--T_upper', type=float, default=40, help="Valeur seuil supérieur dans le Seuil d'hystérésis")
parser.add_argument('-Tl','--T_lower', type=float, default=20, help="Valeur seuil inférieur dans le Seuil d'hystérésis")
parser.add_argument('-n','--nbImg', type=float, default=5, help="Nombre d'images a analyser")
parser.add_argument('-b','--nbBatch', type=float, default=2, help='Nombre de batch de figures')
args = parser.parse_args()

# ------ Hyperparamètres------
# Valeur seuil inférieure dans le Seuil d'hystérésis
T_lower = args.T_lower
# Valeur seuil supérieur dans le Seuil d'hystérésis
T_upper = args.T_lower

# ------ Parametres interface ------
# Nombre de batch de figures
nbBatch = args.nbBatch
# Nombre d'images a analyser
nbImg = args.nbImg
# Noms des formes selon les cotés
shapes = np.array(["Rien", "Trait", "Angle", "Triangle","Quadrillatere","Pentagone",
                    "Hexagone", "Heptagone", "Octogone", "Nonagone", "Etoile"])

for b in range(nbBatch):
    # Dimension des figures affichées
    plt.figure(figsize=(15,15))

    # Boucle pour analyse du nombre d'images
    for i in range(nbImg):
        # Choix de l'image aléatoire
        file = random.choice(os.listdir(img_folder))
        # Joins le nom du fichier image avec chemin d'accés du dataset
        image_path= os.path.join(img_folder, file)
        # Charge l'image dans une variable
        img=mpimg.imread(image_path)
        # Prépare l'emplacement de l'image dans la figure sur 2 colonnes
        ax=plt.subplot(2,nbImg,i+1)
        ax.title.set_text("Image " + str(i+1))
        # Ajoute l'image à la figure
        plt.imshow(img)

        # Charge la meme image dans une variable mais en 2 couleurs
        grayscale = cv2.imread(image_path,0)
        # Utilisation d'une fonction pour détécter les bords de l'images
        edged = cv2.Canny(grayscale, T_lower, T_upper)
        # Trouve le nombre de contours et les charges dans une variable contenant leurs caractéristiques
        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # Selectionne l'un des contours 
        cnt = contours[0]
        # Fait l'approximation de la forme du contour séléctionné
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)

        # Détérmine le nom de la forme selon le nombre de cotés de la forme approximée
        if(len(approx) < 11):
            shape = shapes[len(approx)]
        else:
            shape = "Cercle"

        # Prépare l'emplacement de l'image dans la figure sur la 2ème colonnes
        ax=plt.subplot(2,nbImg,i+1+nbImg)
        ax.title.set_text(shape)
        # Ajoute l'image a la figure
        plt.imshow(cv2.drawContours(grayscale, [cnt], 0, (0, 0, 255), 2))

    # Sauvegarde la figure
    plt.savefig("ShapesBatchN"+str(b+1))
    # Affiche la figure du batch
    plt.show()
