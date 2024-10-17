import math

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.m = self.calc_m(point1, point2)
        self.n = self.calc_n(self.m, point1)
        
    def calc_m(self, point1, point2):
        return (point1[1] - point2[1]) / (point1[0] - point2[0]) if point1[0] != point2[0] else math.inf
        
    def calc_n(self, m, point1):
        return point1[1] - self.m * point1[0]
    
    def point(self, m, n, x):
        return (x, m * x + n)
    
    def point_in_radio(self, r) -> 'Line':
        dx = self.point2[0] - self.point1[0]
        dy = self.point2[1] - self.point1[1]

        magnitude = math.sqrt(dx**2 + dy**2)

        if magnitude == 0:
            return None  

        ux = dx / magnitude
        uy = dy / magnitude

        new_x = round(self.point1[0] + r * ux)
        new_y = round(self.point1[1] + r * uy)

        return Line(self.point1, (new_x, new_y))
             
    @staticmethod
    def dist_point_to_point(self, start_point: tuple[int, int], end_point: tuple[int, int]):
        dx = end_point[0] - start_point[0]
        dy = end_point[1] - start_point[1]
        return math.sqrt(dx**2 + dy**2)
        
        
    def dist(self, x2, y2, m, n, d, vector):
        start_point = vector[0]
        end_point = vector[1]

        dx = end_point[0] - start_point[0]
        dy = end_point[1] - start_point[1]

        magnitude = math.sqrt(dx**2 + dy**2)

        if magnitude == 0:
            return None

        ux = dx / magnitude
        uy = dy / magnitude

        new_x = round(x2 + d * ux)
        new_y = round(y2 + d * uy)

        return (new_x, new_y)