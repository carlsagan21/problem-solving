def read_file(path):
    with open(path, 'r') as f:
        lines = list(f)

    return lines


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
