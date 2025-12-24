from os import path

def laboratories(filename: str) -> int:
    with open(path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}.txt')) as file:
        prior_line = list(file.readline().strip().replace('S', '|'))
        num_chars = len(prior_line)
        splits = 0
        for line in file:
            cleaned = line.strip()
            if not cleaned:
                break

            new_line: list[str] = []
            index = 0
            while index < num_chars:
                if prior_line[index] in ('.', '^'):
                    new_line.append('.')
                    index +=1
                    continue

                if cleaned[index] == '.':
                    new_line.append('|')
                    index +=1
                    continue

                left, right = index -1, index + 1
                splits +=1
                if left >=0:
                    new_line.pop()
                    new_line.append('|')

                new_line.append('^')
                if right < num_chars:
                    new_line.append('|')

                index += 2

            prior_line = new_line

        return splits


def part_2(filename: str) -> int:
    with open(path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}.txt')) as file:
        prior_line = [( 1 if x == 'S' else x) for x in file.readline().strip()]
        num_chars = len(prior_line)
        for line in file:
            cleaned = line.strip()
            if not cleaned:
                break

            new_line: list[str | int] = []
            index = 0
            while index < num_chars:
                if prior_line[index] in ('.', '^'):
                    new_line.append('.')
                    index +=1
                    continue

                if cleaned[index] == '.':
                    new_line.append(prior_line[index])
                    index += 1
                    continue

                left, right = index -1, index + 1
                if left >=0:
                    prior_left = new_line.pop()
                    if isinstance(prior_left, str):
                        new_line.append(prior_line[index])

                    else:
                        new_line.append(prior_line[index] + prior_left)


                new_line.append('^')
                if right < num_chars:
                    prior_right = prior_line[index + 1]
                    if isinstance(prior_right, str):
                        new_line.append(prior_line[index])

                    else:
                        new_line.append(prior_line[index] + prior_right)

                index += 2

            prior_line = new_line

        return sum(x for x in prior_line if isinstance(x, int))





       

if __name__ == '__main__':
    assert laboratories('sample_7') == 21
    print(laboratories('input_7'))
    assert part_2('sample_7') == 40
    print(part_2('input_7'))
