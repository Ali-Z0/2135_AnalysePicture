import cv2
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import os


# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-F','--dossierImg', type=str, default=r'C:\Users\alizoubir\Documents\ETML-ES-2eme\POBJ\2135_AnalysePicture\soft\V2\Shapes-Dataset\output', help="")
parser.add_argument('-A','--modeAff', type=bool, default=True, help="Active ou desactive le mode affichage des resultats")
parser.add_argument('-Th','--T_upper', type=float, default=50, help="Valeur supérieur dans le Seuil d'hystérésis")
parser.add_argument('-Tl','--T_lower', type=float, default=10, help="Valeur inférieur dans le Seuil d'hystérésis")
parser.add_argument('-n','--nbImg', type=float, default=6, help="Nombre d'images a analyser")
parser.add_argument('-b','--nbBatch', type=float, default=2, help='Nombre de batch de figures')
args = parser.parse_args()

# Chemin d'accés au dossier contenant le dataset de formes
img_folder=args.dossierImg

# ------ Hyperparamètres------
# Valeur seuil inférieure dans le Seuil d'hystérésis
T_lower = args.T_lower
# Valeur seuil supérieur dans le Seuil d'hystérésis
T_upper = args.T_upper

# ------ Parametres interface ------
# Nombre de batch de figures
nbBatch = args.nbBatch
# Nombre d'images a analyser
nbImg = args.nbImg
# Noms des formes selon les cotés
shapes = np.array(["Nothing", "Line", "Angle", "Triangle","Square","Pentagon",
                    "Hexagon", "Heptagon", "Octagon", "Nonagon", "Star"])
# Si le mdoe affichage est activé
modeAffichage = args.modeAff

# Moyenne de succés de tous les batch
MoyenneBatch = 0
for b in range(nbBatch):
    # Dimension des figures affichées
    plt.figure(figsize=(15,15))

    # Boucle pour analyse du nombre d'images
    i = 0
    # Calcul moyenn succés
    Moyenne = 0
    # Nb images ratées
    missed = 0
    # Tant que pas toutes les images analysées
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
        #grayscale = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2GRAY)
        # Utilisation d'une fonction pour détécter les bords de l'images
        # edged = cv2.Canny((grayscale*255).astype(np.uint8), T_lower, T_upper)
        edged = cv2.Canny(grayscale, T_lower, T_upper)
        # Trouve le nombre de contours et les charges dans une variable contenant leurs caractéristiques
        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # Selectionne l'un des contours si contenu existant
        if len(contours):
            cnt = contours[0]
            # Fait l'approximation de la forme du contour séléctionné
            approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
            # Détérmine le nom de la forme selon le nombre de cotés de la forme approximée
            if(len(approx) < 11):
                shape = shapes[len(approx)]
            else:
                shape = "Circle"
            # Prépare l'emplacement de l'image dans la figure sur la 2ème colonnes
            ax=plt.subplot(2,nbImg,i+1+nbImg)
            # Récupère le nom réelle de la forme pour comparer
            realShape = str(file).split('_') 
            # Calcul moyenne de réussite
            if shape == realShape[0]:
                Moyenne += 1
            ax.title.set_text(shape + " vs " + realShape[0])
            # Ajoute l'image a la figure
            plt.imshow(cv2.drawContours(grayscale, [cnt], 0, (0, 0, 255), 2), cmap = plt.cm.gray)
        else:
            # Si rien détécté, refait la manipulation
            i -= 1
            # Indique une image manquante
            missed += 1

    # Calcul la moyenne de succés de la figure actuelle
    Moyenne = (Moyenne / (nbImg - missed))*100
    # Additionne la moyenne du batch au total des batchs
    MoyenneBatch += Moyenne
    # Affiche le résultat
    print("Moyenne figure " + str(b+1) + " : " + "%.2f" % Moyenne + " %")

    # Si mode affichage
    if modeAffichage:
        # Sauvegarde la figure
        plt.savefig("ShapesBatchN"+str(b+1))
        # Affiche la figure du batch
        plt.show()

# Calcul la moyenne de succés de tous les batchs
MoyenneBatch = (MoyenneBatch / nbBatch)
# Affiche le résultat
print("Moyenne totale : " + "%.2f" % MoyenneBatch + " %")