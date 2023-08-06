from PIL import Image

def image_resize(image):
    img = Image.open(image)
    width, height = img.size
    new_width = 800
    new_height = round(height*new_width/width)
    resized_img = img.resize((new_height,new_width))
    return resized_img

