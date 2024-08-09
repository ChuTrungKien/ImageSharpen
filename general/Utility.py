import base64
from PIL import Image
from io import BytesIO


# convert base64 to image:
def base64_to_image(base64_string):
    # Remove the data URI prefix if present
    if "data:image" in base64_string:
        base64_string = base64_string.split(",")[1]

    # Decode the Base64 string into bytes
    img_bytes = base64.b64decode(base64_string)

    # Create a BytesIO object to handle the image data
    img_stream = BytesIO(img_bytes)

    # Open the image using Pillow (PIL)
    image = Image.open(img_stream)
    return image


def image_to_base64(image):
    image_data = image.read()

    # Encode the image data to base64
    encoded_string = base64.b64encode(image_data).decode('utf-8')
    return encoded_string
