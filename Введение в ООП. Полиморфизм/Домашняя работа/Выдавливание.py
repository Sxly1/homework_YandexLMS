from math import pi


class Square:
    def __init__(self, side):
        self.side = side

    def extrude(self, h):
        return self.side ** 2 * h


class Rectangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def extrude(self, h):
        return (self.side1 * self.side2) * h


class Triangle:
    def __init__(self, side):
        self.side = side

    def extrude(self, h):
        return (self.side ** 2) * (3 ** 0.5) / 4 * h


class Circle:
    def __init__(self, r):
        self.r = r

    def extrude(self, h):
        return pi * self.r ** 2 * h