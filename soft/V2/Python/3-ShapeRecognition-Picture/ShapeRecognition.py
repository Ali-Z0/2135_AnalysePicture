""" Script qui trace les contours d'images reelles """
import numpy as np
import random
#import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import time
import os
import cv2

#%%
# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-I','--image', type=str, default=0, help="Chemin d'acces a l'image")
parser.add_argument('-D','--DossImg', type=str, default=r'C:\Users\alizoubir\Documents\ETML-ES-2eme\POBJ\2135_AnalysePicture\soft\V2\Python\3-ShapeDetection-Picture\PycharmProject\Images-examples', help="Choisi une image aleatoire dans le dossier specifie")
parser.add_argument('-Th','--T_upper', type=float, default=500, help="Valeur superieur dans le Seuil d'hysteresis")
parser.add_argument('-Tl','--T_lower', type=float, default=225, help="Valeur inferieur dans le Seuil d'hysteresis")
args = parser.parse_args()
# %%

# Chemin d'acces au dossier contenant le dataset de formes
img_folder = args.DossImg

# ------ Hyperparametres------
# Valeur seuil inferieure dans le Seuil d'hysteresis
T_lower = args.T_lower
# Valeur seuil superieur dans le Seuil d'hysteresis
T_upper = args.T_upper
# ------ Parametres interface ------
# Noms des formes selon les cotes
shapes = np.array(["Nothing", "Line", "Angle", "Triangle", "Rectangle", "Pentagon",
                   "Hexagon", "Heptagon", "Octagon", "Nonagon", "Star"])

if args.image == 0 :
    # Choix de l'image aleatoire
    file = random.choice(os.listdir(img_folder))
    # Joins le nom du fichier image avec chemin d'acces du dataset
    image_path = os.path.join(img_folder, file)
    # Charge l'image dans une variable
    img = mpimg.imread(image_path)
else:
    # Choisi l'image pointee
    img = mpimg.imread(args.imagePath)

# creating grid for subplots
fig = plt.figure()
# fig.set_figheight(9)
# fig.set_figwidth(9)

# Prepare l'emplacement de l'image dans la figure sur 2 colonnes
ax = plt.subplot(1, 2, 1)
ax.title.set_text("Image sans contours")
# Ajoute l'image à la figure
plt.imshow(img)

# %%
# Charge la meme image dans une variable mais en 2 couleurs
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Utilisation d'une fonction pour detecter les bords de l'images
edged = cv2.Canny(grayscale, T_lower, T_upper)
# Trouve le nombre de contours et les charges dans une variable contenant leurs caracteristiques
contours, hierarchy = cv2.findContours(
edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
nbContours = len(contours)
# Variable contenant les formes
shape = []
    
# Selectionne l'un des contours si contenu existant
if nbContours:
    for ContCnt in range(nbContours):
        cnt = contours[ContCnt]
        # Fait l'approximation de la forme du contour selectionne
        epsilon = 0.03 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        # Determine le nom de la forme selon le nombre de cotes de la forme approximee
        if len(approx) < 11:
            shape.append(shapes[len(approx)])
            #shape[ContCnt] = shapes[len(approx)]
        else:
            shape.append("Circle")
            #shape[ContCnt] = "Circle"
        # Prepare l'emplacement de l'image dans la figure sur la 2eme colonnes
        ax = plt.subplot(1, 2, 2)
        ax.title.set_text("Image avec contours")
        # Reconvertit l'image en format couleur
        imgRecolored = cv2.cvtColor(
        grayscale, cv2.COLOR_GRAY2BGR)
        # Affiche l'image avec les contours en couleurs
        plt.imshow(cv2.drawContours(
            imgRecolored, contours, -1, (255, 0, 0), 2))

        #plt.imshow(cv2.drawContours(grayscale, [cnt], -1, (0, 255, 0), 3),cmap = plt.cm.gray)

#%%
# Shape recognition
cv2.HuMoments(cv2.moments(grayscale)).flatten()



# Sauvegarde la figure
plt.savefig('logs/SavedFig'+time.strftime("%Y-%m-%d_%H%M%S")+".png")
# Affiche la figure du batch
plt.show()
# %%
