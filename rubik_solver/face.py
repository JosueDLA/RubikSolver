import numpy as np
import cv2


class Face(tuple):
    def __new__(self, width):
        self.width = width
        return tuple.__new__(Face, (self.width,))

    def get_coordinates(self):
        faces = []
        y = []
        x = []

        margin = 1
        initial = 40
        available = 80
        border = (100 - available)/2
        size = (available/4) - (margin*2)

        first = border + margin

        for i in range(4):
            x.append(first)
            second = first + size
            x.append(second)
            first = second + (margin*2)
            second = first + size

        first = initial + margin

        for i in range(3):
            y.append(first)
            second = first + size
            y.append(second)
            first = second + (margin*2)
            second = first + size

        x = [int((e/100) * self.width) for e in x]
        y = [int((e/100) * self.width) for e in y]

        # Faces U L F R B D
        faces.append(((x[2], y[0]), (x[3], y[1])))
        faces.append(((x[0], y[2]), (x[1], y[3])))
        faces.append(((x[2], y[2]), (x[3], y[3])))
        faces.append(((x[4], y[2]), (x[5], y[3])))
        faces.append(((x[6], y[2]), (x[7], y[3])))
        faces.append(((x[2], y[4]), (x[3], y[5])))

        return faces
