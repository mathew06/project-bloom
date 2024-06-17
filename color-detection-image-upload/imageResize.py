from PIL import Image

# Function to resize image to specified size
def resize_image(x,y,image):
    # Open the image
    img = Image.open(image)
    # Resize the image to specified size
    img_resized = img.resize((x, y), Image.LANCZOS)
    return img_resized