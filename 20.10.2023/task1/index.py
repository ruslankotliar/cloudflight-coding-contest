land = "L"
water = "W"


def solution(lines):
    size = int(lines[0])
    matrix = [list(line) for line in lines[1 : size + 1]]
    num_points = int(lines[size + 1])
    points = [
        tuple(map(int, line.split(",")))
        for line in lines[size + 2 : size + 2 + num_points]
    ]

    for x in points:
        print(matrix[x[1]][x[0]])

    return


with open("level1/level1_5.in", "r") as file:
    # Read all lines and remove trailing newlines
    lines = [line.strip() for line in file.readlines()]
    solution(lines)
