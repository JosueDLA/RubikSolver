import numpy as np
import cv2


class Cube:
    def __init__(self, U, R, F, D, L, B):
        self.U = U
        self.R = R
        self.F = F
        self.D = D
        self.L = L
        self.B = B

    def get_string(self):
        cube = "".join(self.U + self.R + self.F + self.D + self.L + self.B)
        return cube

    def get_faces(self):
        faces = []
        faces.append(self.U[4])
        faces.append(self.R[4])
        faces.append(self.F[4])
        faces.append(self.D[4])
        faces.append(self.L[4])
        faces.append(self.B[4])

        return faces
