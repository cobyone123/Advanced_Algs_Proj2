from PyQt5.QtCore import QLineF, QPointF
from itertools import cycle


class hull:

    def __init__(self, points):
        self.points = list(points)
        self.UL = 0
        self.LL = 0
        self.UR = 0
        self.LR = 0

    def get_next(self):
        point = cycle(self.points)
        return next(point)

    def get_previous(self):
        point = reversed(self.points)
        return iter(point)

    def get_right_most(self):
        pointsIterator = self.points
        xIndex = max(range(len(pointsIterator)), key=lambda i: pointsIterator[i].x())
        return xIndex


    def get_points(self):
        return self.points

    def add_point(self, point):
        for i in range(len(self.points)):
            print(self.slope(self.points[i], self.points[0]) < self.slope(point, self.points[i]))
            if self.slope(self.points[i], self.points[0]) < self.slope(point, self.points[i]):
                self.points.insert(i, point)
                print(self.points[i], point.x)