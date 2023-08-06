from PIL import Image
from io import BytesIO
def image_inference(image):
    #image = Image.open(BytesIO(file.read()))
    image = image.convert('L')
    return image