import cv2
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

IMG_WIDTH=200
IMG_HEIGHT=200
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

    ax=plt.subplot(2,5,i+1+5)
    ax.title.set_text("Image gray " + str(i))
    grayscale = cv2.imread(image_path,0)
    edge = cv2.Canny(grayscale, 10, 20)
    plt.imshow(edge)

plt.show()

# convert to grayscale

#grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# perform edge detection
#edges = cv2.Canny(grayscale, 30, 100)

#ax=plt.subplot(1,6,6)
#ax.title.set_text("Image 6")
