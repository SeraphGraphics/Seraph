
class Structure2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

class ViewContainer:
    def __init__(self, left, right, up, bottom):
        self.left = left
        self.right = right
        self.up = up
        self.bottom = bottom


