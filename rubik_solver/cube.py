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

    def __str__(self):
        pass

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

    @staticmethod
    def sort_contours(contours, method="left-to-right"):
        """
        Returns contours sorted from right to left and top to bottom
        """

        # Get bound box for each contour
        bounding_boxes = [cv2.cv2.boundingRect(
            contour) for contour in contours]

        # Zip contour and bounding boxes
        squares = zip(contours, bounding_boxes)
        squares = list(squares)

        if len(contours) >= 7:
            # Sort squares by Y value
            squares.sort(key=lambda b: b[1][1])

            first_row = squares[:3]
            second_row = squares[3:6]
            third_row = squares[6:9]

            # Sort squares by X value
            first_row.sort(key=lambda b: b[1][0])
            second_row.sort(key=lambda b: b[1][0])
            third_row.sort(key=lambda b: b[1][0])

            squares = first_row + second_row + third_row

            contours, bounding_boxes = zip(*squares)

        return contours, bounding_boxes
