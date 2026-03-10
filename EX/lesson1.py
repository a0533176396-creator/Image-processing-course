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
def fun_of_matrix():
    orginal_mat=[
        [1,5,7,6,],
        [1,5,7,6,],
        [1,5,7,6,]
    ]
    orginal_mat=np.matrix(orginal_mat)
    print(f"original matrix: {orginal_mat}")
    r_30=turn_the_mat(orginal_mat,30)
    print(f"after turn 30: {r_30}")
    sx_2=scale_x_manual(orginal_mat)
    print(sx_2)
    rs= r_30 @ sx_2
    sr= sx_2 @ r_30
    fig, ax = plt.subplots()
    ax.imshow(orginal_mat, cmap='gray')
    rect = patches.Rectangle((2, 3), width=5, height=4, linewidth=2, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    plt.show()

                 
if __name__ == "__main__":
    # # x = degrees_to_radians(90)
    # # print(x)
    # cos_and_sin()
    # mat=[
    #     [1,5,7,6,],
    #     [1,5,7,6,],
    #     [1,5,7,6,]
    # ]
    # mat=np.matrix(mat)
    # # x= turn_the_mat(mat,5)
    # x=scale(mat)
    # print(mat)
    # print(x)
    fun_of_matrix()