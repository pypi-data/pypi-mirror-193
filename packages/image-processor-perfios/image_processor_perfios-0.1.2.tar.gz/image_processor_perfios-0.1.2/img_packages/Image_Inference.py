from PIL import Image
from io import BytesIO
def image_inference(image):
    #image = Image.open(BytesIO(file.read()))
    img = Image.open(image)
    img = img.convert('L')
    return img