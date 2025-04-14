from csv_extractor import points_from_csv

def mid(values: list[int]) -> int:
    if len(values) == 0:
        return 0
    return sum(values) / len(values)

class Table():
    def __init__(self, csv_file_path: str):
        table = points_from_csv(csv_file_path)
        self.title = table[0]
        self.points = table[1:]
        for i in range(len(self.points)):
            point = self.points[i]
            self.points[i] = tuple(float(value) for value in point)

    def get_stats(self) -> dict:
        stats = dict.fromkeys(self.title)
        for i in range(len(stats.keys())):
            values = [val[i] for val in self.points]
            block = (max(values), min(values), mid(values))
            stats[self.title[i]] = block
        return stats
    
    @property
    def x(self) -> list:
        return list(point[0] for point in self.points)
    
    @property
    def y(self) -> list:
        return list(point[1] for point in self.points)
    
    def swap_x_y(self) -> None:
        new_points = []
        for point in self.points:
            new_point = (point[1], point[0])
            new_points.append(new_point)
        self.points = new_points
        self.title = (self.title[1], self.title[0])
    
class LineFunction():
    def __init__(self, w0: float, w1: float, x: list):
        self.w0 = w0
        self.w1 = w1
        self.x = x

    @property
    def y(self) -> list:
        return list(self.w0 + self.w1*value for value in self.x)
        
    
# table = Table("student_scores.csv")
# print(table.get_stats())
# print(table.points)
# print(table.y)