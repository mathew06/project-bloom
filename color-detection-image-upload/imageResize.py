from PIL import Image

# Function to resize image to specified size
def resize_image(image):
    # Open the image
    img = Image.open(image)
    # Resize the image to specified size
    img_resized = img.resize((700, 550), Image.LANCZOS)
    return img_resized