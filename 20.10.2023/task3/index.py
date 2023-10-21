def solution(pairs, matrix, size):
    visited = set()

    prev = None
    for dest in pairs:
        if not prev:
            prev = dest
            visited.add(dest)
            continue

        if dest in visited:
            return "INVALID"

        y1 = prev[0] + (dest[0] - prev[0])
        coord1 = (y1, prev[1])

        x2 = prev[1] + (dest[1] - prev[1])
        coord2 = (prev[0], x2)

        print("-----")
        print(prev, dest)
        print(coord1, coord2)

        if coord2 in visited and coord1 in visited:
            return "INVALID"

        prev = dest

        visited.add(dest)

    return "VALID"


with open("level3/level3_5.in", "r") as file:
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
        "w",
    )

    for pairs in points:
        res = solution(pairs, matrix, size)
        f.write(res + "\n")

    f.close()
