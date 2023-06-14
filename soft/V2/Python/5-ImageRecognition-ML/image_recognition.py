""" Script qui trace les contours d'images reelles """
from transformers import AutoFeatureExtractor, ResNetForImageClassification
import torch
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import os
import random
from deep_translator import GoogleTranslator

#%%
# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i','--image', type=str, default=0, help="Chemin d'acces a l'image")
parser.add_argument('-D','--DossImg', type=str, default=r'C:\Users\Ady\Documents\ETML-ES\2eme\POBJ\2135_AnalysePicture\soft\V2\Shapes-Dataset\images_objets')
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
ax.title.set_text("Image")
# Ajoute l'image à la figure
plt.imshow(img)

# %%
# Pointe sur le dossier avec les models de machine learning
os.chdir('../../ML_Models')
# Utilise les libraire pour récuperer les features du model
feature_extractor = AutoFeatureExtractor.from_pretrained("resnet-18")
# Utiliser les libraire pour charger le model
model = ResNetForImageClassification.from_pretrained("resnet-18")
# Image d'entrée
inputs = feature_extractor(img, return_tensors="pt")

#%%
# Utlise torch sans calcul de gradient
with torch.no_grad():
    # Charge les probabilités pour chaques labels de classification
    logits = model(**inputs).logits
    
# 
predicted_label = logits.argmax(-1).item()
to_translate = model.config.id2label[predicted_label]
translated = GoogleTranslator(source='auto', target='fr').translate(to_translate)
print(to_translate)
print(translated)

#%%
