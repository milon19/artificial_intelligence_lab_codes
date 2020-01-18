from PIL import Image
img = Image.open('7.jpg')
img.resize((200, 200)).save('newSize.png')
img_new = Image.open('newSize.png')
img_new.show()