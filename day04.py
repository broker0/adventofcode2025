
STEPS = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1),
]


def scan_area(area: set) -> list:
    result = []

    for (x, y) in area:
        adj_rolls = 0
        for (dx, dy) in STEPS:
            if (x+dx, y+dy) in area:
                adj_rolls += 1

        if adj_rolls < 4:
            result.append((x, y))

    return result


with open('day04.txt', 'rt') as fl:
    area = set()

    for y, line in enumerate(fl):
        for x, c in enumerate(line.strip()):
            if c == '@':
                area.add((x, y))

    rolls = scan_area(area)
    print(len(rolls))

    good_rolls = 0
    while len(rolls):
        good_rolls += len(rolls)
        area.difference_update(rolls)

        rolls = scan_area(area)

    print(good_rolls)
