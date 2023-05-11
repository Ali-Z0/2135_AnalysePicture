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
parser.add_argument('-i','--image', type=str, default=0, help="Chemin d'acces a l'image")
parser.add_argument('-D','--DossImg', type=str, default=r'C:\Users\alizoubir\Documents\ETML-ES-2eme\POBJ\2135_AnalysePicture\soft\V2\Shapes-Dataset\Images-examples', help="Choisi une image aleatoire dans le dossier specifie")
args = parser.parse_args()
# %%

# Chemin d'acces au dossier contenant le dataset de formes
img_folder = args.DossImg

if args.image == 0 :
    # Choix de l'image aleatoire
    file = random.choice(os.listdir(img_folder))
    # Joins le nom du fichier image avec chemin d'acces du dataset
    image_path = os.path.join(img_folder, file)
    # Charge l'image dans une variable
    img = mpimg.imread(image_path)
else:
    # Choisi l'image pointee
    img = mpimg.imread(args.image)

# creating grid for subplots
fig = plt.figure()

# Prepare l'emplacement de l'image dans la figure sur 2 colonnes
ax = plt.subplot(1, 2, 1)
ax.title.set_text("Image sans contours")
# Ajoute l'image à la figure
plt.imshow(img)

# %%



#%%

# Sauvegarde la figure
plt.savefig('logs/SavedFig'+time.strftime("%Y-%m-%d_%H%M%S")+".png")
# Affiche la figure du batch
plt.show()
# %%
