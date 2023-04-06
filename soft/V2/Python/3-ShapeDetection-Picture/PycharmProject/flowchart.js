op2=>operation: " Script qui trace les contours d'images réelles "
op4=>operation: import numpy as np
op6=>operation: import random
op8=>operation: import matplotlib.pyplot as plt
op10=>operation: import matplotlib.image as mpimg
op12=>operation: import argparse
op14=>operation: import time
op16=>operation: import os
op18=>operation: import cv2
op20=>operation: img_folder = 'C:\\Users\\alizoubir\\Documents\\ETML-ES-2eme\\POBJ\\2135_AnalysePicture\\soft\\V2\\Python\\3-ShapeDetection-Picture\\PycharmProject\\Images-examples'
op22=>operation: parser = argparse.ArgumentParser()
sub24=>subroutine: parser.add_argument('-Th', '--T_upper', type=float, default=50, help="Valeur supérieur dans le Seuil d'hystérésis")
sub26=>subroutine: parser.add_argument('-Tl', '--T_lower', type=float, default=10, help="Valeur inférieur dans le Seuil d'hystérésis")
op28=>operation: args = parser.parse_args()
op30=>operation: T_lower = 235
op32=>operation: T_upper = 500
op34=>operation: shapes = np.array(['Nothing', 'Line', 'Angle', 'Triangle', 'Square', 'Pentagon', 'Hexagon', 'Heptagon', 'Octagon', 'Nonagon', 'Star'])
op36=>operation: file = random.choice(os.listdir(img_folder))
op38=>operation: image_path = os.path.join(img_folder, file)
op40=>operation: img = mpimg.imread(image_path)
op42=>operation: fig = plt.figure()
op44=>operation: ax = plt.subplot(1, 2, 1)
sub46=>subroutine: ax.title.set_text('Image sans contours')
sub48=>subroutine: plt.imshow(img)
op50=>operation: grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
op52=>operation: edged = cv2.Canny(grayscale, T_lower, T_upper)
op54=>operation: (contours, hierarchy) = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
op56=>operation: nbContours = len(contours)
cond59=>condition: if nbContours
cond64=>condition: for ContCnt in range(nbContours)
op93=>operation: cnt = contours[ContCnt]
op95=>operation: approx = cv2.approxPolyDP(cnt, (0.01 * cv2.arcLength(cnt, True)), True)
cond98=>condition: if (len(approx) < 11)
op102=>operation: shape = shapes[len(approx)]
op109=>operation: ax = plt.subplot(1, 2, 2)
sub111=>subroutine: ax.title.set_text('Image avec contours')
op113=>operation: imgRecolored = cv2.cvtColor(grayscale, cv2.COLOR_GRAY2BGR)
sub115=>subroutine: plt.imshow(cv2.drawContours(imgRecolored, contours, (- 1), (255, 0, 0), 2))
op106=>operation: shape = 'Circle'
sub122=>subroutine: plt.savefig((('logs/SavedFig' + time.strftime('%Y-%m-%d %H%M%S')) + '.png'))
sub124=>subroutine: plt.show()

op2->op4
op4->op6
op6->op8
op8->op10
op10->op12
op12->op14
op14->op16
op16->op18
op18->op20
op20->op22
op22->sub24
sub24->sub26
sub26->op28
op28->op30
op30->op32
op32->op34
op34->op36
op36->op38
op38->op40
op40->op42
op42->op44
op44->sub46
sub46->sub48
sub48->op50
op50->op52
op52->op54
op54->op56
op56->cond59
cond59(yes)->cond64
cond64(yes)->op93
op93->op95
op95->cond98
cond98(yes)->op102
op102->op109
op109->sub111
sub111->op113
op113->sub115
sub115(left)->cond64
cond98(no)->op106
op106->op109
cond64(no)->sub122
sub122->sub124
cond59(no)->sub122