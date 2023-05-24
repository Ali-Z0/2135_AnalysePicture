""" Script qui trace les contours d'images reelles """
from transformers import AutoFeatureExtractor, ResNetForImageClassification
import torch
import matplotlib.image as mpimg
import os
from deep_translator import GoogleTranslator


def getAnalyze(_img: str, _model: str):
    img = mpimg.imread(_img)
    
    # Pointe sur le dossier avec les models de machine learning
    os.chdir(_model)
    # Utilise les libraire pour récuperer les features du model
    feature_extractor = AutoFeatureExtractor.from_pretrained("resnet-18")
    # Utiliser les libraire pour charger le model
    model = ResNetForImageClassification.from_pretrained("resnet-18")
    # Image d'entrée
    inputs = feature_extractor(img, return_tensors="pt")
    
    # Utlise torch sans calcul de gradient
    with torch.no_grad():
        # Charge les probabilités pour chaques labels de classification
        logits = model(**inputs).logits
        
    # 
    predicted_label = logits.argmax(-1).item()
    to_translate = model.config.id2label[predicted_label]
    translated = GoogleTranslator(source='auto', target='fr').translate(to_translate)
    
    return to_translate, translated

