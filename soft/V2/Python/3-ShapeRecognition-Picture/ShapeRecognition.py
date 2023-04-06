""" Script qui trace les contours d'images réelles """
import numpy as np
import random
#import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import time
import os
import cv2

# %%
# Chemin d'accés au dossier contenant le dataset de formes
img_folder = r'C:\Users\alizoubir\Documents\ETML-ES-2eme\POBJ\2135_AnalysePicture\soft\V2\Python\3-ShapeDetection-Picture\PycharmProject\Images-examples'

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-Th', '--T_upper', type=float, default=50,
                    help="Valeur supérieur dans le Seuil d'hystérésis")
parser.add_argument('-Tl', '--T_lower', type=float, default=10,
                    help="Valeur inférieur dans le Seuil d'hystérésis")
args = parser.parse_args()
# ------ Hyperparamètres------
# Valeur seuil inférieure dans le Seuil d'hysteresis
T_lower = 235
# Valeur seuil supérieur dans le Seuil d'hysteresis
T_upper = 500
# ------ Parametres interface ------
# Noms des formes selon les cotés
shapes = np.array(["Nothing", "Line", "Angle", "Triangle", "Square", "Pentagon",
                   "Hexagon", "Heptagon", "Octagon", "Nonagon", "Star"])
# Choix de l'image aléatoire
file = random.choice(os.listdir(img_folder))
# Joins le nom du fichier image avec chemin d'accés du dataset
image_path = os.path.join(img_folder, file)
# Charge l'image dans une variable
img = mpimg.imread(image_path)

# creating grid for subplots
fig = plt.figure()
# fig.set_figheight(9)
# fig.set_figwidth(9)

# Prépare l'emplacement de l'image dans la figure sur 2 colonnes
ax = plt.subplot(1, 2, 1)
ax.title.set_text("Image sans contours")
# Ajoute l'image à la figure
plt.imshow(img)

# %%
# Charge la meme image dans une variable mais en 2 couleurs
#grayscale = cv2.imread(image_path,0)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Utilisation d'une fonction pour détécter les bords de l'images
# edged = cv2.Canny((grayscale*255).astype(np.uint8), T_lower, T_upper)
edged = cv2.Canny(grayscale, T_lower, T_upper)
# Trouve le nombre de contours et les charges dans une variable contenant leurs caractéristiques
contours, hierarchy = cv2.findContours(
    edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
nbContours = len(contours)
# Selectionne l'un des contours si contenu existant
if nbContours:
    for ContCnt in range(nbContours):
        cnt = contours[ContCnt]
        # Fait l'approximation de la forme du contour séléctionné
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        # Détérmine le nom de la forme selon le nombre de cotés de la forme approximée
        if len(approx) < 11:
            shape = shapes[len(approx)]
        else:
            shape = "Circle"
        # Prépare l'emplacement de l'image dans la figure sur la 2ème colonnes
        ax = plt.subplot(1, 2, 2)
        ax.title.set_text("Image avec contours")
        # Reconvertit l'image en format couleur
        imgRecolored = cv2.cvtColor(
            grayscale, cv2.COLOR_GRAY2BGR)  # add this line
        # Affiche l'image avec les contours en couleurs
        plt.imshow(cv2.drawContours(
            imgRecolored, contours, -1, (255, 0, 0), 2))

        #plt.imshow(cv2.drawContours(grayscale, [cnt], -1, (0, 255, 0), 3),cmap = plt.cm.gray)

# Sauvegarde la figure
plt.savefig('logs/SavedFig'+time.strftime("%Y-%m-%d %H%M%S")+".png")
# Affiche la figure du batch
plt.show()
# %%
