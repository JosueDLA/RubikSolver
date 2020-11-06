import numpy as np
import cv2


class Face(tuple):
    def __new__(self, width):
        self.width = width
        return tuple.__new__(Face, (self.width,))

    def get_coordinates(self):
        faces = []
        horizontal = []
        vertical = []

        margin = 1
        initial = 40
        available = 80
        border = (100 - available)/2
        size = (available/4) - (margin*2)

        first = border + margin
        for i in range(4):
            vertical.append(first)
            second = first + size
            vertical.append(second)
            first = second + (margin*2)
            second = first + size

        first = initial + margin
        for i in range(3):
            horizontal.append(first)
            second = first + size
            horizontal.append(second)
            first = second + (margin*2)
            second = first + size

        # Faces U L F R B D
        faces.append(((horizontal[2], vertical[0]),
                      (horizontal[3], vertical[1])))
        faces.append(((horizontal[0], vertical[2]),
                      (horizontal[1], vertical[3])))
        faces.append(((horizontal[2], vertical[2]),
                      (horizontal[3], vertical[3])))
        faces.append(((horizontal[4], vertical[2]),
                      (horizontal[5], vertical[3])))
        faces.append(((horizontal[6], vertical[2]),
                      (horizontal[7], vertical[3])))
        faces.append(((horizontal[2], vertical[4]),
                      (horizontal[3], vertical[5])))

        return faces
