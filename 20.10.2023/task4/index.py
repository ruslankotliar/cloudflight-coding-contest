directions = [
    (-1, 0),  # Up
    (1, 0),  # Down
    (0, -1),  # Left
    (0, 1),  # Right
    (-1, -1),  # Upper-left diagonal
    (-1, 1),  # Upper-right diagonal
    (1, -1),  # Lower-left diagonal
    (1, 1),  # Lower-right diagonal
]


def checkDiag(prev, dest, visited):
    if prev == None:
        return True

    y1 = prev[0] + (dest[0] - prev[0])
    coord1 = (y1, prev[1])

    x2 = prev[1] + (dest[1] - prev[1])
    coord2 = (prev[0], x2)

    if coord2 in visited and coord1 in visited:
        return False

    return True


from collections import deque


def solution(pairs, matrix, size):
    start = pairs[0]
    end = pairs[1]
    visited = set()
    queue = deque([(start, [])])

    while queue:
        (x, y), path = queue.popleft()

        # If the node was visited, skip it
        if (x, y) in visited:
            continue

        # Mark the node as visited
        visited.add((x, y))

        # Update the path
        new_path = path + [(y, x)]

        # If we reach the destination
        if (y, x) == end:
            return new_path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < size
                and 0 <= ny < size
                and matrix[nx][ny] != "L"
                and checkDiag((x, y), (nx, ny), visited)
            ):
                queue.append(((nx, ny), new_path))


with open("task4/level4/level4_example.in", "r") as file:
    # Read all lines and remove trailing newlines
    lines = [line.strip() for line in file.readlines()]

    size = int(lines[0])
    matrix = [list(line) for line in lines[1 : size + 1]]
    num_points = int(lines[size + 1])

    points = [
        (tuple(map(int, coord.split(","))) for coord in line.split(" "))
        for line in lines[size + 2 : size + 2 + num_points]
    ]

    points = [tuple(p) for p in points]

    f = open(
        "task4/solutions/1.txt",
        "w",
    )

    for pairs in points:
        res = solution(pairs, matrix, size)
        print(len(res))
        str_res = " ".join(f"{x},{y}" for x, y in res)
        f.write(str_res + "\n")

    # res = solution(points[0], matrix, size)
    # str_res = " ".join(f"{x},{y}" for x, y in res)
    # print(str_res)

    f.close()
