class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, origin, width, height):
        self.origin = origin
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_ending_point(self):
        end_point_x = self.origin.x + self.width
        end_point_y = self.origin.y + self.height
        return Point(end_point_x, end_point_y);
    
    def print_coordinates(self):
        end_point = self.get_ending_point();
        
        print('Starting Point (X)): ' + str(self.origin.x))
        print('Starting Point (Y)): ' + str(self.origin.y))
        print('End Point X-Axis (Top Right): ' + str(end_point.x))
        print('End Point Y-Axis (Bottom Left): ' + str(end_point.y))


def make_rectangle():
    rectangle_origin = Point(50, 100)
    rectangle = Rectangle(rectangle_origin, 90, 10);
    return rectangle


rectangle = make_rectangle()

print(rectangle.get_area())
rectangle.print_coordinates()