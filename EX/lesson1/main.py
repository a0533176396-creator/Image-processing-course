import ex1
import ex2
import ex3
import numpy as np

if __name__ == "__main__":
    x = ex1.degrees_to_radians(90)
    print(x)
    ex1.cos_and_sin()
    mat=[
        [1,5,7,6,],
        [1,5,7,6,],
        [1,5,7,6,]
    ]
    mat=np.matrix(mat)
    x= ex2.turn_the_mat(mat,5)
    x=ex2.scale(mat)
    print(mat)
    print(x)
    ex3.fun_of_matrix()