# Rotate a matrix
import numpy as np
def rotation_2d_matrix_theta(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

def rotate_2d_matrix(matrix_2d_to_rotate, theta):
    return rotation_2d_matrix_theta(theta) @ matrix_2d_to_rotate.T