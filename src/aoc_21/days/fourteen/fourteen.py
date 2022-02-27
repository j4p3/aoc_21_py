import utils.input as input


# Not a DP problem - need to do a frequency count type solution instead. Never mind.
def one(filename, steps):
    template, rules = _parse_input(filename)
    step = 0
    while step < steps:
        template = polymerize(template, rules)
        step += 1

    return template


def polymerize(polymer, rules):
    return input.chunk(polymer)


def _split_line(line):
    tuple(line.split(" -> "))


def _parse_input(filename):
    lines = input.file_lines(f"/days/fourteen/{filename}.txt")
    template = [c for c in lines.pop(0)]
    rules = dict([_split_line(line) for line in lines])
    (template, rules)
