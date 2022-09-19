from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
pathOut = './editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN())
    edit = ImageEnhance.Contrast(edit).enhance(1.3).rotate(-90)

    cleanname = os.path.splitext(filename)[0]

    edit.save(f"{pathOut}/{cleanname}_edited.png", 'png')