import ex2
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def fun_of_matrix():
    orginal_mat=[
        [1,5,7,6,],
        [1,5,7,6,],
        [1,5,7,6,]
    ]
    orginal_mat=np.matrix(orginal_mat)
    print(f"original matrix: {orginal_mat}")
    r_30=ex2.turn_the_mat(orginal_mat,30)
    print(f"after turn 30: {r_30}")
    sx_2=ex2.scale_x_manual(orginal_mat)
    print(sx_2)
    rs= r_30 @ sx_2
    sr= sx_2 @ r_30
    fig, ax = plt.subplots()
    ax.imshow(orginal_mat, cmap='gray')
    rect = patches.Rectangle((2, 3), width=5, height=4, linewidth=2, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    plt.show()
