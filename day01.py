
START = 50
MAX = 100

current = START
zero_stop = 0
zero_cross = 0

with open('day01.txt', 'rt') as fl:
    for line in fl:
        line = line.strip()
        direction, count = line[0], int(line[1:])

        if count >= MAX:
            zero_cross += (count // MAX)
            count = count % MAX

        if direction == 'L':    # decrement
            if count > current and current:
                zero_cross += 1

            current = (current - count) % MAX

        elif direction == 'R':  # increment
            if current + count > MAX:
                zero_cross += 1

            current = (current + count) % MAX

        else:
            raise ValueError(f'Invalid direction {direction}')

        if current == 0:
            zero_stop += 1

    print(zero_stop)
    print(zero_stop + zero_cross)
