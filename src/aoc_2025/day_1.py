import os

def part_1(filename: str) -> int:
    curr, pword = 50, 0
    with open(os.path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}_1.txt')) as file:
        for line in file:
            nloc = ( -1 if line[0] == 'L' else 1) * int(line[1:].strip()) + curr
            curr = nloc % 100
            if curr == 0:
                pword +=1

    return pword


def part_2(filename: str) -> int:
    curr, pword = 50, 0
    path = os.path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}_1.txt')
    
    with open(path) as file:
        for line in file:
            direction, turns = line[0], int(line[1:].strip())
            if direction == 'R':
                nloc = curr + turns
                pword += nloc // 100
                curr = nloc % 100
                continue

            curr = (100 - curr) % 100
            nloc = curr + turns
            pword += nloc // 100
            curr = (100 - nloc) % 100

    return pword


if __name__ == '__main__':
    print(part_1('input'))
    print(part_2('input'))
