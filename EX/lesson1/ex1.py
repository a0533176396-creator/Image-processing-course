import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ex1

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

def cos_and_sin():
    arrMaalot= [0, 90, 180, 45, 30, 10, 5, 1]
    print("degrees, radians, sin, cos")
    for i in range(8):
        x = degrees_to_radians(arrMaalot[i])
        print(f"{arrMaalot[i]}, {x} ,{math.cos(x)} , {math.sin(x)}")


                 
