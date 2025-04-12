import csv

def points_from_csv(file_path) -> list[tuple]:
    points = []
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            points.append(tuple(row))
    return points