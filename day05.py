import bisect


def merge_ranges(ranges: list[tuple[int, int]]):
    result = [ranges[0]]

    for rng in ranges[1:]:
        last = result[-1]
        if rng[0] <= last[1]:
            result[-1] = (last[0], max(last[1], rng[1]))
        else:
            result.append(rng)

    return result


fresh_ranges = []
ingredient_ids = []

with open('day05.txt', 'rt') as fl:
    while line := fl.readline().strip():
        start, end = line.split('-')
        fresh_ranges.append((int(start), int(end)))

    while line := fl.readline().strip():
        ingredient_ids.append(int(line))


fresh_ranges = merge_ranges(sorted(fresh_ranges))

fresh_ids = 0
for curr_id in ingredient_ids:
    idx = bisect.bisect_right(fresh_ranges, curr_id, key=lambda e: e[0])
    if idx > 0:
        rng = fresh_ranges[idx-1]
        if rng[0] <= curr_id <= rng[1]:
            fresh_ids += 1

print(fresh_ids)

total_fresh_ids = 0
for rng in fresh_ranges:
    total_fresh_ids += rng[1]-rng[0]+1

print(total_fresh_ids)
