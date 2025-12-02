
def find_divisors(n):
    divisors = []
    for d in range(1, n):
        if n % d == 0:
            divisors.append(d)

    return divisors


with open('day02.txt', 'rt') as fl:
    line = fl.readline().strip()

print(line)
all_invalid_ids = set()
twin_invalid_ids = set()

for ids_range in line.split(","):
    first_id, last_id = ids_range.split('-')
    for curr_id in range(int(first_id), int(last_id) + 1):
        str_id = str(curr_id)
        id_len = len(str_id)

        for div in find_divisors(id_len):
            chunks = [str_id[i:i+div] for i in range(0, id_len, div)]
            if len(set(chunks)) == 1:
                all_invalid_ids.add(curr_id)

                if len(chunks) == 2:
                    twin_invalid_ids.add(curr_id)

print(sum(twin_invalid_ids))
print(sum(all_invalid_ids))
