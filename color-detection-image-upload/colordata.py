import json

# Load color data from JSON file
with open('colors.json', 'r') as f:
    colors_data = json.load(f)

def getColorInfo(color_name):
    # Find the color data corresponding to the given color name
    color_info = next((color for color in colors_data if color['name'] == color_name), None)

    if color_info:
        return color_info
    else:
        return 'Color not found'