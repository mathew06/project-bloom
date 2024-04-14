import cv2
import pandas as pd

def set_imgLocation(loc):
    img_path = loc
    global img
    img = cv2.imread(img_path)

# declaring global variables (are used later on)
r = g = b = x_pos = y_pos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('C:/Users/Downloads/test-project/flask-server/colors.csv', names=index, header=None)


# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

def color_function(x, y):
    global b, g, r, x_pos, y_pos 
    x = int(x)
    y = int(y)
    x_pos = x
    y_pos = y
    b, g, r = img[y, x]
    b = int(b)
    g = int(g)
    r = int(r)
    color = get_color_name(r, g, b)
    return color
    
