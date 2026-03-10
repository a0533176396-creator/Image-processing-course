import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ex2
def turn_the_mat(point_matrix, maatot):
    (h, w) = point_matrix.shape[:2]
    # הגדרת הראשית כציר הסיבוב
    origin = (0, 0)
    
    # יצירת מטריצת הטרנספורמציה 2x3
    R_cv2 = cv2.getRotationMatrix2D(origin, maatot, 1.0)
    
    # הפעלת הסיבוב על המטריצה השלמה
    # warpAffine עוברת על כל תא, מחשבת את מיקומו החדש ומעתיקה את הערך
    rotated_matrix = cv2.warpAffine(point_matrix, R_cv2, (w, h))
    
    return rotated_matrix

def scale(mat):
    h = int(len(mat))
    w = int(len(mat[0]))
    mat2 = np.zeros((h*2, w*2))
    for i in range(h):
        for j in range(w):
            pixel_value = mat[i][j]
            
            # במקום לשים את הפיקסל רק בתא אחד, נשכפל אותו לבלוק של 2x2
            mat2[i*2,j*2]= pixel_value # שמאלי עליון
            mat2[i*2+1,j*2]= pixel_value # שמאלי תחתון
            mat2[i*2,j*2+1]= pixel_value # ימני עליון
            mat2[i*2+1,j*2+1]= pixel_value # ימני תחתון
            
    return mat2
def scale_x_manual(mat):
    h = len(mat)
    w = len(mat[0])
    
    # יצירת המטריצה החדשה: הגובה נשאר h, הרוחב מוכפל פי 2
    mat2 = np.zeros((h, w * 2), dtype=np.uint8)
    
    for i in range(h):
        for j in range(w):
            pixel_value = mat[i][j]
            
            # שכפול הפיקסל רק ימינה (על ציר ה-X, כלומר באותה שורה i)
            mat2[i, j * 2]     = pixel_value # המיקום המקורי המורחב
            mat2[i, j * 2 + 1] = pixel_value # הפיקסל המשוכפל מימינו
            
    return mat2
