from os import path
import functools
import operator


def trash_compacter(filename: str) -> int:
    total = 0
    lines: list[list[str]] = []
    with open(path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}.txt')) as file:
        for line in file:
            if line.strip():
                lines.append(line.strip().split())

    operations = lines.pop(len(lines) - 1)
    for i in range(len(lines[0])):
        total += functools.reduce(operator.add if operations[i] == '+' else operator.mul, map(int, (line[i] for line in lines)))

    return total


def part_2(filename: str) -> int:
    total = 0
    lines: list[str] = []
    with open(path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}.txt')) as file:
        for line in file:
            if (cleaned :=line.rstrip('\n')):
                lines.append(cleaned[::-1])


    operations = lines.pop(len(lines) - 1).split()
    num_rows = len(lines)
    num_cols = len(lines[0])
    stack: list[str] = []
    for j in range(num_cols):
        current = ''.join(val for i in range(num_rows) if (val:=lines[i][j]) != ' ')
        if not current:
            curr_operator = operations.pop(0)
            total += functools.reduce(operator.add if curr_operator == '+' else operator.mul, map(int, stack))
            stack = []
            continue

        stack.append(current)

    curr_operator = operations.pop(0)
    return total + functools.reduce(operator.add if curr_operator == '+' else operator.mul, map(int, stack))



if __name__ == '__main__':
    assert trash_compacter('sample_6') == 4277556
    print(trash_compacter('input_6'))
    assert part_2('sample_6') == 3263827
    print(part_2('input_6'))





        




