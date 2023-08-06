from PIL import Image
from io import BytesIO
def image_bw(image):
    image = image.convert('L')
    return image