import cv2
import pandas as pd
from colordata import getColorInfo

# Reading csv file with pandas and giving names to each column
index = ["color", "R", "G", "B", "hex"]
csv = pd.read_csv('./colorshades.csv', names=index, header=None)


# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color"]
            hex = csv.loc[i, "hex"]
    color_info = getColorInfo(cname)
    return cname,hex,color_info

def color_function(img_path,x, y):
    img = cv2.imread(img_path)
    x = int(x)
    y = int(y)
    b, g, r = img[y, x]
    b = int(b)
    g = int(g)
    r = int(r)
    color = get_color_name(r, g, b)
    return color
    
