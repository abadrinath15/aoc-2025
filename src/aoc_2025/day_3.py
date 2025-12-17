import helper

def lobby(filename: str) -> int:
    total_joltage = 0
    with helper.file_opener(filename) as file:
        for line in file:
            cleaned = line.strip()
            if not cleaned:
                break

            num_chars = len(cleaned)
            left, right = num_chars - 2, num_chars - 1
            max_left_ind, max_right_ind = left, right
            while left >= 0:
                if line[left] >= line[max_left_ind]:
                    max_left_ind = left

                for i in range(max_right_ind, max_left_ind, -1):
                    if line[i] > line[max_right_ind]:
                        max_right_ind = i

                left -= 1

            total_joltage += int(line[max_left_ind] + line[max_right_ind])

    return total_joltage
    


if __name__ == '__main__':
    assert lobby('sample_3') == 357
    print(lobby('input_3'))
