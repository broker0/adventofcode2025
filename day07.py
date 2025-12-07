

with open('day07.txt', 'rt') as fl:
    s = fl.readline()
    split_count = 0
    current_beams = {s.index('S'): 1}
    splits = dict()
    for y, line in enumerate(fl):
        new_beams = dict()
        line = line.strip()
        for (curr_beam_x, curr_beam_cnt) in current_beams.items():
            if line[curr_beam_x] == '.':
                new_beams[curr_beam_x] = new_beams.get(curr_beam_x, 0) + curr_beam_cnt

            elif line[curr_beam_x] == '^':
                new_beams[curr_beam_x-1] = new_beams.get(curr_beam_x-1, 0) + curr_beam_cnt
                new_beams[curr_beam_x+1] = new_beams.get(curr_beam_x+1, 0) + curr_beam_cnt
                split_count += 1

        current_beams = new_beams

    print(split_count)
    print(sum(current_beams.values()))
