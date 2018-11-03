# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import pytesseract
import PIL.ImageOps    

#english text picture
#open the image and change to RGB mode
image = Image.open('C:/Users/LeeYipFung/Desktop/trip cost.png').convert('RGB')

#invert image colour
inverted_image = PIL.ImageOps.invert(image)

#save inverted image
inverted_image.save('C:/Users/LeeYipFung/Desktop/INVT_trip cost.png')


#extract and print the text from image
print ("English text\n--------------------------------------\n\n"+pytesseract.image_to_string(inverted_image))




#chinese simplified text picture
#open the image and change to RGB mode
image = Image.open('C:/Users/LeeYipFung/Desktop/cn_text.PNG').convert('RGB')

#invert image colour
inverted_image = PIL.ImageOps.invert(image)

#save inverted image
inverted_image.save('C:/Users/LeeYipFung/Desktop/INVT_cn_text.png')



print ("\n\n\nChinese Simplfied text\n--------------------------------------\n\n"+pytesseract.image_to_string(image, lang='chi_sim'))
#print (pytesseract.image_to_string(inverted_image, lang='chi_sim'))




