import re
from os import path
import collections

PATTERN = re.compile(r'^([^:]+):\s*(.*)$')

def parse_line(line: str, paths: dict[str, list[str]]) -> None:
    if (match := re.match(PATTERN, line)) is None:
        raise ValueError("pattern didn't match!")

    paths[match[1].strip()] = match[2].strip().split(' ')


def solve_paths(node: str, paths: dict[str, list[str]], current_path: collections.deque[str], num_solutions_at_node: dict) -> None:
    if node == 'out':
        for c in current_path:
            num_solutions_at_node[c] = num_solutions_at_node.get(c, 0) + 1

        return

    if node in num_solutions_at_node:
        for c in current_path:
            num_solutions_at_node[c] = num_solutions_at_node.get(c, 0) + num_solutions_at_node[node]

        return
    
    if node in current_path:
        return

    current_path.append(node)
    for nn in paths[node]:
        solve_paths(nn, paths, current_path, num_solutions_at_node)

    current_path.pop()


            





def reactor(filetype: str) -> int:
    paths = {}
    with open(path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filetype}_11.txt')) as file:
        for line in file:
            if cleaned := line.strip():
                parse_line(cleaned, paths)

    num_solutions_at_node = {}
    solve_paths('you', paths, collections.deque(), num_solutions_at_node)
    return num_solutions_at_node['you']


if __name__ == '__main__':
    assert reactor('sample') == 5
    print(reactor('input'))

