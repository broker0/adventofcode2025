from collections import Counter

with open('day07.txt', 'rt') as fl:
    s = fl.readline()
    split_count = 0
    current_beams = Counter({s.index('S'): 1})

    for line in fl:
        new_beams = Counter()
        line = line.strip()
        for (curr_beam_x, curr_beam_cnt) in current_beams.items():
            if line[curr_beam_x] == '.':
                new_beams[curr_beam_x] += curr_beam_cnt

            elif line[curr_beam_x] == '^':
                new_beams[curr_beam_x-1] += curr_beam_cnt
                new_beams[curr_beam_x+1] += curr_beam_cnt
                split_count += 1

        current_beams = new_beams

    print(split_count)
    print(current_beams.total())
