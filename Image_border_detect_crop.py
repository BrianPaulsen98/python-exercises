# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:02:35 2017

@author: asinghal
"""
# please insall ENIMDA using this: pip install enimda
from enimda import ENIMDA
from PIL import Image, ImageChops

#function to detect if the image has any border
def has_border(img_name):
    em=ENIMDA(fp=img_name)
    borders=em.scan(fast=False)
    if (borders[0]==0) & (borders[1]==0) & (borders[2]==0) & (borders[3]==0):
        return 'False'
    else:
        print(borders)
        return 'True'
    
#function to remove any border present in the image. If no border then image remains as is. No rescaling done. Only cropping.    
def filter_border(img_name):
    em=ENIMDA(fp=img_name)
    im = Image.open(img_name)
    width=im.size[0]
    height=im.size[1]
    borders=em.scan(fast=False)
    top=borders[0]
    right=borders[1]
    bottom=borders[2]
    left=borders[3]
    im_edited=im.crop((0+right,0+top,width-left,height-bottom))
    img_arr=img_name.split('\\')
    img_file=img_arr[-1]
    img_new=img_file.replace('.','_edited.')
    new_img_path='\\'.join(img_arr[0:len(img_arr)-1])+'\\'+img_new
    im_edited.save(new_img_path)

 

#print(has_border('7213212-5.jpeg'))
filter_border('7213212-5.jpeg')

#print(has_border('C:\\Users\\asinghal.CONTATAS\\Pictures\\7161094-1.jpeg'))
#filter_border('C:\\Users\\asinghal.CONTATAS\\Pictures\\7161094-1.jpeg')