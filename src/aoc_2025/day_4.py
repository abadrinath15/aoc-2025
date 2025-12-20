import helper
import pprint


def printing_department(filename: str) -> int:
    lines: list[list[str]] = []
    accessible_rolls = 0
    with helper.file_opener(filename) as file:
        for line in file:
            if (cleaned := line.strip()):
                lines.append(list(cleaned))

    cols = len(lines[0])
    rows = len(lines)
    for i in range(rows):
        for j in range(cols):
            if lines[i][j] == '.':
                continue

            num_neighbors = 0
            for row_adds in range(-1, 2, 1):
                for col_adds in range(-1, 2, 1):
                    if row_adds == col_adds == 0:
                        continue

                    neighbor_row, neighbor_col = i + row_adds, j + col_adds

                    if neighbor_row < 0 or neighbor_row == rows:
                        continue
                    
                    if neighbor_col < 0 or neighbor_col == cols:
                        continue

                    if lines[neighbor_row][neighbor_col] == '@':
                        num_neighbors += 1

            if num_neighbors <4:
                accessible_rolls += 1

    return accessible_rolls



def part_2(filename: str) -> int:
    lines: list[list[str]] = []
    with helper.file_opener(filename) as file:
        for line in file:
            if (cleaned := line.strip()):
                lines.append(list(cleaned))

    cols = len(lines[0])
    rows = len(lines)
    removed_rolls = 0
    while True:
        any_changed = False
        for i in range(rows):
            for j in range(cols):
                if lines[i][j] == '.':
                    continue

                num_neighbors = 0
                for row_adds in range(-1, 2, 1):
                    for col_adds in range(-1, 2, 1):
                        if row_adds == col_adds == 0:
                            continue

                        neighbor_row, neighbor_col = i + row_adds, j + col_adds

                        if neighbor_row < 0 or neighbor_row == rows:
                            continue
                        
                        if neighbor_col < 0 or neighbor_col == cols:
                            continue

                        if lines[neighbor_row][neighbor_col] == '@':
                            num_neighbors += 1

                if num_neighbors <4:
                    removed_rolls  += 1
                    lines[i][j] = '.'
                    any_changed = True

        if not any_changed:
            return removed_rolls
                   
                    





if __name__ == '__main__':
    assert printing_department('sample_4') == 13
    print(printing_department('input_4'))
    assert part_2('sample_4') == 43
    print(part_2('input_4'))
