import cv2
import numpy as np


Camera_intrinsic = {
    "mtx": np.array([[539.4118538, 0.00000000e+00, 321.1254354],
                     [0.00000000e+00, 540.02901063, 234.35062125], 
                     [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]],
                    dtype=np.double),
    "dist": np.array([[-0.06488393,  0.14645391, -0.0042577,  -0.00099087,
                       0.01829749]], dtype=np.double),
}

def pnp(img_points, d=20):
    # object_points = np.zeros((4, 3), np.float32)  
    # #print(object_points)
    # object_points[:, :2] = np.mgrid[0:2, 0:2].T.reshape(-1, 2)  
    # #print(object_points)

    # object_points = object_points*20
    object_points=np.array([[0, 0, 2.35], [0, 2.35, 2.35], [0, 0, 0], [0, 2.35, 0]], dtype=np.float32)
    print(object_points)


    image_points = np.array(img_points, dtype=np.float32)

    success, rotation_vector, translation_vector = cv2.solvePnP(
                                                                object_points,
                                                                image_points,
                                                                Camera_intrinsic["mtx"],
                                                                Camera_intrinsic["dist"])
    
    rotation_matrix, _ = cv2.Rodrigues(rotation_vector)
    # print("Rotation Vector:\n", rotation_vector)
    print("Translation Vector:\n", translation_vector)
    print("Rotation Matrix:\n", rotation_matrix)

    return rotation_matrix, translation_vector

if __name__ == "__main__":
    img_points = [[1608.5, 1250.5], [2025.5, 1095.5], [1784.5, 1684.5], [2195.5, 1502.5]]
    pnp(img_points)