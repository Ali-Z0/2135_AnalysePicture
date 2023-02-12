import cv2
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

img_folder=r'C:\Users\alizoubir\Documents\ETML-ES-2eme\POBJ\2135_AnalysePicture\soft\V2\Shapes-Dataset\output'


#datasetPath = "./Shapes-Dataset/output"

plt.figure(figsize=(20,20))


for i in range(5):
    file = random.choice(os.listdir(img_folder))
    image_path= os.path.join(img_folder, file)
    img=mpimg.imread(image_path)
    ax=plt.subplot(2,5,i+1)
    ax.title.set_text("Image " + str(i))
    plt.imshow(img)


    # Convert image in grayscale
    grayscale = cv2.imread(image_path,0)
    #grayscale = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2GRAY)
    
    # setting threshold of gray image
    #_, threshold = cv2.threshold(grayscale, 127, 255, 0)
    # using a findContours() function
    #contour, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #edge = cv2.Canny((grayscale*255).astype(np.uint8), 10, 20)

    edged = cv2.Canny(grayscale, 30, 200)

    #contours = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #contours, hierarchy = cv2.findContours(threshold, 1, 2) 

    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    ax=plt.subplot(2,5,i+1+5)
    ax.title.set_text("Image Shape " + str(i))

    # list for storing names of shapes
    for contour in contours:
      
        # here we are ignoring first counter because 
        # findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue
      
        # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        # using drawContours() function
        plt.imshow(cv2.drawContours(grayscale, [contour], 0, (0, 0, 255), 2))
      
        # finding center point of shape
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
      
        # putting shape name at center of each shape
        if len(approx) == 3:
            print("Triangle")
      
        elif len(approx) == 4:
            print("Quadrilatere")
      
        elif len(approx) == 5:
            print("Pentagone")
      
        elif len(approx) == 6:
            print("Hexagone")
      
        else:
            print("Cercle")

plt.show()

# convert to grayscale

#grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# perform edge detection
#edges = cv2.Canny(grayscale, 30, 100)

#ax=plt.subplot(1,6,6)
#ax.title.set_text("Image 6")
