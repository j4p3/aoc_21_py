import utils.input as input

def one(filename):
    increases = 0
    depths = parse_input(filename)
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increases += 1
    return increases

def two(filename):
    increases = 0
    depths = parse_input(filename)
    depth_chunks = input.chunk(depths, 3, 1)
    depth_sums = [sum(chunk) for chunk in depth_chunks]
    for i in range(1, len(depth_sums)):
        if depth_sums[i] > depth_sums[i - 1]:
            increases += 1
    return increases

def parse_input(filename):
    lines = input.file_lines(f"/days/one/{filename}.txt")
    return [int(l) for l in lines]
