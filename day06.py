import math


def parse(lines):
    problems = []

    num_lines_count = len(lines)-1
    delimiter = ' ' * num_lines_count
    curr_problem = []

    for i in range(len(lines[0])):
        curr_slice = [lines[j][i] for j in range(num_lines_count)]
        curr_problem += [curr_slice]
        curr_col = ''.join(curr_slice)

        if curr_col == delimiter:
            problems.append(curr_problem[:-1])
            curr_problem = []

    problems.append(curr_problem[:-1])
    ops = lines[-1].split()

    return ops, problems


def solve1(op: str, nums: list[str]):
    v = []
    for j in range(len(nums[0])):
        n = ""
        for i in range(len(nums)):
            c = nums[i][j]
            n += c
        v.append(int(n))

    if op == '*':
        return math.prod(v)
    elif op == '+':
        return sum(v)

    return None


def solve2(op: str, nums: list[str]):
    v = []
    for i in range(len(nums)):
        n = ""
        for j in range(len(nums[0])):
            c = nums[i][j]
            n += c
        v.append(int(n))

    if op == '*':
        return math.prod(v)
    elif op == '+':
        return sum(v)

    return None


problems = []
with open('day06.txt', 'rt') as fl:
    lines = fl.readlines()

ops, nums = parse(lines)


sum_of_problems1 = 0
sum_of_problems2 = 0
for op, num in zip(ops, nums):
    sum_of_problems1 += solve1(op, num)
    sum_of_problems2 += solve2(op, num)

print(sum_of_problems1)
print(sum_of_problems2)
