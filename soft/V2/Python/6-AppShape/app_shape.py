import tkinter as tk
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import time
import os
import cv2

# creates and runs an instance of the window
window = tk.Tk()
#makes the size of the widow
window.geometry("600x300")

#sets a title for the screen
window.title("Shape detection and analysis")

# Label chemin d'acces a l'image
tk.Label(window,text='Chemin image').place(relx=0.03, rely=0.01)
img_path_txt = tk.Text(window, height=1, width=27)
img_path_txt.place(relx=0.03, rely=0.07)



def btn_img_select():
    path_str = img_path_txt.get(1.0, 'end')

    
    try:
        img = mpimg.imread(path_str)
        plt.imshow(img)
    except ValueError:
        print("Image non-lisible")


btn_img_select = tk.Button(text="Valider", command=btn_img_select).place(relx=0.03, rely=0.16)

window.mainloop()
