def get_max_charges(charges: list, count):
    max_charges = []
    start_idx = 0
    end_index = len(charges) - count + 1

    for i in range(count):
        mc = max(charges[start_idx:end_index])
        max_charges.append(mc)
        start_idx = charges.index(mc, start_idx) + 1
        end_index += 1

    return int(''.join(max_charges))


with open('day03.txt', 'rt') as fl:
    pair_charge = 0
    dozen_charge = 0

    for line in fl:
        line = line.strip()
        charges = [c for c in line]

        pair_charge += get_max_charges(charges, 2)
        dozen_charge += get_max_charges(charges, 12)

    print(pair_charge)
    print(dozen_charge)
