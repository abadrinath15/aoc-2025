from os import path
import math
import typing
import more_itertools
import operator
import functools
import collections
import heapq

def playground(filename: str, num_connections: int) -> int:
    nodes: list[tuple[int, int, int]] = []
    with open(path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}.txt')) as file:
        for line in file:
            if (cleaned := line.strip()):
                nodes.append(typing.cast(tuple[int, int, int], tuple(map(int, cleaned.split(',')))))

    # --- max-heap of size num_connections ---
    edges: list[tuple[float, tuple[int,int,int], tuple[int,int,int]]] = []

    for i, new_node in enumerate(nodes):
        for other in nodes[:i]:
            dist = math.sqrt(sum((x1-x2)**2 for x1, x2 in zip(new_node, other)))
            if len(edges) < num_connections:
                heapq.heappush(edges, (-dist, new_node, other))
            else:
                if dist < -edges[0][0]:  # closer than farthest in heap
                    heapq.heapreplace(edges, (-dist, new_node, other))

    # --- convert heap to ascending distance order ---
    edges = [(-d, n1, n2) for d, n1, n2 in edges]
    edges.sort()  # ascending distance

    # --- circuit merge logic ---
    circuit_id_counter = 0
    circuit_id_to_nodes: dict[int, list[tuple[int,int,int]]] = collections.defaultdict(list)
    circuit_mapping: dict[tuple[int,int,int], int] = {}

    merges_done = 0  # count merges
    for _, node_1, node_2 in edges:
        if merges_done >= num_connections:
            break

        if (circuit_id := circuit_mapping.get(node_1)) is not None:
            if (circuit_id_2 := circuit_mapping.get(node_2)) is not None:
                if circuit_id == circuit_id_2:
                    continue  # same circuit, skip
                # merge two circuits
                for n in circuit_id_to_nodes[circuit_id_2]:
                    circuit_mapping[n] = circuit_id
                circuit_id_to_nodes[circuit_id].extend(circuit_id_to_nodes.pop(circuit_id_2))
                merges_done += 1
                continue

            # node_1 in circuit, node_2 not
            circuit_mapping[node_2] = circuit_id
            circuit_id_to_nodes[circuit_id].append(node_2)
            merges_done += 1
            continue

        if (circuit_id := circuit_mapping.get(node_2)) is not None:
            # node_2 in circuit, node_1 not
            circuit_mapping[node_1] = circuit_id
            circuit_id_to_nodes[circuit_id].append(node_1)
            merges_done += 1
            continue

        # neither node in a circuit → create new
        circuit_id_counter += 1
        circuit_mapping[node_1] = circuit_id_counter
        circuit_mapping[node_2] = circuit_id_counter
        circuit_id_to_nodes[circuit_id_counter].extend((node_1, node_2))
        merges_done += 1

    # multiply sizes of three largest circuits
    return functools.reduce(
        operator.mul,
        more_itertools.take(3, sorted(map(len, circuit_id_to_nodes.values()), reverse=True))
    )

def part_2(filename: str) -> int:
    nodes: list[tuple[int, int, int]] = []
    with open(path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}.txt')) as file:
        for line in file:
            if (cleaned := line.strip()):
                nodes.append(typing.cast(tuple[int, int, int], tuple(map(int, cleaned.split(',')))))

    edges: list[tuple[float, tuple[int,int,int], tuple[int,int,int]]] = []
    for i, new_node in enumerate(nodes):
        for other in nodes[:i]:
            dist = math.sqrt(sum((x1-x2)**2 for x1, x2 in zip(new_node, other)))
            edges.append((dist, new_node, other))

    edges.sort(reverse=True)
    num_nodes = len(nodes)
    circuit_id_counter = 0
    circuit_id_to_nodes: dict[int, list[tuple[int,int,int]]] = collections.defaultdict(list)
    circuit_mapping: dict[tuple[int,int,int], int] = {}

    while True:
        _, node_1, node_2 = edges.pop()

        if (circuit_id := circuit_mapping.get(node_1)) is not None:
            if (circuit_id_2 := circuit_mapping.get(node_2)) is not None:
                if circuit_id == circuit_id_2:
                    continue

                for n in circuit_id_to_nodes[circuit_id_2]:
                    circuit_mapping[n] = circuit_id

                circuit_id_to_nodes[circuit_id].extend(circuit_id_to_nodes.pop(circuit_id_2))
                if len(circuit_id_to_nodes[circuit_id]) == num_nodes:
                    return node_1[0] * node_2[0]

                continue

            circuit_mapping[node_2] = circuit_id
            circuit_id_to_nodes[circuit_id].append(node_2)
            if len(circuit_id_to_nodes[circuit_id]) == num_nodes:
                return node_1[0] * node_2[0]

            continue

        if (circuit_id := circuit_mapping.get(node_2)) is not None:
            # node_2 in circuit, node_1 not
            circuit_mapping[node_1] = circuit_id
            circuit_id_to_nodes[circuit_id].append(node_1)
            if len(circuit_id_to_nodes[circuit_id]) == num_nodes:
                return node_1[0] * node_2[0]

            continue

        circuit_id_counter += 1
        circuit_mapping[node_1] = circuit_id_counter
        circuit_mapping[node_2] = circuit_id_counter
        circuit_id_to_nodes[circuit_id_counter].extend((node_1, node_2))


  



    


    


if __name__ == '__main__':
    assert playground('sample_8', 10) == 40  # note: 10 merges produce sample result
    print(playground('input_8', 1000))
    assert part_2('sample_8') == 25272
    print(part_2('input_8'))
      


