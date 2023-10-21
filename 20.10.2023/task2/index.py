from collections import deque


def solution(pair, grid, size):
    if not grid:
        return 0

    rows, cols = size, size
    visited = set()
    islands = 0

    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (
                    (r) in range(rows)
                    and (c) in range(cols)
                    and grid[r][c] == "L"
                    and (r, c) not in visited
                ):
                    q.append((r, c))
                    visited.add((r, c))

    bfs(pair[0][1], pair[0][0])

    res = "DIFFERENT"

    if (pair[1][1], pair[1][0]) in visited:
        res = "SAME"

    return res


with open("level2/level2_5.in", "r") as file:
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
        "solutions/5.txt",
        "a",
    )

    for pair in points:
        res = solution(pair, matrix, size)
        f.write(res + "\n")

    f.close()
