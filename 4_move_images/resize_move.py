from PIL import Image
import os

for img in os.listdir('.'):
    if img.endswith('.jpg'):
        image = Image.open(img)
        image.thumbnail((400, 400))
        image.save('Resize_to400/{}'.format(img))
