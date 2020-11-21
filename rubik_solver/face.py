import numpy as np
import cv2


class Face(tuple):
    def __new__(self, height, width):
        self.height = height
        self.width = width
        return tuple.__new__(Face, (self.width, self.height))

    def get_coordinates(self, porcentage=40):
        faces = []
        faces_x = []
        faces_y = []

        margin = 1
        available_x = porcentage
        margin_x = (100 - available_x)/2
        size = (available_x/4) - (margin*2)

        # Biggest axis
        axis = self.width if self.width > self.height else self.height

        # Calculate x axis values
        first = margin_x + margin

        for i in range(4):
            faces_x.append(first)
            second = first + size
            faces_x.append(second)
            first = second + (margin*2)
            second = first + size

        # Calculate y axis values
        first = 100 + margin

        for i in range(3):
            faces_y.append(first)
            second = first + size
            faces_y.append(second)
            first = second + (margin*2)
            second = first + size

        # Calculate extra space in x axis
        extra_x = (faces_x[-1]/100) * axis
        extra_x = (self.width - extra_x)
        extra_x = 0 if extra_x > 0 else abs(extra_x)

        # Center faces in x axis
        if extra_x != 0:
            center_x = (margin_x/100) * self.width
            extra_x = center_x - extra_x
            print(extra_x)

        # Calculate extra space in y axis
        extra_y = (faces_y[-1]/100) * axis
        extra_y = (self.height - extra_y)
        extra_y = 0 if extra_y > 0 else abs(extra_y)

        # Calculate faces coordinates according to resolution
        faces_x = [int(((e/100) * axis) - extra_x) for e in faces_x]
        faces_y = [int(((e/100) * axis) - extra_y) for e in faces_y]

        # Faces U L F R B D
        faces.append(((faces_x[2], faces_y[0]), (faces_x[3], faces_y[1])))
        faces.append(((faces_x[0], faces_y[2]), (faces_x[1], faces_y[3])))
        faces.append(((faces_x[2], faces_y[2]), (faces_x[3], faces_y[3])))
        faces.append(((faces_x[4], faces_y[2]), (faces_x[5], faces_y[3])))
        faces.append(((faces_x[6], faces_y[2]), (faces_x[7], faces_y[3])))
        faces.append(((faces_x[2], faces_y[4]), (faces_x[3], faces_y[5])))

        return faces
