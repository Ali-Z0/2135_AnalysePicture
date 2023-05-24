import tkinter as tk
from PIL import ImageTk, Image  
import shape_recognition_func
import img_descr

IMAGE_RES = 400
path_str = "COUCOU"

# creates and runs an instance of the window
window = tk.Tk()
#makes the size of the widow
window.geometry("1000x800")
window.resizable(width=False, height=False)

# sets a title for the screen
window.title("Shape detection and analysis")

# Label chemin d'acces a l'image
tk.Label(window,text='Chemin image').place(relx=0.03, rely=0.01)
img_path_txt = tk.Text(window, height=1, width=27)
img_path_txt.place(relx=0.03, rely=0.04)

# Label + texte TL 
tk.Label(window,text='Seuil hysteresis bas : Th_l').place(relx=0.5, rely=0.01)
tl_txt = tk.Text(window, height=1, width=16)
tl_txt.insert(tk.END, 150)
tl_txt.place(relx=0.5, rely=0.04)

# Label + texte TH
tk.Label(window,text='Seuil hysteresis haut : Th_h').place(relx=0.65, rely=0.01)
th_txt = tk.Text(window, height=1, width=16)
th_txt.insert(tk.END, 300)
th_txt.place(relx=0.65, rely=0.04)

# Label + texte FORME
tk.Label(window,text='Forme déduite :').place(relx=0.5, rely=0.68)
shape_txt = tk.Text(window, height=1, width=16, state= tk.DISABLED)
shape_txt.place(relx=0.5, rely=0.71)

# Label + texte Model ML
tk.Label(window,text='Chemin model Machine learning, resnet-18 :').place(relx=0.03, rely=0.68)
resnet_txt = tk.Text(window, height=1, width=40)
resnet_txt.insert(tk.END, 'C:/Users/alizoubir/Documents/ETML-ES-2eme/POBJ/2135_AnalysePicture/soft/V2/ML_Models')
resnet_txt.place(relx=0.03, rely=0.71)

# Label + texte resultat ML
tk.Label(window,text='Analyse ML image :').place(relx=0.03, rely=0.85)
ml_result_txt = tk.Text(window, height=1, width=35, state=tk.DISABLED)
ml_result_txt.place(relx=0.03, rely=0.88)

def btn_img_select():
    window.path_str = img_path_txt.get(1.0, 'end')
    window.path_str = window.path_str.strip()
    try:
        # Ouverture image depuis chemin
        img = Image.open(window.path_str)
        img_display = img.resize((IMAGE_RES, IMAGE_RES), Image.LANCZOS)
        img_display = ImageTk.PhotoImage(img_display)
        # Affichage label avec image
        lbl_image_loaded = tk.Label(image=img_display)
        lbl_image_loaded.image = img_display
        lbl_image_loaded.place(relx=0.03, rely=0.16)
        # Suppresion image chargée
        img_path_txt.delete(1.0, tk.END)
        # Activation bouton coutour
        btn_img_shape_sel['state'] = tk.NORMAL
    except ValueError:
        print("Image non-lisible")

def btn_img_shape():
    tl = tl_txt.get(1.0, tk.END).strip()
    th = th_txt.get(1.0, tk.END).strip()
    try:
        # Conversion valeurs lue dans textes
        tl = float(tl)
        th = float(th)
        # Chargement image avec coutours
        img_analysis, shape = shape_recognition_func.getshape(window.path_str, th, tl)
        img_shape = Image.fromarray(img_analysis)
        img_shape = img_shape.resize((IMAGE_RES, IMAGE_RES), Image.LANCZOS)
        img_shape = ImageTk.PhotoImage(img_shape)
        # Affichage label image
        lbl_image_shape = tk.Label(image=img_shape)
        lbl_image_shape.image = img_shape
        lbl_image_shape.place(relx=0.5, rely=0.16)
        # Affichage forme
        shape_txt.config(state=tk.NORMAL)
        shape_txt.delete(1.0, tk.END)
        shape_txt.insert(tk.END, shape)
        shape_txt.config(state=tk.DISABLED)
    except ValueError:
        print("Erreur contours")
        

def btn_img_describe():
    try:
        ml_path = resnet_txt.get(1.0, tk.END).strip()
        descr_eng, descr_fr = img_descr.getAnalyze(window.path_str, ml_path)
        
        ml_result_txt.config(state=tk.NORMAL)
        ml_result_txt.delete(1.0, tk.END)
        ml_result_txt.insert(tk.END, descr_eng)
        ml_result_txt.config(state=tk.DISABLED)
        
    except ValueError:
        print("Erreur description de l'image")
        

btn_img_select = tk.Button(text="Charger image", command=btn_img_select, width=25, height=2)
btn_img_select.place(relx=0.03, rely=0.1)

btn_img_shape_sel = tk.Button(text="Analyse d'image", command=btn_img_shape, width=25, height=2, state=tk.DISABLED)
btn_img_shape_sel.place(relx=0.5, rely=0.1)

btn_img_descr = tk.Button(text="Reconnaissance d'image\nMachine learning", command=btn_img_describe, width=25, height=4)
btn_img_descr.place(relx=0.03, rely=0.75)

window.mainloop()
