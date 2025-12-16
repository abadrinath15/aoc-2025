import os
import re

PART_2_PATTERN = re.compile(r'(.+)\1+$')

def gift_shop(filename: str) -> int:
    invalid_sum = 0
    with open(os.path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}.txt')) as file:
        for prod_id in file.readline().strip().split(','):
            if not prod_id:
                return invalid_sum

            first, second = map(int, prod_id.split('-'))
            for maybe_invalid in range(first, second + 1):
                as_str = str(maybe_invalid)
                if (num_chars :=len(as_str)) % 2 != 0:
                    continue

                middle = num_chars // 2
                part_1, part_2 = int(as_str[0: middle]), int(as_str[middle: ])
                if part_1 - part_2 == 0:
                    invalid_sum += maybe_invalid

    return invalid_sum

def part_2(filename: str) -> int:
    invalid_sum = 0
    with open(os.path.expanduser(f'~/Programming/python/aoc-2025/inputs/{filename}.txt')) as file:
        for prod_id in file.readline().strip().split(','):
            if not prod_id:
                return invalid_sum

            first, second = map(int, prod_id.split('-'))
            for maybe_invalid in range(first, second + 1):
                as_str = str(maybe_invalid)
                if re.match(PART_2_PATTERN, as_str):
                    invalid_sum += maybe_invalid


    return invalid_sum

 

        

 
            



if __name__ =='__main__':
    assert gift_shop('sample_2') == 1227775554
    print(gift_shop('input_2'))
    assert(part_2('sample_2')) == 4174379265
    print(part_2('input_2'))
