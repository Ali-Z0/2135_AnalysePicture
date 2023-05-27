# 2135_AnalysePicture
## Processing d’images avec OpenCV pour implémentation sur Raspberry PI.
Le projet consiste en la détéction d'image de pièces via une webcam sur raspberry Pi 3 ainsi que le déduction de la forme de celles-ci, selon plusieurs méthodes.

# Prérequis

Ce projet utilise la distribution Anaconda avec la libraire OPENCV
```bash
conda install -c conda-forge opencv
```
Les autres prérequis sont mentionnés dans le fichier requirements.txt qui permet de créer un environnement Anaconda.

## Utilisation

Ce git contient différents scripts utilisants différentes méthodes de reconnaisance / détéction d'images.

Exemple d'éxecution de scripts via le terminal anaconda :
```bash
2135_AnalysePicture\soft\V2\Python\4-ShapeRecognition-Approx python ShapeRecognition-Approx.py -h
```

#### Scripts

Le répertoire contient les scripts suivants :
| Nom  |  Description |
|---|---|
|  1-LoadDatabase | Charge une base de donnée d'image |
| 2-ShapeDetection-Dataset  | Effectue des batch de test de reconnaissance de forme d'un dataset de formes pour tester les paramètres |
|  3-ShapeDetection-Picture | Effectue une détection de forme et de contours, sans déduire la forme |
| 4-ShapeRecognition-Approx | Détecte les formes et contours et déduit la forme des contours par une approximation en utilisant uniquement openCV |
| 5-ShapeRecognition-ML | Détecte et déduis les objets selon un modèle de machine learning |
| 6-AppShape | Application permettant d'analyser des images via les scripts précédents |


## Structure

l'arborescence contient les répertoire suivants :
| Nom  |  Contenu |
|---|---|
|  Doc | Documentation, datasheet, fichiers word, pdf,...  |
| Hard  | Schéma hardware, routage,...  |
|  Mec | Dessins mecs, plans, pieces,...  |
| Soft | Software, firmware, code source,... |
| Tools | Outils/programmes nécessaires pour développement du projet |

## A propos

Projet réalisé à l'ETML-ES dans le cadre d'un projet de programmation orienté objet.

Lausanne le 09.05.2023
