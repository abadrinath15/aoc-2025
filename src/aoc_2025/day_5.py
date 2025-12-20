from os import path
import re

RANGE_PATTERN = re.compile(r'(\d+)-(\d+)')
ID_PATTERN = re.compile(r'(\d+)')


def cafeteria(filename: str) -> int:
    unspoiled = 0
    intervals: list[tuple[int, int]] = []
    ints_sorted = False
    with open(path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}.txt')) as file:
        for line in file:
            cleaned = line.strip()
            if (m := re.match(RANGE_PATTERN, cleaned)):
                left, right = int(m.group(1)), int(m.group(2))
                intervals.append((left, right))
                continue

            if not ints_sorted:
                intervals = sorted(intervals)

            if (m := re.match(ID_PATTERN, cleaned)):
                food_id = int(m.group(1))
                for left, right in intervals:
                    if left <= food_id <= right:
                        unspoiled +=1
                        break
                       


    return unspoiled

def part_2(filename: str) -> int:
    intervals: list[tuple[int, int]] = []
    unspoiled = 0
    with open(path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}.txt')) as file:
        for line in file:
            cleaned = line.strip()
            if (m := re.match(RANGE_PATTERN, cleaned)):
                left, right = int(m.group(1)), int(m.group(2))
                intervals.append((left, right))
                continue

            else: 
                break

    intervals = sorted(intervals)
    while True:
        for i in range(1, len(intervals)):
            if intervals[i-1][0] <= intervals[i][0] <= intervals[i-1][1]:
                overlap = intervals.pop(i)
                if overlap[1] > intervals[i-1][1]:
                    intervals[i-1] = (intervals[i-1][0], overlap[1])
                break

        else:
            break


    for left, right in intervals:
        unspoiled += (right - left) + 1

    return unspoiled

if __name__ == '__main__':
    assert cafeteria('sample_5') == 3
    print(cafeteria('input_5'))
    assert part_2('sample_5') == 14
    print(part_2('input_5'))

