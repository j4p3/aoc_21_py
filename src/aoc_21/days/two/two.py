import utils.input as input

def one(filename):
    directions = parse_input(filename)
    x = y = 0
    for direction, distance in directions:
        match direction:
            case "forward":
                x += distance
            case "down":
                y += distance
            case "up":
                y -= distance
    return x * y

def two(filename):
    directions = parse_input(filename)
    x = y = aim = 0
    for direction, distance in directions:
        match direction:
            case "forward":
                x += distance
                y += aim * distance
            case "down":
                aim += distance
            case "up":
                aim -= distance
    return x * y

        
def _process_line(line):
    [direction, distance] = line.split()
    return (direction, int(distance))


def parse_input(filename):
    lines = input.file_lines(f"/days/two/{filename}.txt")
    return map(_process_line, lines)