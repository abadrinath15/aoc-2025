from os import path
import collections
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



def part_2(filetype: str) -> int:
    nodes: list[tuple[int, int]] = []
    max = 0
    row_intervals: collections.defaultdict[int, list[int]] = collections.defaultdict(list)
    col_intervals: collections.defaultdict[int, list[int]] = collections.defaultdict(list)

    with open(path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filetype}_9.txt')) as file:
        for line in file:
            cleaned = line.strip()
            if not cleaned:
                break

            new_node = typing.cast(tuple[int, int], tuple(map(int, cleaned.split(','))))
            nodes.append(new_node)

    for node in nodes:
        row_intervals[node[1]].append(node[0])
        col_intervals[node[0]].append(node[1])


    for v in row_intervals.values():
        v.sort()

    for v in col_intervals.values():
        v.sort()


    # row intervals + col intervals need to be unioned

       


                
            



if __name__ == '__main__':
    assert movie_theater('sample') == 50
    print(movie_theater('input'))
            
        
        
