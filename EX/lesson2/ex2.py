import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import lesson1.ex1 as l1x1
import lesson1.ex2 as l1x2



def rectangle():
    orginal_mat=[
        [1,5,7,6,],
        [1,5,7,6,],
        [1,5,7,6,]
    ]
    fig, ax = plt.subplots()
    ax.imshow(orginal_mat, cmap='gray')
    rect = patches.Rectangle((2, 3), width=5, height=4, linewidth=2, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    # הוספת כותרת והצגה על המסך
    plt.title("Rectangle on a Matrix")
    plt.show()
    mat_after_turn= l1x2.turn_the_mat(orginal_mat, 30)
    ax.add_patch(mat_after_turn)
    mat_after_turn= l1x2.turn_the_mat(orginal_mat, 45)
    mat_after_turn= l1x2.scale_x_manual(mat_after_turn)
    ax.add_patch(mat_after_turn)
    mat_after_turn=l1x2.scale_x_manual(orginal_mat)
    mat_after_turn=l1x2.turn_the_mat(mat_after_turn, 45)
    ax.add_patch(mat_after_turn)
