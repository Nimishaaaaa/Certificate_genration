from PIL import Image, ImageDraw, ImageFont
img=Image.open(r'''./Certificate.jpg''')

import matplotlib.pyplot as plt
import numpy as np

def print_img(img):
    plt.imshow(np.array(img))  
    plt.show()

import cv2
img=cv2.imread("./Certificate.jpg")

def generated_certificate(img,name="enter name"):
    generated_img=img.copy()
    font=cv2.FONT_HERSHEY_SIMPLEX
    cordinates =(700,750)
    font_size=3.5
    font_color=(51,51,51)
    font_thic=10
    cv2.putText(generated_img, name,cordinates,font,font_size,font_color, font_thic)
    return generated_img

def save_img(img,name):
    path="./certi_{}.jpg".format(name)
    print(cv2.imwrite(path,img))
    
name=input(("KINDLY ENTER THE NAME OF PARTICIPANT::"))
generated_img= generated_certificate(img,name)
save_img(generated_img, name)

