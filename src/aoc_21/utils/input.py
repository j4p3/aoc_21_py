from config import PROJECT_PATH

def file_lines(filepath):
    with open(PROJECT_PATH + filepath) as file:
        lines = [line.rstrip() for line in file]
    return lines


def chunk(list, chunk_size, chunk_step):
    for i in range(0, len(list) + chunk_step - chunk_size, chunk_step):
        yield list[i : i + chunk_size]
