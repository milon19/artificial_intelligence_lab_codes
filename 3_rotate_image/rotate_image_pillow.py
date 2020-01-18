from PIL import Image
img = Image.open('9.jpg')
img.rotate(90).save('newSize.png')
img_new = Image.open('newSize.png')
img_new.show()