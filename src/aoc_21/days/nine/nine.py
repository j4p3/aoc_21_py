import utils.input as input
from functools import reduce


def one(filename):
    elevations = parse_input(filename)
    low_points = _low_point_elevations(elevations)
    risk_levels = [i + 1 for i in low_points]
    return sum(risk_levels)


def two(filename):
    elevations = parse_input(filename)
    low_points = _low_points(elevations)
    basins = [_watershed(elevations, point) for point in low_points]
    basin_sizes = [len(basin) for basin in basins]
    three_largest = sorted(basin_sizes, reverse=True)[:3]
    return reduce(lambda acc, i: acc * i, three_largest)


def _watershed(elevations, point):
    visited = set([point])
    to_visit = _neighbors(elevations, point)

    while len(to_visit) > 0:
        x, y = next_point = to_visit.pop(0)
        if elevations[y][x] != 9:
            visited.add(next_point)
            to_visit += [
                p for p in _neighbors(elevations, next_point) if p not in visited
            ]

    return visited


def _low_point_elevations(elevations):
    low_points = []
    for y, row in enumerate(elevations):
        for x, elevation in enumerate(row):
            if _is_low_point(elevations, (x, y)):
                low_points.append(elevation)
    return low_points


def _low_points(elevations):
    low_points = []
    for y, row in enumerate(elevations):
        for x, elevation in enumerate(row):
            if _is_low_point(elevations, (x, y)):
                low_points.append((x, y))
    return low_points


def _is_low_point(elevations, coords):
    x, y = coords
    for xi, yi in _neighbors(elevations, coords):
        if elevations[yi][xi] < elevations[y][x]:
            return False
    return True


def _neighbors(elevations, coords):
    x, y = coords
    elevation = elevations[y][x]
    increments = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    borders = [(x + xi, y + yi) for xi, yi in increments]
    is_in_bounds = (
        lambda xi, yi: xi >= 0
        and yi >= 0
        and xi < len(elevations[0])
        and yi < len(elevations)
    )
    return [(xi, yi) for xi, yi in borders if is_in_bounds(xi, yi)]


def _split_line(line: str) -> list[int]:
    return [int(i) for i in line]


def parse_input(filename):
    lines = input.file_lines(f"/days/nine/{filename}.txt")
    return [_split_line(l) for l in lines]
