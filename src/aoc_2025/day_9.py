from os import path
import typing


def movie_theater(filetype: str) -> int:
    nodes: list[tuple[int, int]] = []
    max = 0
    with open(path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filetype}_9.txt')) as file:
        for index, line in enumerate(file):
            cleaned = line.strip()
            if not cleaned: 
                continue

            new_node = typing.cast(tuple[int, int], tuple(map(int, cleaned.split(','))))
            for node in nodes[:index]:
                area = (abs(new_node[0] - node[0]) + 1) * (abs(new_node[1] - node[1]) + 1)
                if area > max:
                    max = area

            nodes.append(new_node)

    return max

if __name__ == '__main__':
    assert movie_theater('sample') == 50
    print(movie_theater('input'))
            
        
        
