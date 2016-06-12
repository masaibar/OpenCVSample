# -*- coding:utf-8 -*-

class PolkaDot:

    def __init__(self, center_x, center_y, radius):
        self.x = center_x
        self.y = center_y
        self.r = radius

    def get_center(self):
        return (self.x, self.y)

    def get_radius(self):
        return self.r