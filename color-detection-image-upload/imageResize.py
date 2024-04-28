from PIL import Image

# Function to resize image to 500x500 size
def resize_image(image):
    # Open the image
    img = Image.open(image)
    # Resize the image to 500x500
    img_resized = img.resize((500, 500), Image.LANCZOS)
    return img_resized