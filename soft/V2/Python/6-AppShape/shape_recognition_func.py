""" Script qui trace les contours d'images reelles """
import numpy as np
import matplotlib.image as mpimg
import cv2

#%%
def getshape(_img: str, Th: float, Tl: float):
    
    # ------ Hyperparametres------
    # Valeur seuil inferieure dans le Seuil d'hysteresis
    T_lower = Tl
    # Valeur seuil superieur dans le Seuil d'hysteresis
    T_upper = Th
    # ------ Parametres interface ------
    # Noms des formes selon les cotes
    shapes = np.array(["Nothing", "Line", "Angle", "Triangle", "Rectangle", "Pentagon",
                       "Hexagon", "Heptagon", "Octagon", "Nonagon", "Star"])
    

    img = mpimg.imread(_img)

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
            # Reconvertit l'image en format couleur
            imgRecolored = cv2.cvtColor(
            grayscale, cv2.COLOR_GRAY2BGR)
            # Affiche l'image avec les contours en couleurs
            imgCnt = cv2.drawContours(imgRecolored, contours, -1, (255, 0, 0), 2)
    
    
    #%%
    # Shape recognition
    cv2.HuMoments(cv2.moments(grayscale)).flatten()
    
    return(imgCnt, shape[0])
    # %%
