from os import path
from collections import abc
import collections
import re


PATTERN = re.compile(r'\[([.#]+)\]((?:\s*\(\d+(?:,\d+)*\))+)')

def apply_button(state: list[int], button: abc.Iterable[int]) -> list[int]:
    new_state = list(state)
    for index in button:
        new_state[index] = (new_state[index] + 1) % 2

    return new_state


def parse_line(cleaned: str) -> None | tuple[list[int], list[list[int]]]:
    match = re.match(PATTERN, cleaned)
    if match is None:
        return None

    target = [0 if x == '.' else 1 for x in match[1]]
    buttons = []
    for button_raw in match[2].split(' '):
        if button_raw !='':
            buttons.append(list(map(int, button_raw.strip('()').split(','))))

    return target, buttons


def number_of_presses(target: list[int], buttons: abc.Iterable[abc.Iterable[int]]) -> int:
    queue = collections.deque()
    for button in buttons:
        queue.append((apply_button([0] * len(target), button), 1))

    while queue:
        state, steps = queue.popleft()
        if state == target: 
            return steps

        for button in buttons:
            queue.append((apply_button(state, button), steps + 1))

    else:
        raise ValueError
                


def factory(filetype: str) -> int:
    with open(path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filetype}_10.txt')) as file:
        total = 0
        for line_num, line in enumerate(file):
            print(line_num)
            cleaned = line.strip()
            match parse_line(cleaned):
                case None:
                    return total

                case (target, buttons):
                    total += number_of_presses(target, buttons)
                    continue

    return total

if __name__ == '__main__':
    assert apply_button([0, 0, 0, 0], [2]) == [0, 0, 1, 0] 
    assert number_of_presses([0, 1, 1, 0], [(1,3), (2,), (2,3), (0,2), (0,1)]) == 2
    assert factory('sample') == 7
    print(factory('input'))
